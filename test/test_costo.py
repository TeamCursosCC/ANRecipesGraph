import unittest

from RecipesEngine.price_engine import prices

recipe_example = {
    
}

class CostoTestCase(unittest.TestCase):
   def testLoadCsvData(self): # test method names begin with 'test'
        stop_count = 1
        for recipe in csv_loader.getRecipe():
            print(recipe)
            stop_count -= 1
            if stop_count <= 0:
                break
            pass
        self.assertTrue(True, "Test Runned")
        pass

if __name__ == '__main__':
    unittest.main()
    pass