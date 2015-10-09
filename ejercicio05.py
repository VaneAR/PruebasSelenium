def conversion_pesos(cantidad, precio_dolar):
    """
    >>> conversion_pesos(200.0,17.50)
    11.429
    """
    resultado = cantidad / precio_dolar
    return round(resultado, 3)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
