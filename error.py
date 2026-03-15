
from PyQt5.QtWidgets import QMessageBox

#displays an error message for the user after an error occurs
def displayError(self, ErrorName, ErrorTitle):

    ErrorMsgBox = QMessageBox(self)
    ErrorMsgBox.setIcon(QMessageBox.Warning)

    ErrorMsgBox.setText(ErrorName)
    ErrorMsgBox.setWindowTitle(ErrorTitle)
    ErrorMsgBox.exec_()

