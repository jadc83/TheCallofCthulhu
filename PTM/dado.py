import random


def dados(tiradas, caras):
    total = 0
    for x in range(1,tiradas):
        num = random.randint(1,caras)
        total += num
    return total