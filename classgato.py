from classanimal import Animal

class Gato(Animal):
    def __init__(self, nome, tipo, som, cor):
        super().__init__(nome, tipo, som)
        self.cor = cor