import math


class ErroGeometrico(Exception):
    pass

def hipotenusa(cat_a: float, cat_b: float):
    if (cat_a < 0) or (cat_b < 0):
        raise ErroGeometrico("Erro! Cateto com valor negativo")

    return math.sqrt(cat_a**2 + cat_b**2)
