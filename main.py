from RecipesEngine.recipes_engine import RecipesEngine
from ui_cli_menu import add_menu_option, main_loop

GRAPH_PATH = "data/recipes_graph.graphml"
JSON_DATA_PATH = "data/recipes.json"
JSON_RECIPES_DATA_DIR = (
    "C:/Users/Roger/Desktop/work/posgrados/cna/proyecto/Data/parsed_data"
)

recipes_engine = RecipesEngine(GRAPH_PATH)


def update_graph_from_large_dataset():
    "Update graph from a JSON file (needs to match an specific structure for now)"
    if recipes_engine.update_graph_from_large_json_dataset(JSON_RECIPES_DATA_DIR):
        print("Loaded Graph from large data set")
        print("Saving graph")
        recipes_engine.save_graph()
        pass
    pass


def suggest_recipe_for_given_ingredients():
    "Suggest a recipe for given ingredients (at least 3)"
    minimum = 3
    commands = {"suggest": "/suggest", "cancel": "/cancel"}

    print("Agregue los nombres de los ingredientes que desea.")
    print(
        f"Escriba {commands['suggest']} para realizar la sugerencia o {commands['cancel']} para cancelarla"
    )

    ingredients = []
    while True:
        inp = input(">> ")
        if inp == commands["cancel"]:
            return
        if inp == commands["suggest"]:
            if len(ingredients) < minimum:
                print("(!) Debe agregar mas ingredientes.")
                continue
            break
        # TODO: Validar nombre de ingrediente
        # TODO: Realizar busqueda parcial de los nombres de los ingredientes
        ingredients.append(inp)
        pass

    recipe = recipes_engine.suggest_recipes_from_ingredients(ingredients)
    print(f"\nWe suggest:\n{recipe}")
    pass


def find_subsitute_for_an_ingredient():
    "Find a possible ingredient substitute"
    target_ingredient = input("Ingrediente: ")
    recipe_hint = None
    substitute = recipes_engine.suggest_ingredient_substitute(
        target_ingredient, recipe_hint
    )
    print(f"\nResponse -> {target_ingredient} could be replaced by {substitute}")
    pass


def print_related_recipes_for_ingredient():
    "Print related recipes for an ingredient"
    ingredient = input("Ingrediente: ")
    for r in recipes_engine.get_recipes_for_ingredient(ingredient):
        print(r)
    pass


def print_related_ingredients_for_recipe():
    "Print a recipe's ingredients"
    recipe = input("Recipe: ")
    for i in recipes_engine.get_ingredients_for_recipe(recipe):
        print(i)
    pass


def main():
    # Configurar Menu

    add_menu_option(update_graph_from_large_dataset)
    add_menu_option(suggest_recipe_for_given_ingredients)
    add_menu_option(find_subsitute_for_an_ingredient)
    add_menu_option(print_related_recipes_for_ingredient)
    add_menu_option(print_related_ingredients_for_recipe)

    main_loop()
    pass


if __name__ == "__main__":
    main()
