while True:
    try:
        idade = int(input("Digite sua idade: "))

        if idade < 18:
            print("Você é menor de idade")
        elif idade > 18 and idade < 65:
            print("Voce é maior de idade")
        else:
            print("Você é idoso")
    except ValueError:
        print("Você deve digitar um numero inteiro.")


