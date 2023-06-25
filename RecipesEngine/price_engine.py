#Los precios Fecha de actualización: diciembre, 2021
#https://precio-alimentos.eltoque.com/

prices = {}
prices["Arroz"]             = {"price":"45","unit":"lb"}
prices["Frijol Negro"]      = {"price":"80","unit":"lb"}
prices["Frijol Colorado"]   = {"price":"100","unit":"lb"}
prices["Huevo"]             = {"price":"15","unit":"unidad"}

prices["Pollo"]             = {"price":"70","unit":"lb"}
prices["Cerdo"]             = {"price":"250","unit":"lb"}
prices["Res"]               = {"price":"280","unit":"lb"}
prices["Pescado"]           = {"price":"150","unit":"unidad"}

prices["Queso"]             = {"price":"125","unit":"lb"}
prices["leche"]             = {"price":"600","unit":"kg"}

prices["Papa"]              = {"price":"50","unit":"kg"}
prices["Malanga"]           = {"price":"40","unit":"lb"}
prices["Boniato"]           = {"price":"15","unit":"lb"}
prices["Calabaza"]          = {"price":"6","unit":"lb"}
prices["Plátano"]           = {"price":"30","unit":"lb"}
prices["Cebolla"]           = {"price":"30","unit":"lb"}
prices["Pimiento"]          = {"price":"80","unit":"lb"}
prices["Maíz"]              = {"price":"5","unit":"unidad"}
prices["Tomate"]            = {"price":"20","unit":"lb"}
prices["Habichuela"]        = {"price":"15","unit":"lb"}
prices["Zanahoria"]         = {"price":"15","unit":"lb"}
prices["Pepino"]            = {"price":"7","unit":"lb"}
prices["Yuca"]              = {"price":"15","unit":"lb"}

prices["Piña"]				= {"price":"40","unit":"unidad"}
prices["Fruta Bomba"]		= {"price":"10","unit":"lb"}
prices["Mango"]				= {"price":"20","unit":"lb"}
prices["Guayaba"]			= {"price":"20","unit":"lb"}
prices["Limón"]				= {"price":"100","unit":"lb"}

prices["Aceite"]			= {"price":"700","unit":"Litro"}

class PriceEngine(object):
	"""docstring for PriceEngine"""
	def __init__(self, arg):
		super(PriceEngine, self).__init__()
		self.prices = prices

	def get_price(self, product):
		return self.prices[product]
		pass
		