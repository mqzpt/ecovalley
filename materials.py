from dotenv import load_dotenv
from pprint import pprint
import pandas as pd
import cohere
import requests
import os

MATERIAL_NAMES = ['Butyl rubber (IIR)', 'Ethylene vinyl acetate (EVA)' 'Natural rubber', 'Polychloroprene (Neoprene)'
 'Polyisoprene rubber', 'Polyurethane', 'Silicone elastomers', 'Acrylonitrile butadiene styrene (ABS)', 'Cellulose polymers (CA)',
 'Ionomer (I)', 'Polyamides (Nylons, PA)', 'Polycarbonate (PC)', 'Polyetheretherketone (PEEK)', 'Polyethylene (PE)',
 'Polyethylene terephthalate (PET)', 'Polymethyl methacrylate (Acrylic, PMMA)', 'Polyoxymethylene (Acetal, POM)',
 'Polypropylene (PP)', 'Polystyrene (PS)', 'Polytetrafluoroethylene (Teflon, PTFE)', 'Polyurethane (tpPUR)',
 'Polyvinylchloride (tpPVC)', 'Epoxies', 'Phenolics', 'Polyester', 'Flexible Polymer Foam (LD)', 'Flexible Polymer Foam (MD)',
 'Rigid Polymer Foam (HD)', 'Rigid Polymer Foam (LD)', 'Cast iron, ductile (nodular)', 'Cast iron, gray', 'High carbon steel',
 'Low alloy steel', 'Low carbon steel', 'Medium carbon steel', 'Stainless steel', 'Aluminum alloys', 'Copper alloys',
 'Lead alloys', 'Magnesium alloys', 'Nickel alloys', 'Silver', 'Tin', 'Titanium alloys', 'Tungsten alloys', 'Zinc alloys',
 'Cork', 'Paper and cardboard', 'Wood, typical across grain', 'Wood, typical along grain', 'CFRP, epoxy matrix (isotropic)',
 'GFRP, epoxy matrix (isotropic)', 'Borosilicate glass', 'Silica glass', 'Soda-lime glass', 'Alumina', 'Aluminum nitride',
 'Silicon', 'Silicon carbide', 'Tungsten carbides', 'Brick', 'Concrete','Stone']

load_dotenv()

def get_cohere_token():
    return os.getenv("COHERE_API_KEY")

def get_materials_for_product(user_prompt: str) -> dict:
    
    co = cohere.Client(get_cohere_token())
    
    selected_list = co.generate(
        model="command-xlarge-nightly",
        prompt=f"You are a helpful assistant that selects materials for products. Do not provide any text outputs, only return a python list with no new lines or spaces. You may only choose products in the following list: {MATERIAL_NAMES}. Return a Python list of 3 dictionaries, each dictionary MUST contain MULTIPLE keys and values, where the keys are the materials in the proudct, and the values are the amount of each product in kilograms. Complete this task for the following product: {user_prompt}.",
        max_tokens=250,
        num_generations=1,
        temperature=0.5,
    )
    return selected_list.generations[0].text.strip()

def get_material_data(materials) -> pd.DataFrame:
    
    # Get the current file's directory
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, 'resources', 'material_data.csv')

    # Read the CSV file
    materials_df = pd.read_csv(csv_path)
    
    # Get the relevant materials
    materials_df.loc[materials_df['material'].isin(materials.keys()), 'cost_per_kg']
    materials_df['cost'] = materials_df['cost_per_kg'] * materials.values()
        

# CLI for testing prompts
if __name__ == "__main__":
    print("\n*** Get Material Options ***\n")

    prompt = input("\nPlease enter your desired product: ")

    # Check for empty strings or string with only spaces
    
    while not bool(prompt.strip()):
        prompt = input("\nPlease enter your prompt (it was empty): ")

    material_data = get_materials_for_product(prompt)

    print("\n")
    pprint(material_data)
