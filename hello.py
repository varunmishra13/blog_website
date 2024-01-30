from flask import Flask, render_template

#create a Flask Instance
app = Flask(__name__)

#create a route decorator
@app.route('/')

def index():
    first_n = "varun"
    stuff = "This is <strong>Blod</strong> Text"

    favourite_pizza = ["Pepproni", "Cheese", "Mushroom", 41]
    return render_template("index.html",
     n=first_n,
     stuff=stuff,
     favourite_pizza=favourite_pizza)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html",user_name=name )

#creating custom error pages

#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("404.html"), 500