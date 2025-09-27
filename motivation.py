from langchain.tools import tool

import requests


@tool
def instant_motivation(query: str = "motivation") ->str:
    """provides instant motivation to the user."""
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            Data = response.json()
            quote = Data[0]['q']
            author = Data[0]['a']
            return f"{quote} - {author}"
        else:
            return "Could not retrieve a quote at this time. Please try again later."

    except Exception as e:
        return f"An error occurred: {e}"    
    
    
