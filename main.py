from RecipesEngine.recipes_engine import RecipesEngine
from ui_cli_menu import add_menu_option, main_loop

GRAPH_PATH = "data/recipes_graph.graphml"
JSON_DATA_PATH = "data/recipes.json"
JSON_RECIPES_DATA_DIR = "C:/Users/Roger/Desktop/work/posgrados/cna/proyecto/Data/parsed_data"

recipes_engine = RecipesEngine(GRAPH_PATH)

def update_graph_from_large_dataset():
    "Actualizar Grafo desde JSON"
    if recipes_engine.update_graph_from_large_json_dataset(JSON_RECIPES_DATA_DIR):
        print("Loaded Graph from large data set")
        print("Saving graph")
        recipes_engine.save_graph()
        pass
    pass

def find_subsitute_for_an_ingredient():
    "Encontrar Sustituto para un ingrediente"
    target_ingredient = input("Ingrediente: ")
    recipe_hint = None
    substitute = recipes_engine.suggest_ingredient_substitute(target_ingredient, recipe_hint)
    print(f"{target_ingredient} could be replaced by {substitute}")
    pass

def print_related_recipes_for_ingredient():
    "Recetas para un ingrediente especifico"
    ingredient = input("Ingrediente: ")
    for r in recipes_engine.get_recipes_for_ingredient(ingredient):
        print(r)
    pass

def print_related_ingredients_for_recipe():
    "Ingredientes para una receta"
    recipe = input("Recipe: ")
    for i in recipes_engine.get_ingredients_for_recipe(recipe):
        print(i)
    pass

def main():
    # Configurar Menu
    
    add_menu_option(update_graph_from_large_dataset)
    add_menu_option(find_subsitute_for_an_ingredient)
    add_menu_option(print_related_recipes_for_ingredient)
    add_menu_option(print_related_ingredients_for_recipe)
    
    main_loop()
    pass

if __name__ == '__main__':
    main()