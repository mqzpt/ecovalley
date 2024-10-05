# Flask instance
from flask import Flask, render_template, request
from materials import get_materials_for_product
from waitress import serve

app = Flask(__name__)


# @app.route("/")
# @app.route("/index")
# def index():
#     return render_template("index.html")

@app.route('/')
def home():
    return render_template('index.html')

# Materials List Route
@app.route('/materials', methods=['GET', 'POST'])
def materials_list():
    if request.method == 'POST':
        prompt = request.form['prompt']
        materials = get_materials_for_product(prompt)
    else:
        materials = get_materials_for_product('')  # Default to showing all materials
    return render_template('materials.html', materials=materials)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
