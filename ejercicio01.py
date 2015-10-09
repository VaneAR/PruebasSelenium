# -*- coding: utf-8 -*-

def ganancias(sueldo_base, ventas1, ventas2, ventas3):


    """
    >>> ganancias(200,300,400,500)
    Comisiones por ventas: 120.0
    Sueldo total: 320.0
    """
    sueldo_venta1 = ventas1 * 0.10
    sueldo_venta2 = ventas2 * 0.10
    sueldo_venta3 = ventas3 * 0.10

    sueldo_total_ventas = sueldo_venta1 + sueldo_venta2 + sueldo_venta3
    print (("Comisiones por ventas:", sueldo_total_ventas))

    print(("Sueldo total:", sueldo_base + sueldo_total_ventas))

if __name__ == "__main__":
    import doctest
    doctest.testmod()









