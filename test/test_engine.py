import json
import networkx as nx

data_path = "C:/Users/RCF/Desktop/Organizacion/Posgrados UH/Analisis de Redes/RecipesProject/data/recipes_full.json"

# TODO: Procesar en utf-16 u otro formato que no rompa la legibilidad de lapalabras en esp
# TODO: Procesar el input para limpar nombres similares correspondientes al mismo ingrediente o receta, con varianciones minimas.

recipes = {}
with open(data_path) as f:
    recipes = json.load(f)
    pass

recipes_graph = nx.Graph()

for recip_k, recip_data in recipes.items():
    
    recip_name = recip_data.get("nombre")
    recipes_graph.add_node(recip_name)
        
    ingredients = recip_data.get("ingredientes")
    for i in ingredients:
        ingredient_name = i.get("nombre")
        recipes_graph.add_node(ingredient_name)
        recipes_graph.add_edge(recip_name, ingredient_name)
        pass
    
    pass

nx.write_graphml(recipes_graph, "recipes_graph.graphml")
