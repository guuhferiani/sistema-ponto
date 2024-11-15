 # Modelo de dados (para armazenar as marcações)

 import datetime

class Ponto:
    def __init__(self, nome):
        self.nome = nome
        self.entrada = None
        self.saida = None
        self.intervalo = None
    
    def registrar_entrada(self):
        self.entrada = datetime.datetime.now()
    
    def registrar_saida(self):
        self.saida = datetime.datetime.now()
        self.calcular_intervalo()

    def calcular_intervalo(self):
        if self.entrada and self.saida:
            self.intervalo = self.saida - self.entrada

    def __str__(self):
        return f"Nome: {self.nome}\nEntrada: {self.entrada}\nSaída: {self.saida}\nIntervalo: {self.intervalo}"
