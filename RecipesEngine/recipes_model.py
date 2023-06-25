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

    def __init__(self):
        pass

    def getRecipe(self, recipe_source):
        r_name = ""
        r_ingredients = []
        # read next recipe from recipe_source
        for item in recipe_source:
            # get each field and fill the m_recipe obj
            # retrieve the m_recipe obj
            yield Recipe(r_name, r_ingredients)

        pass

    pass

class JsonRecipesLoaderV1(IRecipeGetter):
    """
    Class Description: JsonRecipesLoaderV1
    """
    def __init__(self, *args):
        super(JsonRecipesLoaderV1, self).__init__(*args)
        
        pass
    
    pass
