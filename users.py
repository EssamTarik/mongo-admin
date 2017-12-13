import common
import sys
import backend
from PyQt4.QtGui import *

class Users(QMainWindow):
	def __init__(self, parent=None):
		super(QMainWindow, self).__init__(parent)
		
		grid = QGridLayout()
		w = QWidget()
		w.setLayout(grid)
		
		self.resize(400, 400)
		self.move(300, 300)
		self.setWindowTitle('Mongo Admin - Users')
		self.setCentralWidget(w)

		addBtn = QPushButton('Add')
		addBtn.clicked.connect(self.addUser)

		self.newUserField = QLineEdit()
		self.newUserPasswordField = QLineEdit()
		self.newUserPasswordField.setEchoMode(QLineEdit.Password)

		self.UserList = QListWidget()
		
		grid.addWidget(self.newUserField, 1, 1)
		grid.addWidget(self.newUserPasswordField, 1, 2)
		grid.addWidget(addBtn, 1, 3)
		grid.addWidget(self.UserList, 2, 1)

		self.readUsers()

	def readUsers(self):
		users = backend.find('_config', '_users', {})['message']
		for user in users:
			listItem = QListWidgetItem(user['user'])
			self.UserList.addItem(listItem)

	def addUser(self):
		username = str(self.newUserField.text())
		password = str(self.newUserPasswordField.text())
		backend.insert('_config', '_users', {"user": username, "password": password})
		listItem = QListWidgetItem(username)
		self.UserList.addItem(listItem)