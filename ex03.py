[
  {"dia": 1, "valor": 22174.1664},
  {"dia": 2, "valor": 24537.6698},
  {"dia": 3, "valor": 26139.6134},
  {"dia": 4, "valor": 0.0},
  {"dia": 5, "valor": 0.0},
  {"dia": 6, "valor": 26742.6612}
]



import json

with open('faturamento.json', 'r') as f:
    dados = json.load(f)

valores = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor = min(valores)
maior = max(valores)
media = sum(valores) / len(valores)

dias_acima_media = sum(1 for v in valores if v > media)

print("Menor faturamento:", menor)
print("Maior faturamento:", maior)
print("Dias com faturamento acima da média:", dias_acima_media)
