"""

Wszystkie funkcje do operacji na bazie danych

"""
from szyfrowanie import Klucz,Deszyfruj,Szyfrowanie
import walidacjeDlaBazyDanych
import pyperclip
import sqlite3
import mainBaza
from shutil import copyfile
import os, sys, stat
import time
import wyborOpcjiGeneratora
from menuBaza import Menu_wyswietl2, Menu_wybor_opcji1
import wyswietlacz

def UtworzNowaBaze():
    """
    Tworzenie nowej bazy danych
    z wykonaniem sprawdzenia, czy baza już
    nie została wcześniej stworzona funkcja
    SprawdzenieCzyIsntniejeBaza
    :return:
    """
    wynik_sprawdzenia = SprawdzenieCzyIsntniejeBaza()
    if SprawdzenieCzyIsntniejeBaza():
        UtworzBaze()  # tu bedziemy tworzyć nową baze
    else:
        UsunBaze()  # a tu będzie procedura upewniająca ze chcesz usunac starą bazę i tworząca kopie bezpieczeństwa starej bazy
    mainBaza.Baza()


def SprawdzenieCzyIsntniejeBaza():
    """
    Sprawdzanie, czy plik bazy danych już istnieje.
    :return:
    """
    try:  # sprawdzanie czy baza już istnieje
        baza = open("baza_glowna.db", "r")
        baza.close()
        return False  # zwraca false gdy baza istnieje
    except FileNotFoundError:
        return True  # jak bazy nie mam zwraca True


