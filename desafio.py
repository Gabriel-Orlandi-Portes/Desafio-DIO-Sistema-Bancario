menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limites_saques = 3

while True:
    try:
        escolha = int(input(menu))
    except ValueError:
        print("Digite apenas números.")
        continue

    if escolha == 1:
        deposito = float(input('Digite a o valor que você deseja depositar: '))
        if deposito > 0:
            print(f'Valor de R${deposito} depositado na conta!')
            saldo += deposito
            extrato += f'Deposito: R${deposito:.2f}\n'
        else:
            print('Valor inválido.')
    
    elif escolha == 2:
        saque = float(input('Digite o valor que você deseja sacar: R$'))

        if saque > saldo:
            print('Operação inválida, o valor que você deseja sacar é maior do que o seu saldo')
        
        elif numero_saques >= limites_saques:
            print('Você já excedeu o limite de saques diários, por favor, volte amanhã')
        
        elif saque > limite:
            print('Operação inválida, o limite permitido para saques é de R$500,00')
        
        elif saque > 0:
            print(f'Saque de R${saque} concluído!')
            numero_saques += 1
            saldo -= saque
            extrato += f'Saque: R${saque:.2f}\n'
        
    elif escolha == 3:
        print('*' * 15, 'EXTRATO', '*' * 15)
        if not extrato:
            print('Sem movimentações de extrato\n')
        else:
            print(extrato)
        print(f'Saldo Atual: R${saldo:.2f}')
        print('*' * 39)

    elif escolha == 4:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")  

        

    

