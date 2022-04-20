class ListaException(Exception):
    def init(self,msg):
        super().init(msg)


class ListaDeAgendamento:
    def __init__(self):
        self.__lista = []

    # MÉTODO QUE ADICIONA UM USUÁRIO NA LISTA DE AGENDAMENTO.
    def adicionar_usuario(self, usuario):
        self.__lista.append(usuario)

    # MÉTODO QUE REMOVE UM USUÁRIO DA LISTA DE AGENDAMENTO.
    def remover_usuario(self, usuario):
        for i in range (len(self.__lista)):

            if (usuario == self.__lista[i]):
                indice = self.__lista.index(self.__lista[i])
                self.__lista.pop(indice)
                return f'Foi removido da Lista de Agendamento o usuário {usuario}.'

        raise ListaException (f'Não foi encontrado na Lista de Agendamento o usuário {usuario}.')

    # MÉTODO QUE REMOVE TODOS OS USUÁRIOS DA LISTA DE AGENDAMENTO.
    def remover_todos_usuarios(self):
        self.__lista.clear()
        return 'Todos os usuários foram removidos com sucesso.'
    
    # MÉTODO QUE RETURNA TRUE SE A LISTA DE AGENDAMENTO ESTIVER VAZIA.
    def esta_vazia(self):
        return len(self.__lista) == 0

    # MÉTODO QUE RETORNA O TAMANHO DA LISTA DE AGENDAMENTO.
    def tamanho(self):
        return len(self.__lista)

    # MÉTODO QUE RETORNA TRUE CASO O USUÁRIO JÁ EXISTA.
    def comparar_usuario(self, usuario):
        for i in range (len(self.__lista)):            
            if (usuario == self.__lista[i]):
                return True
        return False
    
    def retorna_lista(self):
        return self.__lista
    
    # MÉTODO QUE RETORNA OS USUÁRIOS CADASTRADOS NA LISTA DE AGENDAMENTO.
    def imprimir_usuarios(self):
        str = '\nUsuários cadastrados na Lista de Agendamento:\n'
        for i in range (len(self.__lista)):
            str += f'{i+1}:{self.__lista[i]}\n'
        return str