# -*- coding: utf-8 -*-


def calificacion_final(par1, par2, par3):
    """
    >>> calificacion_final(10,10,10)
    10.0
    >>> calificacion_final(8,9,10)
    9.0
    """
    calfinal = par1 + par2 + par3
    promedio = calfinal / 3
    return promedio

if __name__ == "__main__":
    import doctest
    doctest.testmod()
