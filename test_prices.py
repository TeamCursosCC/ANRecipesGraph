from RecipesEngine.recipes_engine import RecipesEngine
GRAPH_PATH = "data/recipes_graph.graphml"

def main():
	recipe = "one pot chili"
	recipes_engine = RecipesEngine(GRAPH_PATH)
	#print(recipes_engine.check_recipe(target = "one pot chili"))
	#print(recipes_engine.check_recipe(target = "ground beef"))
	#print(recipes_engine.check_recipe(target = "salsa"))
	#print(recipes_engine.check_recipe(target = 'pinto beans'))
	recipes_engine.estimate_recipe_cost(recipe = "one pot chili")
	pass


if __name__ == '__main__':
	main()
