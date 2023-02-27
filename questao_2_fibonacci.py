#Funcao do processamento do fibonacci e comparação com o numero requisitado
def fibonacci(numero):
    #lista com os valores iniciais do fibonacci
    fibonacci = [0,1]
    #Loop ate o numero requisitado ser maior que ultimo termo da listaa
    while fibonacci[-1] < numero:
        #soma dos dois ultimos indices
        novo_indice = fibonacci[-1] + fibonacci[-2]
        #adicionando a soma dos dois indices do fibonacci
        fibonacci.append(novo_indice)
    #Retornando a comparação do ultimo termo da lista com o numero requisitado
    return fibonacci[-1] == numero

#função principal do programa
def main():
    #Entrada de valores 
    numero = int(input("Insira o numero a ser testado:"))
    #Condicional para verificar se o numero pertence a sequencia ou não
    if fibonacci(numero):
        print ("O numero pertence a sequencia de fibonacci")
    else: print ("O numero não pertence a sequencia")

if __name__ == "__main__":
    main()