import common
import sys
import backend
from PyQt4.QtGui import *
import json
from bson.json_util import dumps

class Data(QDialog):
	def __init__(self, parent=None):
		super(QDialog, self).__init__(parent)
		
		grid = QGridLayout()
		self.setLayout(grid)
		
		self.resize(400, 400)
		self.move(300, 300)
		self.setWindowTitle('Mongo Admin - Data')

		self.collectionDropdown = QComboBox()
		self.databaseDropdown = QComboBox()
		self.dbs = backend.getDbs()['message']
		self.databaseDropdown.currentIndexChanged.connect(self.loadCollections)
		for db in self.dbs:
			self.databaseDropdown.addItem(db)

		self.queryLineEdit = QLineEdit()
		self.queryLineEdit.setPlaceholderText('query')

		self.resultsArea = QTextEdit()

		deleteBtn = QPushButton("Delete")
		deleteBtn.clicked.connect(self.deleteData)
		findBtn = QPushButton("Find")
		findBtn.clicked.connect(self.findData)

		grid.addWidget(self.databaseDropdown, 1, 1)
		grid.addWidget(self.collectionDropdown, 1, 2)
		grid.addWidget(self.queryLineEdit, 2, 1)
		grid.addWidget(findBtn, 2, 2)
		grid.addWidget(deleteBtn, 2, 3)
		grid.addWidget(self.resultsArea, 3, 1, 2, 3)

	def loadCollections(self):
		self.collectionDropdown.clear()
		db = self.dbs[self.databaseDropdown.currentIndex()]
		collections = backend.getCollections(db)['message']
		print collections
		for collection in collections:
			self.collectionDropdown.addItem(collection)

	def findData(self, getAll=False):
		db = str(self.dbs[self.databaseDropdown.currentIndex()])
		collection = str(self.collectionDropdown.currentText())
		query = str(self.queryLineEdit.text())
		if len(query) > 0 and getAll == False:
			query = json.loads(query)
		else:
			query = {}
		result = backend.find(db, collection, query)
		if result['code'] == 1:
			result['message'] = dumps(result['message']).replace(',', ',\n')
		self.resultsArea.setText(result['message'])

	def deleteData(self):
		db = str(self.dbs[self.databaseDropdown.currentIndex()])
		collection = str(self.collectionDropdown.currentText())
		query = str(self.queryLineEdit.text())
		if len(query) > 0:
			query = json.loads(query)
		result = backend.delete(db, collection, query)
		self.findData(True)
