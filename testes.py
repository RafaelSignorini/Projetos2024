def media(bimestre):
    notas1 = []
    notas2 = []
    ACs = []
    produtividade = []
    for i in range(0, 4):
        notas1.append(float(input('')))
    for i in range(0, 4):
        notas2.append(float(input('')))
    for i in range(0, 4):
        ACs.append(float(input('')))
    for i in range(0, 4):
        produtividade.append(float(input('')))
    media = ((notas1 * 0.25) + (notas2 * 0.25) + (ACs * 0.3) + (produtividade * 0.2))
    return media