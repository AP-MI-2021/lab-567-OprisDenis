from Domain.rezervari import get_id, get_nume, get_clasa, get_pret, get_checkin
from Logic.CRUD import adauga_rezervare, get_by_id, sterge_rezervare, modifica_rezervare


def test_adauga_rezervare():
    lista = adauga_rezervare("1", "avion1", "business", 1200, True, [])
    assert len(lista) == 1
    assert get_id(get_by_id("1", lista)) == "1"
    assert get_nume(get_by_id("1", lista)) == "avion1"
    assert get_clasa(get_by_id("1", lista)) == "business"
    assert get_pret(get_by_id("1", lista)) == 1200
    assert get_checkin(get_by_id("1", lista)) is True


def test_sterge_rezervare():
    lista = adauga_rezervare("1", "avion2", "business", 1200, True, [])
    lista = adauga_rezervare("2", "avion2", "economy", 100, True, lista)
    lista = sterge_rezervare("1", lista)
    assert len(lista) == 1
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None


    try:
        lista = sterge_rezervare("3", lista)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert get_by_id("2", lista) is not None
    except Exception:
        assert False


def test_modifica_rezervare():
    lista = adauga_rezervare("1", "avion1", "business", 1200, True, [])
    lista = adauga_rezervare("2", "avion2", "economy", 100, True, lista)
    lista = modifica_rezervare("1", "avion3", "economy plus", 1800, True, lista)

    rezervare_update = get_by_id("1", lista)
    assert get_id(rezervare_update) == "1"
    assert get_nume(rezervare_update) == "avion3"
    assert get_clasa(rezervare_update) == "economy plus"
    assert get_pret(rezervare_update) == 1800
    assert get_checkin(rezervare_update) is True

    rezervare_fara_update = get_by_id("2", lista)
    assert get_id(rezervare_fara_update) == "2"
    assert get_nume(rezervare_fara_update) == "avion2"
    assert get_clasa(rezervare_fara_update) == "economy"
    assert get_pret(rezervare_fara_update) == 100
    assert get_checkin(rezervare_fara_update) is True


    lista = []
    lista = adauga_rezervare("1", "avion1", "business", 1200, True, lista)
    try:
        lista = modifica_rezervare("3", "avion3", "economy plus", 1800, True, lista)
    except ValueError:
        rezervare_fara_update = get_by_id("1", lista)
        assert get_id(rezervare_fara_update) == "1"
        assert get_nume(rezervare_fara_update) == "avion1"
        assert get_clasa(rezervare_fara_update) == "business"
        assert get_pret(rezervare_fara_update) == 1200
        assert get_checkin(rezervare_fara_update) is True
    except Exception:
        assert False
