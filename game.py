from random import *
import time
from IPython.display import clear_output
import getpass

# DBs

users_scores_p = [["PPE", [0], [0]], ["VCN", [0], [0]], ["MIG", [0], [0]], ["SKM", [0], [0]], ["RZL", [0], [0]]]
users_login = [["RZL", "123"], ["PPE", "123"], ["MIG", "123"], ["SKM", "123"], ["VCN", "123"]]
users = ["RZL", "PPE", "VCN", "MIG", "SKM"]
users_scores = [["RZL", "dificultad : NULL", "0 : 0", "pts : 0"], ["SKM", "dificultad : 1", "0 : 0", "pts: 0"], ["PPE", "dificultad : 1", "0 : 0", "pts: 0"], ["MIG", "dificultad : 1", "0 : 0", "pts: 0"], ["VCN", "dificultad : 1", "0 : 0", "pts: 0"]]

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
    log_user = input("INTRODUZCA SU USUARIO: ")
    log_password = getpass.getpass("INTRODUZCA SU CONTRASEÑA: ")
    log = [log_user, log_password]
    counter = 0
    if log in users_login:
        user = log_user
        transition()
        menu(user)
    else:
        counter = counter + 1
        print("\033[0;37m"+"LOS DATOS INTRODUCIDOS SON INCORRECTOS")
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
    print("SU USUARIO DEBE DE SER DE 3 LETRAS DE LARGO")
    New_User = input("USUARIO: ")
    pasword = getpass.getpass("CONTRASEÑA: ")
    if len(New_User) == 3:
        if New_User in users:
            print("\033[0;37m"+"LO SENTIMOS PERO ESE USUARIO YA ESTA OCUPADO")

        else:
            New_User = New_User.upper()
            Push_p_score = [New_User,[],[]]
            Push_User = [New_User, pasword]
            Push_User_Score = [New_User, "dificultad : NULL", "0 : 0", "ratio : 0"]
            users.append(New_User)
            users_login.append(Push_User)
            users_scores.append(Push_User_Score)
            users_scores_p.append(Push_p_score)
            time.sleep(1)
            clear_output()
            user = New_User
            menu(user)
    else:
        print("\033[0;37m"+"EL USUARIO QUE INTRODUJO NO TIENE LA LONGITUD CORRECTA")


def log_out(user_logout):

    user = "default"
    menu(user)


# Function list


list_frases_facil = ["inteligencia es la habilidad de adaptarse al cambio", "quien tiene paciencia tendra lo que desea", "cuando el hombre no se encuentra a si mismo, no encuentra nada", "el exito depende del esfuerzo", "una buena cabeza y un buen corazon son siempre combinaciones formidables"]
list_frases_inter = ["inteligencia es la habilidad de adaptarse al cambio", "quien tiene paciencia tendra lo que desea", "cuando el hombre no se encuentra a si mismo, no encuentra nada", "el exito depende del esfuerzo", "una buena cabeza y un buen corazon son siempre combinaciones formidables",
 "de todos los animales de la creacion el hombre es el unico que toma agua sin tener sed, come sin tener hambre y habla sin tener nada que decir", "todos somos muy ignorantes. lo que ocurre es que no todos ignoramos las mismas cosas", "el placer y la accion hacen que las horas parezcan cortas", "la gente se rie de mi por que soy diferente, yo me rio de ellos por que son todos iguales", "la ocasion hay que crearla, no esperar a que llegue"]
list_frases_dificil = ["inteligencia es la habilidad de adaptarse al cambio", "quien tiene paciencia tendra lo que desea", "cuando el hombre no se encuentra a si mismo, no encuentra nada", "el exito depende del esfuerzo", "una buena cabeza y un buen corazon son siempre combinaciones formidables",
 "de todos los animales de la creacion el hombre es el unico que toma agua sin tener sed, come sin tener hambre y habla sin tener nada que decir", "todos somos muy ignorantes. lo que ocurre es que no todos ignoramos las mismas cosas", "el placer y la accion hacen que las horas parezcan cortas", "la gente se rie de mi por que soy diferente, yo me rio de ellos por que son todos iguales", "la ocasion hay que crearla, no esperar a que llegue", 
 "educacion es lo que queda despues de olvidar lo que se ha aprendido en la escuela", "adentro del vaticano todo estaa forrado de oro y afuere los pibes estan muriendo de hambre", "la  envidia  es una declaracion de inferioridad", "solo hay una felicidad en la vida, amar y ser amado", "no malgastes tu tiempo pues de esa materia esta formada la vida"]



