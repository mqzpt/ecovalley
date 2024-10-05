from flask import Flask, render_template, request
from materials import get_materials_for_product
from waitress import serve

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Materials list route
@app.route('/materials', methods=['GET', 'POST'])
def materials_list():
    if request.method == 'POST':
        prompt = request.form['prompt']
        materials = get_materials_for_product(prompt)
    else:
        materials = get_materials_for_product('')  # Default to showing all materials
    return render_template('materials.html', materials=materials)

# Comparison page route
@app.route('/compare', methods=['POST'])
def compare():
    # Get selected materials IDs from form submission (for simplicity, assuming form submission)
    selected_ids = request.form.getlist('material_ids')
    
    # Filter out the selected materials for comparison
    compared_materials = [material for material in materials if str(material['id']) in selected_ids]
    
    return render_template('compare.html', compared_materials=compared_materials)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
