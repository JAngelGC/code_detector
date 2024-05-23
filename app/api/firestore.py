import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("/home/angelg/Documents/school/code_detector/app/api/private_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()