#Los precios Fecha de actualización: diciembre, 2021
#https://precio-alimentos.eltoque.com/

prices = {}
prices["rice"]             = {"price":"45","unit":"lb"}
prices["black bean"]      = {"price":"80","unit":"lb"}
prices["red bean"]   = {"price":"100","unit":"lb"}
prices["eggs"]             = {"price":"15","unit":"unidad"}

prices["chicken"]             = {"price":"70","unit":"lb"}
prices["pork"]             = {"price":"250","unit":"lb"}
prices["beef"]               = {"price":"280","unit":"lb"}
prices["fish"]           = {"price":"150","unit":"unidad"}

prices["cheese"]             = {"price":"125","unit":"lb"}
prices["milk"]             = {"price":"600","unit":"kg"}

prices["potatoes"]              = {"price":"50","unit":"kg"}
prices["taro"]           = {"price":"40","unit":"lb"}
prices["sweet potato"]           = {"price":"15","unit":"lb"}
prices["pumpkin"]          = {"price":"6","unit":"lb"}
prices["banana"]           = {"price":"30","unit":"lb"}
prices["onions"]           = {"price":"30","unit":"lb"}
prices["pepper"]          = {"price":"80","unit":"lb"}
prices["corn"]              = {"price":"5","unit":"unidad"}
prices["tomato"]            = {"price":"20","unit":"lb"}
prices["string beans"]        = {"price":"15","unit":"lb"}
prices["carrots"]         = {"price":"15","unit":"lb"}
prices["cucumbers"]            = {"price":"7","unit":"lb"}
prices["yucca"]              = {"price":"15","unit":"lb"}

prices["pineapples"]				= {"price":"40","unit":"unidad"}
prices["papaya"]		= {"price":"10","unit":"lb"}
prices["mango"]				= {"price":"20","unit":"lb"}
prices["guava"]			= {"price":"20","unit":"lb"}
prices["lemon"]				= {"price":"100","unit":"lb"}

prices["oil"]			= {"price":"700","unit":"L"}

class PriceEngine(object):
	"""docstring for PriceEngine"""
	def __init__(self, arg):
		super(PriceEngine, self).__init__()
		self.prices = prices

	def get_price(self, product):
		return self.prices[product]
		pass
		