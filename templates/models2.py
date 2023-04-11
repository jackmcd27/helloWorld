from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = "student"

    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100))
    phone_num = db.Column(db.String(10), nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey('university.university_id'))
    major_id1 = db.Column(db.Integer, db.ForeignKey('major.major_id'))
    major_2 = db.Column(db.String(25)) #Made second major text in case not biz related
    year = db.Column(db.Integer, db.ForeignKey('year.year_id'))
    grad_year = db.Column(db.String(4))

def __init__(self, first_name, last_name, email, phone_num, university_id, major_id1, major_2, year_id, grad_year):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.major_id1 = major_id1
        self.major_2 = major_2
        self.phone_num = phone_num
        self.university_id = university_id
        self.year_id = year_id
        self.grad_year = grad_year

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    class Major(db.Model):
        __tablename__ = "major"

        major_id = db.Column(db.Integer, primary_key=True)
        major = db.Column(db.String(30), nullable=False)
        students = db.relationship('Student', backref='students')

     class University(db.Model):
         __tablename__ = "university"

         university_id = db.Column(db.Integer, primary_key=True)
         university = db.Column(db.String(30), nullable=False)
        students = db.relationship('Student', backref='students')


    class Year(db.Model):
        __tablename__ = "year"

        year_id = db.Column(db.Integer, primary_key=True)
        year = db.Column(db.String(30), nullable=False)
        students = db.relationship('Student', backref='students')