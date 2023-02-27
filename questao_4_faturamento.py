#Função de calcular porcentagem a partir de uma lista
def calcular_porcentagem_por_lista(lista):
    #definindo as variaveis iniciais
    valor_total = 0
    lista_de_porcentagem = []
    #calculando o valor total da lista  para calcular porcentagem (poderia ser feito com sum(lista))
    for i in lista:
        valor_total += i
    #Calculando para cada item da lista uma porcentagem relativa ao valor total
    for i in lista:
        porcentagem = round(100*(i / valor_total),2)
        lista_de_porcentagem.append(porcentagem)
    #retornando os valores das porcentagens
    return lista_de_porcentagem

#Função principal do programa
def main():
    faturamento = {"SP": 67836.43, "RJ": 36678.66,"MG":29229.88,"ES":27165.48,"Outros":19849.53}
    lista = list(faturamento.values())
    lista_porcentagens = calcular_porcentagem_por_lista(lista)
    print (f"A partir dos seguintes valores: {faturamento} \n Obtiveram as respectivas porcentagens{lista_porcentagens}")

#Chamando a função principal do python
if __name__ == "__main__":
    main()