import math 

# Constantes
# Fórmula: F = k * (q1 * q2) / d**2
q1 = 3 * (10**-6)
q2 = 5 * (10**-6)
k = 9 * (10**9)                                                         # Constante de Coulomb (N m^2/C^2)
d = 5 * (10**-2)                                                        # Distância entre as cargas (m)
print("A váriavel 'F' tem o valor de {}".format(k * (q1 * q2) / d**2))  # Impressão do resultado