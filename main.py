import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import requests

# Import your UI classes from their respective files
from register_form import RegisterUi_Form
from login_form import LoginUi_Form
from dashboard_form import Ui_MainWindow  # Re-enabled: This should be your dashboard UI setup class

# Import the new Quiz Main Menu Widget
# IMPORTANT: Ensure 'quiz_main.py' is the correct filename for your QuizMainMenuWidget
from quiz_main import QuizMainMenuWidget


class MainApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MindZap Application")
        self.setGeometry(100, 100, 800, 600)

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.current_username = None  # To store the username (email/username) of the logged-in user

        self.init_pages()
        self.init_connections()
        self.show_login_page()  # Start with the login page

    def init_pages(self):
        """Initializes all UI pages and adds them to the stacked widget."""
        # Login Page
        self.login_page = LoginUi_Form()
        self.stacked_widget.addWidget(self.login_page)

        # Registration Page
        self.register_page = RegisterUi_Form()
        self.stacked_widget.addWidget(self.register_page)

        # Dashboard Page (Re-added)
        self.dashboard_window = QtWidgets.QMainWindow()
        self.dashboard_ui = Ui_MainWindow()
        self.dashboard_ui.setupUi(self.dashboard_window)
        self.stacked_widget.addWidget(self.dashboard_window)

        # Profile Page (assuming it's a sub-widget within dashboard_ui's stackedWidget)
        if hasattr(self.dashboard_ui, 'page_7'):
            self.profile_page_widget = self.dashboard_ui.page_7
        else:
            self.profile_page_widget = None
            print("Warning: 'page_7' (Profile Page) not found in dashboard_ui. Profile functionality might be limited.")

        # Quiz Main Menu Page
        self.quiz_main_menu_page = QuizMainMenuWidget()
        self.stacked_widget.addWidget(self.quiz_main_menu_page)


    def init_connections(self):
        """Sets up all signal-slot connections for navigation and data flow."""
        # Login Page Connections
        self.login_page.login_successful_signal.connect(self._handle_login_attempt)
        self.login_page.switch_to_register_signal.connect(self.show_register_page)

        # Registration Page Connections
        self.register_page.registration_successful_signal.connect(self.show_login_page)
        self.register_page.switch_to_login_signal.connect(self.show_login_page)

        # Dashboard Page Connections
        if self.profile_page_widget:
            if hasattr(self.profile_page_widget, 'logout_requested'):
                self.profile_page_widget.logout_requested.connect(self.show_login_page)
            if hasattr(self.profile_page_widget, 'profile_updated'):
                self.profile_page_widget.profile_updated.connect(self._handle_profile_updated)

        if hasattr(self.dashboard_ui, 'user_btn'):
            self.dashboard_ui.user_btn.clicked.connect(self.show_profile_page)
        else:
            print("Warning: 'user_btn' not found in dashboard_ui. Profile page navigation might not work.")

        if hasattr(self.dashboard_ui, 'setting_1'):
            self.dashboard_ui.setting_1.toggled['bool'].connect(
                lambda checked: self.dashboard_ui.stackedWidget.setCurrentIndex(5) if checked else None)
        else:
            print("Warning: 'setting_1' button not found in dashboard_ui.")

        if hasattr(self.dashboard_ui, 'setting_2'):
            self.dashboard_ui.setting_2.toggled['bool'].connect(
                lambda checked: self.dashboard_ui.stackedWidget.setCurrentIndex(5) if checked else None)
        else:
            print("Warning: 'setting_2' button not found in dashboard_ui.")

        # --- FIX: Connect the actual quiz buttons from dashboard_form.py ---
        if hasattr(self.dashboard_ui, 'quizze_btn_1'): # Check for the icon-only quiz button
             self.dashboard_ui.quizze_btn_1.clicked.connect(self.show_quiz_main_menu_page)
        else:
             print("Warning: 'quizze_btn_1' not found in dashboard_ui. Quiz menu navigation (icon-only) might not work.")

        if hasattr(self.dashboard_ui, 'quizze_btn_2'): # Check for the full menu quiz button
             self.dashboard_ui.quizze_btn_2.clicked.connect(self.show_quiz_main_menu_page)
        else:
             print("Warning: 'quizze_btn_2' not found in dashboard_ui. Quiz menu navigation (full menu) might not work.")


    def _handle_login_attempt(self, username, password):
        """
        Handles the login attempt by making a request to the backend.
        This method is connected to login_page.login_successful_signal.
        """
        backend_url = "http://127.0.0.1:5000/login"
        login_data = {
            "username": username,
            "password": password
        }

        print(f"Frontend Debug (MainApp - Login): Sending data to backend: {login_data}")

        response = None
        try:
            response = requests.post(backend_url, json=login_data)
            response.raise_for_status()

            response_data = response.json()
            print(f"Frontend Debug (MainApp - Login): Received response: {response_data}")

            if response.status_code == 200:
                QtWidgets.QMessageBox.information(self, "Login Success",
                                                  response_data.get("message", "Login successful!"))
                self.login_page.clear_fields()
                self.current_username = response_data.get("username", username)
                self.show_dashboard_page(self.current_username)
            else:
                QtWidgets.QMessageBox.warning(self, "Login Failed",
                                              response_data.get("message", "An unknown error occurred during login."))

        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.critical(self, "Connection Error",
                                           "Could not connect to the backend server. Please ensure Flask app is running.")
        except requests.exceptions.HTTPError as e:
            error_message = f"Backend returned an error: {e.response.status_code}"
            try:
                if response:
                    error_json = response.json()
                    error_message += f" - {error_json.get('message', response.text)}"
                else:
                    error_message += f" - No response received."
            except requests.exceptions.JSONDecodeError:
                if response:
                    error_message += f" - {response.text}"
                else:
                    error_message += f" - No response received."
            QtWidgets.QMessageBox.critical(self, "Server Error", error_message)
        except requests.exceptions.JSONDecodeError as e:
            QtWidgets.QMessageBox.critical(self, "Response Error",
                                           f"Failed to parse server response as JSON. Error: {e}. Raw Response: '{response.text if response else 'No response'}'")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Unexpected Error", f"An unexpected error occurred during login: {e}")

    def _fetch_profile_data(self, username):
        """Fetches user profile data from the backend."""
        if not username:
            print("Error: No username available to fetch profile.")
            return None

        backend_url = f"http://127.0.0.1:5000/profile/{username}"
        response = None
        try:
            response = requests.get(backend_url)
            response.raise_for_status()
            profile_data = response.json()
            print(f"Frontend Debug (MainApp - Profile Fetch): Fetched profile: {profile_data}")
            return profile_data
        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.critical(self, "Connection Error", "Could not connect to backend to fetch profile.")
        except requests.exceptions.HTTPError as e:
            error_message = f"Backend returned an error: {e.response.status_code}"
            try:
                if response:
                    error_json = response.json()
                    error_message += f" - {error_json.get('message', response.text)}"
                else:
                    error_message += f" - No response received."
            except requests.exceptions.JSONDecodeError:
                if response:
                    error_message += f" - {response.text}"
                else:
                    error_message += f" - No response received."
            QtWidgets.QMessageBox.critical(self, "Server Error", error_message)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Unexpected Error",
                                           f"An unexpected error occurred fetching profile: {e}")
        return None

    def _handle_profile_updated(self):
        """
        Handles the signal emitted when profile data is updated in ProfileWidget.
        Re-fetches profile data to ensure dashboard and profile page are in sync
        if the username (email) was updated.
        """
        print("Frontend Debug (MainApp): Profile updated signal received.")
        if self.current_username:
            updated_profile_data = self._fetch_profile_data(self.current_username)
            if updated_profile_data:
                if self.profile_page_widget and hasattr(self.profile_page_widget, 'load_profile_data'):
                    self.profile_page_widget.load_profile_data(updated_profile_data)
                if hasattr(self.dashboard_ui, 'set_username_display'):
                    self.dashboard_ui.set_username_display(updated_profile_data.get('username', self.current_username))
                self.current_username = updated_profile_data.get('username', self.current_username)
                self.setWindowTitle(f"MindZap - Dashboard ({self.current_username})")
            else:
                QtWidgets.QMessageBox.warning(self, "Profile Sync Error", "Could not re-fetch updated profile data.")

    def show_login_page(self):
        self.stacked_widget.setCurrentWidget(self.login_page)
        self.setWindowTitle("MindZap - Login")
        self.current_username = None
        print("Switched to Login Page")

    def show_register_page(self):
        self.stacked_widget.setCurrentWidget(self.register_page)
        self.setWindowTitle("MindZap - Register")
        print("Switched to Register Page")

    def show_dashboard_page(self, username):
        """Switches to the Dashboard page and updates its display."""
        if hasattr(self.dashboard_ui, 'set_username_display'):
            self.dashboard_ui.set_username_display(username)
        else:
            print("Warning: 'set_username_display' method not found in dashboard_ui. Username might not display.")

        self.stacked_widget.setCurrentWidget(self.dashboard_window)
        self.setWindowTitle(f"MindZap - Dashboard ({username})")
        print(f"Switched to Dashboard Page for user: {username}")

    def show_profile_page(self):
        """
        This method is called when the user clicks the profile button on the dashboard.
        It fetches the profile data and loads it into the ProfileWidget.
        """
        if self.current_username:
            profile_data = self._fetch_profile_data(self.current_username)
            if profile_data:
                if self.profile_page_widget and hasattr(self.profile_page_widget, 'load_profile_data'):
                    self.profile_page_widget.load_profile_data(profile_data)
                if hasattr(self.dashboard_ui, 'stackedWidget'):
                    self.dashboard_ui.stackedWidget.setCurrentIndex(1)
                    self.setWindowTitle(f"MindZap - Profile ({self.current_username})")
                    print(f"Switched to Profile Page for user: {self.current_username}")
                else:
                    print("Warning: 'stackedWidget' not found in dashboard_ui. Cannot switch to profile page.")
            else:
                QtWidgets.QMessageBox.warning(self, "Profile Error", "Could not load profile data.")
        else:
            QtWidgets.QMessageBox.warning(self, "Profile Error", "No user logged in to view profile.")
            self.show_login_page()

    def show_quiz_main_menu_page(self):
        """Switches to the new Quiz Main Menu page."""
        self.stacked_widget.setCurrentWidget(self.quiz_main_menu_page)
        self.setWindowTitle("MindZap - Quiz Main Menu")
        print(f"Switched to Quiz Main Menu Page for user: {self.current_username}")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApplicationWindow()
    main_app.show()
    sys.exit(app.exec_())
