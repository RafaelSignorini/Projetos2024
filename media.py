print("Escolha o bimestre para calcular a nota.")

print("Preencha abaixo as informações da sua primeira média.")
AVAparcial1 = float(input("Nota da AVA parcial: "))
AVAfinal1 = float(input("Nota da AVA final: "))
AC1 = float(input("Nota da AC: "))

print("Agora as informações da sua produtividade.")

desempenho1 = float(input("Nota do desempenho: "))
participacao1 = float(input("Nota da participação: "))
caderno1 = float(input("Nota das anotações do caderno: "))
autoavaliacao1 = float(input("Nota da autoavaliação: "))

Produtividade1 = (desempenho1 + participacao1 + caderno1 + autoavaliacao1) / 4

if AVAparcial1 > AVAfinal1:
    M1 = ((AVAparcial1 * 0.25) + (AVAfinal1 * 0.25) + (AC1 * 0.3) + (Produtividade1 * 0.2)) / 4
    print(f"Sua primeira média é de {M1} pontos.")
elif AVAparcial1 <= AVAfinal1:
    M1 = ((AVAfinal1 * 0.5) + (AC1 * 0.3) + (Produtividade1 * 0.2)) / 3
    print(f"Sua primeria média é de {M1} pontos.")
else:
    print("Erro, tente novamente")

print("Preencha abaixo as informações da sua segunda média.")
AVAparcial2 = float(input("Nota da AVA parcial: "))
AVAfinal2 = float(input("Nota da AVA final: "))
AC2 = float(input("Nota da AC: "))

print("Agora as informações da sua produtividade.")
desempenho2 = float(input("Nota do desempenho: "))
participacao2 = float(input("Nota da participação: "))
caderno2 = float(input("Nota das anotações do caderno: "))
autoavaliacao2 = float(input("Nota da autoavaliação: "))

Produtividade2 = (desempenho2 + participacao2 + caderno2 + autoavaliacao2) / 4

M2 = ((AVAparcial2 * 0.25) + (AVAfinal2 * 0.25) + (AC2 * 0.3) + (Produtividade2 * 0.2)) / 4

print(f"Sua segunda média é de {M2} pontos.")

print("Preencha abaixo as informações da sua terceira média.")
AVAparcial3 = float(input("Nota da AVA parcial: "))
AVAfinal3 = float(input("Nota da AVA final: "))
AC3 = float(input("Nota da AC: "))

print("Agora as informações da sua produtividade.")

desempenho3 = float(input("Nota do desempenho: "))
participacao3 = float(input("Nota da participação: "))
caderno3 = float(input("Nota das anotações do caderno: "))
autoavaliacao3 = float(input("Nota da autoavaliação: "))

Produtividade3 = (desempenho3 + participacao3 + caderno3 + autoavaliacao3) / 4

M3 = ({AVAparcial3 * 0.25}, {AVAfinal3 * 0.25}, {AC3 * 0.3}, {Produtividade3 * 0.2}) / 4

print(f"Sua terceira média é de {M3} pontos.")

print("Preencha abaixo as informações da sua quarta média.")
AVAparcial4 = float(input("Nota da AVA parcial: "))
AVAfinal4 = float(input("Nota da AVA final: "))
AC4 = float(input("Nota da AC: "))

print("Agora as informações da sua produtividade.")

desempenho4 = float(input("Nota do desempenho: "))
participacao4 = float(input("Nota da participação: "))
caderno4 = float(input("Nota das anotações do caderno: "))
autoavaliacao4 = float(input("Nota da autoavaliação: "))

Produtividade4 = (desempenho4 + participacao4 + caderno4 + autoavaliacao4) / 4

M4 = ({AVAparcial4 * 0.25}, {AVAfinal4 * 0.25}, {AC4 * 0.3}, {Produtividade4 * 0.2}) / 4

print(f"Sua quarta média é de {M4} pontos.")

MF1 = (M1 + M2) / 2
if MF1 >= 7 and MF1<= 10:
    print("Só o básico também")
elif MF1 >= 0 and MF1 <7:
    print("Você não passou. (Tinha que ser protótipo de henry).")
    EF1 = float(input("Escreva a nota do seu exame final do primeiro semestre: "))
    if EF1 >= 5 and EF1 <= 10:
        MF1 = ((M1 + M2) + EF1 * 2) / 4
        print(f"Sua nota final do primeiro semestre foi de {MF1} pontos.")
    elif EF1 <5 and EF1 >= 0:
        print("Você não passou no exame.")
    else:
        print("Valor inserido inválido, tente novamente.")
else:
    print("Algum(ns) valor(es) inserido(s) está(ão) inválido(s), refaça o processo desde o início.")

MF2 = (M3 + M4) / 2
if MF2 >=7 and MF2 <= 10:
    print("Só o básico também")
elif MF2 >=0 and MF2 <7:
    print("Você não passou. (Tinha que ser protótipo de henry).")
    EF2 = float(input("Escreva a nota do seu exame final do segundo semestre: "))
    if EF2 >= 5 and EF2 <+ 10:
        MF2 = ((M1 + M2) + EF2 * 2) / 4
        print(f"Sua nota final do segundo semestre foi de {MF2} pontos.")
    elif EF2 <5 and EF2 >= 0:
        print("Você não passou no exame.")
    else:
        print("Valor inserido inválido, tente novamente.")
else:
    print("Algum(ns) valor(es) inserido(s) está(ão) inválido(s), refaça o processo desde o início.")

MF = (MF1 + MF2) / 2
print(f"Sua primeira média foi de {MF1} pontos.")
print(f"Sua segunda média foi de {MF2} pontos.")
if MF >= 7 and MF <= 10:
    print(f"Você passou com {MF} pontos na média anual.")
elif MF >= 0 and MF <7:
    print(f"Você não passou com {MF} pontos na média anual.")
else:
    print("Valores inseridos inválidos, tente novamente.")
#Só deus sabe como ta a mente do palhaço KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK