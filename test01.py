# -*- coding: utf-8 -*-


def calcular_edad(edad):
    """
    >>> calcular_edad(0)
    No existes

    >>> calcular_edad(13)
    Eres niño

    >>> calcular_edad(18)
    Eres adolescente

    >>> calcular_edad(65)
    Eres adulto

    >>> calcular_edad(120)
    Eres adulto mayor
    """

    if edad <= 0:
        print "No existes"
    elif edad <= 13:
        print "Eres niño"
    elif edad <= 18:
        print "Eres adolescente"
    elif edad <= 65:
        print "Eres adulto"
    elif edad <= 120:
        print "Eres adulto mayor"
    else:
        print "Eres Mummm-Ra"

    if __name__ == "__main__":
        import doctest
        doctest.testmod()
