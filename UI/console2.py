from Domain.rezervari import to_string
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.functionalitati import update_clasa, ieftinire_rezervare, pret_maxim_clasa, ordonare_descrescatoare, \
    suma_pret


def help_menu():
    print("1.Pentru comanda adaugare rezervare introduceti: id, nume, clasa, pret, checkin(boolean)")
    print("2.Pentru comanda stergere rezervare introduceti id-ul")
    print("3.Pentru comanda modificare rezervare introduceti: id-ul care trebuie modificat, nume, clasa, pret, checkin")
    print("4.Pentru comanda update clasa introduceti: nume")
    print("5.Pentru comanda ieftinire rezervare introduceti: reducere")
    print("6.Pret maxim clase")
    print("7.Ordonare descrescatoare")
    print("8.Afisarea sumelor preturilor")
    print("a.Afisare rezervari")
    print("x.Iesire")


def run_menu2():
    help_menu()
    while True:
        commands = input("Dati comenzile separate cu \";\" cu parametrii separati prin \",\"")
        cerinte = commands.split(";")
        lista = []
        for i in cerinte:
            tokens = i.split(",")
            if tokens[0] == "1":
                try:
                    lista = adauga_rezervare(tokens[1], tokens[2], tokens[3], int(tokens[4]), bool(tokens[5]), lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif tokens[0] == "2":
                lista = sterge_rezervare(tokens[1], lista)
            elif tokens[0] == "3":
                try:
                    lista = modifica_rezervare(tokens[1], tokens[2], tokens[3], int(tokens[4]), bool(tokens[5]), lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif tokens[0] == "4":
                lista = update_clasa(tokens[1], lista)
            elif tokens[0] == "5":
                lista = ieftinire_rezervare(lista, tokens[1])
            elif tokens[0] == "6":
                print(pret_maxim_clasa(lista))
            elif tokens[0] == "7":
                print(ordonare_descrescatoare(lista))
            elif tokens[0] == "8":
                print(suma_pret(lista))
            elif tokens[0] == "a":
                for rezervare in lista:
                    print(to_string(rezervare))
            elif tokens[0] == "x":
                break
            else:
                print("Optiune gresita! Reincercati!")
