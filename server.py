# Flask instance
from flask import Flask, render_template, request
from materials import get_current_weather
from waitress import serve

app = Flask(__name__)


# @app.route("/")
# @app.route("/index")
# def index():
#     return render_template("index.html")

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
