from pymongo import MongoClient

client = MongoClient()

def insert(dbname, collection, data):
	try:
		db = client[dbname]
		collection = db[collection]
		collection.insert(data)
	except:
		return {"code": 2, "message": "Insert failed"}

	return {"code": 1, "message": "Successfully inserted"}


def find(dbname, collection, query):
	try:
		db = client[dbname]
		collection = db[collection]
		result = collection.find(query)
	except:
		return {"code": 2, "message": "Find error"}

	return {"code": 1, "message": list(result)}

def delete(dbname, collection, query):
	try:
		db = client[dbname]
		collection = db[collection]
		collection.remove(query)
	except:
		return {"code": 2, "message": "Delete error"}

	return {"code": 1, "message": "Successfully Deleted"}

def login(user, password):
	try:
		db = client['_config']
		collection = db['_users']
		result = collection.find({"user": user, "password": password})
	except:
		return {"code": 2, "message": "Login error"}

	return {"code": 1, "message": list(result)}

def signup(user, password):
	try:
		db = client['_config']
		collection = db['_users']
		collection.insert({"user": user, "password": password})
	except:
		return {"code": 2, "message": "Signup error"}

	return {"code": 1, "message": "Signed up sucessfully"}
