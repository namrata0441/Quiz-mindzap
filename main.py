from PyQt5 import QtCore, QtWidgets
from ui.createArithmeticQuestion import CreateArithmeticQuestionUi
from ui.createMultipleChoiceQuestion import CreateMultipleChoiceQuestionUi
from ui.createTest import CreateTestUi
from ui.listTests import ListTestsUi
from ui.reviewCompletedTests import ReviewCompletedTestsUi


class MainWindowUi(object):
    """Main Menu window ui

    This class creates the menu and handles the instantiation of the desired 'action' dialog.

    Building the application this way enables the application to be run as one rather than having to run
    individual ui's for each action."""

    # define actions as 'constants' rather than just passing random strings around
    CREATE_ARITHMETIC_QUESTION = 1
    CREATE_MULTIPLE_CHOICE_QUESTION = 2
    CREATE_A_TEST = 3
    TAKE_A_TEST = 4
    REVIEW_COMPLETED_TESTS = 5

    # set up the ui
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.createArithmeticQuestionButton = QtWidgets.QPushButton(self.centralwidget)
        self.createArithmeticQuestionButton.setGeometry(QtCore.QRect(190, 20, 391, 31))
        self.createArithmeticQuestionButton.setObjectName("createArithmeticQuestionButton")
        self.createArithmeticQuestionButton.clicked.connect(lambda: self.openDialog(self.CREATE_ARITHMETIC_QUESTION))

        self.createMultipleChoiceQuestionButton = QtWidgets.QPushButton(self.centralwidget)
        self.createMultipleChoiceQuestionButton.setGeometry(QtCore.QRect(190, 70, 391, 31))
        self.createMultipleChoiceQuestionButton.setObjectName("createMultipleChoiceQuestionButton")
        self.createMultipleChoiceQuestionButton.clicked.connect(lambda: self.openDialog(self.CREATE_MULTIPLE_CHOICE_QUESTION))

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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.createArithmeticQuestionButton.setText(_translate("MainWindow", "Create an Arithmetic Question"))
        self.createMultipleChoiceQuestionButton.setText(_translate("MainWindow", "Create a Multiple Choice Question"))
        self.createTestButton.setText(_translate("MainWindow", "Create a Test"))
        self.takeTestButton.setText(_translate("MainWindow", "Take a Test"))
        self.reviewTestsButton.setText(_translate("MainWindow", "Review Completed Tests"))

    def openDialog(self, dialogType):
        # close dialog if already open
        if hasattr(self, 'dialog'):
            self.dialog.close()

        if dialogType == self.CREATE_ARITHMETIC_QUESTION:
            self.ui = CreateArithmeticQuestionUi()
        elif dialogType == self.CREATE_MULTIPLE_CHOICE_QUESTION:
            self.ui = CreateMultipleChoiceQuestionUi()
        elif dialogType == self.CREATE_A_TEST:
            self.ui = CreateTestUi()
        elif dialogType == self.TAKE_A_TEST:
            self.ui = ListTestsUi()
        elif dialogType == self.REVIEW_COMPLETED_TESTS:
            self.ui = ReviewCompletedTestsUi()
        else:
            return False

        self.dialog = QtWidgets.QDialog()
        self.ui.setupUi(self.dialog)
        self.dialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUi()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

