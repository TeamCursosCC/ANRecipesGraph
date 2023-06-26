import pprint
"""
Volumen: 
cucharadas (tbsp) a mililitros (mL), 
cucharaditas (tsp) a mL, 
onzas líquidas (oz) a mL, 
tazas (cup) a litros (L).

Masa: 
onzas (oz) a gramos (g), 
libras (lb) a kilogramos (kg), 
gramos (g) a kilogramos (kg).
"""

class ConversionUnidadesCocina:
	# Volumen
	def tbsp_to_mL(self, tbsp):
		mL = tbsp * 14.787
		return mL

	def tsp_to_mL(self, tsp):
		mL = tsp * 4.929
		return mL

	def oz_to_mL(self, oz):
		mL = oz * 29.574
		return mL

	def cup_to_L(self, cup):
		L = cup * 0.2366
		return L

	# Masa
	def oz_to_g(self, oz):
		g = oz * 28.35
		return g

	def lb_to_kg(self, lb):
		kg = lb * 0.4536
		return kg

	def g_to_kg(self, g):
		kg = g / 1000
		return kg

test = 	{
		"name": "No-Bake Nut Cookies",
		"ingredients": [
			{
				"sentence": "1 cups firmly packed brown sugar",
				"quantity": "1",
				"unit": "cup",
				"name": "brown sugar"
			},
			{
				"sentence": "1/2 cups evaporated milk",
				"quantity": "0.5",
				"unit": "cups",
				"name": "milk"
			},
			{
				"sentence": "1/2 teaspoon vanilla",
				"quantity": "0.5",
				"unit": "teaspoons",
				"name": "vanilla"
			},
			{
				"sentence": "1/2 cups broken nuts (pecans)",
				"quantity": "0.5",
				"unit": "cups",
				"name": "broken nuts"
			},
			{
				"sentence": "2 tablespoon butter or margarine",
				"quantity": "2",
				"unit": "tablespoons",
				"name": "butter"
			},
			{
				"sentence": "3 1/2 cups bite size shredded rice biscuits",
				"quantity": "3.5",
				"unit": "cups",
				"name": "bite size shredded rice biscuits"
			}
		]
	} 

#pprint.pprint(test) 
conversor = ConversionUnidadesCocina()

for ing in test["ingredients"]:
	print(ing["name"])
	print(ing["unit"])
	print(ing["quantity"])
	if ing["unit"] in ["cups","cup"]:
		value = conversor.cup_to_L(float(ing["quantity"]))
		pass
	elif ing["unit"] == "tablespoons":
		value = (conversor.tbsp_to_mL(float(ing["quantity"])))/1000
		pass
	elif ing["unit"] == "teaspoons":
		value = (conversor.tsp_to_mL(float(ing["quantity"])))/1000
		pass
	print(value)
	pass      