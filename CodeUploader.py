import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
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
firebase_admin.initialize_app(cred)

db = firestore.client()

user_ref = db.collection(u'codes').document(u'challenges')
doc_ref = user_ref.collection(u'WeeklyChallenge 2').document(
    u'Area Perimeter')
doc_ref.set({
    u'Question': u'Area Perimeter',
    u'Answer': '''
import java.util.Scanner;

abstract class Shape {
int length;
int width;
int radius;

abstract void calculatePerimeter();

abstract void calculateArea();
}

class Square extends Shape {
public Square(int width) {
this.width = width;
}

@Override
void calculatePerimeter() {
double perimeter = width * 4;
System.out.printf("Perimeter : %.2f\\n", perimeter);
}

@Override
void calculateArea() {
double area = width * width;
System.out.printf("Area : %.2f\\n", area);
}
}

class Rectangle extends Shape {
public Rectangle(int width, int length) {
this.width = width;
this.length = length;
}

@Override
void calculatePerimeter() {
double perimeter = width * 2 + length * 2;
System.out.printf("Perimeter : %.2f\\n", perimeter);
}

@Override
void calculateArea() {
double area = width * length;
System.out.printf("Area : %.2f\\n", area);
}
}

class Circle extends Shape {
public Circle(int radius) {
this.radius = radius;
}

@Override
void calculatePerimeter() {
double perimeter = 2 * 3.141592 * radius;
System.out.printf("Circumference : %.2f\\n", perimeter);
}

@Override
void calculateArea() {
double area = 3.141592 * radius * radius;
System.out.printf("Area : %.2f\\n", area);
}
}

class Triangle extends Shape {
public Triangle(int radius, int length, int width) {
this.radius = radius;
this.width = width;
this.length = length;
}

@Override
void calculatePerimeter() {
double perimeter = length + width + radius;
System.out.printf("Perimeter : %.2f\\n", perimeter);
}

@Override
void calculateArea() {
int p = (radius + width + length) / 2;
double area = Math.sqrt((p - radius) * (p - width) * (p - length) * p);
System.out.printf("Area : %.2f\\n", area);
}
}

class Main4 {
public static void main(String[] args) {
Scanner scanner = new Scanner(System.in);
char choice = scanner.next().charAt(0);

switch (choice) {
case 'S':
int len = scanner.nextInt();
Square square = new Square(len);
square.calculatePerimeter();
square.calculateArea();
break;

case 'R':
int width = scanner.nextInt();
int length = scanner.nextInt();
Rectangle rectangle = new Rectangle(width, length);
rectangle.calculatePerimeter();
rectangle.calculateArea();
break;

case 'C':
int rad = scanner.nextInt();
Circle circle = new Circle(rad);
circle.calculatePerimeter();
circle.calculateArea();
break;

case 'T':
int a = scanner.nextInt();
int b = scanner.nextInt();
int c = scanner.nextInt();
Triangle triangle = new Triangle(a, b, c);
triangle.calculatePerimeter();
triangle.calculateArea();
break;
}
}
}
'''
        })
