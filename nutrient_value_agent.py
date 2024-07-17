import requests

class NutrientValueAgent:
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.api_url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
        
    def get_nutrient_values(self, query):
        headers = {
            'Content-Type': 'application/json',
            'x-app-id': self.app_id,
            'x-app-key': self.app_key
        }
        body = {
            "query": query
        }
        
        response = requests.post(self.api_url, headers=headers, json=body)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch nutrient information", "status_code": response.status_code}
        
    def run(self, ingredients):
        ingredient_list = [ingredient.strip() for ingredient in ingredients.split(',')]
        nutrient_values = {}
        for ingredient in ingredient_list:
            nutrition_info = self.get_nutrient_values(ingredient)
            nutrient_values[ingredient] = nutrition_info

        return nutrient_values
