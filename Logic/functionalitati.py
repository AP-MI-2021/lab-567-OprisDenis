from Domain.rezervari import get_clasa, get_nume, get_id, get_pret, get_checkin, creeaza_rezervare
from Logic.CRUD import modifica_rezervare


def update_clasa(nume, lista):
    """
Modificam clasa initiala la o clasa superioara
    :param nume: string
    :param lista: lista de rezervari
    :return: lista noua
    """
    for rezervare in lista:
        if get_nume(rezervare) == nume:
            if get_clasa(rezervare) == "economy":
                lista = modifica_rezervare(get_id(rezervare), get_nume(rezervare), "economy plus", get_pret(rezervare), get_checkin(rezervare), lista)
            elif get_clasa(rezervare) == "economy plus":
                lista = modifica_rezervare(get_id(rezervare), get_nume(rezervare), "business", get_pret(rezervare), get_checkin(rezervare), lista)
    return lista


def ieftinire_rezervare(lista, reducere):
    """
Reducem pretul rezervarii daca s-a facut checkin
    :param lista: lista rezervarilor
    :param reducere: integer
    :return: lista noua cu ieftinirea rezervarilor
    """
    if reducere < 0:
        raise ValueError("Reducerea trebuie sa fie un numaer pozitiv!")
    lista_noua = []
    for rezervare in lista:
        if get_checkin(rezervare) is True:
            rezervare_noua = creeaza_rezervare(
                get_id(rezervare),
                get_nume(rezervare),
                get_clasa(rezervare),
                get_pret(rezervare) - (reducere * get_pret(rezervare) // 100),
                get_checkin(rezervare)
            )
            lista_noua.append(rezervare_noua)
        else:
            lista_noua.append(rezervare)
    return lista_noua


def pret_maxim_clasa(lista):
    """
Determinam pretul maxim pentru fiecare clasa
    :param lista: lista rezervarilor
    :return: un dictionar cu preturile maxime ale claselor
    """
    rezultat = {"economy": 0, "economy plus": 0, "business": 0}
    for rezervare in lista:
        if get_clasa(rezervare) == "economy":
            if get_pret(rezervare) > rezultat["economy"]:
                rezultat["economy"] = get_pret(rezervare)
        elif get_clasa(rezervare) == "economy plus":
            if get_pret(rezervare) > rezultat["economy plus"]:
                rezultat["economy plus"] = get_pret(rezervare)
        elif get_clasa(rezervare) == "business":
            if get_pret(rezervare) > rezultat["business"]:
                rezultat["business"] = get_pret(rezervare)
    return rezultat


def ordonare_descrescatoare(lista):
    """
Ordonarea descrescător dupa pret
    :param lista: lista rezervarilor
    :return: lista ordonata
    """
    sorted_list = sorted(lista, key = lambda rezervare: get_pret(rezervare))
    return sorted_list[::-1]


def suma_pret(lista):
    """
Determiam suma preturilor pentru fiecare nume
    :param lista:lista rezervarilor
    :return:dictionar cu sumele
    """
    rezultat = {}
    for rezervare in lista:
        if get_nume(rezervare) in rezultat:
            rezultat[get_nume(rezervare)] += get_pret(rezervare)
        else:
            rezultat[get_nume(rezervare)] = get_pret(rezervare)
    return rezultat
