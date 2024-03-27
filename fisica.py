import math 

# Constantes
k = 9 * 10 ** 9     # Constante de Coulomb (N m^2/C^2)
d = 0.09            # Distância entre as cargas (m)
F = 4 * 10 ** -3    # Força eletrostática (N)

# Cálculo das cargas
q1_q2 = F * d ** 2 / k

# Impressão do resultado
print('q1 * q2 = {} C^2'.format(q1_q2))