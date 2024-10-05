from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_materials_for_product(prompt: str) -> dict:
    # Mock data for now, you can replace this with actual API calls later
    materials_data = [
        {
            "name": "Recycled Steel",
            "carbon_footprint": "0.5 kg CO2/kg",
            "recyclability": 98,
            "sustainability_score": 85
        },
        {
            "name": "Bamboo",
            "carbon_footprint": "0.2 kg CO2/kg",
            "recyclability": 100,
            "sustainability_score": 90
        },
        {
            "name": "Hemp Plastic",
            "carbon_footprint": "0.1 kg CO2/kg",
            "recyclability": 90,
            "sustainability_score": 80
        }
    ]

    # Filter based on the prompt (optional)
    return [material for material in materials_data if prompt.lower() in material['name'].lower()]

def get_cost(material_name: str) -> dict:
    # Mock data for now, you can replace this with actual API calls later
    cost_data = [
        {
            "name": "Recycled Steel",
            "cost": 0.5
        },
        {
            "name": "Bamboo",
            "cost": 0.2
        },
        {
            "name": "Hemp Plastic",
            "cost": 0.1
        }
    ]

    # Filter based on the material name
    return [cost for cost in cost_data if material_name.lower() in cost['name'].lower()]

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
