from PyQt4.QtGui import *

def showError(title, message):
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Warning)
	msg.setText(message)
	msg.setWindowTitle(title)
	msg.setStandardButtons(QMessageBox.Ok)
	msg.exec_()

def showMsg(title, message):
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Information)
	msg.setText(message)
	msg.setWindowTitle(title)
	msg.setStandardButtons(QMessageBox.Ok)
	msg.exec_()
