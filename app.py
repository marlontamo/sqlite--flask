from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='./templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    from routes import register_routes
    register_routes(app, db)
    migrate = Migrate(app, db)

    return app
# @app.route('/')
# def index():
#     return render_template('index.html',utc='test-yehey')

