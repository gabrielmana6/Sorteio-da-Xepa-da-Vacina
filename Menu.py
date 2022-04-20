from ListaDeAgendamento import ListaDeAgendamento, ListaException
from DicionarioDeVacinas import DicionarioDeVacinas, VacinaException


class Menu:
    def __init__(self):
        pass   
    
    # MÉTODO QUE CADASTRA UM USUÁRIO NA LISTA DE AGENDAMENTO.
    def a(self, lista_de_agendamento):
        while True:
            try:
                usuario = input('\nDigite o nome da pessoa a ser cadastrada na Lista de Agendamento (X para voltar ao menu): ').upper()
                if (usuario == 'X'):    break
            
                assert (usuario.isalpha() == True), '*ERRO: Contém caracteres que não estão no alfabeto.'
                
                usuario = usuario.capitalize()

                assert (lista_de_agendamento.comparar_usuario(usuario) == False), f'*ERRO: Já existe o usuário {usuario} na Lista de Agendamento.'

            except AssertionError as ae:
                print(ae)

            else:
                lista_de_agendamento.adicionar_usuario(usuario)
    
    # MÉTODO QUE REMOVE UM USUÁRIO NA LISTA DE AGENDAMENTO.
    def b(self, lista_de_agendamento):
        while True:
            try:
                assert (lista_de_agendamento.esta_vazia() == False), '*ERRO: Não é possível realizar a operação pois não há nenhum usuário cadastrado na Lista de Agendamento.'
            
                usuario = input('\nDigite o nome da pessoa a ser removida da Lista de Agendamento (X para voltar ao menu): ').upper()
                if (usuario == 'X'):    break

                usuario = usuario.capitalize()

                print(lista_de_agendamento.remover_usuario(usuario))
            
            except AssertionError as ae:
                print(ae)
                break
            except ListaException as ve:
                print(ve)
    
    #MÉTODO QUE REMOVE TODOS OS USUÁRIOS DA LISTA DE AGENDAMENTO.
    def c(self, lista_de_agendamento):
        try:
            assert (lista_de_agendamento.esta_vazia() == False), '*ERRO: Não é possível realizar a operação pois não há nenhum usuário cadastrado na Lista de Agendamento.'
        
        except AssertionError as ae:
            print(ae)
        
        else:
            while True:
                opcao = input('\nTem certeza que deseja remover todos os usuários da Lista de Agendamento? S/N:').upper()
                if (opcao == 'S'):
                    print(lista_de_agendamento.remover_todos_usuarios())
                    break
                
                elif (opcao == 'N'):    break

                else:
                    print('Opção inválida.')            

    # MÉTODO QUE EXIBI NA TELA TODOS OS USUÁRIOS CADASTRADOS NA LISTA DE AGENDAMENTO.
    def d(self, lista_de_agendamento):
        print(lista_de_agendamento.imprimir_usuarios())

    # MÉTODO QUE CADASTRA UMA VACINA E SUA DOSE NO DICIONÁRIO DE VACINAS.
    def e(self, dicionario_de_vacinas):
        while True:
            try:
                vacina_nome = input('\nDigite o nome da vacina (X para voltar ao menu anterior): ')
                if (vacina_nome.upper() == 'X'):    break

                vacina_nome = vacina_nome.strip()
                teste_vacina_nome = vacina_nome.split()

                assert (len(teste_vacina_nome) > 0), '*ERRO: Contém apenas espaços em branco.'
                
                assert (dicionario_de_vacinas.comparar_vacina(vacina_nome) == False), f'*ERRO: Já existe a vacina {vacina_nome} no Dicionario de Vacinas.'
            
            except AssertionError as ae:
                print(ae)
            
            else:
                while True:
                    try:
                        dose = input(f'\nDigite a quantidade de doses da vacina {vacina_nome} (X para voltar ao menu): ')
                        if (dose.upper() == 'X'):    break

                        dose = int(dose)
                        assert (dose > 0), '*ERRO: Digite um valor maior do que zero para a quantia de doses da vacina.'
                    
                    except ValueError:
                        print('Digite um valor de número inteiro para a quantia da doses de vacina.')
                    except AssertionError as ae:
                        print(ae)

                    else:
                        dicionario_de_vacinas.adicionar_vacina(vacina_nome, dose)
                        break
                
                if (str(dose).upper() == 'X'):    break


    # MÉTODO QUE ALTERA A DOSE DE UMA VACINA NO DICIONÁRIO DE VACINAS.
    def f(self, dicionario_de_vacinas):
        while True:
            try:
                assert (dicionario_de_vacinas.esta_vazia() == False), '*ERRO: Não é possível realizar a operação pois não há nenhuma vacina cadastrada.'
                
                vacina_nome = input('\nDigite o nome da vacina que deseja alterar a dose (X para voltar ao menu anterior): ')
                if (vacina_nome.upper() == 'X'):    break

                vacina_nome = vacina_nome.strip()
                teste_vacina_nome = vacina_nome.split()

                assert (len(teste_vacina_nome) > 0), '*ERRO: Contém apenas espaços em branco.'

                assert (dicionario_de_vacinas.comparar_vacina(vacina_nome) == True), f'*ERRO: A vacina {vacina_nome} não está cadastrada.'
                
            except AssertionError as ae:
                print(ae)
                break
            
            else:
                while True:
                    try:
                        dose = input(f'\nDigite a quantidade de doses da vacina {vacina_nome} (X para voltar ao menu): ')
                        if (dose.upper() == 'X'):    break

                        dose = int(dose)
                        assert (dose >= 0), '*ERRO: Digite um valor maior do que zero para a quantia de doses da vacina.'
                    
                    except ValueError:
                        print('Digite um valor de número inteiro para a quantia da doses de vacina.')
                    except AssertionError as ae:
                        print(ae)

                    else:
                        print(dicionario_de_vacinas.alterar_dose(vacina_nome, dose))
                        break
                
                if (str(dose).upper() == 'X'):    break

    # MÉTODO QUE REMOVE UMA VACINA DO DICIONÁRIO DE VACINAS.
    def g(self, dicionario_de_vacinas):
        while True:
            try:
                assert (dicionario_de_vacinas.esta_vazia() == False), '*ERRO: Não é possível realizar a operação pois não há nenhuma vacina cadastrada.'

                vacina_nome = input('\nDigite o nome da vacina que deseja remover (X para voltar ao menu anterior): ')
                if (vacina_nome.upper() == 'X'):    break

                vacina_nome = vacina_nome.strip()
                
                
                while True:
                    opcao = input(f'\nTem certeza que deseja remover a vacina {vacina_nome}? S/N:').upper()
                    if (opcao == 'S'):
                        print(dicionario_de_vacinas.remover_vacina(vacina_nome))
                        break
                    
                    elif (opcao == 'N'):    break

                    else:
                        print('Opção inválida.')
            
            except AssertionError as ae:
                print(ae)
                break
            except VacinaException as ve:
                print(ve)

    # MÉTODO QUE REMOVE TODAS AS VACINAS DO DICIONÁRIO DE VACINAS.
    def h(self, dicionario_de_vacinas):
        try:
            assert (dicionario_de_vacinas.esta_vazia() == False), '*ERRO: Não é possível realizar a operação pois não há nenhuma vacina cadastrada.'
        
        except AssertionError as ae:
            print(ae)
        
        else:
            while True:
                opcao = input('\nTem certeza que deseja remover todos as vacinas? S/N:').upper()
                if (opcao == 'S'):
                    print(dicionario_de_vacinas.remover_todas_vacinas())
                    break
                
                elif (opcao == 'N'):    break

                else:
                    print('Opção inválida.')   

    # MÉTODO QUE EXIBE NA TELA TODAS AS VACINAS CADASTRADAS NO DICIONÁRIO DE VACINAS.
    def i(self, dicionario_de_vacinas):
        print(dicionario_de_vacinas.imprimir_vacinas(dicionario_de_vacinas))
    
    # MÉTODO QUE REALIZA O SORTEIO E EXIBE NA TELA O RESULTADO DO MESMO.
    def j(self, sorteio, lista_de_agendamento, dicionario_de_vacinas):
        try:
            assert (lista_de_agendamento.esta_vazia() == False), '*ERRO: Não é possível realizar a operação pois não há nenhum usuário cadastrado na Lista de Agendamento.'
            assert (dicionario_de_vacinas.esta_vazia() == False), '*ERRO: Não é possível realizar a operação pois não há nenhuma vacina cadastrada.'
            assert (dicionario_de_vacinas.quantidade_total_vacinas() > 0), '*ERRO: Não há vacinas disponíveis.'
            
        except AssertionError as ae:
            print(ae)
        
        else:
            dados = sorteio.realizar_sorteio()
            
            print(sorteio.imprimir_sorteio(dados))

    def imprimir (self):
        return '-----------------------------------------------\n(A) Cadastrar usuário na Lista de Agendamento.\n(B) Remover usuário da Lista de Agendamento.\n(C) Remover todos os usuários da Lista de Agendamento.\n(D) Exibe os usuários cadastrados na Lista de Agendamento.\n\n(E) Cadastrar vacina e sua quantidade de doses.\n(F) Alterar quantidade de doses de uma vacina.\n(G) Remover vacina e sua quantidade de doses.\n(H) Remover todas as vacinas.\n(I) Exibe as vacinas cadastradas.\n\n(J) Realiza o sorteio.\n\n(X) Para sair do programa.\n-----------------------------------------------'