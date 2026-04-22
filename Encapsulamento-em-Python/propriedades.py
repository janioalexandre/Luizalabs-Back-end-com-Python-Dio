class Pessoa: 
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
    
    @property
    def idade(self):
        self._ano_nascimento = 2022
        return _ano_atual - self._ano_nascimento

pessoa = Pessoa("Janio", 1986)
print(f"Nome: {pessoa._nome}, Idade: {pessoa.idade}")