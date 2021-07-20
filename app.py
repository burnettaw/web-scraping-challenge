#import libraries
from flask import Flask, render_template

#nitalize the app
app = Flask(__name__)

# serves the webpage
@app.route('/')
def index():
    return render_template("index.html",text="web page Text from the flask pages")
