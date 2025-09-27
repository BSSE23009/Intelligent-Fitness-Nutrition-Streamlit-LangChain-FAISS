import os
import requests
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()

API_KEY = os.getenv("API_NINJAS_KEY")

@tool
def get_nutrition_info(meal: str) -> str:
    """Fetches nutritional information for a given meal using the Nutritionix API."""
    try:
        url = f"https://api.api-ninjas.com/v1/nutrition?query={meal}"
        response = requests.get(url, headers={'X-Api-Key': API_KEY})
        data = response.json()
        if response.status_code == 200 and data:
            item = data[0]
            return (
                f"Nutritional Information for {item.get('name', 'Unknown')}:\n"
                f"Calories: {item.get('calories', 'N/A')} kcal\n"
                f"Total Fat: {item.get('fat_total_g', 'N/A')} g\n"
                f"Protein: {item.get('protein_g', 'N/A')} g\n"
                f"Total Carbohydrates: {item.get('carbohydrates_total_g', 'N/A')} g\n"
                f"Fiber: {item.get('fiber_g', 'N/A')} g\n"
                f"Sugar: {item.get('sugar_g', 'N/A')} g"
            )
        else:
            return "Could not retrieve nutritional information. Please check the meal name and try again."
    except Exception as e:
        return f"An error occurred: {e}"
