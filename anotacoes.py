# Código do Gustax0
def calcular_media(bimestre):

  notas = []
  for i in range(4):
    notas.append(float(input(f"Nota da AVA {i+1}: ")))
  AC = float(input("Nota da AC: "))

  desempenho = float(input("Nota do desempenho: "))
  participacao = float(input("Nota da participação: "))
  caderno = float(input("Nota das anotações do caderno: "))
  autoavaliacao = float(input("Nota da autoavaliacao: "))

  Produtividade = (desempenho + participacao + caderno + autoavaliacao) / 4

  if notas[0] > notas[1]:
    M = ((notas[0] * 0.25) + (notas[1] * 0.25) + (AC * 0.3) + (Produtividade * 0.2)) / 4
  elif notas[0] <= notas[1]:
    M = ((notas[1] * 0.5) + (AC * 0.3) + (Produtividade * 0.2)) / 3
  else:
    print("Placeholder")
    return None

  return M

medias = []
for bimestre in range(1, 5):
  medias.append(calcular_media(bimestre))

MF1 = (medias[0] + medias[1]) / 2
MF2 = (medias[2] + medias[3]) / 2

if MF1 >= 7 and MF1 <= 10:
  print("Só o básico também")
elif MF1 >= 0 and MF1 < 7:
  print("Você não passou. (Tinha que ser protótipo de henry).")
  EF1 = float(input("Escreva a nota do seu exame final do primeiro semestre: "))
  if EF1 >= 5 and EF1 <= 10:
    MF1 = ((medias[0] + medias[1]) + EF1 * 2) / 4
    print(f"Sua nota final do primeiro semestre foi de {MF1} pontos.")
  elif EF1 < 5 and EF1 >= 0:
    print("Você não passou no exame.")
  else:
    print("Valor inserido inválido, tente novamente.")
else:
  print("Algum(ns) valor(es) inserido(s) está(ão) inválido(s), refaça o processo desde o início.")

if MF2 >= 7 and MF2 <= 10:
  print("Só o básico também")
elif MF2 >= 0 and MF2 < 7:
  print("Você não passou. (Tinha que ser protótipo de henry).")
  EF2 = float(input("Escreva a nota do seu exame final do segundo semestre: "))
  if EF2 >= 5 and EF2 <= 10:
    MF2 = ((medias[2] + medias[3]) + EF2 * 2) / 4
    print(f"Sua nota final do segundo semestre foi de {MF2} pontos.")
  elif EF2 < 5 and EF2 >= 0:
    print("Você não passou no exame.")
  else:
    print("Valor inserido inválido, tente novamente.")
else:
  print("Algum(ns) valor(es) inserido(s) está(ão) inválido(s), refaça o processo desde o início.")

MF = (MF1 + MF2) / 2
print(f"Sua média anual foi de {MF} pontos.")

# Código do Noobpro112
def calcular_media(bimestre):
  notas = [float(input(f"Nota da AVA {i+1}: ")) for i in range(4)]
  AC = float(input("Nota da AC: "))
  Produtividade = sum(float(input(f"Nota do {item}: ")) for item in ["desempenho", "participação", "anotações do caderno", "autoavaliacao"]) / 4

  M = ((max(notas) * 0.5) + (AC * 0.3) + (Produtividade * 0.2))

  return M

medias = [calcular_media(bimestre) for bimestre in range(1, 5)]

MF1 = sum(medias[:2]) / 2
MF2 = sum(medias[2:]) / 2

for i, MF in enumerate([MF1, MF2], 1):
  if 7 <= MF <= 10:
    print("Só o básico também")
  elif 0 <= MF < 7:
    print("Você não passou. (Tinha que ser protótipo de henry).")
    EF = float(input(f"Escreva a nota do seu exame final do semestre {i}: "))
    if 5 <= EF <= 10:
      MF = (MF + EF * 2) / 3
      print(f"Sua nota final do semestre {i} foi de {MF} pontos.")
    elif 0 <= EF < 5:
      print("Você não passou no exame.")
    else:
      print("Valor inserido inválido, tente novamente.")
  else:
    print("Algum(ns) valor(es) inserido(s) está(ão) inválido(s), refaça o processo desde o início.")

MF = (MF1 + MF2) / 2
print(f"Sua média anual foi de {MF} pontos.")