from Domain.rezervari import to_string
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.functionalitati import update_clasa, ieftinire_rezervare, pret_maxim_clasa, ordonare_descrescatoare, \
    suma_pret


def print_menu():
    print("1.Adaugare rezervare")
    print("2.Stergere rezervare")
    print("3.Modifica rezervare")
    print("4.Trecerea tuturor rezervarilor pe un nume dat la o clasa superioara")
    print("5.Ieftinirea rezervarilor la care s-a facut checkin cu un procentaj dat")
    print("6.Determinare pretului maxim pentru fiecare clasa")
    print("7.Ordonarea descrescător rezervarilor dupa pret")
    print("8.Afisarea sumelor preturilor pentru fiecare nume")
    print("u.Undo")
    print("r.Redo")
    print("a.Afisare rezervari")
    print("x.Iesire")


def ui_adauga_rez(lista):
    try:
        id = input("Dati id-ul:")
        nume = input("Dati numele:")
        clasa = input("Dati clasa:")
        pret = float(input("Dati pretul:"))
        checkin = bool(input("Dati checkin-ul:"))
        return adauga_rezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_sterge_rez(lista):
    try:
        id = input("Dati id-ul rezervarii de sters:")
        return sterge_rezervare(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_modifica_rez(lista):
    try:
        id = input("Dati id-ul rezervarii de modificat:")
        nume = input("Dati noul nume:")
        clasa = input("Dati noua clasa:")
        pret = int(input("Dati noul pret:"))
        checkin = bool(input("Dati noul checkin:"))
        return modifica_rezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_update_clasa(lista):
    try:
        nume = input("Dati un nume pentru a modifica clasa:")
        return update_clasa(nume, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_ieftinire_rezervare(lista):
    try:
        reducere = float(input("Dati un numar pentru a reduce rezervarea:"))
        return ieftinire_rezervare(lista, reducere)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_pret_maxim_clasa(lista):
    print(pret_maxim_clasa(lista))


def ui_ordonare_descrescatoare(lista):
    print(ordonare_descrescatoare(lista))


def ui_suma_pret(lista):
    print(suma_pret(lista))


def show_all(lista):
    for rezervare in lista:
        print(to_string(rezervare))


def run_menu():
    undo_list = []
    redo_list = []
    lista = []
    while True:
        print_menu()
        optiune = input("Dati optiune: ")
        if optiune == "1":
            if len(lista) > 0:
                undo_list.append(lista)
            lista = ui_adauga_rez(lista)
        elif optiune == "2":
            if len(lista) > 0:
                undo_list.append(lista)
            lista = ui_sterge_rez(lista)
        elif optiune == "3":
            if len(lista) > 0:
                undo_list.append(lista)
            lista = ui_modifica_rez(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "4":
            if len(lista) > 0:
                undo_list.append(lista)
            lista = ui_update_clasa(lista)
        elif optiune == "5":
            if len(lista) > 0:
                undo_list.append(lista)
            lista = ui_ieftinire_rezervare(lista)
        elif optiune == "6":
            if len(lista) > 0:
                undo_list.append(lista)
            ui_pret_maxim_clasa(lista)
        elif optiune == "7":
            if len(lista) > 0:
                undo_list.append(lista)
            ui_ordonare_descrescatoare(lista)
        elif optiune == "8":
            if len(lista) > 0:
                undo_list.append(lista)
            ui_suma_pret(lista)
        elif optiune == "u":
            if len(undo_list) > 0:
                redo_list.append(undo_list[len(undo_list)-1])
                redo_list.append(lista)
                lista = undo_list.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redo_list) > 0:
                lista = redo_list.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati!")
