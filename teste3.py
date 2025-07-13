# Lista para armazenar os 50 números
numeros = []

# Leitura dos 50 números
for i in range(50):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

# Verificar e mostrar os números repetidos e suas posições
repetidos = {}
for i, num in enumerate(numeros):
    if num in repetidos:
        repetidos[num].append(i)
    else:
        repetidos[num] = [i]

# Exibir os números repetidos e suas posições
for num, posicoes in repetidos.items():
    if len(posicoes) > 1:
        print(f'O número {num} se repete nas posições: {posicoes}')
