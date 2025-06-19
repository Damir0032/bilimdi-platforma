import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore

firebaseConfig = {
  'apiKey': "AIzaSyAClsdr7MwNndWFc7_L-BlZRNLeMjsxxxQ",
  'databaseURL': "https://bilimdi-platform.firebaseio.com",
  'authDomain': "edication-ce7a0.firebaseapp.com",
  'projectId': "edication-ce7a0",
  'storageBucket': "edication-ce7a0.firebasestorage.app",
  'messagingSenderId': "336523450386",
  'appId': "1:336523450386:web:c63104c263520f594c60cb",
  'measurementId': "G-GLKBYPXMPC"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

cred = credentials.Certificate(os.path.join(BASE_DIR, 'edu_platform', 'edication-ce7a0-firebase-adminsdk-fbsvc-b596336647.json'))

firebase_admin.initialize_app(cred)
db = firestore.client()
