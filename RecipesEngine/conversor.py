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

        