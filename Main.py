from ListaDeAgendamento import ListaDeAgendamento, ListaException
from DicionarioDeVacinas import DicionarioDeVacinas, VacinaException
from Sorteio import Sorteio
from Menu import Menu

if __name__ == '__main__':
    
    menu = Menu()
    lista_de_agendamento = ListaDeAgendamento()
    dicionario_de_vacinas = DicionarioDeVacinas()
    sorteio = Sorteio(lista_de_agendamento, dicionario_de_vacinas)
    
    while True:
        print(menu.imprimir())

        try:
            opcao = input('\nDigite sua opção (X para sair): ').upper()
            assert opcao in ['A','B','C','D','E','F','G','H','I','J','X'], '*ERRO: Digite uma opção contida no menu.'
        
        except AssertionError as ae:
            print(ae)
        
        else:
            # MÉTODO QUE CADASTRA UM USUÁRIO NA LISTA DE AGENDAMENTO.
            if (opcao == 'A'):
                menu.a(lista_de_agendamento)

            # MÉTODO QUE REMOVE UM USUÁRIO NA LISTA DE AGENDAMENTO.
            elif (opcao == 'B'):
                menu.b(lista_de_agendamento)

            # MÉTODO QUE REMOVE UM USUÁRIO NA LISTA DE AGENDAMENTO.
            elif (opcao == 'C'):
                menu.c(lista_de_agendamento)

            # MÉTODO QUE EXIBI NA TELA TODOS OS USUÁRIOS CADASTRADOS NA LISTA DE AGENDAMENTO.
            elif (opcao == 'D'):
                menu.d(lista_de_agendamento)

            # MÉTODO QUE CADASTRA UMA VACINA E SUA DOSE NO DICIONÁRIO DE VACINAS.
            elif (opcao == 'E'):
                menu.e(dicionario_de_vacinas)

            # MÉTODO QUE ALTERA A DOSE DE UMA VACINA NO DICIONÁRIO DE VACINAS.
            elif (opcao == 'F'):
                menu.f(dicionario_de_vacinas)

            # MÉTODO QUE REMOVE UMA VACINA DO DICIONÁRIO DE VACINAS.
            elif (opcao == 'G'):
                menu.g(dicionario_de_vacinas)

            # MÉTODO QUE REMOVE TODAS AS VACINAS DO DICIONÁRIO DE VACINAS.
            elif (opcao == 'H'):
                menu.h(dicionario_de_vacinas)
            
            # MÉTODO QUE EXIBE NA TELA TODAS AS VACINAS CADASTRADAS NO DICIONÁRIO DE VACINAS.
            elif (opcao == 'I'):
                menu.i(dicionario_de_vacinas)

            # MÉTODO QUE REALIZA O SORTEIO E EXIBE NA TELA O RESULTADO DO MESMO.
            elif (opcao == 'J'):
                menu.j(sorteio, lista_de_agendamento, dicionario_de_vacinas)
            
            # MÉTODO QUE SAI DO PROGRAMA.
            elif (opcao == 'X'):
                break