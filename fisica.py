def descubraForca():
    import math 

    # Constantes
    # Fórmula: F = k * (q1 * q2) / d**2
    q1 = 3 * (10**-6)
    q2 = 5 * (10**-6)
    k = 9 * (10**9)                                                         
    d = 5 * (10**-2)                                                        
    return "A váriavel 'F' tem o valor de {}".format(k * abs(q1 * q2) / d**2)  

def descubraCampoAfastado():
    dQuadrado = 40**2 + 20**2
    hipotenusa = dQuadrado**(1/2)

    Qa = 48 * (10**-6)
    Qb = 16 * (10**-6)
    k = 9 * (10**9)
    F = 40 * (10**5)
    d = (k * abs(Qa * Qb / F)**0.5)
    return "A variável 'F' tem o valor de {} e a distância 'd' é {:.2f}".format(F, d)

print(descubraCampoAfastado())