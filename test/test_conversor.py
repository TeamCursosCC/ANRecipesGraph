import unittest

from RecipesEngine.conversor import ConversionUnidadesCocina

recipe_example = {
    "name": "No-Bake Nut Cookies",
    "ingredients": [
        {
            "sentence": "1 cups firmly packed brown sugar",
            "quantity": "1",
            "unit": "cup",
            "name": "brown sugar",
        },
        {
            "sentence": "1/2 cups evaporated milk",
            "quantity": "0.5",
            "unit": "cups",
            "name": "milk",
        },
        {
            "sentence": "1/2 teaspoon vanilla",
            "quantity": "0.5",
            "unit": "teaspoons",
            "name": "vanilla",
        },
        {
            "sentence": "1/2 cups broken nuts (pecans)",
            "quantity": "0.5",
            "unit": "cups",
            "name": "broken nuts",
        },
        {
            "sentence": "2 tablespoon butter or margarine",
            "quantity": "2",
            "unit": "tablespoons",
            "name": "butter",
        },
        {
            "sentence": "3 1/2 cups bite size shredded rice biscuits",
            "quantity": "3.5",
            "unit": "cups",
            "name": "bite size shredded rice biscuits",
        },
    ],
}


class UnitConverterTestCase(unittest.TestCase):
    def testUnitConverter(self):  # test method names begin with 'test'
        conversor = ConversionUnidadesCocina()
        value = None
        for ing in recipe_example["ingredients"]:
            print(ing["name"])
            print(ing["unit"])
            print(ing["quantity"])
            if ing["unit"] in ["cups", "cup"]:
                value = conversor.cup_to_L(float(ing["quantity"]))
                pass
            elif ing["unit"] == "tablespoons":
                value = (conversor.tbsp_to_mL(float(ing["quantity"]))) / 1000
                pass
            elif ing["unit"] == "teaspoons":
                value = (conversor.tsp_to_mL(float(ing["quantity"]))) / 1000
                pass
            print(value)
            pass
        self.assertTrue(value > 0.0, "converted")
        pass


if __name__ == "__main__":
    unittest.main()
    pass
