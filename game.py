from random import *
import time
from IPython.display import clear_output
import getpass

# DBs

users_login = [["super usuario", "123"]]
users = ["super usuario", ]
users_scores = [["RZL", "dificultad : NULL", "0 : 0", "ratio : 0"]]
user = "default"
# function login


def login(user_login):
    time.sleep(0.05)
    clear_output()
    print("\033[1;34m"+"                          _____ _   _ _____ _____ _____          _____        _____ ______  _____ _____ ____  _   _ ")
    print("\033[1;34m"+"                         |_   _| \ | |_   _/ ____|_   _|   /\   |  __ \      / ____|  ____|/ ____|_   _/ __ \| \ | |")
    print("\033[1;34m"+"                           | | |  \| | | || |      | |    /  \  | |__) |    | (___ | |__  | (___   | || |  | |  \| |")
    print("\033[1;34m"+"                           | | | . ` | | || |      | |   / /\ \ |  _  /      \___ \|  __|  \___ \  | || |  | | . ` |")
    print("\033[1;34m"+"                          _| |_| |\  |_| || |____ _| |_ / ____ \| | \ \      ____) | |____ ____) |_| || |__| | |\  |")
    print("\033[1;34m"+"                         |_____|_| \_|_____\_____|_____/_/    \_\_|  \_\    |_____/|______|_____/|_____\____/|_| \_|")
    print("")
    print("\033[0;37m"+"                                          ~~PARA INICIAR SESION INGRESE SU USUARIO Y CONTRASEÑA~~")
    log_user = input("INTRODUZCA SU USUARIO :")
    log_password = getpass.getpass("INTRODUZCA SU CONTRASEÑA")
    log = [log_user, log_password]
    counter = 0
    if log in users_login:
        user = log_user
        menu(user)
    else:
        counter = counter + 1
        print("LOS DATOS INTRODUCIDOS SON INCORRECTOS")
        while counter < 3:
            login(user)
# function sign_up


def sign_up():
    time.sleep(0.05)
    clear_output()
    print("\033[1;34m"+"                                          _____  ______ _____ _____  _____ _______ _____   _____  ")
    print("\033[1;34m"+"                                         |  __ \|  ____/ ____|_   _|/ ____|__   __|  __ \ / __  \ ")
    print("\033[1;34m"+"                                         | |__) | |__ | |  __  | | | (___    | |  | |__) | |  | |")
    print("\033[1;34m"+"                                         |  _  /|  __|| | |_ | | |  \___ \   | |  |  _  /| |  | |")
    print("\033[1;34m"+"                                         | | \ \| |___| |__| |_| |_ ____) |  | |  | | \ \| |__| |")
    print("\033[1;34m"+"                                         |_|  \_\______\_____|_____|_____/   |_|  |_|  \_\\_____/")
    print("")
    print("\033[0;37m"+"                                          ~~PARA REGISTRARSE INGRESE UN USUARIO Y CONTRASEÑA~~")
    print("\033[0;37m")
    print("su usuario debe de ser de 3 letras de largo")
    New_User = input("USUARIO: ")
    pasword = getpass.getpass("CONTRASEÑA: ")
    if len(New_User) == 3:
        if New_User in users:
            print("LO SENTIMOS PERO ESE USUARIO YA ESTA OCUPADO")

        else:
            New_User = New_User.upper()
            Push_User = [New_User, pasword]
            Push_User_Score = [New_User, "dificultad : NULL", "0 : 0", "ratio : 0"]
            users.append(New_User)
            users_login.append(Push_User)
            users_scores.append(Push_User_Score)
            time.sleep(1)
            clear_output()
            user = New_User
            menu(user)
    else:
        print("el usuario que a introducido no tiene la longitud correcta")


def log_out(user_logout):
    user = "default"
    menu(user)


# Function list


listpalabrasf = ["agua", "diamante", "luz", "calor", "intensidad", "ropa", "cama",
    "jabón", "salida", "cansancio", "lápiz", "saludo", "carpeta", "leche", "silla"]
listapalabrasin = ["variable", "agua", "intensidad", "lenguaje", "numero", "cama", "codigo", "binario",
    "computadora", "tecla", "carpeta", "leche", "agua", "letra", "camara", "link", "metrica", "coordenada"]
