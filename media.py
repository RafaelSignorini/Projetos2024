print("Escolha o bimestre para calcular a nota")

print("Preencha abaixo as informações da sua primeira média")
AVAparcial1 = float(input("Nota da AVA parcial: "))
AVAfinal1 = float(input("Nota da AVA final: "))
AC1 = float(input("Nota da AC: "))

print("Agora as informações da sua produtividade")

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

print(f"Sua primeira média é de {M1} pontos")

print("Preencha abaixo as informações da sua segunda média")
AVAparcial2 = float(input("Nota da AVA parcial: "))
AVAfinal2 = float(input("Nota da AVA final: "))
AC2 = float(input("Nota da AC: "))

print("Agora as informações da sua produtividade")
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

print(f"Sua segunda média é de {M2} pontos")

print("Preencha abaixo as informações da sua terceira média")
AVAparcial3 = float(input("Nota da AVA parcial: "))
AVAfinal3 = float(input("Nota da AVA final: "))
AC3 = float(input("Nota da AC: "))

print("Agora as informações da sua produtividade")

desempenho3 = float(input("Nota do desempenho: "))
participacao3 = float(input("Nota da participação: "))
caderno3 = float(input("Nota das anotações do caderno: "))
autoavaliacao3 = float(input("Nota da autoavaliação: "))

Produtividade3 = (desempenho3 + participacao3 + caderno3 + autoavaliacao3) / 4

AVAp03 = AVAparcial3 * 0.25
AVAf03 = AVAfinal3 * 0.25
AC03 = AC3 * 0.3
Prod03 = Produtividade3 * 0.2

M3 = (AVAp03 + AVAf03 + AC03 + Prod03)

print(f"Sua terceira média é de {M3} pontos")

print("Preencha abaixo as informações da sua quarta média")
AVAparcial4 = float(input("Nota da AVA parcial: "))
AVAfinal4 = float(input("Nota da AVA final: "))
AC4 = float(input("Nota da AC: "))

print("Agora as informações da sua produtividade")

desempenho4 = float(input("Nota do desempenho: "))
participacao4 = float(input("Nota da participação: "))
caderno4 = float(input("Nota das anotações do caderno: "))
autoavaliacao4 = float(input("Nota da autoavaliação: "))

Produtividade4 = (desempenho4 + participacao4 + caderno4 + autoavaliacao4) / 4

AVAp04 = AVAparcial4 * 0.25
AVAf04 = AVAfinal4 * 0.25
AC04 = AC4 * 0.3
Prod04 = Produtividade4 * 0.2

M4 = (AVAp04 + AVAf04 + AC04 + Prod04)

print(f"Sua quarta média é de {M4} pontos")

MF1 = (M1 + M2) / 2
if MF1 >= 7 and MF1<= 10:
    print("Só o básico também")
elif MF1 >= 0 and MF1 <7:
    print("Tinha que ser protótipo de henry")
else:
    print("Algum(ns) valor(es) inserido(s) está(ão) inválido(s), refaça o processo desde o início.")
    
#Só deus sabe como ta a mente do palhaço KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK