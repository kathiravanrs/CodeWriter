import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('certificate.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
for i in range(1, 5):
    for j in range(1, 5):
        user_ref = db.collection(u'codes').document(u'challenges')
        doc_ref = user_ref.collection(u'WeeklyChallenge ' + str(i)).document(
            u'Create 4 class Person, Staff, TemporaryStaff and a Main class . . .')
        doc_ref.set({
            u'Question': u'Create 4 class Person, Staff, TemporaryStaff and a Main class . . .',
            u'Answer': '''
import java.util.Scanner;

class Person {

private String name;

Person(String name) {
this.name = name;
}

String getName() {
return name;
}

public void setName(String name) {
this.name = name;
}

public void DisplayName(){
System.out.println(name);
}
}

class Staff extends Person{
int getStaffID() {
return staffID;
}

public void setStaffID(int staffID) {
this.staffID = staffID;
}

Staff(String name, int staffID) {
super(name);
this.staffID = staffID;
}

private int staffID;
}

class TemporaryStaff extends Staff {
TemporaryStaff(String name, int staffID, int days, int hours) {
super(name, staffID);
this.days = days;
this.hours = hours;
}

private int getDays() {
return days;
}

public void setDays(int days) {
this.days = days;
}

private int getHours() {
return hours;
}

public void setHours(int hours) {
this.hours = hours;
}

private int days;
private int hours;

private int salary() {
return days * hours * 50;
}

void display() {
System.out.println("Name : " + getName());
System.out.println("Staff Id : " + getStaffID());
System.out.println("No. of Days : " + getDays());
System.out.println("No. of Hours Worked: " + getHours());
System.out.println("Total Salary : " + salary());
}

}
class main{
public static void main(String args[]){
Scanner scanner = new Scanner(System.in).useDelimiter("\\n");
String n = scanner.nextLine();
int id = scanner.nextInt();
int days = scanner.nextInt();
int hour = scanner.nextInt();
TemporaryStaff st = new TemporaryStaff(n, id, days, hour);
st.display();
}

}
'''
        })
