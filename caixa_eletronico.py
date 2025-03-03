import os
saldo_inicial= 0
extrato_deposito = []
extrato_saque = [] 

while True:
    print('Menu:')
    print('1. Saldo')
    print('2. Sacar')
    print('3. Depositar')
    print('4. Extrato')
    print('5. Sair')
    opcao = input('Operação: ')

    if opcao == '1':
        print(f'R${saldo_inicial:,.2f}')
        
    elif opcao == '2':
        os.system('cls')
        valor_saque = (input('Valor saque R$'))

        try:
            valor_saque= float(valor_saque)
        except ValueError:
            print('Apenas número. Informe o valor de saque')
            continue
        
        if valor_saque <= 9:
            print('Valor mínimo para saque R$10,00')
        
        if saldo_inicial < valor_saque:
            print('Saldo insuficiente')

        else: 
            saldo_inicial -= valor_saque
            extrato_saque.append(valor_saque)
            print(f'Saque realizado com sucesso.')

    elif opcao == '3':
        os.system('cls')
        valor_deposito = input('Valor para depósito R$')
        
        try:
            valor_deposito= float(valor_deposito)  
        except ValueError:
            print('Apenas número. Informe o valor de deposito.')
            continue
        
        if valor_deposito >= 10:
            saldo_inicial += valor_deposito
            extrato_deposito.append(valor_deposito)
            print('Depósito efetuado com sucesso.')

        else:
            print(f'Valor minimo para depósito R$10,00')
        
    elif opcao == '4':
        os.system('cls')
        print('Extrato de saques:')
        for n, negativo in enumerate(extrato_saque):
            print(f'R$-{negativo:,.2f}')
        print('-' *30)

        print('Extrato de Depositos:')
        for n, positivo in enumerate(extrato_deposito):
            print (f'R${positivo:,.2f}')
        print('-' *30)
    elif opcao == '5':
        print('Saindo do caixa eletronico...')
        break
    else:
        print('Operação inválida.')
