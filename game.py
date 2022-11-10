import random
import time
from IPython.display import clear_output
import getpass

#DBs

users_login = [["super usuario", "123"]]
users = ["super usuario",]
users_scores = [["super usuario", "0 : 0", "ratio : 0"]]
user = "default"
#function login

def login ():
    log_user = input("INTRODUZCA SU USUARIO :")
    log_password = input("INTRODUZCA SU CONTRASEÑA")
    log =  [log_user, log_password]
    contador = 0
    if log in users_login:
        user = log_user
        menu(user)
    else:
        counter = counter + 1
        print("LOS DATOS UINTRODUCIDOS SON INCORRECTOS")
        while counter < 3:
            login()
#function sign_up

def sign_up():
    time.sleep(1)
    clear_output()
    print("PARA REGISTRARSE INGRESE UN USUARIO Y CONTRASEÑA")
    New_User = input("USUARIO : ")
    pasword = getpass.getpass("CONTRASEÑA : ")

    if New_User in users:
        print("LO SENTIMOS PERO ESE USUARIO YA ESTA OCUPADO")

    else:
        Push_User = [New_User, pasword]
        Push_User_Score = [New_User, "0:0", "ratio : 0", "Dificulty : NULL"]
        users.append(New_User)
        users_login.append(Push_User)
        users_scores.append(Push_User_Score)


def log_out(user_logout):
    user = "default"
    menu()
#funtion scores

def scores():
    pass

#function  game

def game ():
    pass







#main menu

def menu(user_menu):
    if user_menu == "default":
        print("\033[1;34m"+"         _ _    _ ______ _____  ____    _____  ______   __  __ ______ _____          _   _  ____   _____ _____            ______ _____          ")
        print("\033[1;34m"+"        | | |  | |  ____/ ____|/ __ \  |  __ \|  ____| |  \/  |  ____/ ____|   /\   | \ | |/ __ \ / ____|  __ \     /\   |  ____|_   _|   /\    ")
        print("\033[1;34m"+"        | | |  | | |__ | |  __| |  | | | |  | | |__    | \  / | |__ | |       /  \  |  \| | |  | | |  __| |__) |   /  \  | |__    | |    /  \   ")
        print("\033[1;34m"+"    _   | | |  | |  __|| | |_ | |  | | | |  | |  __|   | |\/| |  __|| |      / /\ \ | . ` | |  | | | |_ |  _  /   / /\ \ |  __|   | |   / /\ \  ")
        print("\033[1;34m"+"   | |__| | |__| | |___| |__| | |__| | | |__| | |____  | |  | | |___| |____ / ____ \| |\  | |__| | |__| | | \ \  / ____ \| |     _| |_ / ____ \ ")
        print("\033[1;34m"+"    \____/ \____/|______\_____|\____/  |_____/|______| |_|  |_|______\_____/_/    \_\_| \_|\____/ \_____|_|  \_\/_/    \_\_|    |_____/_/    \_\ ")  
        print ("BIENVENIDO AL JUEGO DE LOS AMIGUELADOS")
        print ("eliga una opcion para continuar")
        print ("\033[1;37m"+"1.- LOGIN")
        print ("\033[1;37m"+"2.- SIGN UP")
        print ("\033[1;37m"+"3.- SCORES")
        print ("\033[1;37m"+"4.- EXIT")

        answer = int(input())

        if answer == 0:
            #ENTER SA MODE
            pass
        elif answer == 1:
            pass
        elif answer == 2:
            sign_up()

        elif answer == 3:
            pass
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
        print ("BIENVENIDO {} AL JUEGO DE LOS AMIGUELADOS" .format(user))
        print ("eliga una opcion para continuar")
        print ("\033[1;37m"+"1.- JUGAR")
        print ("\033[1;37m"+"2.- SCORES")
        print ("\033[1;37m"+"2.- LOGOUT")
        print ("\033[1;37m"+"4.- EXIT")

        if answer == 0:
            #ENTER SA MODE
            pass
        elif answer == 1:
            pass
        elif answer == 2:
            pass
        elif answer == 3:
            log_out(user)
        elif answer == 4:
            pass
        else:
            print ("LA OPCION MARCADA ES INEXISTENTE")


menu(user)