def UtworzBaze():
    """
    Mechanizm tworzenia czystej bazy danych.
    :return:
    """
    # print("ok tworzymy baze wirtualnie poniewaz parcujemy na razie i nie trzeba nam 200 baz :) ")
    con = sqlite3.connect("baza_glowna.db")
    con.row_factory = sqlite3.Row  # ustawia parametr row_factory w celu umozliwienia dostępu do kolumny nie tylko po indekise ale tez po nazwie
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Sejf")  # jeśli istnieje usuń
    con.commit()
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE Sejf (id INTEGER PRIMARY KEY ASC, Rodzaj_hasła varchar(20) NOT NULL, Login varchar(40) NOT NULL, 
        Hasło varchar(40) NOT NULL, Adres varchar(250) NOT NULL, Data_utworzenia DATE NOT NULL, Dodatkowy_opis varchar(250))""")

    con.close()
    print("Utworzono nową bazę danych ! \n")


def UsunBaze():
    """
    Funkcja usuwająca bazę danych na żądanie użytkownika
    jednocześnie zapobiegająca przypadkowemu usunięciu bazy, przez
    zastosowanie dodatkowego pytania, oraz w przypadku decyzji na usunięcie
    tworząca kopię zapasową kasowanej bazy o nazwie pliku 'zabezpieczenie_bazy(data i godzina usunięcia).db
    :return:
    """
    print("\n\n")
    print("!!! UWAGA !!! baza juz istnieje !!!! ale ja skasujemy i utworzymy kopię bezpieczenstwa jeśli się upierasz.")
    print(
        "nadpisaną bazę znajdziesz w katalogu głównym aplikacji pod nazwą  ' zabezpieczenie_bazy + aktuany czas.db',\n ")
    print("\n\n")
    wybor = str.upper(input("Czy jesteś pewien tego kroku ? : (T/N)"))
    match wybor:
        case "T":
            dodatek = time.strftime("%d_%H_%M_%S", time.localtime())
            zabezpieczony = "zabezpieczenie_bazy" + dodatek + ".db"

            # copyfile("baza_glowna.db", zabezpieczony)
            # print("wirtualne nadpisanie opcja w celach testowych wylaczona")

            print()
            print(" BAZA ZOSTAŁA NADPISANA !\n")
            UtworzBaze()
        case "N":
            print("\n\n")
            print("Ok ! Baza nie nadpisana!\n")

            return


def WyswietlBaze():
    """
    Funkcja realizująca wyświetlanie rekordów bazy danych.
    :return:
    """
    wynik = SprawdzenieCzyIsntniejeBaza()
    if wynik:
        print(" Baza nie istnieje, utwórz najpierw bazę!\n")
        mainBaza.Baza()
    else:
        print("tu bedziemy wyświetlac baze\n")
        Menu_wyswietl2()
        wybor=Menu_wybor_opcji1()
        match wybor:
            case "1":
                wyswietlacz.Cała()
                WyswietlBaze()
            case "2":
                wyswietlacz.WyszukajWWW()
                WyswietlBaze()
            case "3":
                wyswietlacz.WyszukajMail()
                WyswietlBaze()
            case "4":
                wyswietlacz.WyszukajNieokreslone()
                WyswietlBaze()
            case "5":
                wyswietlacz.WyszukajLogin()
                WyswietlBaze()
            case "6":
                wyswietlacz.WyszukajOpis()
                WyswietlBaze()
            case "7":
                wyswietlacz.WyszukajData()
                WyswietlBaze()
            case "8":
                mainBaza.Baza()
            case other:
                print("nie dokonano właściwego wyboru\n")
                return

        mainBaza.Baza()


def MenuDodajWpis():
    """
    Zbieranie parametrówi przekkazanie ich do funkcji samego dodawania.
    Poszczególne operacje:
    podawanie rodzaju wpisu, walidacja tego rodzaju, pytanie o hasło (generowanie, wpisanie czy wklejenie),
    podawanie loginu przypisanego do hasła, adresu usługi i ewentualnie opisu, w przypadku braku opisu, wstawiany jest ciąg
    'brak opisu' w pole opisu.
    :return:
    """
    print("Dodawanie wpisu do bazy danych\n")
    rodzaj_wpisu = ""
    wybor = input("Jaki to rodzaj hasła ? \n"
                  "1-Strona WWW\n"
                  "2-Usługa Email\n"
                  "3-Inne hasło\n"
                  "4-Rezygnuję\n")
    Wybory(wybor)
    match wybor:
        case "1":
            rodzaj_wpisu = "Usługa WWW"

        case "2":
            rodzaj_wpisu = "Usługa Email"

        case "3":
            rodzaj_wpisu = "Inne"

        case "4":
            print("Przerwane !!\n")
            mainBaza.Baza()
        case other:
            return

    match rodzaj_wpisu:
        case ("Usługa WWW"):  # zalezności od wyboru rodzaju wpis ( czy strona www czy email czy haslojawne typu inne odpowiedni wybór dla pola adres
            adres = walidacjeDlaBazyDanych.SprawdzWWW()

        case ("Usługa Email"):

            adres = walidacjeDlaBazyDanych.SprawdzMaila()

        case other:
            adres = "Usługa niezdefiniowana"

    loginJawny = walidacjeDlaBazyDanych.SprawdzLogin()

    klucz=Klucz()
    login=Szyfrowanie(loginJawny,klucz)

    haslojawne = ""
    wybor = input("hasło wpisujesz sam czy chcesz wygenerować ?\n"
                  "1-Wygeneruj\n"
                  "2-Wpiszę sam!\n"
                  "3-Wklej ze schowka\n"
                  "4-Przerwij!\n")

    Wybory(wybor)
    match wybor:
        case "1":
            wyborOpcjiGeneratora.Wybor()
            haslojawne = pyperclip.paste()
            haslo = Szyfrowanie(haslojawne, klucz)

        case "2":
            haslojawne = input("Wpisz swoje hasło:\n")
            haslo = Szyfrowanie(haslojawne, klucz)
        case "3":
            haslojawne = pyperclip.paste()
            haslo = Szyfrowanie(haslojawne, klucz)

        case "4":
            print("przerwane !!\n")
            mainBaza.Baza()
        case other:
            return


    opis = input("Jeśli chcesz umieścic dodatkowy opis to tutaj:\n"
                 "jeśli niechcesz opisu lub skończysz pisac nacisnij ENTER.")
    if opis == "":
        opis = "brak opisu"

    DodawanieWpisu(rodzaj_wpisu, login, haslo, adres, opis)


def DodawanieWpisu(rodzaj_wpisu, login, haslo, adres, opis):
    """
    Procedura dodawania nowego wpisu do bazy danych na podstawie wygenerowanych
     i pobranych danych z funkcji MenuDodajWpis
  .
    :param rodzaj_wpisu:
    :param login:
    :param haslo:
    :param adres:
    :param opis:
    :return:
    """
    data = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    con = sqlite3.connect("baza_glowna.db")
    con.row_factory = sqlite3.Row  # ustawia parametr row_factory w celu umozliwienia dostępu do kolumny nie tylko po indekise ale tez po nazwie
    cur = con.cursor()
    cur.execute('INSERT INTO Sejf VALUES(NULL, ?, ?, ?, ?, ?, ?);', (rodzaj_wpisu, login, haslo, adres, data, opis))
    con.commit()


def Wybory(wybor):
    """
    Obsługuje wszystkie menu tworzenia nowego wpisu w bazie danych.
    :param wybor:
    :return:
    """

    match wybor:
        case "1":
            wybor = "1"
            return wybor
        case "2":
            wybor = "2"
            return wybor
        case "3":
            wybor = "3"
            return wybor
        case "4":
            wybor = "4"
            return wybor

        case other:
            print("nie dokonano właściwego wyboru\n")
            MenuDodajWpis()