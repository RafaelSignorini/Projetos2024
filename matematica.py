def jurosAnualComposto():
    # Este código não está perfeitamente funcional
    C = float(input("Digite o valor do Capital: \n"))
    t = float(input("Digite o valor do tempo investido em anos: \n"))
    i = float(input("Digite o valor da taxa anual: \n"))
    M = C * (1 + i)**t
    return "O juros após {} anos sobre um capital de {} reais e uma taxa de {}%, será de {}".format(t, C, i * 100, M - C)

def taxaMensalComposto():
    # Este código não está perfeitamente funcional
    C = float(input("Digite o valor do capital: \n"))
    t = float(input("Digite o tempo em que será investido o dinheiro: \n"))
    M = float(input("Digite o valor montante após o investimento: \n"))
    return "A taxa de juros aplicada ao capital de {} reais por {} meses com um montante de {} reais, foi {}%".format(C, t, M, M / C **(1/t))

print(1.5 ** (1/3))