from RecipesEngine.recipes_engine import RecipesEngine
import pprint
GRAPH_PATH = "data/recipes_graph.graphml"

recipe_name = "one pot chili"
recipes_engine = RecipesEngine(GRAPH_PATH)

cost_df = recipes_engine.estimate_recipe_cost(recipe = recipe_name)


"""
def main():
	recipe = "one pot chili"
	recipes_engine = RecipesEngine(GRAPH_PATH)
	
	print(recipes_engine.check_recipe(target = "one pot chili"))
	print(recipes_engine.check_recipe(target = "ground beef"))
	print(recipes_engine.check_recipe(target = "salsa"))
	print(recipes_engine.check_recipe(target = 'pinto beans'))
	recipes_engine.estimate_recipe_cost(recipe = "one pot chili")
	
	ingredients = ["milk","brown sugar","vanilla","broken nuts","beef", "sour cream"]
	suggest_recipes = recipes_engine.suggest_recipes_from_ingredients(ingredients)
	pprint.pprint(suggest_recipes)
	pass


if __name__ == '__main__':
	main()
"""