def listas(dificultad):

    list = []
    if dificultad == 1:
        list = list_frases_facil
    elif dificultad == 2:
        for m in range (0, 5):
            frase = list_frases_inter[randint(0, 9)]
            list.append(frase)

    elif dificultad == 3:
        for m in range (0, 5):
            frase = list_frases_dificil[randint(0, 14)]
            list.append(frases)
    return list

# funtion scores


def inversor():

    counter = -1
    while counter > -5:
        new_list = new_list.apend(users_scores[counter])
        counter = counter - 1
    scores_general()


def sort(arg):

    global users_scores

    if arg == 1:
        newlist = sorted(users_scores, key=lambda x: x[0])
        users_scores = newlist
        scores_general()

    elif arg == 2:
        newlist = sorted(users_scores, key=lambda x: x[1])
        users_scores = newlist
        scores_general()

    elif arg == 3:
        users_scores = sorted(users_scores, key=lambda x: x[2])
        users_scores = newlist
        scores_general()

    elif arg == 4:
        newlist = sorted(users_scores, key=lambda x: x[3])
        users_scores = newlist
        inversor()

def ranking ():

    global users_scores_p

    list_s = sorted(users_scores_p, reverse = True, key = lambda x: x[2])
    users_scores_p = list_s
    for i in range(0, (len(list_s) - 1)):
        print (users_scores_p[i])



def get_ranking(user):
    
    global users_scores_p

    global rank
    for i in range(0, (len(users_scores_p) - 1)):
        check = users_scores_p [i]
        if check[0] == user:
            rank = i + 1
    
    return rank

def scores_particular(user):

    for element in users_scores_p:
        if element[0] == user:
            score_l = element[1]
            for i in range (0, len(score_l- 1)):
                pts = score_l[i]
                print ("\n PARTIDA {}: {}" .format((i + 1), pts))
                score_t += pts
            print ("\033[0;37m"+"TU PUNTAJE GLOGAL ES: {}" .format(score_t))
            
            

def scores_general():

    time.sleep(0.005)
    clear_output()
    print("\033[0;37m"+"PARA SALIR PRESIONE: 0")
    for elements in users_scores:
        print("| usuario : {} | {} | {} | {} |".format(elements[0], elements[1],elements[2], elements[3]))
    
    print("\033[0;37m"+"ORDENAR POR USUARIO: 1")
    print("\033[0;37m"+"ORDENAR POR DIFICULTAD: 2")
    print("\033[0;37m"+"ORDENAR POR TIEMPO: 3")
    print("\033[0;37m"+"ORDENAR POR PORCENTAJE DE ACIERTOS: 4")
    sort_arg = int(input())
    if sort_arg == 0 :
        menu(user)
    elif sort_arg == 1 or sort_arg == 2 or sort_arg == 3 or sort_arg == 4:
        sort(sort_arg)
    elif sort_arg == 5:
        inversor()
    else :
        print("\033[0;37m"+"EL ARGUMENTO INTRODUCIDO ES INVALIDO")



# function  game


def start_game(user_game):

    time.sleep(0.05)
    clear_output()
    transition()
    print("\033[0;37m"+"SELECCIONE LA DIFICULTAD DE JUEGO: ")
    print("\033[0;37m"+"1- FACIL")
    print("\033[0;37m"+"2- MEDIO")
    print("\033[0;37m"+"3- DIFICIL")
    dificultad = int(input())
    game(dificultad, user_game)
    time.sleep(0.005)
    clear_output()


