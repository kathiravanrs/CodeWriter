from tkinter import *
import pyautogui
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def findWeeks():
    docs = db.collection(u'weeks').stream()
    for doc in docs:
        return doc.to_dict()['number']


def findQues(i):
    docs = db.collection(str(i)).stream()
    for doc in docs:
        return doc.to_dict()['question']


def typeCode(challenge, program):
    users_ref = db.collection('codes').document('challenges').collection(str(challenge)).document(str(program))
    doc = users_ref.get()
    code = doc.to_dict()['Answer']
    time.sleep(5)
    pyautogui.typewrite(code)
    for i in range(1, 50):
        pyautogui.keyDown('Delete')


cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "weeklychallenge-93ffe",
  "private_key_id": "0d117e8e31a6787b945d0e60b24da11b39c801bd",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCa9mn5oQjElX1l\nTF/pVFTLChu+qni8nCPhydZGM5g5uw7hYTST6t7skwwV1yGXPTAGzGMZ/fONdYzg\n+y1sp1zaXG7BOSzFtf/pel8SBt6PJknTAB8G+5pqpVe+qzDtR1p7fyR6HXBN+FSG\nZRLR4dSQqfYw3pqG2Cegey58hP9sIrZfnEUtMlrerXPRMWBk3Qt2UDsJox6eBPQT\nE3UShdED1bWr9+FCik3zo26534BG6I1iQZj7kgtMrIPrqZVf7H1cSnvrQeWLzRIC\nuin5hkM8x85qIZfQQyazolhptA+5yV8U7siCueX3chu/HBtqoxmavS32AU7rTn2C\n6A192tAZAgMBAAECggEAFApVFzr7ssywbFbNupO06ZMzlltehOnefBdJtkd64tBt\nsrkK/ywrS0YTFIn/Zps7qE1rbZOZmUw//WKOc9RLHlRA4I0/3IvWfj/cpqyrwLCP\ncJG98X29cRhT+i0ShUUqjvkY4xAGk5bPe5f7sJf3kQPh+lz3eAPhUBBOKT1b+QRq\ntBbGDkzEwIPrao2wMu4+xM+Razh0gxDyPd4qquhcdLl6r52gnJzItwc7Kfs/ILs5\n1RXBE9GoZTC3ZNVBbKUW/WGfyLHcm6ukQZJ7CACC9xmCGVN8z/BtutQ245h1Em/U\nroBHobe+Vdp6Eu+bRj1d/mFsudN9Vn4UhP4oHOiP3wKBgQDH/+PDJ/mEpZHfAcki\nMop4QnntXb5eiDDuBFPVyx/IOcX7z05sMLWS1RYEm02XnJZu9k4/Z9lLFzmbRt/g\nwD0vC+emp4HCCw89OeucXpbamCMb+l+LyFKhLWwhD34fS/RsDM/WFGddkWvwjkOV\n5/ofKCxZNHW1TgYJ8yRivdmDOwKBgQDGWj1A0kHCv2CpWaanQpMKeqwOIIxGEpzY\ncGNUpAz2+yVisDTMwwPTRg/RStKS5lOsJduiYh5SoXUgUxhCnn3EINsDOgFPsQBI\npKjmXL4OJX9XyDmX0hPHzPusQ/RYNzHHqa/hWaqIWa0RKC/KqzDFiVeyFqu3wlyc\n2WXojACcuwKBgAUmuh8UsICSIyezTBLtalOeorVSbMzShTAcPGyNRsxJcKgDtuli\nd8rIYkDMHzuAdP92qJ1Jd3dPqdQuByYqzWigzd6lAdqVnlbdXwwwA4Kt2HmoAT4A\ncuBj4x0W4RC9TBZcXh4NeHwYesc/Ys5Bo1eaGUpS55U75TvsX0uLyEZxAoGAQjNB\n+E10VzwqVbsvLOnCS6APppNkXcq+gFpaPJiYHyJJIvvuU1zO/QeIJfEUAKVQzcbA\n3BxlRGzQu54gHbPqA7h3gEcuwtsvXg9es6vGXtBTBQg1eJ9LrMaURLVVas/ZFGtk\n4RBdIy7S3UQNV1X1bChflXeNjkIXSN4h7hAz8BsCgYBteMdb1I/JHUId36vlYFh5\ndBwq/t0WcNXZXBmg4WRKzIeov177uqYReSMaqYyW+SKEB7cNKusA6Xabx9xkY3De\n4b3v89qH5Ae6kL9tLTbwo8DkQS5DQozLjDNrKxuvZQUbG9DCSIzhWDxbiNniacnx\npM4GUGCWT2NNXkVRGsJ7HQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-x6ai3@weeklychallenge-93ffe.iam.gserviceaccount.com",
  "client_id": "117181522046355754192",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-x6ai3%40weeklychallenge-93ffe.iam.gserviceaccount.com"
}
)
print('This program types the selected code wherever the cursor is placed.\n'
      'Open the online coding portal first and then choose the required program.\n')
firebase_admin.initialize_app(cred)
db = firestore.client()

root = Tk()
root.title("Code For Me      -Kathiravan S")
root.minsize(500, 500)


# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.pack(pady=100, padx=100)

tkvar = StringVar(root)
tkvar2 = StringVar(root)

# Dictionary with options
choicesWeek = findWeeks()
tkvar.set('Select Week')  # set the default option

WeekMenu = OptionMenu(mainframe, tkvar, *choicesWeek)
Label(mainframe, text="Choose the Challenge").grid(row=1, column=1)
WeekMenu.grid(row=2, column=1)


# on change dropdown value
def change_dropdown(*args):
    selected = tkvar.get()
    print(tkvar.get())
    quesChoices = findQues(selected)
    print(quesChoices)
    tkvar2.set('Select Question')  # set the default option

    quesMenu = OptionMenu(mainframe, tkvar2, *quesChoices)
    Label(mainframe, text="Choose the Question").grid(row=4, column=1)
    quesMenu.grid(row=5, column=1)

    Menu = Button(mainframe, text='Start', command=lambda: typeCode(tkvar.get(), tkvar2.get()))
    Label(mainframe, text="").grid(row=6, column=1)
    Menu.grid(row=7, column=1)
    Label(mainframe, text="").grid(row=8, column=1)
    Label(mainframe, text="").grid(row=9, column=1)
    Label(mainframe, text="").grid(row=10, column=1)

    Label(mainframe, text="Keep the online coding portal ready before clicking START.").grid(row=11, column=1)
    Label(mainframe, text="After clicking START, quickly move to the portal and click on the coding Area").\
        grid(row=12, column=1)
    print('\nClick on the coding area immediately after pressing START')
    Label(mainframe, text="within 5 seconds.").grid(row=13, column=1)


# link function to change dropdown
tkvar.trace('w', change_dropdown)
root.mainloop()
