frutas = ["banana", "maçã", "uva", "pera", "manga"]

for fruta in frutas:
    print(fruta)
    
#utilizando input para criar a lista de frutas


frutas = []

while True:
    fruta = input("Digita o nome da fruta: ")
    if fruta =="sair":
        break
    frutas.append(fruta)
    
print(frutas)