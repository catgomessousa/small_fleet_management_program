import funçoes as f

#1 MANIPULAR DADOS
def manipular_dados():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Dados sobre os condutores')
        print('2 - Dados sobre as carrinhas')
        print('3 - Dados sobre as viagens')
        print('4 - Dados sobre os contentores')
        print('5 - Dados sobre as rotas')
        print('0 - Terminar')
        print('==========================================================')
        print(' ')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        print(' ')
        print(' ')
        if opcao == 1:
            dados_condutores()
        elif opcao == 2:
            dados_carrinhas()
        elif opcao == 3:
            dados_viagens()
        elif opcao == 4:
            dados_contentores()
        elif opcao == 5:
            dados_rotas()
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')
            

#1.1 MANIPULAR CONDUTORES
def dados_condutores():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Eliminar dados')
        print('2 - Alterar dados')
        print('3 - Adicionar dados')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.eliminar('Condutores', 'condutor')
        elif opcao == 2:
            f.alterar('Condutores')
        elif opcao == 3:
            f.adicionar('Condutores', 'condutor')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')


#1.2 MANIPULAR CARRINHAS
def dados_carrinhas():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Eliminar dados')
        print('2 - Alterar dados')
        print('3 - Adicionar dados')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.eliminar('Carrinhas', 'carrinha')
        elif opcao == 2:
            f.alterar('Carrinhas')
        elif opcao == 3:
            f.adicionar('Carrinhas', 'carrinha')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')


#1.3 MANIPULAR VIAGENS
def dados_viagens():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Eliminar dados')
        print('2 - Alterar dados')
        print('3 - Adicionar dados')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.eliminar('Viagens', 'viagem')
        elif opcao == 2:
            f.alterar('Viagens')
        elif opcao == 3:
            f.adicionar('Viagens', 'viagem')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')


#1.4 MANIPULAR CONTENTORES
def dados_contentores():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Eliminar dados')
        print('2 - Alterar dados')
        print('3 - Adicionar dados')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.eliminar('Contentores', 'contentor')
        elif opcao == 2:
            f.alterar('Contentores')
        elif opcao == 3:
            f.adicionar('Contentores', 'contentor')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')
 
    
#1.5 MANIPULAR ROTAS
def dados_rotas():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Eliminar dados')
        print('2 - Alterar dados')
        print('3 - Adicionar dados')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.eliminar('Rotas', 'rota')
        elif opcao == 2:
            f.alterar('Rotas')
        elif opcao == 3:
            f.adicionar('Rotas', 'rota')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')
            


#2 CONDUTORES
def condutores():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Apresentar as informações sobre os condutores')
        print('2 - Apresentar as informações sobre um condutor')
        print('3 - Ordenar os condutores')
        print('4 - Informações relativas aos quilómetros percorridos')
        print('5 - Informações relativas ao número de acidentes')
        print('6 - Informações relativas ao número de atrasos')
        print('7 - Informações relativas ao número de faltas')
        print('8 - Informações relativas à idade')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.info('Condutores')
        elif opcao == 2:
            f.procura('Condutores', 'B')
        elif opcao == 3:
            ordenar_condutores()
        elif opcao == 4:
            kms_percorridos_condutores()
        elif opcao == 5:
            acidentes_condutores()
        elif opcao == 6:
            atrasos_condutores()
        elif opcao == 7:
            faltas_condutores()
        elif opcao == 8:
            idade_condutores()
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')
            

#2.3 ORDENAR OS CONDUTORES
def ordenar_condutores():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Ordenar por quilómetros percorridos')
        print('2 - Ordenar por número de acidentes')
        print('3 - Ordenar por número de atrasos')
        print('4 - Ordenar por número de faltas')
        print('5 - Ordenar por idade')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.ordenacao('Condutores', 'B', 'F')
        elif opcao == 2:
            f.ordenacao('Condutores', 'B', 'G')
        elif opcao == 3:
            f.ordenacao('Condutores', 'B', 'D')
        elif opcao == 4:
            f.ordenacao('Condutores', 'B', 'E')
        elif opcao == 5:
            f.ordenacao('Condutores', 'B', 'C')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')


