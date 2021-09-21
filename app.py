"""Flask app for dessert demo."""

from flask import Flask, request, jsonify
from flask.templating import render_template
from models import db, connect_db, Cupcake

DEFAULT_IMG_URL = 'https://tinyurl.com/demo-cupcake'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.get('/')
def get_homepage():

    return render_template('index.html')

@app.get('/api/cupcakes')
def get_cupcakes():
    """Get all cupcakes and return JSON"""
    cupcakes = Cupcake.query.all()
    serialized = [ cupcake.serialize() for cupcake in cupcakes ]

    return jsonify(cupcakes=serialized)

@app.get('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    """Get one cupcake and return JSON"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.post('/api/cupcakes')
def make_cupcake():
    """Add a cupcake to the database and 
    return JSON of the new cupcake"""
    
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]

    new_cupcake = Cupcake(
        flavor=flavor,
        size=size,
        rating=rating,
        image=image
        )

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)

@app.patch('/api/cupcakes/<int:cupcake_id>')
def update_cupcake(cupcake_id):
    """Update cupcake given a patch request, 
    update the database and return the updated cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    updated_data = request.json

    cupcake.flavor = updated_data.get("flavor", cupcake.flavor)
    cupcake.rating = updated_data.get("rating", cupcake.rating)
    cupcake.size = updated_data.get("size", cupcake.size)
    cupcake.image = updated_data.get("image", cupcake.image)
    
    db.session.commit()
    
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


# DELETE /api/cupcakes/[cupcake-id]
# This should raise a 404 if the cupcake cannot be found.

# Delete cupcake with the id passed in the URL. Respond with JSON like {deleted: [cupcake-id]}.

@app.delete('/api/cupcakes/<int:cupcake_id>')
def delete_cupcake(cupcake_id):
    """Delete a cupcake from the database (using cupcake_id)
        and returns id of deleted cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify({"deleted": cupcake_id}) #format could be the same as return in patch