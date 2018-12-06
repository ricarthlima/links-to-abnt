entrada = ""
lista = []
while entrada == "":
    titulo = input("Insira o titulo: ")
    autor = input("Insira o autor: ")
    link = input("Insira o link: ")
    dia = input("Dia do acesso (dd/mm/aaaa): ")
    hora = input("Hora do acesso (HHhMM): ")
    tupla = (titulo,autor,link,dia,hora)
    lista.append(tupla)
    entrada = input()

file = open("referencias.txt","a")
file.write("\n")
i = 0
while i < len(lista):
    file.write(lista[i][0]+", "+lista[i][1]+". Disponível em:<"+lista[i][2]+">. Acesso em "+lista[i][3]+" às "+lista[i][4]+".\n")
    i = i + 1
file.close()

    
