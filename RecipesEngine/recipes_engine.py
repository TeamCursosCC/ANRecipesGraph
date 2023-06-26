import networkx as nx
import json
import random
import pprint
import pandas as pd
from RecipesEngine.amazon_scraper import AmazonPriceScraper
import sys
sys.setrecursionlimit(10000)


class RecipesEngine:
	"""
	Class Description: RecipesEngine
	"""

	def __init__(self, graph_path):
		self.graphPath = graph_path

		self.recipesGraph = None

		self.is_loaded = False
		self.amazon_scraper = AmazonPriceScraper()
		try:
			self.is_loaded = True
			self.load_graph()
			pass
		except Exception as e:
			print(e)
			self.is_loaded = False
			pass

		if self.recipesGraph is None:
			self.recipesGraph = nx.DiGraph()
			# self.recipesGraph = nx.Graph()

		pass

	def load_graph(self):
		self.recipesGraph = nx.read_graphml(self.graphPath)
		pass

	def save_graph(self):
		nx.write_graphml(self.recipesGraph, self.graphPath)
		pass

	def update_graph_from_json(self, json_data_path):
		recipes = {}
		with open(json_data_path) as f:
			recipes = json.load(f)

		# TODO: Add Filter for similar names on recipes or ingredients

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

	def update_graph_from_large_json_dataset(self, dataset_dir_path):
		from RecipesEngine.recipes_model import JsonRecipesLoaderV1

		json_loader = JsonRecipesLoaderV1(self.recipesGraph)
		success = json_loader.load_json_files(dataset_dir_path)
		return success
	
	def check_ingredient(self, target:str):
		return self.recipesGraph.in_degree(target) > 0
	
	def check_recipe(self, target:str):
		return self.recipesGraph.out_degree(target) > 0

	def suggest_recipes_from_ingredients(self, ingredients: list):
		# 5. Para sugerir platos a partir de ingredientes dados, se puede utilizar el grafo de ingredientes y recetas para encontrar las recetas que contengan los ingredientes dados y sugerir los platos correspondientes.

		# 1. Análisis de centralidad: Este análisis se utiliza para identificar los nodos más importantes en una red. En el contexto de un grafo de recetas e ingredientes, se puede utilizar para identificar los ingredientes más utilizados en las recetas. Esto puede ser útil para sugerir platos a partir de ingredientes dados, ya que los ingredientes más comunes probablemente se utilizarán en muchas recetas diferentes.

		# 3. Análisis de caminos mínimos: Este análisis se utiliza para encontrar la ruta más corta entre dos nodos en una red. En el contexto de un grafo de recetas e ingredientes, se puede utilizar para encontrar la ruta más corta entre dos ingredientes dados. Esto puede ser útil para sugerir platos a partir de ingredientes dados, ya que los ingredientes que están conectados por una ruta corta probablemente se utilizan juntos con frecuencia.

		# 4. Análisis de comunidades: Este análisis se utiliza para identificar grupos de nodos altamente interconectados que están más densamente conectados entre sí que con el resto de la red. En el contexto de un grafo de recetas e ingredientes, se puede utilizar para identificar grupos de recetas que comparten ingredientes comunes. Esto puede ser útil para sugerir platos a partir de ingredientes dados, ya que las recetas que comparten ingredientes comunes pueden ser similares en sabor y estilo.

		# Para sugerir platos a partir de ingredientes dados, se puede utilizar una combinación de estas técnicas, como la centralidad de grado para identificar los ingredientes más comunes, el análisis de caminos mínimos para encontrar los ingredientes conectados a los ingredientes dados y el análisis de comunidades para identificar grupos de recetas que comparten ingredientes comunes.

		pass

	def suggest_ingredient_substitute(self, target_ingredient, recipe_hint):
		
		selected_communities = []

		# 1. Calcular varias veces las comunidades (buscar comunidades pequeñas) con el mismo algoritmo
		print("Louvain Community detections")
		iterations = 5
		louvain_resolution = 1.5
		louvain_threshold = 0.0000001
		
		for i in range(iterations):
			random_seed = random.randint(0, 2**32 - 1)

			print("\nIteration", i)
			print("Louvain Resolution", louvain_resolution)
			print("Louvain Threshold", louvain_threshold)
			print("Louvain Seed", random_seed)
			
			community = nx.community.louvain_communities(
				self.recipesGraph,
				resolution=louvain_resolution,
				threshold=louvain_threshold,
				seed=random_seed,
			)

			print("Community count", len(community))

			# 2. Encontrar el ingrediente que se quiere reemplazar por cada iteracion y guardar la comunidad correspondiente 
			for c in community:
				# print(c)
				if target_ingredient in c:
					selected_communities.append(c)
					break                
				pass

			pass
		
		# 3. Por cada comunidad extraer los ingredientes e incrementar un orden de aparicion para cada ingrediente
		selected_ingredients = {}
		for sel_com in selected_communities:
			for member in sel_com:
				if member == target_ingredient:
					continue
				if self.check_ingredient(member):
					if member not in selected_ingredients:
						selected_ingredients[member] = 0
					selected_ingredients[member] += 1
					pass 
				pass
			pass
		
		# 4. Devolver el ingrediente con mayor orden de aparicion, o la lista con los ingredientes coincidentes con el marcador de orden de aparicion. Se puede normalizar el orden de aparicion de 0 a 1 para tomarlo como probabilidad de aparicion.
		
		total = len(selected_ingredients)
		print("\nSelected Ingredients distribution:")
		for k in selected_ingredients:
			selected_ingredients[k] /= total
			print(f"{k}: {selected_ingredients[k]:.3f}")
			pass
				
		max_item = max(selected_ingredients.items(), key=lambda x: x[1])

		# TODO: Luego se pudiera reforzar buscando caminos minimos del nodo a sustituir a los ingredientes que aparecieron en las comunidades coincidentes con un mayor grado de ocurrencia.
		# Si la receta objetivo aparece en el camino minimo entre el ingrediente objetivo y el supuesto sustituto, es mas probable que pueda ser un buen sustituto???
		# Quiza ya el propio algoritmo de modularidad tiene en cuenta eso???

		return max_item[0]

	def build_a_familly_weak_menu(self, available_recipes, hints):
		pass

	def get_recipes_from_node(self, recipe: str):        
		if self.check_recipe(target = recipe):
			recipe_dict = {}
			recipe_dict["name"] = recipe 
			recipe_dict["ingredient"] = []
			for ingredient in list(self.recipesGraph.neighbors(recipe)):
				edges = self.recipesGraph.get_edge_data(recipe, ingredient)
				recipe_dict["ingredient"].append(
					{"name":ingredient,"quantity":edges.get("quantity"),"unit":edges.get("unit")})               
				pass
			return recipe_dict
			pass
		return None    
		pass

	def recursive_search(self, recipe: str, visited=None):
		if recipe in self.visited:
			return
			pass
		self.visited.append(recipe)
		for neighbor in list(self.recipesGraph.neighbors(recipe)):
			if self.check_recipe(neighbor):
				#print(neighbor)
				self.visited.append(neighbor)
				self.recursive_search(neighbor, self.visited)
				pass
			pass
		return self.visited
		pass

	def estimate_recipe_cost(self, recipe: str):
		# Buscar en un dict de ingredientes sus datos de costo
		# de la receta sacar la cantidad de ingredientes
		# normalizar las cantidades bajo cirterios conocidos para multiplicar costo por cantidad
		# retornar suma de costos por ingredientes

		self.visited = list()
		recipe_list = self.recursive_search(recipe, visited = self.visited)

		recipe_search = {}
		for _recipe in recipe_list:
			
			datos = {'NAME':[],'ASIN':[],"QUANTITY":[],"UNIT":[],'PRICE':[],'RATINGS':[],'RATINGS NUM':[],'LINK':[]}
			report_df = pd.DataFrame.from_dict(datos)
			
			for x in self.get_recipes_from_node(_recipe)['ingredient']:
				amazon_scraper = AmazonPriceScraper()
				dataframe_row = amazon_scraper.scraper_engine(product = x['name'])
				del amazon_scraper
				print(dataframe_row)
				report_df = report_df.append(dataframe_row, ignore_index=True)
				pass
			
			output = f'{_recipe}.csv'
			report_df.to_csv(output, index=True)
			pass

		pass

	pass



