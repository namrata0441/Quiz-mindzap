from PyQt5 import QtCore, QtGui, QtWidgets
from question.Question import Question, QuestionBank
from question.AutoMarkedQuestion import ArithmeticQuestion


class CreateArithmeticQuestionUi(object):
    """Create an ArithmeticQuestion ui

      This class creates the ui for creating an arithmetic question."""

    # setup up the ui
    def setupUi(self, createArithmeticQuestion):
        createArithmeticQuestion.setObjectName("createArithmeticQuestion")
        createArithmeticQuestion.resize(401, 305)
        self.buttonBox = QtWidgets.QDialogButtonBox(createArithmeticQuestion)
        self.buttonBox.setGeometry(QtCore.QRect(30, 260, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.questionInput = QtWidgets.QLineEdit(createArithmeticQuestion)
        self.questionInput.setGeometry(QtCore.QRect(160, 50, 211, 21))
        self.questionInput.setObjectName("questionInput")
        self.answerInput = QtWidgets.QLineEdit(createArithmeticQuestion)
        self.answerInput.setGeometry(QtCore.QRect(160, 80, 211, 21))
        self.answerInput.setObjectName("answerInput")
        self.label = QtWidgets.QLabel(createArithmeticQuestion)
        self.label.setGeometry(QtCore.QRect(30, 50, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(createArithmeticQuestion)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 111, 20))
        self.label_2.setObjectName("label_2")
        self.tagsInput = QtWidgets.QPlainTextEdit(createArithmeticQuestion)
        self.tagsInput.setGeometry(QtCore.QRect(30, 210, 341, 41))
        self.tagsInput.setObjectName("TagsInput")
        self.label_4 = QtWidgets.QLabel(createArithmeticQuestion)
        self.label_4.setGeometry(QtCore.QRect(30, 180, 341, 31))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(createArithmeticQuestion)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 67, 17))
        self.label_3.setObjectName("label_3")
        self.pointsInput = QtWidgets.QComboBox(createArithmeticQuestion)
        self.pointsInput.setGeometry(QtCore.QRect(160, 120, 211, 25))
        self.pointsInput.setObjectName("pointsInput")
        self.pointsInput.addItem("")
        self.pointsInput.addItem("")
        self.pointsInput.addItem("")
        self.pointsInput.addItem("")
        self.pointsInput.addItem("")
        self.pointsInput.addItem("")
        self.pointsInput.addItem("")
        self.pointsInput.addItem("")
        self.pointsInput.addItem("")
        self.pointsInput.addItem("")
        self.pointsInput.setItemText(9, "")
        self.label_5 = QtWidgets.QLabel(createArithmeticQuestion)
        self.label_5.setGeometry(QtCore.QRect(30, 150, 141, 17))
        self.label_5.setObjectName("label_5")
        self.yearGroupInput = QtWidgets.QSpinBox(createArithmeticQuestion)
        self.yearGroupInput.setGeometry(QtCore.QRect(160, 150, 211, 21))
        self.yearGroupInput.setMinimum(1)
        self.yearGroupInput.setMaximum(13)
        self.yearGroupInput.setObjectName("yearGroupInput")
        self.label_6 = QtWidgets.QLabel(createArithmeticQuestion)
        self.label_6.setGeometry(QtCore.QRect(30, 10, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.retranslateUi(createArithmeticQuestion)
        self.buttonBox.accepted.connect(lambda: self.createQuestion(createArithmeticQuestion))
        self.buttonBox.rejected.connect(createArithmeticQuestion.close)
        QtCore.QMetaObject.connectSlotsByName(createArithmeticQuestion)

    def retranslateUi(self, createArithmeticQuestion):
        _translate = QtCore.QCoreApplication.translate
        createArithmeticQuestion.setWindowTitle(_translate("createArithmeticQuestion", "Create an Arithmetic Question"))
        self.label.setText(_translate("createArithmeticQuestion", "Question:"))
        self.label_2.setText(_translate("createArithmeticQuestion", "Correct Answer:"))
        self.label_4.setText(_translate("createArithmeticQuestion", "Tags (Enter values, separated by a comma):"))
        self.label_3.setText(_translate("createArithmeticQuestion", "Points:"))
        self.pointsInput.setItemText(0, _translate("createArithmeticQuestion", "10"))
        self.pointsInput.setItemText(1, _translate("createArithmeticQuestion", "15"))
        self.pointsInput.setItemText(2, _translate("createArithmeticQuestion", "20"))
        self.pointsInput.setItemText(3, _translate("createArithmeticQuestion", "25"))
        self.pointsInput.setItemText(4, _translate("createArithmeticQuestion", "30"))
        self.pointsInput.setItemText(5, _translate("createArithmeticQuestion", "35"))
        self.pointsInput.setItemText(6, _translate("createArithmeticQuestion", "40"))
        self.pointsInput.setItemText(7, _translate("createArithmeticQuestion", "45"))
        self.pointsInput.setItemText(8, _translate("createArithmeticQuestion", "50"))
        self.label_5.setText(_translate("createArithmeticQuestion", "Target year group:"))
        self.label_6.setText(_translate("createArithmeticQuestion", "Create an Arithmetic Question"))

    def createQuestion(self, dialog):
        # get the input values
        answer = self.answerInput.text()
        question = self.questionInput.text()
        points = self.pointsInput.currentText()
        tags = self.tagsInput.toPlainText()
        yearGroup = self.yearGroupInput.text()

        # some simple validation, if the question or answer is empty then just return.
        # Potential improvement would be to show an error message to the user in the ui.
        if not answer or not question:
            return False

        # if no tags, use year group as default
        if not tags:
            tags = [yearGroup]
        else:
            # string to list of tags
            tags = Question.stringInputToList(tags)

        # we know that this is an arithmetic question, so can just new up an ArithmeticQuestion here.
        question = ArithmeticQuestion(question, answer, tags, points)

        # get singleton questionBank, add new question and save
        bank = QuestionBank.getInstance()
        bank.add(question)
        bank.save()

        # close dialog
        dialog.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createArithmeticQuestion = QtWidgets.QDialog()
    ui = CreateArithmeticQuestionUi()
    ui.setupUi(createArithmeticQuestion)
    createArithmeticQuestion.show()
    sys.exit(app.exec_())

