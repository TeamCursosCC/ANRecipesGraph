import unittest

from RecipesEngine.recipes_model import CsvRecipesLoader

CSV_DATA_PATH = "C:/Users/Roger/Desktop/work/posgrados/cna/proyecto/Data/dataset.csv"

csv_loader = CsvRecipesLoader(CSV_DATA_PATH)

class CsvRecipesDataLoaderTestCase(unittest.TestCase):
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