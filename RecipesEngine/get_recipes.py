import epublib
import lxml.html
import re
import nltk
import pandas as pd

# Open the ePub file
book = epublib.open_epub('Nitza_Villapol_Cocina_al_minuto_Penguin_Random_House_Grupo_Editorial.epub')

# Extract the content from the book
content = 
for item in book.get_items_of_type(epublib.ITEM_DOCUMENT):
    content += item.get_content()

# Parse the content using lxml
doc = lxml.html.fromstring(content)

# Find all recipe titles
recipe_titles = doc.xpath('//h1[contains(@class, "recipe-title")]/text()')

# Find all ingredient lists
ingredient_lists = doc.xpath('//ul[contains(@class, "ingredient-list")]/li/text()')

# Find all cooking instructions
cooking_instructions = doc.xpath('//div[contains(@class, "cooking-instructions")]/p/text()')

# Use regular expressions to extract cooking times (e.g., "Cook for 30 minutes")
cooking_times = []
for instruction in cooking_instructions:
    match = re.search(r'Cook for (\d+) minutes', instruction)
    if match:
        cooking_times.append(int(match.group(1)))

# Use nltk to extract ingredient names
ingredient_names = []
for ingredient_list in ingredient_lists:
    tokens = nltk.word_tokenize(ingredient_list)
    tags = nltk.pos_tag(tokens)
    for tag in tags:
        if tag[1] == 'NN':
            ingredient_names.append(tag[0])

# Create a pandas DataFrame to store the recipe information
recipes = pd.DataFrame({
    'title': recipe_titles,
    'ingredients': ingredient_lists,
    'cooking_instructions': cooking_instructions,
    'cooking_time': cooking_times,
    'ingredient_names': ingredient_names
})