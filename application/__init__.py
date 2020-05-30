from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///climb.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application.routes import views
from application.auth import views

from application.routes import models
from application.auth import models

db.create_all()