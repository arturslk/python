nome = input("Digite seu nome")
peso = float(input("Digite seu peso"))
altura = float(input("digite sua altura"))
imc =  peso / (altura**2)
if imc < 18.5:
    print("abaixo do peso", imc)
elif imc >= 18.5 <= 25:
    print("peso normal", imc)
elif imc <= 25 <= 30:
    print("Acima do peso", imc)
else:
    print("OBESO", imc)