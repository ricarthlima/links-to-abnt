import random
DOMINIOS = ["COM","BR","NET","ORG"]

file = open("arq.txt","r")
links = file.readlines()
file.close()

file = open("res.txt","a+")

for link in links:
    infos = link.split("/")

    #Extrair autor
    autor = ""
    autorLista = infos[2].upper().split(".")
    for i in range(0,3):
        if autorLista[0] == "WWW":
            autorLista = autorLista[1:]
        if autorLista[-1] in DOMINIOS:
            autorLista = autorLista[:-1]

    for palavra in autorLista:
        autor = autor + palavra + " "
    
    

    #Extarir título que estará na variável -titulo-
    titulo = ""
    
    tituloLista = infos[-1].split("-")    
    primeira = tituloLista[0][0].upper()
    i = 1
    while i < len(tituloLista[0]):
        primeira += tituloLista[0][i]
        i = i + 1

    titulo = titulo + primeira + " "
        
    i = 1
    while i < len(tituloLista):
        titulo = titulo + tituloLista[i] + " "
        i = i + 1

    string = ""

    dia = random.randint(11,29)
    print(autor+". "+titulo+". Disponível em: <"+link+"> Acesso em: " + str(dia) + " de junho de 2018\n")    
 
