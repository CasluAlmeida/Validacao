import random


def gerar_nome_aleatorio():
    """
    Gera um nome completo aleatório a partir de listas predefinidas,
    garantindo que o comprimento total não exceda 50 caracteres.
    """
    # Listas de nomes e sobrenomes comuns
    nomes = [
        'Maria', 'João', 'Ana', 'Pedro', 'Carla', 'Lucas', 'Juliana', 'Rafael', 'Fernanda',
        'Bruno', 'Camila', 'André', 'Mariana', 'Gustavo', 'Isabela', 'Daniel', 'Leticia',
        'Felipe', 'Amanda', 'Ricardo', 'Beatriz', 'Thiago', 'Patricia', 'Eduardo', 'Viviane'
    ]

    sobrenomes = [
        'Silva', 'Santos', 'Oliveira', 'Souza', 'Pereira', 'Ferreira', 'Lima', 'Gomes',
        'Martins', 'Rodrigues', 'Alves', 'Ribeiro', 'Costa', 'Carvalho', 'Nascimento',
        'Pires', 'Duarte', 'Machado', 'Melo', 'Barbosa', 'Freitas', 'Azevedo', 'Dias',
        'Monteiro', 'Nunes'
    ]

    # Escolhe um nome e um sobrenome aleatoriamente
    nome_escolhido = random.choice(nomes)
    sobrenome_escolhido = random.choice(sobrenomes)

    # Combina os dois em um nome completo
    nome_completo = f"{nome_escolhido} {sobrenome_escolhido}"

    # Verifica se o nome completo excede 50 caracteres
    if len(nome_completo) > 50:
        # Se for muito longo, trunca o sobrenome para caber
        # Calcula o espaço restante após o nome e o espaço
        espaco_restante = 50 - len(nome_escolhido) - 1

        # Trunca o sobrenome para o tamanho restante
        sobrenome_truncado = sobrenome_escolhido[:espaco_restante]

        return f"{nome_escolhido} {sobrenome_truncado}"

    return nome_completo

# Gera e imprime 5 nomes aleatórios
for _ in range(5):
    print("'" + gerar_nome_aleatorio() + "'")