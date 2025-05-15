import random

size, steps = 30, 15
# Estado inicial: 0 ou 1 aleatório
cells = [random.choice([0, 1]) for _ in range(size)]

for _ in range(steps):
    # Exibe ASCII art do estado
    print("".join("█" if c else " " for c in cells))
    # Nova geração: regra 30
    cells = [
        cells[i-1] ^ (cells[i] | cells[(i+1) % size])
        for i in range(size)
    ]