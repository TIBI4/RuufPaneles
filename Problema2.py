# El ejercicio base, considerando un techo triangular, isóceles.
def max_abrect_in_xhtri(a,b,x,h):

    # Para lo siguiente se utiliza la ecuación de las rectas tangentes de los lados del triángulo
    # y_lado_izq = pendiente * x_coord
    # y_lado_der = -pendiente * x_coord + 2*h
    pendiente = h / (x/2)

    # Cuantos caben en 0° (1) en la base del triángulo
    x_interseccion_izq_1 = b / pendiente
    x_interseccion_der_1 = (b - 2*h) / -pendiente
    ancho_base_usable_1 = x_interseccion_der_1 - x_interseccion_izq_1

    # Cuantos caben en 90° (2) en la base del triángulo
    x_interseccion_izq_2 = a / pendiente
    x_interseccion_der_2 = (a - 2*h) / -pendiente
    ancho_base_usable_2 = x_interseccion_der_2 - x_interseccion_izq_2

    # Se comprueba si cabe un panel en alguna posición
    if ancho_base_usable_1 < a and ancho_base_usable_2 < b:
        pass
        return 0
    
    presicion = 0.99999999999
    max_paneles_base_1 = int(ancho_base_usable_1 / (a*presicion))
    max_paneles_base_2 = int(ancho_base_usable_2 / (b*presicion))

    # Bifurcación recursión
    rama_1 = max_paneles_base_1 + max_abrect_in_xhtri(a,b,ancho_base_usable_1,h-b)
    rama_2 = max_paneles_base_2 + max_abrect_in_xhtri(a,b,ancho_base_usable_2,h-a)

    return max(rama_1, rama_2)

# Testeo de casos
caso1 = max_abrect_in_xhtri(2, 8.001, 10, 10) # 0
caso2 = max_abrect_in_xhtri(5, 5, 10, 10) # 1 (supongo)
caso3 = max_abrect_in_xhtri(6, 2, 10, 10) # 2 (supongo)
caso4 = max_abrect_in_xhtri(3, 2, 10, 10) # 5 (supongo)
caso5 = max_abrect_in_xhtri(8, 1.1, 10, 10) # 1
caso6 = max_abrect_in_xhtri(0.5, 0.5, 10, 1) # 10
caso7 = max_abrect_in_xhtri(3, 1, 4, 10) # 4

# Resultados
print("Caso 1:", caso1)
print("Caso 2:", caso2)
print("Caso 3:", caso3)
print("Caso 4:", caso4)
print("Caso 5:", caso5)
print("Caso 6:", caso6)
print("Caso 7:", caso7)