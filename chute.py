from random import randint
def numero_aleatorio():
    aleatorio = randint(1,10)
    chute=0
    while aleatorio != chute:
        chute = int (input("Digite um numero de 1 a 10: "))
        if (aleatorio == chute):
            print("Parabens você acertou, que legal!")
        else:
            print("Errou, tenta de novo ai!")
numero_aleatorio()
