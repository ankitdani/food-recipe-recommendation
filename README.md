# food-recipe-recommendation

## Project Goals

The aim of this project is to develop a web-based application that recommends food recipes based on the ingredients provided by the user. This application leverages the Tavily API to fetch recipes and integrates several agents to provide additional functionalities like feedback and nutrient value analysis.

## Architecture

The project follows a modular architecture with the following main components:

1. **App Module (`app.py`)**: The main entry point of the application that sets up the Flask server and handles incoming requests.
2. **Feedback Agent (`feedback_agent.py`)**: This module handles user feedback on recipes and stores the feedback for future improvements.
3. **Nutrient Value Agent (`nutrient_value_agent.py`)**: This module calculates and provides nutrient values for the recommended recipes.
4. **Search Agent (`search_agent.py`)**: This module interfaces with the Tavily API to fetch recipes based on the user's input ingredients.

### Dependencies

The project requires the following Python packages:

- `flask`: For setting up the web server.
- `tavily-python`: For interacting with the Tavily API.
- `langgraph`: For handling natural language processing tasks.
- `langchain-openai`: For integrating OpenAI's language models.
- `requests`: For making HTTP requests.

Install the necessary packages by running the following commands:

```sh
pip3 install flask
pip3 install tavily-python
pip3 install langgraph
pip3 install -qU langchain-openai
pip3 install requests
```

Add your OPENAI API KEY in the app.py file.

To run the application:

```
python3 app.py
```

Go to `http://127.0.0.1:5000` and enjoy your next recipe !!
