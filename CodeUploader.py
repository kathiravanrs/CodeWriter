import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('certificate.json')
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
