"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Model Cupcake"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, 
        autoincrement=True, 
        primary_key=True)
    flavor = db.Column(db.Text, 
        nullable=False)
    size = db.Column(db.Text, 
        nullable=False)
    rating = db.Column(db.Integer, 
        nullable=False)
    image = db.Column(db.Text, 
        nullable=False, 
        default='https://tinyurl.com/demo-cupcake')

