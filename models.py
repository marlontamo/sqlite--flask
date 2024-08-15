from app import db
from flask import render_template



class Person(db.Model):
    __tablaname__='people'
    pid =db.Column(db.Integer,primary_key=True)
    name =db.Column(db.Text,nullable=False)
    age =db.Column(db.Integer)
    job = db.Column(db.Text)
    
    def __init__(self, name: str, job: str, age: int): 
        self.name = name 
        self.job = job 
        self.age = age
    
    def create(self): 
        new_user = Person(self.name, self.age, self.job) 
        db.session.add(new_user) 
        db.session.commit() 
        return f'Person {self.name} was added'
    
    def __repr__(self):
        return f'Person with name {self.name} and age {self.job}'