# Leitura dos dois valores inteiros
try:
    valor1 = int(input("Digite o primeiro numero: "))
    valor2 = int(input("Digite o segundo numero: "))

    # Garantir que o segundo valor seja maior que o primeiro
    if valor1 > valor2:
        valor1, valor2 = valor2, valor1
except ValueError:
    print("A entrada não é um número válido.")

# Calcular a soma dos valores entre os dois inteiros, incluindo os próprios inteiros
soma = sum(range(valor1, valor2 + 1))

# Imprimir o resultado
print(f'A soma entre os inteiros dentro dos dois valores {valor1} e {valor2} é {soma}.')
