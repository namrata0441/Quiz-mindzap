from PyQt5 import QtCore, QtWidgets

# Import the UI classes for the dialogs that the menu will open.
# IMPORTANT: Adjust these import paths based on where your generated UI files are.
# Assuming they are in a 'ui' subfolder and named like 'createArithmeticQuestion.py'
# and the class names are as specified (e.g., CreateArithmeticQuestionUi).
# If your generated UI files are named differently (e.g., ui_createArithmeticQuestion.py), adjust accordingly.
from ui.createArithmeticQuestion import CreateArithmeticQuestionUi  # Assuming class name
from ui.createMultipleChoiceQuestion import CreateMultipleChoiceQuestionUi  # Assuming class name
from ui.createTest import CreateTestUi  # Assuming class name
from ui.listTests import ListTestsUi  # Assuming class name
from ui.reviewCompletedTests import ReviewCompletedTestsUi  # Assuming class name


class QuizMainMenuWidget(QtWidgets.QWidget):  # Changed from object to QWidget
    """Quiz Main Menu window widget.

    This class creates the menu and handles the instantiation of the desired 'action' dialogs.
    It's designed to be a page within a QStackedWidget."""

    # Define actions as 'constants'
    CREATE_ARITHMETIC_QUESTION = 1
    CREATE_MULTIPLE_CHOICE_QUESTION = 2
    CREATE_A_TEST = 3
    TAKE_A_TEST = 4
    REVIEW_COMPLETED_TESTS = 5

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Call setupUi on this widget instance

    # set up the ui
    def setupUi(self, QuizMainMenuWidgetInstance):  # Renamed 'MainWindow' to 'QuizMainMenuWidgetInstance' for clarity
        QuizMainMenuWidgetInstance.setObjectName("QuizMainMenuWidget")  # Set object name for the widget
        QuizMainMenuWidgetInstance.resize(800, 600)  # Set initial size for the widget

        # Central widget is no longer needed as this IS the central widget.
        # We'll place buttons directly on QuizMainMenuWidgetInstance or a layout.
        # For simplicity, let's keep the centralwidget structure but make it part of this widget.
        self.centralwidget = QtWidgets.QWidget(QuizMainMenuWidgetInstance)
        self.centralwidget.setObjectName("centralwidget")

        # Set a layout for the QuizMainMenuWidgetInstance and add centralwidget to it
        # This ensures the buttons are properly laid out within the widget.
        main_layout = QtWidgets.QVBoxLayout(QuizMainMenuWidgetInstance)
        main_layout.addWidget(self.centralwidget)
        main_layout.setContentsMargins(0, 0, 0, 0)  # Remove extra margins if centralwidget handles them

        # Buttons are now children of self.centralwidget
        self.createArithmeticQuestionButton = QtWidgets.QPushButton(self.centralwidget)
        self.createArithmeticQuestionButton.setGeometry(QtCore.QRect(190, 20, 391, 31))
        self.createArithmeticQuestionButton.setObjectName("createArithmeticQuestionButton")
        self.createArithmeticQuestionButton.clicked.connect(lambda: self.openDialog(self.CREATE_ARITHMETIC_QUESTION))

        self.createMultipleChoiceQuestionButton = QtWidgets.QPushButton(self.centralwidget)
        self.createMultipleChoiceQuestionButton.setGeometry(QtCore.QRect(190, 70, 391, 31))
        self.createMultipleChoiceQuestionButton.setObjectName("createMultipleChoiceQuestionButton")
        self.createMultipleChoiceQuestionButton.clicked.connect(
            lambda: self.openDialog(self.CREATE_MULTIPLE_CHOICE_QUESTION))

        self.createTestButton = QtWidgets.QPushButton(self.centralwidget)
        self.createTestButton.setGeometry(QtCore.QRect(190, 120, 391, 31))
        self.createTestButton.setObjectName("createTestButton")
        self.createTestButton.clicked.connect(lambda: self.openDialog(self.CREATE_A_TEST))

        self.takeTestButton = QtWidgets.QPushButton(self.centralwidget)
        self.takeTestButton.setGeometry(QtCore.QRect(190, 170, 391, 31))
        self.takeTestButton.setObjectName("takeTestButton")
        self.takeTestButton.clicked.connect(lambda: self.openDialog(self.TAKE_A_TEST))

        self.reviewTestsButton = QtWidgets.QPushButton(self.centralwidget)
        self.reviewTestsButton.setGeometry(QtCore.QRect(190, 220, 391, 31))
        self.reviewTestsButton.setObjectName("reviewTestsButton")
        self.reviewTestsButton.clicked.connect(lambda: self.openDialog(self.REVIEW_COMPLETED_TESTS))

        # No need for QuizMainMenuWidgetInstance.setCentralWidget as QuizMainMenuWidgetInstance is a QWidget itself
        # and we've added centralwidget to its layout.

        self.retranslateUi(QuizMainMenuWidgetInstance)  # Pass the instance for retranslation
        QtCore.QMetaObject.connectSlotsByName(QuizMainMenuWidgetInstance)

    def retranslateUi(self, QuizMainMenuWidgetInstance):
        _translate = QtCore.QCoreApplication.translate
        # The main window title is set in app.py, so this might be redundant here for the widget
        QuizMainMenuWidgetInstance.setWindowTitle(
            _translate("QuizMainMenuWidget", "Quiz Main Menu"))  # Set title for the widget itself
        self.createArithmeticQuestionButton.setText(_translate("QuizMainMenuWidget", "Create an Arithmetic Question"))
        self.createMultipleChoiceQuestionButton.setText(
            _translate("QuizMainMenuWidget", "Create a Multiple Choice Question"))
        self.createTestButton.setText(_translate("QuizMainMenuWidget", "Create a Test"))
        self.takeTestButton.setText(_translate("QuizMainMenuWidget", "Take a Test"))
        self.reviewTestsButton.setText(_translate("QuizMainMenuWidget", "Review Completed Tests"))

    def openDialog(self, dialogType):
        # close dialog if already open
        if hasattr(self, 'dialog') and self.dialog.isVisible():
            self.dialog.close()

        # Instantiate the correct UI class based on dialogType
        # These classes are expected to be QDialogs or QWidgets that can be shown.
        # If they are just Ui_Form classes, you'll need to wrap them in QDialogs as done below.
        dialog_ui_instance = None
        if dialogType == self.CREATE_ARITHMETIC_QUESTION:
            dialog_ui_instance = CreateArithmeticQuestionUi()
        elif dialogType == self.CREATE_MULTIPLE_CHOICE_QUESTION:
            dialog_ui_instance = CreateMultipleChoiceQuestionUi()
        elif dialogType == self.CREATE_A_TEST:
            dialog_ui_instance = CreateTestUi()
        elif dialogType == self.TAKE_A_TEST:
            dialog_ui_instance = ListTestsUi()
        elif dialogType == self.REVIEW_COMPLETED_TESTS:
            dialog_ui_instance = ReviewCompletedTestsUi()
        else:
            return False  # Unknown dialog type

        if dialog_ui_instance:
            self.dialog = QtWidgets.QDialog(self)  # Create a QDialog, parented to this widget
            dialog_ui_instance.setupUi(self.dialog)  # Set up the UI on the new dialog
            self.dialog.exec_()  # Show as modal dialog (blocks parent until closed)


# This __main__ block is for testing this widget independently.
# In your main application, you will import and use QuizMainMenuWidget.
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_menu_widget = QuizMainMenuWidget()
    main_window = QtWidgets.QMainWindow()  # Create a QMainWindow to hold the widget for testing
    main_window.setCentralWidget(main_menu_widget)
    main_window.setWindowTitle("Test Quiz Main Menu")
    main_window.show()
    sys.exit(app.exec_())
