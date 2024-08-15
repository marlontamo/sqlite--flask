import time
from flask import redirect, render_template, request
from models import Person
def register_routes(app,db):
    
    @app.route('/list')
    def users_list():
        people = Person.query.all()
        return render_template('viewusers.html', people = people)
    
    @app.route('/save',methods= ['POST'])
    def save():
        
        person = Person
        person.name = request.form['name']
        person.age = request.form['age']
        person.job = request.form['job']
        person.create(person)
        
    
        return render_template('index.html', message='user successfully created')
    @app.route('/store')
    def index():
        return render_template('store.html')
    
    @app.route('/')
    def main():
        return render_template('index.html')
    
        