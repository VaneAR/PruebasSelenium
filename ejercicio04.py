
def porcentaje_sexo(total, hombres, mujeres):
    """
    >>> porcentaje_sexo(2,1,1)
    % Mujeres 50.0
    % Hombres 50.0
    """

    cant_hombres = (hombres * 100) / total
    cant_mujeres = (mujeres * 100) / total
    print ("% Mujeres", cant_mujeres)
    print ("% Hombres", cant_hombres)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
