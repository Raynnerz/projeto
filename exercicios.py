# exercício 01
print("\n Exercício 01")

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)
# resultado 91

# exercício 02
print("\n Exercício 02")

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
a, b = 0, 1
pertence = False

while a <= numero:
    if a == numero:
        pertence = True
        break
    a, b = b, a + b

if pertence:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

# exercício 03
print("\n Exercício 03")

import json

faturamento_json = '''
{
  "faturamento_diario": [
    {"dia": 1, "valor": 1000.0},
    {"dia": 2, "valor": 0.0},
    {"dia": 3, "valor": 1500.5},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 850.75},
    {"dia": 6, "valor": 1250.0},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 750.5},
    {"dia": 9, "valor": 0.0}
  ]
}
'''

dados = json.loads(faturamento_json)
faturamento = [dia['valor'] for dia in dados['faturamento_diario'] if dia['valor'] > 0]

if faturamento:
    menor_faturamento = min(faturamento)
    maior_faturamento = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)

    dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)

    print(f"Menor valor de faturamento: {menor_faturamento}")
    print(f"Maior valor de faturamento: {maior_faturamento}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
else:
    print("Não há faturamento para calcular.")

# exercício 04
print("\n Exercício 04")

faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento_estados.values())
percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estados.items()}
print(percentuais)

# exercício 05
print("\n Exercício 05")

string_original = "Distribuidora"

string_invertida = ""
for i in range(len(string_original) - 1, -1, -1):
    string_invertida += string_original[i]

print(string_invertida)
