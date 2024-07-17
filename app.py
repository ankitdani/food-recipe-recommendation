from flask import Flask, render_template, request
from search_agent import SearchAgent
from nutrient_value_agent import NutrientValueAgent
from feedback_agent import FeedbackAgent

app = Flask(__name__)

feedback_agent = FeedbackAgent(openai_api_key="YOUR_OPENAI_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    recipes = None
    nutrient_values = None
    feedback = None

    if request.method == 'POST':
        user_data = {
            "diet": request.form['diet'],
            "cuisine": request.form['cuisine'],
            "ingredients": request.form['ingredients'],
            "meal_type": request.form['meal_type']
        }

        search_agent = SearchAgent()
        recipes = search_agent.run(user_data)

        app_id = "6bdf2757"
        app_key = "3bd2e262fc1cd9395b09cdddcec2331b"
        nutrient_value_agent = NutrientValueAgent(app_id, app_key)
        nutrient_values = nutrient_value_agent.run(user_data["ingredients"])

        feedback = feedback_agent.run(user_data)

    return render_template('index.html', recipes=recipes, nutrient_values=nutrient_values, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
