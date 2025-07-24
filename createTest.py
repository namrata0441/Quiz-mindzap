from PyQt5 import QtCore, QtGui, QtWidgets
from question.Question import QuestionBank
from question.Test import Test, TestBank

class CreateTestUi(object):
    def setupUi(self, createTest):
        createTest.setObjectName("createTest")
        createTest.resize(399, 591)
        self.buttonBox = QtWidgets.QDialogButtonBox(createTest)
        self.buttonBox.setGeometry(QtCore.QRect(30, 550, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.label_6 = QtWidgets.QLabel(createTest)
        self.label_6.setGeometry(QtCore.QRect(30, 10, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(createTest)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 81, 17))
        self.label_2.setObjectName("label_2")
        
        self.testNameInput = QtWidgets.QLineEdit(createTest)
        self.testNameInput.setGeometry(QtCore.QRect(160, 60, 211, 21))
        self.testNameInput.setObjectName("testNameInput")
        
        self.line = QtWidgets.QFrame(createTest)
        self.line.setGeometry(QtCore.QRect(30, 90, 341, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.label = QtWidgets.QLabel(createTest)
        self.label.setGeometry(QtCore.QRect(30, 110, 311, 21))
        self.label.setObjectName("label")
        
        self.searchInput = QtWidgets.QLineEdit(createTest)
        self.searchInput.setGeometry(QtCore.QRect(30, 140, 231, 25))
        self.searchInput.setObjectName("searchInput")
        
        self.searchSubmit = QtWidgets.QPushButton(createTest)
        self.searchSubmit.setGeometry(QtCore.QRect(260, 140, 101, 25))
        self.searchSubmit.setObjectName("searchSubmit")
        self.searchSubmit.clicked.connect(self.search)
        
        self.questionList = QtWidgets.QListWidget(createTest)
        self.questionList.setGeometry(QtCore.QRect(30, 180, 331, 271))
        self.questionList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.questionList.setObjectName("questionList")
        
        self.addSelectedToTest = QtWidgets.QPushButton(createTest)
        self.addSelectedToTest.setGeometry(QtCore.QRect(180, 460, 181, 25))
        self.addSelectedToTest.setObjectName("addSelectedToTest")
        self.addSelectedToTest.clicked.connect(self.addQuestionsToTest)

        self.label_3 = QtWidgets.QLabel(createTest)
        self.label_3.setGeometry(QtCore.QRect(40, 510, 341, 31))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(createTest)
        self.buttonBox.accepted.connect(lambda: self.saveTest(createTest))
        self.buttonBox.rejected.connect(createTest.close)
        QtCore.QMetaObject.connectSlotsByName(createTest)

    def retranslateUi(self, createTest):
        _translate = QtCore.QCoreApplication.translate
        createTest.setWindowTitle(_translate("createTest", "Create a Test"))
        self.label_6.setText(_translate("createTest", "Create a Test"))
        self.label_2.setText(_translate("createTest", "Test Name:"))
        self.label.setText(_translate("createTest", "Find questions by searching for a tag:"))
        self.searchSubmit.setText(_translate("createTest", "Search"))
        __sortingEnabled = self.questionList.isSortingEnabled()
        self.questionList.setSortingEnabled(False)
        self.questionList.setSortingEnabled(__sortingEnabled)
        self.addSelectedToTest.setText(_translate("createTest", "Add selected to Test"))
        self.label_3.setText(_translate("createTest", "Once finished adding questions, save the test!"))

    def search(self):
        # get value of search input
        term = self.searchInput.text()

        # clear existing list entries
        self.questionList.clear()

        # search question bank for questions with tags matching search term
        questions = QuestionBank.getInstance().findQuestionsByTag(term)

        # add matching entries to list
        for question in questions:
            item = QtWidgets.QListWidgetItem()
            item.setText('{} - {}'.format(question.ident, question.question))
            self.questionList.addItem(item)
        
    def addQuestionsToTest(self):
        # check whether a test exists already exits and if not create one
        if not hasattr(self, 'test'):
            self.test = Test()


        # get idents of selected items
        questionIdents = []
        for item in self.questionList.selectedItems():
            questionIdents.append([y.strip() for y in item.text().split('-')][0])

        # get questions from question bank
        questions = QuestionBank.getInstance().getQuestions()

        # loop question idents and add to test
        for ident in questionIdents:
            self.test.add(questions[ident])

    def saveTest(self, dialog):
        if self.testNameInput.text():
            self.test.setName(self.testNameInput.text())

        # add the test we have been adding questions to the test bank in order for us to re-use later,
        bank = TestBank.getInstance()
        bank.add(self.test)
        bank.save()

        # close dialog
        dialog.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createTest = QtWidgets.QDialog()
    ui = CreateTestUi()
    ui.setupUi(createTest)
    createTest.show()
    sys.exit(app.exec_())

