from datetime import datetime
from langchain_community.adapters.openai import convert_openai_messages
from langchain_openai import ChatOpenAI
import re

class FeedbackAgent:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key

    def provide_feedback(self, user_data: dict):
        prompt = [
            {"role": "system", "content": "You are an AI culinary consultant. Your task is to provide suggestions and feedback on meal preparations based on user inputs."},
            {"role": "user", "content": f"Date: {datetime.now().strftime('%d/%m/%Y')}\nDiet: {user_data['diet']}\nCuisine: {user_data['cuisine']}\nIngredients: {user_data['ingredients']}\nMeal Type: {user_data['meal_type']}\nPlease provide your suggestions for improving this meal or any other feedback."}
        ]

        lc_messages = convert_openai_messages(prompt)
        response = ChatOpenAI(model='gpt-3.5-turbo', max_retries=1, openai_api_key=self.openai_api_key).invoke(lc_messages).content

        return self.parse_feedback(response)

    def parse_feedback(self, feedback):
        parsed_feedback = {
            "title": "",
            "ingredients": [],
            "instructions": []
        }

        title_match = re.search(r"consider making (.*?). Here's a simple recipe", feedback)
        ingredients_match = re.search(r"Ingredients:\n- (.*?)\n\n", feedback, re.DOTALL)
        instructions_match = re.search(r"Instructions:\n(.*)", feedback, re.DOTALL)

        if title_match:
            parsed_feedback["title"] = title_match.group(1)

        if ingredients_match:
            parsed_feedback["ingredients"] = ingredients_match.group(1).split("\n- ")

        if instructions_match:
            parsed_feedback["instructions"] = [step.strip() for step in instructions_match.group(1).split("\n") if step.strip()]

        return parsed_feedback

    def run(self, user_data: dict):
        feedback = self.provide_feedback(user_data)
        return feedback
