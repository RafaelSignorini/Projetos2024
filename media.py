AVAparcial1 = float(input("Nota da AVA parcial: "))
AVAfinal1 = float(input("Nota da AVA final: "))
AC1 = float(input("Nota da AC: "))

desempenho1 = float(input("Nota do desempenho: "))
participacao1 = float(input("Nota da participação: "))
caderno1 = float(input("Nota das anotações do caderno: "))
autoavaliacao1 = float(input("Nota da autoavaliação: "))

Produtividade1 = (desempenho1 + participacao1 + caderno1 + autoavaliacao1) / 4

AVAp01 = AVAparcial1 * 0.25
AVAf01 = AVAfinal1 * 0.25
AC01 = AC1 * 0.3
Prod01 = Produtividade1 * 0.2

M1 = (AVAp01 + AVAf01 + AC01 + Prod01)

AVAparcial2 = float(input("Nota da AVA parcial: "))
AVAfinal2 = float(input("Nota da AVA final: "))
AC2 = float(input("Nota da AC: "))

desempenho2 = float(input("Nota do desempenho: "))
participacao2 = float(input("Nota da participação: "))
caderno2 = float(input("Nota das anotações do caderno: "))
autoavaliacao2 = float(input("Nota da autoavaliação: "))

Produtividade2 = (desempenho2 + participacao2 + caderno2 + autoavaliacao2) / 4

AVAp02 = AVAparcial2 * 0.25
AVAf02 = AVAfinal2 * 0.25
AC02 = AC2 * 0.3
Prod02 = Produtividade2 * 0.2

M2 = (AVAp02 + AVAf02 + AC02 + Prod02)

EF = float(input("Nota do exame final: "))

if (M1 + M2) >= 14:
    MF = ((M1 + M2) * 2) / 3
    if MF >= 7:
        print("Você passou, meu mano <3")
    elif MF < 7:
        print("Burro pra caralho, num passa nem fodendo KKKKKKKKKKKKKKKK")
elif (M1 + M2) < 14:
    print("Vai ter que fazer exame, burrão")
    MF = ((M1 + M2) + EF * 2) / 4
    if MF >= 7:
        print("Só o básico também")
    elif MF < 7:
        print("Tinha que ser um protótipo de henry")
