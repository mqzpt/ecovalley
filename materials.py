from dotenv import load_dotenv
from pprint import pprint
import pandas as pd
import cohere
import requests
import os, ast

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
        prompt=f"You are a helpful assistant that selects materials for products. Do not provide any text outputs, only return a python list with no new lines or spaces. You may only choose products EXACTLY as they appear in the following list: {MATERIAL_NAMES}. Return a Python list of 3 dictionaries, each dictionary MUST contain MULTIPLE keys and values, where the keys are the materials in the proudct, and the values are the amount of each product in kilograms. Complete this task for the following product: {user_prompt}.",
        max_tokens=350,
        num_generations=1,
        temperature=0.5,
    )
    selected_list = ast.literal_eval(selected_list.generations[0].text.strip())
    
    return selected_list

def get_option_dataframes(material_dict) -> pd.DataFrame:
    
    option_frames = []
    
    # Get the current file's directory
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, 'resources', 'material_data.csv')

    # Read the CSV file
    materials_df = pd.read_csv(csv_path)
    
    for option in material_dict:
        option_df = materials_df.loc[materials_df['material'].isin(option.keys())]
        option_df['cost'] = round(option_df['price_per_kg'] * list(option.values()), 4)
        
        amount_used_series = pd.Series(list(option.values()))
        option_df['amount_used_kg'] = amount_used_series.round(3)
        
        option_df['energy_used_mj'] = round(option_df['energy_mj_per_kg'] * list(option.values()), 3)
        option_df['carbon_used_kg'] = round(option_df['carbon_kg_per_kg'] * list(option.values()), 3)
        option_frames.append(option_df[['material', 'amount_used_kg', 'cost', 'energy_used_mj', 'carbon_used_kg']])
        
    return option_frames
        
# CLI for testing prompts
if __name__ == "__main__":
    print("\n*** Get Material Options ***\n")

    prompt = input("\nPlease enter your desired product: ")

    # Check for empty strings or string with only spaces
    
    while not bool(prompt.strip()):
        prompt = input("\nPlease enter your prompt (it was empty): ")

    material_dict = get_materials_for_product(prompt)

    print("\n")
    pprint(material_dict)
    
    option_frames = get_option_dataframes(material_dict)
    
    pprint(option_frames)
    
