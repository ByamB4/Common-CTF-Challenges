import pyrebase
import requests

config = {
  "apiKey": "AIzaSyAXsK0qsx4RuLSA9C8IPSWd0eQ67HVHuJY",
  "authDomain": "firestorm-9d3db.firebaseapp.com",
  "databaseURL": "https://firestorm-9d3db-default-rtdb.firebaseio.com",
  "storageBucket": "firestorm-9d3db.appspot.com",
  "projectId": "firestorm-9d3db"
}


firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
email = "TK757567@pwnsec.xyz"
password = "C7_dotpsC7t7f_._In_i.IdttpaofoaIIdIdnndIfC"
user = auth.sign_in_with_email_and_password(email, password)

db = firebase.database()

print(db.get(user['idToken']).val()) 