def comparador(lista_original, lista_usuario, dificultad):

    m = 0
    n = 0
    total_score = 0
    errores = 0
    bool = False
    for i in range(0, (len(lista_original) - 1)):
        errores = 0
        o = lista_original[i]
        u = lista_usuario[i]
        z = 0
        j = 0
        if len(u) >= len(o):

            for j in range (0, (len(o)-1)):
                if u[z] == o[j]:
                    pass

                elif u[z] != o[j] and u[z] == o[j+1]:
                    errores += 1
                    j -= 1

                elif u[z] != o[j] and u[z] == o[j - 1]:
                    errores += 1
                    j += 1

                elif u[z] != o[j] and u[z+1] == o[j + 1]:
                    errores += 1
                
                elif u[z] != o[j] and u[z] == o[j + 1]:
                    errores += 1
                    j -= 1
                
                elif u[z] == o[j + 1] and u[z + 1] == o[j]:
                    errores += 1
                    j += 1
                    z += 1
                
                else :
                    errores += 1

        elif len(u) < len(o) :
            for j in range (0, (len(u)-1)):
                if u[z] == o[j]:
                    pass

                elif u[z] != o[j] and u[z] == o[j+1]:
                    errores += 1
                    j -= 1

                elif u[z] != o[j] and u[z] == o[j - 1]:
                    errores += 1
                    j += 1

                elif u[z] != o[j] and u[z+1] == o[j + 1]:
                    errores += 1
                
                elif u[z] != o[j] and u[z] == o[j + 1]:
                    errores += 1
                    j -= 1
                
                elif u[z] == o[j + 1] and u[z + 1] == o[j]:
                    errores += 1
                    j += 1
                    z += 1
                
                else :
                    errores += 1

            
            if dificultad == 1:
                
                if dificultad < 6:
                    total_score += (30 - (errores * 5))


                elif errores >= 6:
                    total_score -= 25

            elif dificultad == 2:
                if errores < 6:
                    total_score += (50 - (errores * 5))
                

                elif errores >= 6:
                    total_score -= 25

            elif dificultad == 3:
                if errores < 6:
                    total_score += (70 - (errores * 5))

                elif errores >= 6:
                    total_score -= 25
            
            if errores != 0:
                bool = True

    if bool == False:
        total_score = total_score * 2        
            
    return total_score


def game(dificultad, user):

    transition()
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
    time_push1 = time_resoult // 60
    time_push2 = time_resoult % 60 
    time_format1 = str(time_push1)
    time_format2 = str(time_push2)
    time_push =  time_format1 +" : " + time_format2
    calificacion = comparador(lista_original, lista_user, dificultad)
    ratio = "ratio : " + str(calificacion)
    dificultad_txt = 0

    for i in range( 0, len(users_scores_p) ):
        element = users_scores_p[i]
        score_t = element[2]
        score_p = element[1] 
        if element[0] == user:
            score_p.append(calificacion)
            score_t = sum(score_p)
             
            

    if dificultad == 1:
        dificultad_txt = "FACIL"
    elif dificultad == 2:
        dificultad_txt = "MEDIA"
    elif dificultad == 3:
        dificultad_txt = "DIFICIL"
    
    dificultad = "dificultad : " + dificultad_txt
    push_score = [user, dificultad, time_push, ratio]
    users_scores.append(push_score)

    transition()
    game_final(user, lista_original, lista_user)
        
def game_final(user, lista_original, lista_user):

    time.sleep(0.5)
    clear_output()
    transition()
    for i in range (0, (len(lista_original) - 1)):
        print(lista_original[i])
        print(lista_user[i])
        if lista_original[i] == lista_user[i]:

            print ("\033[0;37m"+"ESTA FRASE SE COMPLETO SIN ERRORES")
        else:
            print ("\033[0;37m"+"ESTA FRASE SE COMPLETO CON ERRORES")

    scores_particular(user)
    ranking()
    rank = get_ranking(user)
    print ("\033[0;37m"+"FELICIDADES, ACTUALMENTE TE ENCUENTRAS EN EL TOP: {}" .format( rank))
    i = 1
    while i > 0:
        print ("\033[0;37m"+"DESEA:")
        print ("\033[0;37m"+"1)VOLVER A JUGAR ")
        print ("\033[0;37m"+"2)VOLVER AL MENU ")
        selector = int(input())
        if selector == 1:
            transition()
            start_game(user)
        elif selector == 2:
            transition()
            menu(user)
        else:
            print ("\033[0;37m"+"ESTA OPCION NO ES VALIDA")


