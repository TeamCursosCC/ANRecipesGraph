
import networkx as nx
import json

JSON_DATA_PATH = "data/recipes_graph.graphml"
GRAPH_PATH = "data/recipes.json"

class RecipesEngine():
    """
    Class Description: RecipesEngine
    """
    def __init__(self):
        
        self.recipesGraph = None
        
        try:
            self.load_graph()
            pass
        except Exception as e:
            print(e)
            pass
        
        if self.recipesGraph is None:
            self.recipesGraph = nx.Graph()
        
        pass
    
    def load_graph(self):
        self.recipesGraph = nx.read_graphml(GRAPH_PATH)      
        pass
    
    def save_graph(self):
        nx.write_graphml(self.recipesGraph, GRAPH_PATH)    
        pass
    
    def update_graph_from_parsed_json_datasets(self):
        
        PARSED_DIR = ""
        
        
        
        pass
    
    def update_graph_from_json(self):
        
        recipes = {}
        with open(JSON_DATA_PATH) as f:
            recipes = json.load(f)
            
        #TODO: Add Filter for similar names on recipes or ingredients
        
        for recip_k, recip_data in recipes.items():
    
            recip_name = recip_data.get("nombre")
            self.recipesGraph.add_node(recip_name)
                
            ingredients = recip_data.get("ingredientes")
            for i in ingredients:
                ingredient_name = i.get("nombre")
                self.recipesGraph.add_node(ingredient_name)
                self.recipesGraph.add_edge(recip_name, ingredient_name)
                pass
            
            pass

        pass
    
    def suggest_recipes_from_ingredients(self, ingredients:list):
        # 5. Para sugerir platos a partir de ingredientes dados, se puede utilizar el grafo de ingredientes y recetas para encontrar las recetas que contengan los ingredientes dados y sugerir los platos correspondientes.
        
        # 1. Análisis de centralidad: Este análisis se utiliza para identificar los nodos más importantes en una red. En el contexto de un grafo de recetas e ingredientes, se puede utilizar para identificar los ingredientes más utilizados en las recetas. Esto puede ser útil para sugerir platos a partir de ingredientes dados, ya que los ingredientes más comunes probablemente se utilizarán en muchas recetas diferentes.
        
        # 3. Análisis de caminos mínimos: Este análisis se utiliza para encontrar la ruta más corta entre dos nodos en una red. En el contexto de un grafo de recetas e ingredientes, se puede utilizar para encontrar la ruta más corta entre dos ingredientes dados. Esto puede ser útil para sugerir platos a partir de ingredientes dados, ya que los ingredientes que están conectados por una ruta corta probablemente se utilizan juntos con frecuencia.

        # 4. Análisis de comunidades: Este análisis se utiliza para identificar grupos de nodos altamente interconectados que están más densamente conectados entre sí que con el resto de la red. En el contexto de un grafo de recetas e ingredientes, se puede utilizar para identificar grupos de recetas que comparten ingredientes comunes. Esto puede ser útil para sugerir platos a partir de ingredientes dados, ya que las recetas que comparten ingredientes comunes pueden ser similares en sabor y estilo.
        
        # Para sugerir platos a partir de ingredientes dados, se puede utilizar una combinación de estas técnicas, como la centralidad de grado para identificar los ingredientes más comunes, el análisis de caminos mínimos para encontrar los ingredientes conectados a los ingredientes dados y el análisis de comunidades para identificar grupos de recetas que comparten ingredientes comunes.
        
        pass
    
    def suggest_ingredient_substitute(self, ingredient, recipe_hint):
        
        # 6. Para sugerir sustitutos de ingredientes para una receta dada, se pueden utilizar técnicas de análisis de similitud para encontrar ingredientes que sean similares en propiedades y características a los ingredientes originales y sugerir su uso como sustitutos.
        
        # 2. Análisis de modularidad: Este análisis se utiliza para identificar grupos de nodos altamente interconectados en una red. En el contexto de un grafo de recetas e ingredientes, se puede utilizar para identificar grupos de ingredientes que se utilizan juntos con frecuencia en las recetas. Esto puede ser útil para sugerir ingredientes sustitutos para un ingrediente dado en una receta, ya que los ingredientes que se utilizan en los mismos grupos pueden ser intercambiables en cierta medida.
        
        # Para sugerir ingredientes sustitutos para un ingrediente dado en una receta, se puede utilizar el análisis de modularidad para identificar otros ingredientes que se utilizan en los mismos grupos que el ingrediente dado, lo que sugiere que pueden ser intercambiables en cierta medida. También se puede utilizar el análisis de caminos mínimos para encontrar ingredientes conectados al ingrediente dado que pueden ser utilizados como sustitutos.
        
        pass
    
    def build_a_familly_weak_menu(self, available_recipes, hints):
        
        pass
    
    def estimate_recipe_cost(self, recipe: dict):

        
        
        # Buscar en un dict de ingredientes sus datos de costo
        
        # de la receta sacar la cantidad de ingredientes
        
        # normalizar las cantidades bajo cirterios conocidos para multiplicar costo por cantidad
        
        # retornar suma de costos por ingredientes
        
        pass
    
    pass