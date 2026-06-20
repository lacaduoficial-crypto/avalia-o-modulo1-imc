Peso = float(input("Digite seu peso:"))
Altura = float(input("Digite sua altura:"))

IMC = Peso/(Altura**2)

if IMC < 18.5:
    print("Abaixo do peso")
elif IMC < 24.9:
    print("Peso normal")
elif IMC < 29.9:
    print("Sobrepeso")
elif IMC < 34.9:
    print("Obesidade Grau I")
elif IMC < 39.9:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")
 