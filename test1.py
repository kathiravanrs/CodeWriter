import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('certificate.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
week_ref = db.collection(u'weeks').document(u'challenges')
ques_ref = db.collection(u'WeeklyChallenge 1').document(u'ques')
week_ref.set({u'number': ['WeeklyChallenge ' + str(j) for j in range(1, 5)]})
ques_ref.set({u'question': [u'Create 4 class Person, Staff, TemporaryStaff and a Main class . . .',
                            u'test',
                            u'test2',
                            u'test3']})
