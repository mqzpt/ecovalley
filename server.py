from flask import Flask, render_template, request
from materials import get_materials_for_product, get_option_dataframes
from waitress import serve
import pandas as pd

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
        material_dict = get_materials_for_product(prompt)
        option_frames = get_option_dataframes(material_dict)
    else:
        material_dict = get_materials_for_product('')  # Default to showing all materials
        option_frames = get_option_dataframes(material_dict)
    
    # Pass the option_frames to the template for rendering
    return render_template('materials.html', option_frames=option_frames)

@app.route('/compare', methods=['POST'])
def compare():
    selected_names = request.form.getlist('material_names')  # List of selected material names
    
    # Reload materials from the CSV (or pass them from previous route if necessary)
    materials_df = pd.read_csv('resources/material_data.csv')  # Assuming materials are stored in a CSV
    
    # Filter the DataFrame to get the selected materials
    compared_materials_df = materials_df[materials_df['material'].isin(selected_names)]
    
    # Pass the filtered materials to the comparison template
    return render_template('compare.html', compared_materials=compared_materials_df.to_dict(orient='records'))

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