#2.4 INFORMAÇÕES KMS
def kms_percorridos_condutores():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Condutor com mais quilómetros percorridos')
        print('2 - Condutor com menos quilómetros percorridos')
        print('3 - Média dos condutores por quilómetros percorridos')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.maxi('Condutores', 'km percorridos',' nº interno', 'Dos', 'o', 'B', 'F' )
        elif opcao == 2:
            f.mini('Condutores', 'km percorridos','nº interno', 'Dos', 'o', 'B', 'F' )
        elif opcao == 3:
            f.media('Condutores', 'km percorridos', 'F')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')


#2.5 INFORMAÇÕES NÚMERO DE ACIDENTES
def acidentes_condutores():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Condutor com mais acidentes')
        print('2 - Condutor com menos acidentes')
        print('3 - Média dos condutores por acidentes')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.maxi('Condutores', 'acidentes', 'nº interno', 'Dos', 'o', 'B', 'G')
        elif opcao == 2:
            f.mini('Condutores', 'acidentes', 'nº interno', 'Dos', 'o', 'B', 'G')
        elif opcao == 3:
            f.media('Condutores', 'acidentes', 'G')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')
 
    
#2.6 INFORMAÇÕES NÚMERO DE ATRASOS          
def atrasos_condutores():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Condutor com mais atrasos')
        print('2 - Condutor com menos atrasos')
        print('3 - Média dos condutores por atrasos')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.maxi('Condutores', 'atrasos', 'nº interno', 'Dos', 'o', 'B', 'D')
        elif opcao == 2:
            f.mini('Condutores', 'atrasos', 'nº interno', 'Dos', 'o', 'B', 'D')
        elif opcao == 3:
            f.media('Condutores', 'atrasos', 'D')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')
            
            
#2.7 INFORMAÇÕES NÚMERO DE FALTAS         
def faltas_condutores():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Condutor com mais faltas')
        print('2 - Condutor com menos faltas')
        print('3 - Média dos condutores por faltas')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.maxi('Condutores', 'faltas', 'nº interno', 'Dos', 'o', 'B', 'E')
        elif opcao == 2:
            f.mini('Condutores', 'faltas', 'nº interno', 'Dos', 'o', 'B', 'E')
        elif opcao == 3:
            f.media('Condutores', 'faltas', 'E')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')


#2.8 INFORMAÇÕES IDADE        
def idade_condutores():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Condutor mais velho')
        print('2 - Condutor mais novo')
        print('3 - Média dos condutores por idade')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.maxi('Condutores', 'idade', 'nº interno', 'Dos', 'o', 'B', 'C')
        elif opcao == 2:
            f.mini('Condutores', 'idade', 'nº interno', 'Dos', 'o', 'B', 'C')
        elif opcao == 3:
            f.media('Condutores', 'idade', 'C')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')
            


#3 CARRINHAS
def carrinhas():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Apresentar as informações sobre as carrinhas')
        print('2 - Apresentar as informações sobre uma carrinha')
        print('3 - Ordenar as carrinhas')
        print('4 - Informações relativas ao número de quilómetros percorridos')
        print('5 - Informações relativas ao volume de carga')
        print('6 - Informações relativas ao número de acidentes')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.info('Carrinhas')
        elif opcao == 2:
            f.procura('Carrihas', 'A')
        elif opcao == 3:
            ordenar_carrinhas()
        elif opcao == 4:
            kms_carrinhas()
        elif opcao == 5:
            carga_carrinhas()
        elif opcao == 6:
            acidentes_carrinhas()
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')


