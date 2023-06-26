# from RecipesEngine.recipes_model import JsonRecipesLoaderV1
from RecipesEngine.recipes_engine import RecipesEngine

GRAPH_PATH = "data/recipes_graph.graphml"
JSON_DATA_PATH = "data/recipes.json"

JSON_RECIPES_DATA_DIR = "C:/Users/Roger/Desktop/work/posgrados/cna/proyecto/Data/parsed_data"

recipes_engine = RecipesEngine(GRAPH_PATH)

def main():
    print("Hello")
    
    print("Loading Graph from large data set")
    
    recipes_engine.update_graph_from_large_json_dataset(JSON_RECIPES_DATA_DIR)
    
    print("Saving graph")
    
    recipes_engine.save_graph()
    
    print("End")

    pass

if __name__ == "__main__":
    main()
    pass