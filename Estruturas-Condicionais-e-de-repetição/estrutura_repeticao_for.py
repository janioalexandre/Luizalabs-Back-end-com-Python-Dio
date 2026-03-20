# Exibindo a tabuada do número informado

num = int(input("Digite um número para exibir a tabuada: "))
print(f"Tabuada do {num}:")
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