#3.3 ORDENAR AS CARRINHAS
def ordenar_carrinhas():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Ordenar por número de quilómetros percorridos')
        print('2 - Ordenar por volume de carga')
        print('3 - Ordenar por número de acidentes')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.ordenacao('Carrinhas', 'A', 'B')
        elif opcao == 2:
            f.ordenacao('Carrinhas', 'A', 'C')
        elif opcao == 3:
            f.ordenacao('Carrinhas', 'A', 'D')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')


#3.4 INFORMAÇÕES KMS
def kms_carrinhas():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Carrinha com mais quilómetros percorridos')
        print('2 - Carrinha com menos quilómetros percorridos')
        print('3 - Média das carrinhas por quilómetros percorridos')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.maxi('Carrinhas', 'km percorridos',' matrícula', 'Das', 'a', 'A', 'B')
        elif opcao == 2:
            f.mini('Carrinhas', 'km percorridos',' matrícula', 'Das', 'a', 'A', 'B')
        elif opcao == 3:
            f.media('Carrinhas', 'km percorridos', 'B')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')
            
            
#3.5 INFORMAÇÕES VOLUME CARGA
def carga_carrinhas():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Carrinha com mais volume de carga')
        print('2 - Carrinha com menos volume de carga')
        print('3 - Média das carrinhas por volume de carga')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.maxi('Carrinhas', 'volume de carga',' matrícula', 'Das', 'a', 'A', 'C')
        elif opcao == 2:
            f.mini('Carrinhas', 'volume de carga',' matrícula', 'Das', 'a', 'A', 'C')
        elif opcao == 3:
            f.media('Carrinhas', 'volume de carga', 'C')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')
            
            
#3.6 INFORMAÇÕES NÚMERO ACIDENTES
def acidentes_carrinhas():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Carrinha com maior número de acidentes')
        print('2 - Carrinha com menor número de acidentes')
        print('3 - Média das carrinhas por acidentes')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.maxi('Carrinhas', 'acidentes',' matrícula', 'Das', 'a', 'A', 'D')
        elif opcao == 2:
            f.mini('Carrinhas', 'acidentes',' matrícula', 'Das', 'a', 'A', 'D')
        elif opcao == 3:
            f.media('Carrinhas', 'acidentes', 'D')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')



#4 VIAGENS
def viagens():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Apresentar as informações sobre as viagens')
        print('2 - Apresentar as informações sobre uma viagem')
        print('3 - Ordenar as viagens')
        print('4 - Informações relativas ao volume de mercadoria')
        print('5 - Informações relativas ao número de ocorrências')
        print('6 - Informações relativas ao número de pausas')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.info('Viagens')
        elif opcao == 2:
            f.procura('Viagens','A')
        elif opcao == 3:
            ordenar_viagens()
        elif opcao == 4:
            volume_viagens()
        elif opcao == 5:
            ocorrencias_viagens()
        elif opcao == 6:
            pausas_viagens()
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')


#4.3 ORDENAR AS VIAGENS
def ordenar_viagens():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Ordenar por número de ocorrências')
        print('2 - Ordenar por número de pausas')
        print('3 - Ordenar por volume de mercadoria')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.ordenacao('Viagens', 'A', 'I')
        elif opcao == 2:
            f.ordenacao('Viagens', 'A', 'K')
        elif opcao == 3:
            f.ordenacao('Viagens', 'A', 'L')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')
            

#4.4 INFORMAÇÕES VOLUME MERCADORIA
def volume_viagens():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Viagem com mais volume de mercadoria')
        print('2 - Viagem com menos volume de mercadoria')
        print('3 - Média das viagens por volume de mercadoria')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.maxi('Viagens', 'volume de mercadoria',' nº de identificação', 'Das', 'a', 'A', 'L')
        elif opcao == 2:
            f.mini('Viagens', 'volume de mercadoria',' nº de identificação', 'Das', 'a', 'A', 'L')
        elif opcao == 3:
            f.media('Viagens', 'volume de mercadoria', 'L')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')


