import random
import time


#DBs

users_login = []
users = ["default_user", "super usuario",]
users_scores = []

#function login

def login ():
    pass

#function sign_up

def sign_up():
    pass

#funtion scores

def scores():
    pass

#function  game

def game ():
    pass

#main menu
user = users[0]
if user == users[0]:
    print ("BIENVENIDO AL JUEGO DE MECANOGRAFIA DE LOS AMIGUELADOS")
    print ("eliga una opcion para continuar")
    print ("1.- LOGIN")
    print ("2.- SIGN UP")
    print ("3.- SCORES")
    print ("4.- EXIT")

    answer = int(input())

    if answer == 0:
        #ENTER SA MODE
        pass
    elif answer == 1:
        pass
    elif answer == 2:
        pass
    elif answer == 3:
        pass
    elif answer == 4:
        pass
    else:
        print ("LA OPCION MARCADA ES INEXISTENTE")
if user in users:
    print ("BIENVENIDO {} AL JUEGO DE MECANOGRAFIA DE LOS AMIGUELADOS" .format(user))
    print ("eliga una opcion para continuar")
    print ("1.- JUGAR")
    print ("2.- SCORES")
    print ("2.- LOGOUT")
    print ("4.- EXIT")

    if answer == 0:
        #ENTER SA MODE
        pass
    elif answer == 1:
        pass
    elif answer == 2:
        pass
    elif answer == 3:
        pass
    elif answer == 4:
        pass
    else:
        print ("LA OPCION MARCADA ES INEXISTENTE")
