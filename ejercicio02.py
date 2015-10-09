# -*- coding: utf-8 -*-

def total_pagar(costo):

    """
    >>> total_pagar(500)
    425.0
    >>> total_pagar(950)
    807.5
    """
    descuento = costo * 0.15
    return (costo - descuento)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
