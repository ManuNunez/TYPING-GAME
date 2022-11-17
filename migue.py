#Function list
listpalabrasf[agua,diamante,luz,calor,intensidad,ropa,cama,jabón,salida,cansancio,lápiz,saludo,carpeta,leche,silla]
listapalabrasin[variable,agua,intensidad,lenguaje,numero,cama,codigo,binario,computadora,tecla,carpeta,leche,agua,letra,camara,link,metrica,coordenada]
listapalabrasdif[lenguaje,intensidad,binario,computadora,letra,camara,complejo,variable,diamante,luz,calor,jabon,salida,carpeta,leche,cortafuegos,paraguas,telescopio,universo,gramatica,parangaricutirimicuaro,celular]

def listas(dificultad):
    list = []
    if dificultad == 1:
        v1= random(10-15)
        for i in range (0,v1):
            list.append(listpalabrasf[random(0,14)])
            
    elif dificultad == 2:
        v1= random(15-20)
        for i in range (0,v1):
             list.append(listapalabrasin[random(0,19)])

    elif == 3:
        v1=random(20-25)
        for i in range (0,v1):
             list.append(listapalabrasdif[random(0,24)])
    return list
