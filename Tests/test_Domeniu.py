from Domain.rezervari import creeaza_rezervare, get_id, get_nume, get_clasa, get_pret, get_checkin


def test_rezervare():
    rezervare = creeaza_rezervare("1", "avion", "economy", 1200, True)
    assert get_id(rezervare) == "1"
    assert get_nume(rezervare) == "avion"
    assert get_clasa(rezervare) == "economy"
    assert get_pret(rezervare) == 1200
    assert get_checkin(rezervare) is True
