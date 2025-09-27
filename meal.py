import requests
from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()

@tool


def get_nutrition_info(meal: str) ->str:
    """Fetches nutritional information for a given meal using the Nutritionix API."""
    try:
        url = f"https://api.api-ninjas.com/v1/nutrition?query={meal}"
        response = requests.get(url, headers={ 'X-Api-Key': '0q9g2hrbshEerRlt7YqThw==4z2XcH5NDFQklIc7'})
        Data = response.json()
        if response.status_code == 200 and Data:
            item = Data[0]
            name = item.get('name', 'Unknown')
            calories = item.get('calories', 'N/A')
            fat_total_g = item.get('fat_total_g', 'N/A')
            protein_g = item.get('protein_g', 'N/A')
            carbs_total_g = item.get('carbohydrates_total_g', 'N/A')
            fiber_g = item.get('fiber_g', 'N/A')
            sugar_g = item.get('sugar_g', 'N/A')

            return (f"Nutritional Information for {name}:\n"
                    f"Calories: {calories} kcal\n"
                    f"Total Fat: {fat_total_g} g\n"
                    f"Protein: {protein_g} g\n"
                    f"Total Carbohydrates: {carbs_total_g} g\n"
                    f"Fiber: {fiber_g} g\n"
                    f"Sugar: {sugar_g} g")
        else:
            return "Could not retrieve nutritional information. Please check the meal name and try again."

    except Exception as e:
        return f"An error occurred: {e}"
