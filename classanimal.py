class Animal:
    def __init__(self, nome,tipo,som):
        self.nome = nome
        self._tipo = tipo
        self.__som = som
    
    def fazer_som(self):
        return self.__som

    def set_som(self, som):
        self.__som = som

    def __str__(self):
        return self.nome