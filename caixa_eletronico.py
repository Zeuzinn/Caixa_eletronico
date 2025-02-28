import os
saldo_inicial= 0
minimo_saque = 10
minimo_deposito = 10
extrato_deposito = []
extrato_saque = [] 

while True:
    print('Menu:')
    print('1. Saldo')
    print('2. Sacar')
    print('3. Depositar')
    print('4. Extrato')
    opcao = input('Opção: ')

    if opcao == '1':
        print(f'R${saldo_inicial:,.2f}')
        
    elif opcao == '2':
        os.system('cls')
        valor_saque = (input('Valor saque R$'))

        try:
            letra= float(valor_saque)
            saque = letra
        except ValueError:
            print('Apenas número. Informe o valor de saque')
            continue
        
        if saque < saldo_inicial:
            saldo_inicial -= saque
            extrato_saque.append(saque)
            print(f'Saque realizado. Saldo atual R${saldo_inicial:,.2f}')

        elif saque < minimo_saque:
            print(f'Valor minimo para saque R${minimo_saque:.2f}')
        else:
            print(f'Saldo insuficiente. Seu saldo é R${saldo_inicial:,.2f}') 

    elif opcao == '3':
        os.system('cls')
        valor_deposito = input('Valor para depósito R$')
        
        try:
            letras= float(valor_deposito)
            deposito = letras
        except ValueError:
            print('Apenas número. Informe o valor de deposito.')
            continue
        
        if deposito > minimo_deposito:
            saldo_inicial += deposito
            extrato_deposito.append(deposito)
            print('Depósito efetuado.')
            print(f'Saldo R${saldo_inicial:,.2f}')

        else:
            print(f'Valor minimo para depósito R${minimo_deposito:,.2f}')
        
    elif opcao == '4':
        os.system('cls')
        print('Extrato de saques:')
        for n, negativo in enumerate(extrato_saque):
            print(f'R$-{negativo:,.2f}')
        print('-' *30)

        print('Extrato de Depositos:')
        for n, positivo in enumerate(extrato_deposito):
            print (f'R${positivo:,.2f}')