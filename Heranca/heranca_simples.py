class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor        
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando o motor")
    
    def __str__(self):
        return self.cor

class Carro(Veiculo):
    pass

class Moto(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregando):
        super().__init__(cor, placa, numero_rodas)
        self.carregando = carregando
    
    def esta_carregando(self):
        print(f"{'Sim' if self.carregando else 'Não'} estou carregando")

moto = Moto("Vermelha", "ABC-1234", 2)
moto.ligar_motor()

