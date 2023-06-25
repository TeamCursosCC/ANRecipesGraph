import pandas as pd
import json
import os
import networkx as nx

class Ingredient:
    """
    Class Description: Ingredient
    """

    def __init__(self):
        self.name = ""
        self.sentence = ""
        self.quantity = 0
        self.unit = ""
        pass

    pass


class Recipe:
    """
    Class Description: Recipe
    """

    def __init__(self, name: str = "", ingredients: list = []):
        self.name = name
        self.ingredients = ingredients
        pass

    pass


class IRecipeGetter:
    """
    Class Description: IRecipeGetter
    """

    def __init__(self, recipe_source):
        self._recipe_source = recipe_source
        pass

    def getRecipe(self):
        r_name = ""
        r_ingredients = []
        # read next recipe from recipe_source
        for item in self._recipe_source:
            # get each field and fill the m_recipe obj
            # retrieve the m_recipe obj
            yield Recipe(r_name, r_ingredients)

        pass

    pass


# class JsonRecipesLoaderV1(IRecipeGetter):
class JsonRecipesLoaderV1():
    """
    Class Description: JsonRecipesLoaderV1
    """

    def __init__(self, recipes_graph: nx.Graph):
        # super(JsonRecipesLoaderV1, self).__init__(*args)

        self._recipes_graph = recipes_graph

        pass

    def _add_recipes(self, json_data: dict):
        for recipe_obj in json_data:
            r_name = recipe_obj.get("name").lower()
            
            if not r_name:
                continue

            self._recipes_graph.add_node(r_name)

            for i in recipe_obj.get("ingredients"):
                i_name = i.get("name").lower()
                
                if not i_name:
                    continue
                
                self._recipes_graph.add_node(i_name)
                self._recipes_graph.add_edge(
                    r_name, i_name, quantity=i.get("quantity", 1), unit=i.get("unit", "u")
                )

                pass

            pass

        pass

    def load_json_files(self, directory_path):
        limit = 1
        for filename in os.listdir(directory_path):
            if filename.endswith(".json"):
                # Load the JSON file as a dictionary
                with open(os.path.join(directory_path, filename)) as f:
                    json_data = json.load(f)
                # Call the add_recipes function with the dictionary as input
                self._add_recipes(json_data)
            limit -= 1
            if limit <= 0:
                break
            pass

    # def getRecipe(self):
    #     r_name = ""
    #     r_ingredients = []
    #     # read next recipe from recipe_source
    #     for item in self._recipe_source:
    #         # get each field and fill the m_recipe obj
    #         # retrieve the m_recipe obj
    #         yield Recipe(r_name, r_ingredients)

    #     pass

    pass


class CsvRecipesLoader(IRecipeGetter):
    """
    Class Description: CsvRecipesLoader
    """

    def __init__(self, csv_path: str):
        # super(CsvRecipesLoader, self).__init__(*args)

        self._csv_path = csv_path

        pass

    def readCsvByChunks(self, chunk_size: int = 256):
        # create a lazy iterator to read the CSV file in chunks
        csv_iterator = pd.read_csv(self._csv_path, chunksize=chunk_size)

        yield csv_iterator

        # # iterate over the CSV file in chunks
        # for chunk in csv_iterator:
        #     # do something with the current chunk
        #     print(chunk.head())

        pass

    def getRecipe(self):
        r_name = ""
        r_ingredients = []

        chunk_size = 20

        csv_iterator = pd.read_csv(self._csv_path, chunksize=chunk_size)

        for chunk in csv_iterator:
            for row in chunk:
                # r_name = row["title"]
                # r_ingredients = []
                print(row)

                # yield Recipe(r_name, r_ingredients)

                pass

            pass

    pass
