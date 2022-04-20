import random
import datetime

class Sorteio():
    def __init__(self, lista_de_agendamento, dicionario_de_vacinas):
        self.__lista_de_agendamento = lista_de_agendamento
        self.__dicionario_de_vacinas = dicionario_de_vacinas
        self.__dicionario_dos_escolhidos = {}
        self.__lista_nao_contemplados = []

    # MÉTODO QUE REALIZA O SORTEIO.
    def realizar_sorteio(self):
        #São criadas variáveis que recebem o __init__ das classes ListaDeAgendamento e removem todos os elementos anteriores do dicionario dos escolhidos e lista nao contemplados.
        #lista = self.__lista_de_agendamento._ListaDeAgendamento__lista
        lista = self.__lista_de_agendamento.retorna_lista()
        self.__dicionario_dos_escolhidos.clear()
        self.__lista_nao_contemplados.clear()

        #São criadas as variáveis auxiliadoras para organização dos dados.
        vacinas_disponiveis = self.__dicionario_de_vacinas.vacinas_disponiveis()
        total_vacinas = self.__dicionario_de_vacinas.quantidade_total_vacinas()
        tamanho_lista = self.__lista_de_agendamento.tamanho()
        
        #São criadas as variáveis orientadoras para a realização do sorteio.
        pointer = random.randint(0, tamanho_lista - 1)
        k = random.randint(0, tamanho_lista - 1)
        q = total_vacinas
        
        if (total_vacinas > tamanho_lista):
            q = tamanho_lista

        #Dado o número de vacinas, seleciona e organiza o dicionario dos escolhidos e a lista não contemplados.
        for i in range(q):
            usuario_pointer = lista[pointer]
            contador = pointer
            
            #Dado o número k de saltos, seleciona o usuario_escolhido a ser vacinado.
            for i in range (k+1):
                escolhido_momentaneo = lista[contador]

                if (escolhido_momentaneo == lista[-1]):
                    contador = 0
                else:
                    contador += 1
            
            usuario_escolhido = escolhido_momentaneo
            
            #Seleciona a vacina e remove uma dose no DicionárioDeVacinas.
            vacina_escolhida = self.__dicionario_de_vacinas.vacina_escolhida()
            
            #Adiciona no dicionario dos escolhidos o usuário vacinado e o nome da vacina.
            self.__dicionario_dos_escolhidos[usuario_escolhido] = vacina_escolhida

            #Associa ao próximo usuário o novo pointer.
            if (usuario_escolhido == lista[-1]):
                pointer = 0
            else:
                pointer = lista.index(usuario_escolhido)
            
            #Remove da lista de agendamento o usuário vacinado.
            lista.pop(lista.index(usuario_escolhido))
        
        #Após todas as doses serem distribuídas, lista nao contemplados recebe uma cópia dos usuários restantes da lista de agendamento.
        self.__lista_nao_contemplados = lista.copy()
        lista.clear()
        return vacinas_disponiveis, k, self.__dicionario_dos_escolhidos, self.__lista_nao_contemplados
    
    # MÉTODO QUE EXIBE NA TELA O RESULTADO DO SORTEIO.
    def imprimir_sorteio(self, dados):
        data = (datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
        
        vacinas_disponiveis = dados[0]
        k = dados[1]
        dicionario_escolhidos = dados[2]
        lista_nao_contemplados = dados[3]
        
        str = (f'\nData: {data}\n')
        str += (f'Vacinas disponíveis:\n{vacinas_disponiveis}\n')
        str += ('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n')
        str += (f'Selecionados (k = {k})\n')
        str += ('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n')
        for usuario, vacina in dicionario_escolhidos.items():
            str += (f'{usuario} - {vacina}\n')
        str += ('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n')
        str += ('Não contemplados (fazer novo agendamento)\n')
        str += ('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n')
        for i in range (len(lista_nao_contemplados)):
            str += (f'{lista_nao_contemplados[i]}\n')
        
        return str