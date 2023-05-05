idade = int(input("Digite sua idade: "))
peso = int(input("Digite seu peso: "))

if (idade >= 0 and idade <= 5 and peso <= 20) or (idade >= 6 and idade <= 15 and peso <= 60) or (idade >= 16 and idade <= 25 and peso <= 80):
    print("Não é obeso")
else:
    print("É obeso")
