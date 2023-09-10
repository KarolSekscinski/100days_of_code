from flask import Flask
import random
app = Flask(__name__)
correct_number = random.randint(0,9)
colours = ["cyan", "red", "blue", "aqua", "beige", "brown", "pink", "dimgray"]
@app.route("/")
def hello_world():
    return ("<h1>Guess a number between 0 and 9<h1/>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


@app.route("/<number>")
def guess_number(number):
    number = int(number)
    if number < correct_number:
        colour = random.choice(colours)
        response = (f'<h1 style="color: {colour}">Too low, try again!<h1/>'
                    f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
        return response
    elif number > correct_number:
        colour = random.choice(colours)
        response = (f'<h1 style="color: {colour}">Too high, try again!<h1/>'
                    f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
        return response
    else:
        colour = "green"
        response = (f'<h1 style="color: {colour}">You found me!<h1/>'
                    f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')
        return response


if __name__ == "__main__":
    app.run(debug=True)