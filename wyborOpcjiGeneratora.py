"""
Moduł realizujący wybory użytkownika dotyczące
postaci generowanego hasła.
Możliwości wyboru dotyczą długości hasła, zawierania co najmniej jednego znaku spoecjalnego,
oraz zawierania co najmniej jednej cyfry
"""

from zapiszClipboard import dodajDoSchowka
from generator import Generowanie


class ZlyWybor(Exception):
    pass


def Wybor_dlugosci_hasla():
    """
    Wybór długości hasła, z walidacją do max 40 znaków.
    :return:
    """

    try:
        global dlugoscHasla
        dlugoscHasla = 0
        while dlugoscHasla == 0 or dlugoscHasla >= 41:
            dlugoscHasla = int(input(
                "Tip :(hasło zawsze ma dozwolone małe i wielkie litery)\nPodaj długość żądanego hasła(max 40)  : "))  # wybór długości hasła

            if dlugoscHasla >= 41:
                print("Nie przesadzaj z tą długością hasła (dopuszczalna długość to 40 cyfr.\n")


    except ValueError:
        print("podaj wartość liczbową!!\n")

        Wybor_dlugosci_hasla()

    return dlugoscHasla


def Czy_specjalne():
    """
    Funkcja, w której użytkownik decyduje czy generowane hasło ma zawierać
    co najmniej jeden znak specjalny, z walidacją odpowiedzi (możliwe tylko 't' lub 'n',
    bez względu na wielkość liter).
    :return:
    """
    czy_specjalne = ""
    while czy_specjalne != 'T' and czy_specjalne != 'N':
        try:
            czy_specjalne = input("Czy hasło ma zawierać przynajmniej jeden znak specjalny ? (T/N)")
            czy_specjalne = str.upper(czy_specjalne)
            if czy_specjalne != "T" and czy_specjalne != "N":
                raise ZlyWybor()
        except ZlyWybor:
            print("Dokonano złego wyboru. Dostępne opcje to T/N")

    match czy_specjalne:
        case "T":
            znaki_specjalne = True

            return znaki_specjalne
        case "N":
            znaki_specjalne = False
            return znaki_specjalne


def Czy_zawiera_liczbe():
    """
       Funkcja, w której użytkownik decyduje czy generowane hasło ma zawierać
       co najmniej jedeą cyfrę, z walidacją odpowiedzi, (możliwe tylko 't' lub 'n',
       bez względu na wielkość liter).
       :return:
       """

    czy_liczba = ""
    while czy_liczba != 'T' and czy_liczba != 'N':
        try:
            czy_liczba = input("Czy hasło ma zawierać przynajmniej jedną cyfrę ? (T/N)")
            czy_liczba = str.upper(czy_liczba)
            if czy_liczba != "T" and czy_liczba != "N":
                raise ZlyWybor()
        except ZlyWybor:
            print("Dokonano złego wyboru. Dostępne opcje to T/N")

    match czy_liczba:
        case "T":
            zawiera_liczbe = True

            return zawiera_liczbe
        case "N":
            zawiera_liczbe = False
            return zawiera_liczbe


def Wybor():
    """
    Funkcja wywołująca generator hasła, przygotowująca zmienne do wysłania
    do modułu generującego w zależności od dokonanych wyborów uzytkownika,
    wyświetlająca podsumowanie tych wyborów, wołająca generator, a następnie
    po otrzymaniu od generatora gotowego hasła, wołająca funkcję zapisu tego hasła
    do systemowego schowka i informująca użytkownika, że wygenerowane hasło z automatu
    znalazło się w schowku systemowym.
    :return:
    """

    dlugosc_hasla = int(Wybor_dlugosci_hasla())
    znaki_specjalne = Czy_specjalne()
    zawiera_liczbe = Czy_zawiera_liczbe()

    if znaki_specjalne:
        wynik1 = "Tak"
    else:
        wynik1 = "Nie"
    if zawiera_liczbe:
        wynik2 = "Tak"
    else:
        wynik2 = "Nie"
    podsumowanie = (
        f'Parametry oczekiwanego hasła: \n'
        f'******************************\n'
        f'dlugość hasla:{dlugosc_hasla}\n'
        f'Znaki specjalne :{wynik1}\n'
        f'Czy ma zawierać chociaż jedną cyfrę: {wynik2}\n')
    print("***" * 10)
    print(podsumowanie)
    print("***" * 10)
    haslo = Generowanie(dlugosc_hasla, znaki_specjalne, zawiera_liczbe)

    dodajDoSchowka(haslo)
    print(f"Wygenerowane hasło to : '{haslo}' \n Spokojnie masz już je załadowane do schowka systemowego ;)\n")
    return
