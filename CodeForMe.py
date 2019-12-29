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


cred = credentials.Certificate('certificate.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

root = Tk()
root.title("Code For Me")
root.minsize(400, 400)


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

    Label(mainframe, text="within 5 seconds.").grid(row=13, column=1)

# link function to change dropdown
tkvar.trace('w', change_dropdown)
root.mainloop()
