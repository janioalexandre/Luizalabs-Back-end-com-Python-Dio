class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim ...")
    
    def parar(self):
        print("Parando bicicleta ...")
        print("Bicicleta parada!")
    
    def correr(self):
        print("Vrummmm ...")
    
    def __str__(self):
        return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"


b1 = Bicicleta("vermelha", "caloi", 2020, 1500)
b1.buzinar()
b1.correr()
b1.parar()

print(f"Cor: {b1.cor}")
print(f"Modelo: {b1.modelo}")
print(f"Ano: {b1.ano}")
print(f"Valor: {b1.valor}")