listapalabrasdif = ["lenguaje", "intensidad", "binario", "computadora", "letra", "camara", "complejo", "variable", "diamante", "luz", "calor",
    "jabon", "salida", "carpeta", "leche", "cortafuegos", "paraguas", "telescopio", "universo", "gramatica", "parangaricutirimicuaro", "celular"]


def listas(dificultad):
    list = []
    if dificultad == 1:
        v1 = randint(10, 15)
        for i in range(0, v1):
            list.append(listpalabrasf[randint(0, 14)])

    elif dificultad == 2:
        v1 = randint(15, 20)
        for i in range(0, v1):
             list.append(listapalabrasin[randint(0, 19)])

    elif dificultad == 3:
        v1 = randint(20, 25)
        for i in range(0, v1):
             list.append(listapalabrasdif[randint(0, 24)])
    return list

# funtion scores
def inversor():
    counter = -1
    while counter > -5:
        new_list = new_list.apend(users_scores[counter])
        counter = counter - 1
    scores()


def sort(arg):
    if arg == 1:
        newlist = sorted(users_scores, key=lambda x: x[0])
        users_scores = newlist
        scores()

    elif arg == 2:
        newlist = sorted(users_scores, key=lambda x: x[1])
        users_scores = newlist
        scores()

    elif arg == 3:
        users_scores = sorted(users_scores, key=lambda x: x[2])
        users_scores = newlist
        scores()

    elif arg == 4:
        newlist = sorted(users_scores, key=lambda x: x[3])
        users_scores = newlist
        inversor()


def scores():
    time.sleep(0.005)
    clear_output()
    print("para salir presione : 0")
    for elements in users_scores:
        print("| usuario : {} | {} | {} | {} |".format(elements[0], elements[1],elements[2], elements[3]))
    
    print("ordenar por usuario : 1")
    print("ordenar por dificultad : 2")
    print("ordenar por tiempo : 3")
    print("ordenar por porcentaje de aciertos : 4")
    sort_arg = int(input())
    if sort_arg == 0 :
        menu(user)
    elif sort_arg == 1 or sort_arg == 2 or sort_arg == 3 or sort_arg == 4:
        sort(sort_arg)
    elif sort_arg == 5:
        inversor()
    else :
        print("el argumento introcudiodo es invalido")



# function  game


def start_game(user_game):
    time.sleep(0.05)
    clear_output()
    print("SELECCIONE LA DIFICULTAD DE JUEGO")
    print("1- FACIL")
    print("2- MEDIO")
    print("3- DIFICIL")
    dificultad = int(input())
    game(dificultad)
    time.sleep(0.005)
    clear_output()


def comparador(lista_original, lista_usuario):
    total_score = 0
    word_score = 0
    m = 0
    n = 0
    for element in lista_original:
        if element == lista_usuario[m]:
            n =n + 1
        m = m + 1

    total_score = n / len(lista_original)
    return total_score


def game(dificultad):
    lista_original = listas(dificultad)
    lista_user = []
    time_1 = time.time()
    for element in lista_original:
        print (element)
        nueva_palabra = getpass.getpass()
        lista_user.append(nueva_palabra)
        time.sleep(0.005)
        clear_output()
    time_resoult = time.time() - time_1
    time_push1 = time_resoult / 60
    time_push2 = time_resoult % 60 
    time_format1 = str(time_push1)
    time_format2 = str(time_push2)
    time_push =  time_format1 +" : " + time_format2
    calificacion = comparador(lista_original, lista_user)
    ratio = "ratio : " + str(calificacion)

    if dificultad == 1:
        dificultad = "facil"
    elif dificultad == 2:
        dificultad = "media"
    elif dificultad == 3:
        dificultad = "dificil"
    
    dificultad = "dificultad : " + dificultad
    push_score = [user, dificultad, time_push, ratio]
    users_scores.append(push_score)
    menu(user)
        

# main menu

