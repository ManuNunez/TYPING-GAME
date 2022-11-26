
users_scores = [["RZL", "dificultad : NULL", "0 : 0", "ratio : 0"], ["MAN", "dificultad : NULL", "0 : 0", "ratio : 0"]]


def scores():
    for elements in users_scores:
        print("| usuario : {} | {} | {} | {} |".format(elements[0], elements[1], elements[2], elements[3]))


scores()
