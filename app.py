"""Flask app for Cupcakes"""

from flask import Flask, render_template, redirect, flash
#from flask_debugtoolbar import DebugToolbarExtension


from models import db, connect_db, Cupcake
#from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

# Don't forget to db.drop_all() incase of errors 
db.create_all()