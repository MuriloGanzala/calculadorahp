#faça uma calculadora estilo HP

# PRIMEIRAMENTE INFORMAMOS AO USUÁRIO AS OPÇÕES DISPONIVEIS PARA A RESOLUÇÃO DE CÁLCULOS, ATRÁVES DE UM LOOP WHILE 
# SEGUIDO DE PRINT COM AS OPÇÕES DISPONIVEIS.

while True:
    print("Escolha uma opção:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("X - Sair")

#AQUI ADICIONAMOS UMA ENTRADA DE DADOS PARA QUE O USUÁRIO POSSA SOLICITAR A SUA OPÇÃO ESCOLHIDA
    opcoes = input("Opção: ")

# SE A OPÇÃO FOR ==X, PARAMOS A OPERAÇÃO E ENCERRAMOS A CALCULADORA POIS ESTÁ OPÇÃO ESTÁ SETADA PARA ENCERRAR A OPERAÇÃO 
#CASO A MESMA SEJA SETADA PELO USUÁRIO
    if opcoes == "X" or opcoes == "x":
        break

# AQUI SOLICITAMOS AO USUÁRIO QUE INFORME OS VALORES QUE DESEJA CALCULAR, ATRAVÉS DE UM LOOP, O SISTEMA SOLICIARA 
# QUE O USUÁRIO INSIRA VALORES INFINATAMENTE, AO MENOS QUE, DIGITE 'P', PARA ASSIM SAIR DO LOOP DE INFORMAR VALORES E REALIZAR O CÁLCULO
    valores = []
    while True:
        valor = input("Digite um valor (ou 'P' para parar): ")
        if valor == "P" or valor == "p":
            break
        valores.append(float(valor)) 

#executa a operação escolhida pelo usuario
    if opcoes == '1': #adição
        resultado = sum(valores)
        print(f'Resultado da adição: {resultado}')
    elif opcoes == '2': #subtração
        resultado = valores[0]
        for valor in valores[1:]:
            resultado -= valor
        print(f'Resultado da subtração: {resultado}')
    elif opcoes == '3': #multiplicação
        resultado = 1
        for valor in valores:
            resultado *= valor
        print(f'Resultado da multiplicação: {resultado}')
    elif opcoes == '4': #divisão
        if 0 in valores[1:]:
            print('Erro: Divisão por zero')
        else:
            resultado = valores[0]
            for valor in valores[1:]:
                resultado /= valor
            print(f'Resultado da divisão: {resultado}')
    else:
        print('Opção inválida. Tente novamente.')
