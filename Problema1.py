# La siguiente función obtiene la máxima cantidad de rectángulos de dimensiones “a” y “b” (paneles solares) que caben dentro de un rectángulo de dimensiones “x” e “y” (techo).
def max_abrect_in_xyrect(a,b,x,y):
    
    # Variables
    max_paneles = 0

    # Se prueba el techo en 0° y 90°
    for xx,yy in [[x,y],[y,x]]:

        # Loop paneles en 0° esquina superior-izquierda
        for h1 in range(int(xx//a) + 1): # Filas
            for v1 in range(int(yy//b) + 1): # Columnas

                # Loop paneles en 90° esquina inferior-derecha
                for h2 in range(int(xx//b) + 1): # Filas
                    for v2 in range(int(yy//a) + 1): # Columnas

                        # Vértice inferior-derecho rectángulo de paneles en 0°
                        P1 = h1 * a
                        Q1 = v1 * b
                        # Vértice superior-izquierdo rectángulo de paneles en 90°
                        P2 = xx - h2 * b
                        Q2 = yy - v2 * a

                        # Comprobación de superposición de rectángulo
                        if P2<P1 and Q2<Q1:
                            continue

                        # Suma de paneles en 0° y 90°
                        paneles = h1*v1 + h2*v2
                        if paneles > max_paneles:
                            max_paneles = paneles

    # Retorno
    return max_paneles

# Testeo de casos
caso1 = max_abrect_in_xyrect(1, 2, 2, 4) # 4
caso2 = max_abrect_in_xyrect(1, 2, 3, 5) # 7
caso3 = max_abrect_in_xyrect(2, 2, 1, 10) # 0

# Resultados
print("Caso 1:", caso1)
print("Caso 2:", caso2)
print("Caso 3:", caso3)