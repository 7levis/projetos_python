# Funçoes de operações basicas.
def soma (a, b):
    return a + b

def subtracao (a, b):
    return a - b

def multiplicacao (a, b):
    return a * b

def divisao (a, b):
    if b == 0:
        return "Erro! Não pode dividir por zero!"
    return a / b

# Função principal com menu para seleção de operação.
def calculadora ():
    print("################ Calculadora ###################")
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        escolha = input("Digite a opção (1 ao 4) ou '0' para sair: ")
        
        if escolha == '0':
            print ("Saindo...")
            break

        if escolha in ['1', '2', '3', '4']:
            try:
                n1 = int(input("Digite o primeiro numero: "))
                n2 = int(input("Digte o segundo numero: "))
            except ValueError:
                print("Por favor, insira um numero válido.")
                continue

            if escolha == '1':
                print (f"{n1} + {n2} = {soma(n1, n2)}")
            elif escolha == '2':
                print (f"{n1} - {n2} = {subtracao(n1, n2)}")
            elif escolha == '3':
                print (f"{n1} * {n2} = {multiplicacao(n1, n2)}")
            elif escolha == '4':
                print (f"{n1} / {n2} = {divisao(n1, n2)}")
        else:
            print ("Opção invalida, tente novamente.")

# Executando a calculadora
if __name__ == "__main__":
    calculadora()
