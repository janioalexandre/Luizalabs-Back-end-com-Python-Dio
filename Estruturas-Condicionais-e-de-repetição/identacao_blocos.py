def sacar(valor):
    saldo = 500

    if valor <= saldo:
        print("Valor sacado com sucesso!")    
    else:
        print("Saldo insuficiente para realizar o saque.")

    print("Obrigado por ser nosso cliente!")

sacar(200)