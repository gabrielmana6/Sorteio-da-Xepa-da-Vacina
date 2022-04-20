class VacinaException(Exception):
    def init(self,msg):
        super().init(msg)


class DicionarioDeVacinas:
    def __init__ (self):
        self.__dicionario = {}
    
    # MÉTODO QUE ADICIONA UMA VACINA NO DICIONARIO DE VACINAS.
    def adicionar_vacina(self, vacina_nome, dose):
        self.__dicionario[vacina_nome] = dose

    # MÉTODO QUE REMOVE UMA VACINA NO DICIONARIO DE VACINAS.
    def remover_vacina(self, vacina_nome):
        for vacina, dose in self.__dicionario.items():
            
            if (vacina_nome == vacina):
                dose = self.__dicionario.get(vacina_nome)
                self.__dicionario.pop(vacina_nome)
                return f'Foi removido a vacina {vacina_nome} com {dose} doses.'
        
        raise VacinaException (f'Não foi encontrada a vacina {vacina_nome}.')
    
    # MÉTODO QUE REMOVE TODAS AS VACINAS NO DICIONARIO DE VACINAS.
    def remover_todas_vacinas(self):
        self.__dicionario.clear()
        return 'Todos as vacinas foram removidos com sucesso.'
    
    # MÉTODO QUE RETORNA TRUE SE O DICIONARIO DE VACINAS ESTIVER VAZIO.
    def esta_vazia(self):
        return len(self.__dicionario) == 0

    # MÉTODO QUE RETORNA A QUANTIDADE TOTAL DE VACINAS NO DICIONARIO DE VACINAS.
    def quantidade_total_vacinas(self):
        total_vacinas = 0   
        for dose in self.__dicionario.values():
            total_vacinas += dose
        
        return total_vacinas

    # MÉTODO QUE RETORNA TRUE CASO A VACINA JÁ EXISTA.
    def comparar_vacina(self, vacina_nome):
        for vacina in self.__dicionario.keys():
            if (vacina_nome == vacina):
                return True
        return False
    
    # MÉTODO QUE ALTERA A DOSE DE UMA VACINA RECEBENDO COMO ARGUMENTO SEU NOME.
    def alterar_dose(self, vacina_nome, dose):
        dose_anterior = self.__dicionario.get(vacina_nome)
        self.__dicionario[vacina_nome] = dose
        dose_nova = self.__dicionario.get(vacina_nome)
        return f'A vacina {vacina_nome} teve sua dose alterada de {dose_anterior} para {dose_nova}.'
    
    # MÉTODO QUE RETORNA A VACINA ESCOLHIDA E REMOVE SEU VALOR NO DICIONARIO DE VACINAS.
    def vacina_escolhida(self):
        for vacina, dose in self.__dicionario.items():
            if (self.__dicionario.get(vacina) > 0):
                vacina_escolhida = vacina
                self.__dicionario[vacina] = self.__dicionario.get(vacina) - 1
                return vacina_escolhida
    
    # MÉTODO QUE RETORNA COMO STRING AS VACINAS DISPONÍVEIS.
    def vacinas_disponiveis(self):
        str = ''
        for vacina, dose in self.__dicionario.items():
            if (dose > 0):
                str += (f'{vacina} = {dose}\n')
        return str
    
    # MÉTODO QUE RETORNA AS VACINAS CADASTRADAS NO DICIONARIO DE VACINAS.
    def imprimir_vacinas(self, dicionario_de_vacinas):
        str = f'\nVacinas Cadastradas: ({dicionario_de_vacinas.quantidade_total_vacinas()} doses no total)\n'
        
        for vacina, dose in self.__dicionario.items():
            str += f'{vacina} : {dose}\n'
        
        return str