# main menu

def transition():

    time.sleep(1)
    clear_output() 
    print("\033[0;37m"+"CARGANDO ")
    
    time.sleep(1)
    clear_output()
    print("\033[0;37m"+"CARGANDO . ")

    time.sleep(1)
    clear_output()
    print("\033[0;37m"+"CARGANDO . . ")

    time.sleep(1)
    clear_output()
    print("\033[0;37m"+"CARGANDO . . .")

    time.sleep(1)
    clear_output()

def menu(user_menu):
    time.sleep(0.05)
    clear_output()

    if user_menu == "default":
        print("\033[1;34m"+"         _ _    _ ______ _____  ____    _____  ______   __  __ ______ _____          _   _  ____   _____ _____            ______ _____          ")
        print("\033[1;34m"+"        | | |  | |  ____/ ____|/ __ \  |  __ \|  ____| |  \/  |  ____/ ____|   /\   | \ | |/ __ \ / ____|  __ \     /\   |  ____|_   _|   /\    ")
        print("\033[1;34m"+"        | | |  | | |__ | |  __| |  | | | |  | | |__    | \  / | |__ | |       /  \  |  \| | |  | | |  __| |__) |   /  \  | |__    | |    /  \   ")
        print("\033[1;34m"+"    _   | | |  | |  __|| | |_ | |  | | | |  | |  __|   | |\/| |  __|| |      / /\ \ | . ` | |  | | | |_ |  _  /   / /\ \ |  __|   | |   / /\ \  ")
        print("\033[1;34m"+"   | |__| | |__| | |___| |__| | |__| | | |__| | |____  | |  | | |___| |____ / ____ \| |\  | |__| | |__| | | \ \  / ____ \| |     _| |_ / ____ \ ")
        print("\033[1;34m"+"    \____/ \____/|______\_____|\____/  |_____/|______| |_|  |_|______\_____/_/    \_\_| \_|\____/ \_____|_|  \_\/_/    \_\_|    |_____/_/    \_\ ")  
        print("")
        print("                                            ~~BIENVENIDO AL JUEGO DE LOS AMIGUELADOS~~")
        print("\033[0;37m"+"ELIJA UNA OPCION PARA CONTINUAR : ")
        print("\033[0;37m"+"1.- INICIAR SESION")
        print("\033[0;37m"+"2.- REGISTRARSE")
        print("\033[0;37m"+"3.- SCORES")
        print("\033[0;37m"+"4.- SALIR")

        answer = int(input())

        if answer == 1:
            transition()
            login(user)
        elif answer == 2:
            transition()
            sign_up()

        elif answer == 3:
            transition()
            scores_general(user)
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
        print("\033[0;37m"+"ELIJA UNA OPCION PARA CONTINUAR : ")
        print("\033[0;37m"+"1.- JUGAR")
        print("\033[0;37m"+"2.- SCORES")
        print("\033[0;37m"+"3.- CERRAR SESION")
        print("\033[0;37m"+"4.- SALIR")

        answer = int(input ("SELECIONE LA OPCION QUE DESEE : "))
        if answer == 1:
            transition()
            start_game(user)
        elif answer == 2:
            transition()
            time.sleep(0.5)
            clear_output()
            print("\033[0;37m"+"DESEA VER LOS PUNTAJES :")
            print("\033[0;37m"+"1) PARTICULARES")
            print("\033[0;37m"+"2) GENERALES")
            print("\033[0;37m"+"3) CANCELAR")

            selector = input("\033[0;37m"+"SELECCIONE LA OPCION QUE DESEE: ")

            if selector == 1:
                time.sleep(0.5)
                clear_output()
                scores_particular(user)
                ranking()
                rank = get_ranking(user)
                print ("\033[0;37m"+"FELICIDADES, ACTUALMENTE TE ENCUENTRAS EN EL TOP: {}" .format( rank))


            elif selector == 2:
                scores_general(user)
            elif selector == 3:
                menu(user)


        elif answer == 3:
            transition()
            log_out(user)
        elif answer == 4:
            pass
        else:
            print ("\033[0;37m"+"LA OPCION MARCADA ES INEXISTENTE")


menu(user)