import random


def dados(tiradas, caras):
    tirada = 0
    for x in range(1,tiradas):
        num = random.randint(1,caras)
        tirada += num
    return tirada