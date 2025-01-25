entrada = input("Coloque o numero: ")

try: #tente rodar
    numero = int(entrada)
    if numero % 2 == 0:
        print("Este numero é Par")
    else:
        print("Este numero é Ímpar")
except ValueError:
    print("Você não passou um numero inteiro")