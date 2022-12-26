"""
Moduł odpowiadający za wyszukiwanie i wyświetlanie
z bazy danych
"""
import sqlite3
from szyfrowanie import Deszyfruj, Szyfrowanie
from koloruj import color_text


def WyświetlZadane(wyszukiwanie, wyroznienie=0):
    """
        Procedura wydruku wyszkiwanych danych ze zdefiniowanymi parametrami.
        :param wyszukiwanie:
        :param wyroznienie:
        :return:
        """
    przerwana = False  # zmienna determinująca wyswietlanie komunikatu o ilości znalezionych rekordów jeśli przerwano proces wyświetlania.
    con = sqlite3.connect("baza_glowna.db")  # procedury otwarcia bazy danych ustawienia kursora
    cur = con.cursor()

    sqlite_select_query = wyszukiwanie  # przypisanie zdefiniowanej opcji SELECT dla bazy ze względu na wcześniejsze wybory co do przeszukania
    cur.execute(sqlite_select_query)
    records = cur.fetchall()

    licznik = 0
    for row in records:  # iteracja po wszystkich znalezionych rekordach pasujących do wyszukiwania.

        if wyroznienie == 0:
            print('-' * 36)
        print("Znaleziony: ", row[0])
        if wyroznienie == 0:
            print('-' * 36)
        if wyroznienie == 1:
            print('-' * 36)

        print("Rodzaj Hasła: ", color_text('red', row[1]))
        if wyroznienie == 1:
            print('-' * 36)
        if wyroznienie == 2:
            print('-' * 36)
        print("Login: ", color_text('green', Deszyfruj(row[2])))  # deszyfrowanie przed wyświetleniem
        if wyroznienie == 2:
            print('-' * 36)
        print("Hasło: ", color_text('magenta', Deszyfruj(row[3])))  # deszyfrowanie przed wyświetleniem
        if wyroznienie == 4:
            print('-' * 36)
            print("Adres usługi: ", color_text('yellow', row[4]))
            print('-' * 36)

        if wyroznienie == 5:
            print('-' * 36)
            print("Adres usługi: ", color_text('yellow', row[4]))
            print('-' * 36)
        if wyroznienie != 4 and wyroznienie != 5 and row[4] != "Usługa niezdefiniowana":
            print("Adres usługi: ", color_text('yellow', row[4]))
        if wyroznienie != 4 and wyroznienie != 5 and row[4] == "Usługa niezdefiniowana":
            print("Adres usługi: ", color_text('cyan', row[4]))

        print("Data utworzenia: ", row[5])
        if wyroznienie == 3:
            print('-' * 36)

        opis = row[6]
        if opis == "":
            opis = "(brak)"
        print("Dodatkowy opis: ", color_text('blue', opis))
        if wyroznienie == 3:
            print('-' * 36)
        print("\n")
        licznik += 1  # licznik dla zatrzymania wyświetlania po 4 rekordach
        if licznik == 3:
            test = input("....Nacisnij Enter(dalej)... Wpisz 'q' żeby zakończyć")
            if test == "q":  # Wcześniejsze wyjście z pętli wyświetlania na rządanie
                licznik = 0
                przerwana = True  # zmienna determinująca wyswietlanie komunikatu o ilości znalezionych rekordów jeśli przerwano proces wyświetlania.
                break

            licznik = 0

    con.commit()  # wykonanie
    con.close()  # zamknięcie bazy
    if przerwana:  # komunikat jeśli przerwano wyświetlanie rekordów
        print("\nZnaleziono:  ", len(records),
              " rekordów.")
        print(",ale nie wyświetlono wszytkich (operacja przerwana) !!\n")
    else:
        print("Znaleziono:  ", len(records), " rekordów i wszystkie wyświetlono\n")  # jeśli wyświetlono wszystkie
    input("Enter aby powrócic do menu.")  # input powstrzymujący przed przypadkowym kliknięciem entera
    # (duża ilość ekranów z danymi powoduje, że klikając szybko można rozwalić menu


def Cała():
    """Funkcja pobiera i wyświetla dane z całej bazy."""
    wyszukiwanie = "SELECT * from Sejf "
    wyroznienie = 0
    WyświetlZadane(wyszukiwanie, wyroznienie)
    return


def WyszukajWWW(param):
    """Funkcja pobiera i wyświetla dane dla serwisów WWW."""
    if param == "":  # param to zmienna przekazująca szukany ciąg
        wyszukiwanie = f"SELECT * from Sejf where Rodzaj_hasła= 'Usługa WWW'"

    else:
        szukane = f"LIKE '%{param}%'"
        wyszukiwanie = f"SELECT * from Sejf where Rodzaj_hasła= 'Usługa WWW' AND Adres='{param}'"
    wyroznienie = 5
    WyświetlZadane(wyszukiwanie, wyroznienie)
    return


def WyszukajMail(param):
    """Funkcja pobiera i wyświetla dane dla serwisów emailowych."""
    if param == "":
        wyszukiwanie = "SELECT * from Sejf where Rodzaj_hasła='Usługa Email'"

    else:
        wyszukiwanie = f"SELECT * from Sejf where Rodzaj_hasła= 'Usługa Email' AND Adres='{param}'"
    wyroznienie = 4
    WyświetlZadane(wyszukiwanie, wyroznienie)
    return


def WyszukajNieokreslone():
    """Funkcja pobiera i wyświetla dane dla serwisów nieokreślonych."""
    wyszukiwanie = "SELECT * from Sejf where Rodzaj_hasła='Inne'"
    wyroznienie = 1
    WyświetlZadane(wyszukiwanie, wyroznienie)
    return


def WyszukajLogin(string):
    """Funkcja pobiera i wyświetla dane dla podanego loginu."""
    szukane = f"LIKE '%{Szyfrowanie(string)}%'"  ##maska na szukanie wyrazęnia zawierającego string
    # i mponowne szyfrowanie celem znalezienia loginu (baza jest zaszyfrowana w tym polu
    wyszukiwanie = f"SELECT * from Sejf where Login {szukane} "

    wyroznienie = 2
    WyświetlZadane(wyszukiwanie, wyroznienie)
    return


def WyszukajOpis(param):
    """Funkcja pobiera i wyświetla dane dla podanego słowa z opisu."""

    szukane = f"LIKE '%{param}%'"  # maska na szukanie wyrazęnia zawierającego string param

    wyszukiwanie = f"SELECT * from Sejf where Dodatkowy_opis {szukane}"

    wyroznienie = 3
    WyświetlZadane(wyszukiwanie, wyroznienie)
    return


def WyszukajData():
    pass