#4.5 INFORMAÇÕES NÚMERO OCURRÊNCIAS
def ocorrencias_viagens():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Viagem com mais ocorrências')
        print('2 - Viagem com menos ocorrências')
        print('3 - Média das viagens por ocorrências')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.maxi('Viagens', 'ocorrências',' nº de identificação', 'Das', 'a', 'A', 'I')
        elif opcao == 2:
            f.mini('Viagens', 'ocorrências',' nº de identificação', 'Das', 'a', 'A', 'I')
        elif opcao == 3:
            f.media('Viagens', 'ocorrências', 'I')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')
    
    
#4.6 INFORMAÇÕES NÚMERO PAUSAS
def pausas_viagens():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Viagem com mais pausas')
        print('2 - Viagem com menos pausas')
        print('3 - Média das viagens por pausas')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.maxi('Viagens', 'pausas',' nº de identificação', 'Das', 'a', 'A', 'K')
        elif opcao == 2:
            f.mini('Viagens', 'pausas',' nº de identificação', 'Das', 'a', 'A', 'K')
        elif opcao == 3:
            f.media('Viagens', 'pausas', 'K')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')



#5 CONTENTORES
def contentores():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Apresentar as informações sobre os contentores')
        print('2 - Apresentar as informações sobre um contentor')
        print('3 - Ordenar os contentores')
        print('4 - Informações relativas à capacidade do contentor')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.info('Contentores')
        elif opcao == 2:
            f.procura('Contentores', 'A')
        elif opcao == 3:
            ordenar_contentores()
        elif opcao == 4:
            capacidade_contentores()
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')
            

#5.3 ORDENAR OS CONTENTORES
def ordenar_contentores():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Ordenar por capacidade máxima')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.ordenacao('Contentores','A','B')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')
            
            
#5.4 INFORMAÇÕES CAPACIDADE
def capacidade_contentores():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Contentor com mais capacidade de carga')
        print('2 - Contentor com menos capacidade de carga')
        print('3 - Média dos contentores por capacidade de carga')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.maxi('Contentores', 'capacidade de carga',' nº de identificação', 'Dos', 'o', 'A', 'B')
        elif opcao == 2:
            f.mini('Contentores', 'capacidade de carga',' nº de identificação', 'Dos', 'o', 'A', 'B')
        elif opcao == 3:
            f.media('Contentores', 'capacidade de carga', 'B')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')
            
            
            
#6 ROTAS
def rotas():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Apresentar as informações sobre as rotas')
        print('2 - Apresentar as informações sobre a rota')
        print('3 - Ordenar as rotas')
        print('4 - Informações relativas à distância a percorrer da rota')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.info('Rotas')
        elif opcao == 2:
            f.procura('Rotas','A')
        elif opcao == 3:
            ordenar_rotas()
        elif opcao == 4:
            distancia_rotas()
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')
            

#6.3 ORDENAR AS ROTAS
def ordenar_rotas():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Ordenar por distância a percorrer')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.ordenacao('Rotas','A','E')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')
            

#6.4 INFORMAÇÕES DISTÂNCIA
def distancia_rotas():
    while True:
        print('==========================================================')
        print('                          MENU                            ')
        print('==========================================================')
        print('1 - Rota com maior distância a percorrer')
        print('2 - Rota com menor distância a percorrer')
        print('3 - Média das rotas por distância a percorrer')
        print('0 - Terminar')
        print('==========================================================')
        opcao = float(input('Introduza o número da tarefa a executar: '))
        if opcao == 1:
            f.maxi('Rotas', 'distancia a percorrer',' nº de identificação', 'Das', 'a', 'A', 'E')
        elif opcao == 2:
            f.mini('Rotas', 'distância a percorrer',' nº de identificação', 'Das', 'a', 'A', 'E')
        elif opcao == 3:
            f.media('Rotas', 'distância a percorrer', 'E')
        elif opcao == 0:
            break
        else:
            print('Número de tarefa inválido!')