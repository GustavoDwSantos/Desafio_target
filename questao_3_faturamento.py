import json
#Importando os dados do arquivo json

with open ("./dados.json") as file:
    dados = json.load(file)

#tirando os valores nulos dos dados
valores_nao_nulos = []
dados_nao_nulos = []

for dado in dados:
    if dado['valor'] != 0:
        valores_nao_nulos.append(dado['valor'])
        dados_nao_nulos.append(dado)

#calculando os valores medios 
valor_medio = round(sum(valores_nao_nulos)/len(valores_nao_nulos),4)

#menor e maior valor
menor_valor = min(valores_nao_nulos)
maior_valor = max(valores_nao_nulos)

#retirando os dias dos valores acima da media
dias_acima_media = []
for dado in dados:
    if dado["valor"] > valor_medio:
        dias_acima_media.append(dado["dia"])

#resultados 
print(f"O menor valor de faturamento ocorrido em um dia do mês foi de {menor_valor} no dia {dados_nao_nulos[valores_nao_nulos.index(menor_valor)]['dia']}")
print(f"O maior valor de faturamento ocorrido em um dia do mês foi de {maior_valor} no dia {dados_nao_nulos[valores_nao_nulos.index(maior_valor)]['dia']}")
print(f'Ocorreram {len(dias_acima_media)} dias em que o faturamento foi acima da media, nos dias {dias_acima_media} ')
