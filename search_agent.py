from tavily import TavilyClient

tavily_client = TavilyClient(api_key="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")

class SearchAgent:
    def __init__(self):
        pass

    def search_tavily(self, diet, cuisine, ingredients, meal_type):
        query = f"{meal_type} recipe with {ingredients} for {diet} cuisine {cuisine}"
        results = tavily_client.search(query=query, max_results=2, include_images=True)
        sources = results["results"]
        images = results["images"]

        recipes = []
        for i, source in enumerate(sources):
            image_url = images[i] if i < len(images) else None
            recipes.append({"title": source["title"], "url": source["url"], "content": source["content"], "image": image_url})
        return recipes

    def run(self, recipe: dict):
        recipes = self.search_tavily(recipe["diet"], recipe["cuisine"], recipe["ingredients"], recipe["meal_type"])
        return recipes