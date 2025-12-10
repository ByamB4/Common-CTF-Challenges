# Cloud

Quick references for cloud misconfigurations commonly seen in CTFs.

## Quick wins
- Check if S3 buckets allow anonymous listing or downloads.
- Test if Firebase Realtime Database rules expose `.json` endpoints.
- Keep API keys out of traffic captures; treat them like passwords.

## AWS S3
- List and copy from a world-readable bucket:
  ```
  aws s3 ls s3://domain.mn
  aws s3 cp s3://domain.mn/flag.png flag.png
  ```

## Firebase
- Public database dump (if rules are lax):
  - https://app3-7d107-default-rtdb.firebaseio.com/.json
- Scanner: https://github.com/shivsahni/FireBaseScanner
- Python access example:
  ```py
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
  print(db.get(user["idToken"]).val())
  ```
