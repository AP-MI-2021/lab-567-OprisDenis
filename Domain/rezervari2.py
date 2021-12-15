def creeaza_rezervare(id, nume, clasa, pret, checkin):
    """
creeaza o rezervare
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: boolean
    :return:
    """
    return [id, nume, clasa, pret, checkin]


def get_id(rezervare):
    """
    da id-ul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: id-ul rezervarii
    """
    return rezervare[0]


def get_nume(rezervare):
    return rezervare[1]


def get_clasa(rezervare):
    return rezervare[2]


def get_pret(rezervare):
    return rezervare[3]


def get_checkin(rezervare):
    return rezervare[4]


def to_string(rezervare):
    return "id: {}, nume: {}, clasa: {}, pret: {}, checkin: {}".format(
        get_id(rezervare),
        get_nume(rezervare),
        get_clasa(rezervare),
        get_pret(rezervare),
        get_checkin(rezervare),

    )
