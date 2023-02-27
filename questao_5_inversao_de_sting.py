#função para inverter a string
def inverter_string(string):
    #string vazia para receber os valores 
    nova_string = ""
    #loop referenciando cada letra
    for c in string:
        #adicionando cada letra como primeiro termo ,onde o primeiro termo sempre sera a ultima letra
        nova_string = c + nova_string
    #retornando o valor da string invertida  (no python tambem podemos inverter uma string somente com [--1] na frente da variavel)
    return nova_string
        


#função principal do programa
def main():
    #entrada
    string = input("Insira sua string para ser invertida: ")
    #Processamento
    nova_string = inverter_string(string)
    #saida
    print(nova_string)

#inicialização da função principal
if __name__ == "__main__":
    main()