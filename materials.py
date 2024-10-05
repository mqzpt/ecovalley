from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_materials_for_product(get_materials_for_product="Waterloo"):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("WEATHER_API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print("\n*** Get Material Options ***\n")

    prompt = input("\nPlease enter your prompt: ")

    # Check for empty strings or string with only spaces
    
    while not bool(prompt.strip()):
        prompt = input("\nPlease enter your prompt (it was empty): ")

    material_data = get_materials_for_product(prompt)

    print("\n")
    pprint(material_data)
