# El ejercicio base, considerando dos rectángulos iguales superpuestos. Puedes parametrizar la superposición entre ambos rectángulos.
# Ambos rectángulos orientados en 0°
# Solo se admite para desplazamiento positivo en x e 
def max_abrect_in_two_overlapped_xyrect(a,b,x,y,dx,dy):
    
    # Variables
    max_paneles = 0

    # Se prueba el techo en 0° y 90°
    rango_a_iterar = range(int(max(x,y)//min(a,b)) + 1)
    for xx,yy,dxx,dyy in [[x,y,dx,dy],[y,x,dy,dx]]:

        # Loop paneles en 0° y 90° esquina superior-izquierda
        for panel1_rotado in [True,False]:
            for h1 in rango_a_iterar: # Filas
                for v1 in rango_a_iterar: # Columnas

                    # Loop paneles en 0° y 90° esquina inferior-derecha
                    for panel2_rotado in [True,False]:
                        for h2 in rango_a_iterar: # Filas
                            for v2 in rango_a_iterar: # Columnas

                                # Loop paneles en 0° y 90° esquina inferior-izquierda rectángulo superior izquierdo
                                for panel3_rotado in [True,False]:
                                    for h3 in rango_a_iterar: # Filas
                                        for v3 in rango_a_iterar: # Columnas

                                            # Vértice inferior-derecho cuadrilátero de paneles en 0°
                                            if panel1_rotado:
                                                P1 = h1 * b
                                                Q1 = v1 * a
                                            else:
                                                P1 = h1 * a
                                                Q1 = v1 * b
                                            # Vértice superior-izquierdo cuadrilátero de paneles en 90°
                                            if panel2_rotado:
                                                P2 = xx + dxx - h2 * b
                                                Q2 = yy + dyy - v2 * a
                                            else:
                                                P2 = xx + dxx - h2 * a
                                                Q2 = yy + dyy - v2 * b
                                            # Vértice inferior-izquierdo cuadrilátero de paneles en 90°/0°
                                            if panel3_rotado:
                                                P3 = h3 * b
                                                Q3 = yy - v3 * a
                                            else:
                                                P3 = h3 * a
                                                Q3 = yy - v3 * b

                                            # Comprobación de superposición de cuadriláteros
                                            if P2<P1 and Q2<Q1 or P2<P3 or Q3<Q1:
                                                continue

                                            # Comprobación de boundaries #TERMINAR ESTO!
                                            if (P1 > xx and dyy != 0 or P1 > xx + dxx) or (Q1 > yy and dxx != 0 or Q1 > yy + dxx) or (P2 < dxx and dyy != 0 or P2 < 0) or (Q2 < dyy and dxx != 0 or Q2 < 0) or (P3 > xx + dxx) or (Q3 < 0) or (Q3 < dyy and P3 > xx):
                                                continue

                                            # Suma de paneles en 0° y 90°
                                            paneles = h1*v1 + h2*v2 + h3*v3
                                            if paneles > max_paneles:
                                                #print(h1,v1,h2,v2,h3,v3)
                                                max_paneles = paneles

    # Retorno
    return max_paneles

# Testeo de casos
caso1 = max_abrect_in_two_overlapped_xyrect(1, 2, 2, 4, 0, 0) # 4
caso2 = max_abrect_in_two_overlapped_xyrect(1, 2, 3, 5, 0, 0) # 7
caso3 = max_abrect_in_two_overlapped_xyrect(2, 2, 1, 10, 0, 0) # 0
caso4 = max_abrect_in_two_overlapped_xyrect(2, 3, 3, 3, 1, 1) # 2
caso5 = max_abrect_in_two_overlapped_xyrect(9, 1, 1, 5, 0, 4) # 1
caso6 = max_abrect_in_two_overlapped_xyrect(9, 1, 1, 5, 0, 0) # 0
caso7 = max_abrect_in_two_overlapped_xyrect(2, 5, 7, 8, 1, 1) # 6
caso8 = max_abrect_in_two_overlapped_xyrect(4, 1, 3, 3, 1, 0) # 3

# Resultados
print("Caso 1:", caso1)
print("Caso 2:", caso2)
print("Caso 3:", caso3)
print("Caso 4:", caso4)
print("Caso 5:", caso5)
print("Caso 6:", caso6)
print("Caso 7:", caso7)
print("Caso 8:", caso8)