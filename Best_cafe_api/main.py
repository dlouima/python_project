import random
from config import API_KEY
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route('/random')
def random_cafe():
    all_cafe = Cafe.query.all()
    single_cafe= random.choice(all_cafe)
    return jsonify(cafe=single_cafe.to_dict())

@app.route('/all')
def get_all_data():
    all_place = db.session.query(Cafe).all()
    cafes=[]
    for single_cafe in all_place:
        cafes.append(single_cafe.to_dict())
    return jsonify(cafe=cafes)

@app.route('/search')
def search():
    location = request.args.get("location")
    cafe = Cafe.query.filter_by(location=location).all()
    cafes=[item.to_dict() for item in cafe]
    if  cafes == []:
        return jsonify(Error={ 'Not Fount': 'Sorry we don\'t have a cafe in that location'})
    return jsonify(cafe=cafes)

## HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(Response={'Success': 'Successfuly added the new cafe'})
## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<cafe_id>', methods=['PUT'])
def update_price(cafe_id):
    cafe= Cafe.query.get(cafe_id)
    if cafe:
        Cafe.coffee_price= request.form.get('coffee_price')
        db.session.commit()
        return jsonify(Response={'Success':'Successfully updated the price'})
    else:
        return jsonify(response={'Not Found':' Sorry a cafe with that id was not found'})
      

## HTTP DELETE - Delete Record
@app.route('/report-closed/<cafe_id>', methods=["DELETE"])
def cafe_close(cafe_id):
    if request.args.get('api_key') ==API_KEY:
        cafe = Cafe.query.get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={'Success':"Successfully delete entry"})
        else:
            return jsonify(response={'Not Found': 'Entry not found'})
    else:
        return jsonify(response={'Not Authorizes': 'You do not have permission to delete this entry'})


if __name__ == '__main__':
    app.run(debug=True)
