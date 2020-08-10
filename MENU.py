#MENU PRINCIPAL

import modulos_parametros as m

print(' ')
print('BEM VINDO À EMPRESA BIIF')

a = input('Nome de Utilizador: ')
while a != 'Marco Oliveira' and a != 'Vítor Peixoto'  and a != 'João Alves' and a != 'João Pereira' and a != 'Diogo Machado' and a != 'Gonçalo Freitas' and a != 'Carolina Peixoto' and a != 'Catarina Sousa':
    print('\nNome de utlizador inválido, por favor tente novamente!')
    a = input('Nome de Utilizador: ')
if a == 'Marco Oliveira':
    e = input('PIN: ')
    while e != '81533':
        print('PIN inválido, por favor tente novamente!')
        e = input('PIN: ')
elif a == 'Vítor Peixoto':
    e = input('PIN: ')
    while e != '81093':
        print('PIN inválido, por favor tente novamente!')
        e = input('PIN: ')
elif a == 'João Alves':
    e = input('PIN: ')
    while e != '82246':
        print('PIN inválido, por favor tente novamente!')
        e = input('PIN: ')
elif a == 'João Pereira':
    e = input('PIN: ')
    while e != '80736':
        print('PIN inválido, por favor tente novamente!')
        e = input('PIN: ')
elif a == 'Diogo Machado':
    e = input('PIN: ')
    while e != '80372':
        print('PIN inválido, por favor tente novamente!')
        e = input('PIN: ')
elif a == 'Gonçalo Freitas':
    e = input('PIN: ')
    while e != '82132':
        print('PIN inválido, por favor tente novamente!')
        e = input('PIN: ')
elif a == 'Carolina Peixoto':
    e = input('PIN: ')
    while e != '80853':
        print('PIN inválido, por favor tente novamente!')
        e = float(input('PIN: '))
elif a == 'Catarina Sousa':
    e = input('PIN: ')
    while e != '80331':
        print('PIN inválido, por favor tente novamente!')
        e = input('PIN: ')

while True:
    print('\n==========================================================')
    print('                          MENU                            ')
    print('==========================================================')
    print('1 - Manipular dados')
    print('2 - Consulta de dados dos condutores')
    print('3 - Consulta de dados das carrinhas')
    print('4 - Consulta de dados das viagens')
    print('5 - Consulta de dados dos contentores')
    print('6 - Consulta de dados das rotas')
    print('0 - Terminar')
    print('==========================================================\n')
    opcao = float(input('Introduza o número da tarefa a executar: '))
    if opcao == 1 and a == 'Marco Oliveira':
        m.manipular_dados()
    elif opcao == 1 and a != 'Marco Oliveira':
        print('\nNecessita de privilégios de administrador para aceder a esta função!')
    elif opcao == 2:
        m.condutores()
    elif opcao == 3:
        m.carrinhas()
    elif opcao == 4:
        m.viagens()
    elif opcao == 5:
        m.contentores()
    elif opcao == 6:
        m.rotas()
    elif opcao == 0:
        print('\nPrograma Terminado!')
        break
    else:
        print('\nNúmero de tarefa inválido!')