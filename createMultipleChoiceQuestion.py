from PyQt5 import QtCore, QtGui, QtWidgets
from question.Question import Question, QuestionBank
from question.AutoMarkedQuestion import AutoMarkedQuestion


class CreateMultipleChoiceQuestionUi(object):
    def setupUi(self, createMultipleChoiceQuestion):
        """Create a MultipleChoiceQuestion ui

        This class creates the ui for creating a multiple choice question."""

        # setup up the ui
        createMultipleChoiceQuestion.setObjectName("createMultipleChoiceQuestion")
        createMultipleChoiceQuestion.resize(401, 593)
        self.buttonBox = QtWidgets.QDialogButtonBox(createMultipleChoiceQuestion)
        self.buttonBox.setGeometry(QtCore.QRect(30, 550, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.questionInput = QtWidgets.QLineEdit(createMultipleChoiceQuestion)
        self.questionInput.setGeometry(QtCore.QRect(160, 50, 211, 21))
        self.questionInput.setObjectName("questionInput")

        self.correctAnswerInput = QtWidgets.QLineEdit(createMultipleChoiceQuestion)
        self.correctAnswerInput.setGeometry(QtCore.QRect(160, 370, 211, 21))
        self.correctAnswerInput.setObjectName("correctAnswerInput")

        self.label = QtWidgets.QLabel(createMultipleChoiceQuestion)
        self.label.setGeometry(QtCore.QRect(30, 50, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(createMultipleChoiceQuestion)
        self.label_2.setGeometry(QtCore.QRect(30, 370, 111, 20))
        self.label_2.setObjectName("label_2")

        self.tagsInput = QtWidgets.QPlainTextEdit(createMultipleChoiceQuestion)
        self.tagsInput.setGeometry(QtCore.QRect(30, 500, 341, 41))
        self.tagsInput.setObjectName("tagsInput")

        self.label_4 = QtWidgets.QLabel(createMultipleChoiceQuestion)
        self.label_4.setGeometry(QtCore.QRect(30, 470, 341, 31))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(createMultipleChoiceQuestion)
        self.label_3.setGeometry(QtCore.QRect(30, 410, 67, 17))
        self.label_3.setObjectName("label_3")


        self.pointsInput = QtWidgets.QComboBox(createMultipleChoiceQuestion)
        self.pointsInput.setGeometry(QtCore.QRect(160, 410, 211, 25))
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
        self.label_5 = QtWidgets.QLabel(createMultipleChoiceQuestion)
        self.label_5.setGeometry(QtCore.QRect(30, 440, 141, 17))
        self.label_5.setObjectName("label_5")
        self.yearGroupInput = QtWidgets.QSpinBox(createMultipleChoiceQuestion)
        self.yearGroupInput.setGeometry(QtCore.QRect(160, 440, 211, 21))
        self.yearGroupInput.setMinimum(1)
        self.yearGroupInput.setMaximum(13)
        self.yearGroupInput.setObjectName("yearGroupInput")
        self.label_6 = QtWidgets.QLabel(createMultipleChoiceQuestion)
        self.label_6.setGeometry(QtCore.QRect(30, 10, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(createMultipleChoiceQuestion)
        self.label_7.setGeometry(QtCore.QRect(30, 170, 67, 17))
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(createMultipleChoiceQuestion)
        self.line.setGeometry(QtCore.QRect(30, 70, 341, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.choiceA = QtWidgets.QLineEdit(createMultipleChoiceQuestion)
        self.choiceA.setGeometry(QtCore.QRect(160, 170, 211, 21))
        self.choiceA.setObjectName("choiceA")

        self.choiceB = QtWidgets.QLineEdit(createMultipleChoiceQuestion)
        self.choiceB.setGeometry(QtCore.QRect(160, 200, 211, 21))
        self.choiceB.setObjectName("choiceB")

        self.choiceC = QtWidgets.QLineEdit(createMultipleChoiceQuestion)
        self.choiceC.setGeometry(QtCore.QRect(160, 230, 211, 21))
        self.choiceC.setObjectName("choiceC")

        self.choiceD = QtWidgets.QLineEdit(createMultipleChoiceQuestion)
        self.choiceD.setGeometry(QtCore.QRect(160, 260, 211, 21))
        self.choiceD.setObjectName("choiceD")

        self.textBrowser = QtWidgets.QTextBrowser(createMultipleChoiceQuestion)
        self.textBrowser.setGeometry(QtCore.QRect(30, 90, 341, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.line_2 = QtWidgets.QFrame(createMultipleChoiceQuestion)
        self.line_2.setGeometry(QtCore.QRect(30, 290, 341, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_8 = QtWidgets.QLabel(createMultipleChoiceQuestion)
        self.label_8.setGeometry(QtCore.QRect(30, 200, 67, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(createMultipleChoiceQuestion)
        self.label_9.setGeometry(QtCore.QRect(30, 230, 67, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(createMultipleChoiceQuestion)
        self.label_10.setGeometry(QtCore.QRect(30, 260, 67, 17))
        self.label_10.setObjectName("label_10")
        self.textBrowser_2 = QtWidgets.QTextBrowser(createMultipleChoiceQuestion)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 310, 341, 51))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(createMultipleChoiceQuestion)
        self.buttonBox.accepted.connect(lambda: self.createQuestion(createMultipleChoiceQuestion))
        self.buttonBox.rejected.connect(createMultipleChoiceQuestion.close)
        QtCore.QMetaObject.connectSlotsByName(createMultipleChoiceQuestion)

    def retranslateUi(self, createMultipleChoiceQuestion):
        _translate = QtCore.QCoreApplication.translate
        createMultipleChoiceQuestion.setWindowTitle(_translate("createMultipleChoiceQuestion", "Create a Multiple Choice Question"))
        self.correctAnswerInput.setPlaceholderText(_translate("createMultipleChoiceQuestion", "e.g a or c,d"))
        self.label.setText(_translate("createMultipleChoiceQuestion", "Question:"))
        self.label_2.setText(_translate("createMultipleChoiceQuestion", "Correct Answers:"))
        self.label_4.setText(_translate("createMultipleChoiceQuestion", "Tags (Enter values, separated by a comma):"))
        self.label_3.setText(_translate("createMultipleChoiceQuestion", "Points:"))
        self.pointsInput.setItemText(0, _translate("createMultipleChoiceQuestion", "10"))
        self.pointsInput.setItemText(1, _translate("createMultipleChoiceQuestion", "15"))
        self.pointsInput.setItemText(2, _translate("createMultipleChoiceQuestion", "20"))
        self.pointsInput.setItemText(3, _translate("createMultipleChoiceQuestion", "25"))
        self.pointsInput.setItemText(4, _translate("createMultipleChoiceQuestion", "30"))
        self.pointsInput.setItemText(5, _translate("createMultipleChoiceQuestion", "35"))
        self.pointsInput.setItemText(6, _translate("createMultipleChoiceQuestion", "40"))
        self.pointsInput.setItemText(7, _translate("createMultipleChoiceQuestion", "45"))
        self.pointsInput.setItemText(8, _translate("createMultipleChoiceQuestion", "50"))
        self.label_5.setText(_translate("createMultipleChoiceQuestion", "Target year group:"))
        self.label_6.setText(_translate("createMultipleChoiceQuestion", "Create a Multiple Choice Question"))
        self.label_7.setText(_translate("createMultipleChoiceQuestion", "Choice A"))
        self.textBrowser.setHtml(_translate("createMultipleChoiceQuestion", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You can add up to 4 possible answers, or alternatively could simply be a true/false question</p></body></html>"))
        self.label_8.setText(_translate("createMultipleChoiceQuestion", "Choice B"))
        self.label_9.setText(_translate("createMultipleChoiceQuestion", "Choice C"))
        self.label_10.setText(_translate("createMultipleChoiceQuestion", "Choice D"))
        self.textBrowser_2.setHtml(_translate("createMultipleChoiceQuestion", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">There can be more than one correct answer, just seperate the values with a comma</p></body></html>"))

    def createQuestion(self, dialog):
        # get the input values
        question = self.questionInput.text()

        choices = {
            'a': self.choiceA.text(),
            'b': self.choiceB.text(),
            'c': self.choiceC.text(),
            'd': self.choiceD.text(),
        }

        correctAnswer = self.correctAnswerInput.text()
        points = self.pointsInput.currentText()
        yearGroup = self.yearGroupInput.text()
        tags = self.tagsInput.toPlainText()

        # some simple validation, if the question or answer is empty then just return.
        # Potential improvement would be to show an error message to the user in the ui.
        if not question or not correctAnswer:
            return False

        # could also check that the correct answer does in fact exist in choices

        # if no tags, use year group as default
        if not tags:
            tags = [yearGroup]
        else:
            # string to list of tags
            tags = Question.stringInputToList(tags)

        # use static factory method to get correct question object
        question = AutoMarkedQuestion.createFromInput(question, choices, Question.stringInputToList(correctAnswer),
                                                      tags, points)

        # get singleton questionBank, add new question and save
        bank = QuestionBank.getInstance()
        bank.add(question)
        bank.save()

        # close dialog
        dialog.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createMultipleChoiceQuestion = QtWidgets.QDialog()
    ui = CreateMultipleChoiceQuestionUi()
    ui.setupUi(createMultipleChoiceQuestion)
    createMultipleChoiceQuestion.show()
    sys.exit(app.exec_())

