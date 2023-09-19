from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice
app = Flask(__name__)

API_KEY = "TopSecretAPIKey"

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
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
        dictionary = { column.name: getattr(self, column.name) for column in self.__table__.columns}
        # dictionary = {}
        # for column in self.__table__.columns:
        #     dictionary[column.name] = getattr(self, column.name)
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
    

# HTTP GET - Read Record
@app.route("/random")
def random():
    result = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = choice(result)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all():
    result = db.session.execute(db.select(Cafe)).scalars().all()
    cafe_list = [cafe.to_dict() for cafe in result]
    return jsonify(cafes=cafe_list)


@app.route("/search")
def search():
    location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalar()
    if result:
        searched_cafe = result.to_dict()
        return jsonify(cafe=searched_cafe)
    else:
        return jsonify(error={
            "Not Found": "Sorry, we don't have a cafe at that location."
        })


# HTTP POST - Create Record
@app.route("/add", methods=["POST", "GET"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        seats=request.form.get("seats"),
        has_sockets=bool(request.form.get("sockets")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        coffee_price=request.form.get("coffee_price"),
        has_toilet=bool(request.form.get("toilet"))
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={
        "Success": "Successfully added the new cafe"
    })

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.get(Cafe, cafe_id)
    print(cafe)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={
            "Success": "Successfully patched the cafe"
        }), 200
    else:
        return jsonify(error={
            "Not Found": "Sorry a cafe with that id was not found in the database."
        }), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key_request = request.args.get("api-key")
    cafe = db.session.get(Cafe, cafe_id)
    if cafe and api_key_request == API_KEY:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={
            "Success": "Successfully deleted cafe from database."
        }), 200
    elif not cafe:
        return jsonify(error={
            "Not Found": "Sorry a cafe with that id was not found in the database."
        }), 404
    elif api_key_request != API_KEY:
        return jsonify(error={
            "Not Found": "Sorry, that's not allowed. Make sure you have the correct api_key."
        }), 403


if __name__ == '__main__':
    app.run(debug=True)
