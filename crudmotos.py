cliente = dict()
moto = dict()

def menu():
    print('MENU\n'
          '1. Adicionar novo cliente\n'
          '2. Adicionar nova moto\n'
          '3. Efetuar venda\n'
          '4. Acessar Lista de Clientes\n'
          '5. Acessar lista de motos\n'
          '6. Pesquisar Venda\n'
          '0. Sair')

def add_cliente():
        cliente.clear()
        Nome1 = str(input('Digite seu nome: ')).strip().upper()
        cliente['Nome'] = Nome1
        cliente['CPF'] = int(input('Digite seu CPF, somente digitos: '))
        cliente['e-mail'] = str(input('Digite seu e-mail: ')).strip().upper()
        if len(cliente) > 0:
            clientes()
        else:
            print("Erro ao adicionar novo cliente!")

def add_moto():
        moto.clear()
        moto['codigo'] = int(input('Digite o código do moto: '))
        moto['Modelo'] = input('Digite o modelo: ').strip().upper()
        moto['Marca'] = input('Digite a marca: ').strip().upper()
        moto['Ano'] = int(input('Digite o ano: '))
        if len(moto) > 0:
            motos()
        else:
            print("Erro em adicionar nova moto!")

def clientes():
    try:
        arquivo_clientes = open('clientes.txt', 'a')
        arquivo_clientes.write(f'{cliente}' + '\n')
        print('Novo cliente adicionado')
    except:
        arquivo_clientes = open('clientes.txt', 'x')
        arquivo_clientes = open('clientes.txt', 'w')
        arquivo_clientes.write(f'{cliente}' + '\n')
        print('Novo cliente adicionado')
    finally:
        arquivo_clientes.close()

def motos():
    try:
        arquivo_motos = open('motos.txt', 'a')
        arquivo_motos.write(f'{moto}' + '\n')
        print('nova moto adicionada')
    except:
        arquivo_motos = open('motos.txt', 'x')
        arquivo_motos = open('motos.txt', 'w')
        arquivo_motos.write(f'{moto}' + '\n')
        print('nova moto adicionada')
    finally:
        arquivo_motos.close()

def lista_clientes():
    l_clientes = open('clientes.txt', 'r+')
    for c in l_clientes:
        print(c)
    l_clientes.close()

def lista_motos():
    l_motos = open('motos.txt', 'r+')
    for m in l_motos:
        print(m)
    l_motos.close()

def vendas():
    nome = input('Digite nome do cliente: ').strip().upper()
    cpf = int(input('Digite seu CPF: '))
    cod = int(input('Digite o código da moto: '))
    data = input('Digite a data: ')
    try:
        arquivo_vendas = open('vendas.txt', 'a')
        arquivo_vendas.write(f'O cliente {nome} do CPF {cpf} comprou a moto {cod} no dia {data}' + '\n')
        print('nova venda adicionada')
    except:
        arquivo_vendas = open('vendas.txt', 'x')
        arquivo_vendas = open('vendas.txt', 'w')
        arquivo_vendas.write(f'O cliente {nome} do CPF {cpf} comprou a moto {cod} no dia {data}' + '\n')
        print('nova venda adicionada')
    finally:
        arquivo_vendas.close()

while True:
    menu()
    start = int(input("Digite sua opção: "))
    if start == 0:
        break

    elif start == 1:
        add_cliente()

    elif start == 2:
        add_moto()

    elif start == 3:
        vendas()

    elif start == 4:
        lista_clientes()

    elif start == 5:
        lista_motos()

    elif start == 6:
        consulta = (input("Digite o nome do cliente: ")).strip().upper()
        venda_esp = open('vendas.txt', 'r+')
        for v in venda_esp:
            if (consulta in v) == True:
                print(v)
    else:
        print("Essa opção é invalida, por favor digite um número válido!")

    while True:
        resposta = input('Deseja retornar ao menu inicial? [S/N]').upper()[0]
        if resposta in "SN":
            break
        else:
            print('Erro! Digite apenas S ou N')
        if resposta == "N":
            break
    if resposta == "N":
        break
print('Encerrando o programa!')


#Tratamento de excecao
#Aperfeiçoar Regra do CPF / Verificar se o CPF eh real ou nao e ajudatar pontuacao
#Adicionar Documentacao
#Utilizar Banco de dados no processo
# Explicar os passos