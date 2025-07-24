from PyQt5 import QtCore, QtGui, QtWidgets
from question.Test import TestBank


class ListTestsUi(object):
    def setupUi(self, listTests):
        listTests.setObjectName("listTests")
        listTests.resize(399, 400)
        self.buttonBox = QtWidgets.QDialogButtonBox(listTests)
        self.buttonBox.setGeometry(QtCore.QRect(30, 350, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")

        self.label = QtWidgets.QLabel(listTests)
        self.label.setGeometry(QtCore.QRect(30, 10, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.testList = QtWidgets.QListWidget(listTests)
        self.testList.setGeometry(QtCore.QRect(30, 50, 331, 271))
        self.testList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.testList.setObjectName("testList")

        self.populateTests()

        self.retranslateUi(listTests)

        self.buttonBox.rejected.connect(listTests.close)
        QtCore.QMetaObject.connectSlotsByName(listTests)

    def retranslateUi(self, listTests):
        _translate = QtCore.QCoreApplication.translate
        listTests.setWindowTitle(_translate("listTests", "List Tests"))
        self.label.setText(_translate("listTests", "All Tests"))

        __sortingEnabled = self.testList.isSortingEnabled()
        self.testList.setSortingEnabled(False)
        self.testList.setSortingEnabled(__sortingEnabled)

    def populateTests(self):
        # search question bank for questions with tags matching search term
        tests = TestBank.getInstance().getTests()

        # add matching entries to list
        for test in tests.values():
            if test.getName():
                name = test.getName()
            else:
                name = test.ident

            item = QtWidgets.QListWidgetItem()
            item.setText('{}'.format(name))
            self.testList.addItem(item)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    listTests = QtWidgets.QDialog()
    ui = ListTestsUi()
    ui.setupUi(listTests)
    listTests.show()
    sys.exit(app.exec_())