def menu(user_menu):
    if user_menu == "default":
        print("\033[1;34m"+"         _ _    _ ______ _____  ____    _____  ______   __  __ ______ _____          _   _  ____   _____ _____            ______ _____          ")
        print("\033[1;34m"+"        | | |  | |  ____/ ____|/ __ \  |  __ \|  ____| |  \/  |  ____/ ____|   /\   | \ | |/ __ \ / ____|  __ \     /\   |  ____|_   _|   /\    ")
        print("\033[1;34m"+"        | | |  | | |__ | |  __| |  | | | |  | | |__    | \  / | |__ | |       /  \  |  \| | |  | | |  __| |__) |   /  \  | |__    | |    /  \   ")
        print("\033[1;34m"+"    _   | | |  | |  __|| | |_ | |  | | | |  | |  __|   | |\/| |  __|| |      / /\ \ | . ` | |  | | | |_ |  _  /   / /\ \ |  __|   | |   / /\ \  ")
        print("\033[1;34m"+"   | |__| | |__| | |___| |__| | |__| | | |__| | |____  | |  | | |___| |____ / ____ \| |\  | |__| | |__| | | \ \  / ____ \| |     _| |_ / ____ \ ")
        print("\033[1;34m"+"    \____/ \____/|______\_____|\____/  |_____/|______| |_|  |_|______\_____/_/    \_\_| \_|\____/ \_____|_|  \_\/_/    \_\_|    |_____/_/    \_\ ")  
        print("")
        print("                                            ~~BIENVENIDO AL JUEGO DE LOS AMIGUELADOS~~")
        print("\033[1;37m"+"Elija una opcion para continuar: ")
        print("\033[1;37m"+"1.- INICIAR SESION")
        print("\033[1;37m"+"2.- REGISTRARSE")
        print("\033[1;37m"+"3.- SCORES")
        print("\033[1;37m"+"4.- SALIR")

        answer = int(input())

        if answer == 1:
            login(user)
        elif answer == 2:
            sign_up()

        elif answer == 3:
            scores()
        elif answer == 4:
            pass
        else:
            print ("LA OPCION MARCADA ES INEXISTENTE")
    if user_menu in users:
        print("\033[1;34m"+"         _ _    _ ______ _____  ____    _____  ______   __  __ ______ _____          _   _  ____   _____ _____            ______ _____          ")
        print("\033[1;34m"+"        | | |  | |  ____/ ____|/ __ \  |  __ \|  ____| |  \/  |  ____/ ____|   /\   | \ | |/ __ \ / ____|  __ \     /\   |  ____|_   _|   /\    ")
        print("\033[1;34m"+"        | | |  | | |__ | |  __| |  | | | |  | | |__    | \  / | |__ | |       /  \  |  \| | |  | | |  __| |__) |   /  \  | |__    | |    /  \   ")
        print("\033[1;34m"+"    _   | | |  | |  __|| | |_ | |  | | | |  | |  __|   | |\/| |  __|| |      / /\ \ | . ` | |  | | | |_ |  _  /   / /\ \ |  __|   | |   / /\ \  ")
        print("\033[1;34m"+"   | |__| | |__| | |___| |__| | |__| | | |__| | |____  | |  | | |___| |____ / ____ \| |\  | |__| | |__| | | \ \  / ____ \| |     _| |_ / ____ \ ")
        print("\033[1;34m"+"    \____/ \____/|______\_____|\____/  |_____/|______| |_|  |_|______\_____/_/    \_\_| \_|\____/ \_____|_|  \_\/_/    \_\_|    |_____/_/    \_\ ")  
        print("")       
        print(                                          "BIENVENIDO {} AL JUEGO DE LOS AMIGUELADOS" .format(user))
        print("\033[1;37m"+"Elija una opcion para continuar: ")
        print("\033[1;37m"+"1.- JUGAR")
        print("\033[1;37m"+"2.- SCORES")
        print("\033[1;37m"+"2.- CERRAR SESION")
        print("\033[1;37m"+"4.- SALIR")

        answer = int(input ("SELECIONE LA OPCION QUE DESEE : "))
        if answer == 1:
            start_game(user)
        elif answer == 2:
            scores()
        elif answer == 3:
            log_out(user)
        elif answer == 4:
            pass
        else:
            print ("LA OPCION MARCADA ES INEXISTENTE")


menu(user)
