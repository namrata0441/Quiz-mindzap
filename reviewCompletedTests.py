from PyQt5 import QtCore, QtGui, QtWidgets


class ReviewCompletedTestsUi(object):
    def setupUi(self, ReviewTests):
        ReviewTests.setObjectName("ReviewTests")
        ReviewTests.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(ReviewTests)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(ReviewTests)
        self.label.setGeometry(QtCore.QRect(100, 10, 220, 61))
        self.label.setObjectName("label")

        self.retranslateUi(ReviewTests)
        self.buttonBox.accepted.connect(ReviewTests.accept)
        self.buttonBox.rejected.connect(ReviewTests.reject)
        QtCore.QMetaObject.connectSlotsByName(ReviewTests)

    def retranslateUi(self, ReviewTests):
        _translate = QtCore.QCoreApplication.translate
        ReviewTests.setWindowTitle(_translate("ReviewTests", "Review Completed Tests"))
        self.label.setText(_translate("ReviewTests", "WIP - Review Completed Tests"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReviewTests = QtWidgets.QDialog()
    ui = ReviewCompletedTestsUi()
    ui.setupUi(ReviewTests)
    ReviewTests.show()
    sys.exit(app.exec_())

