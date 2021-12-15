from Domain.rezervari import get_id, creeaza_rezervare


def adauga_rezervare(id, nume, clasa, pret, checkin, lista):
    """
adauga o rezervare dupa id
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: int
    :param checkin: boolean
    :param lista: lista de rezervari
    :return: lista cu rezervarile vechi si cea noua
    """
    if get_by_id(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    rezervare = creeaza_rezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]


def get_by_id(id, lista):
    """
gaseste o rezervare cu id-ul dat intr-o lista
    :param id:string
    :param lista: lista de rezervari
    :return: rezervarea cu id-ul dat din lista sau None, daca aceasta nu exista
    """
    for rezervare in lista:
        if get_id(rezervare) == id:
            return rezervare
    return None


def sterge_rezervare(id, lista):
    """
sterge o rezervare dupa id-ul dat
    :param id: id-ul rezervarii care se va sterge
    :param lista: lista de rezervari
    :return: o lista de rezervari fara rezervarea stearsa
    """
    if get_by_id(id, lista) is None:
        raise ValueError("Rezervarea nu exista!")
    return [rezervare for rezervare in lista if get_id(rezervare) != id]


def modifica_rezervare(id, nume, clasa, pret, checkin, lista):
    """
modifica rezervarea cu id-ul dat
    :param id: id-ul rezervarii
    :param nume: nume rezervare
    :param clasa: clasa rezervarii
    :param pret: pretu rezervarii
    :param checkin: checkinul rezervarii
    :param lista:lista de rezervari
    :return: lista modificata
    """
    if get_by_id(id, lista) is None:
        raise ValueError("Rezervarea nu exista!")
    lista_noua = []
    for rezervare in lista:
        if get_id(rezervare) == id:
            rezervare_noua = creeaza_rezervare(id, nume, clasa, pret, checkin)
            lista_noua.append(rezervare_noua)
        else:
            lista_noua.append(rezervare)
    return lista_noua
