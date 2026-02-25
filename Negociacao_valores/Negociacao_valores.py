nome = input('Digite o nome do cliente: ')
CPF = input('Digite o CPF do cliente: ')
CPF_LIMPO = CPF.replace('.', '').replace('-', '')
CPF = int(CPF_LIMPO)
Valor_da_compra = float(input('Digite o valor da compra: '))

database = {
    36925814700:{
        'nome': 'Fernando Oliveira',
        'Categoria': 'vip'
    },
    12345678900:{
        'nome': 'Christina Castro',
        'Categoria': 'premium'
    },
    506070890:{
        'nome': 'Maria Silva',
        'Categoria': 'comum'
    }
}

if CPF in database:
    print(f'Bem-vindo, {database[CPF]["nome"]}!')

    if database[CPF]['Categoria'] == 'vip':
        Desconto = Valor_da_compra * 0.20
        Valor_final = Valor_da_compra - Desconto
        print(f'O valor final da compra é: R${Valor_final:.2f}')    

    elif database[CPF]['Categoria'] == 'premium':
        Desconto = Valor_da_compra * 0.10
        Valor_final = Valor_da_compra - Desconto
        print(f'O valor final da compra é: R${Valor_final:.2f}')
    else:
        print(f'O valor final da compra é: R${Valor_da_compra:.2f}')

else:
    Cliente = input('Digite a Categoria (vip,premium,comum)').lower()
    database[CPF] = {'nome': nome, 'Categoria': Cliente}

    if Cliente == 'comum':
        resposta = input('Deseja se cadastrar para obter descontos exclusivos? (sim/não)').lower()

        if resposta == 'sim':
            Desconto = Valor_da_compra * 0.05
            Valor_final = Valor_da_compra - Desconto
            print(f'Cadastro realizado com sucesso! Bem-vindo, {nome}! O valor final da compra é: R${Valor_final:.2f}')    
        elif resposta == 'não': 
            print(f'Entendido, {nome}. O valor final da compra é: R${Valor_da_compra:.2f}')
                
        else:
            print('Resposta inválida. Por favor, responda com "sim" ou "não".')

    elif database[CPF]['Categoria'] == 'vip':
        Desconto = Valor_da_compra * 0.20
        Valor_final = Valor_da_compra - Desconto
        print(f'O valor final da compra é: R${Valor_final:.2f}')    

    elif database[CPF]['Categoria'] == 'premium':
        Desconto = Valor_da_compra * 0.10
        Valor_final = Valor_da_compra - Desconto
        print(f'O valor final da compra é: R${Valor_final:.2f}')
    else:
        print(f'Invalido, por favor, escolha entre vip, premium ou comum.')

