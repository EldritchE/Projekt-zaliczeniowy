"""

Wszystkie funkcje do operacji na bazie danych

"""
from shutil import copyfile

from .szyfrowanie import Klucz, Deszyfruj, Szyfrowanie
from . import walidacjeDlaBazyDanych
import pyperclip
import sqlite3
from . import mainBaza
import time
from . import wyborOpcjiGeneratora
from .menuBaza import Menu_wyswietl2, Menu_wybor_opcji1
from . import wyswietlacz
import re
from .koloruj import color_text
from .daneBazy import SciezkaBazyGlownej


class ZlaWarotsc(Exception):
    pass


def Menu_wybor_opcji_kasowanie():
    """
    Funkcja realizująca wybory użytkownika z walidacją tych wyborów.
        :return:
    """
    wybor = input("Dokonaj wyboru(1,2 lub 3)")
    match wybor:
        case "1":
            # print("wybrano 1")
            return wybor
        case "2":
            # print("wybrano 2")
            return wybor
        case "3":
            # print("wybrano 3")
            return wybor
        case other:
            print(color_text('red', 'nie dokonano właściwego wyboru\n'))
            Menu_wybor_opcji_kasowanie()


def Menu_wyswietl_kasowanie():
    """
    Wyświetlanie Menu kasowania wpisu.
    :return:
    """
    print(color_text("blue", "Baza Danych"))
    print(color_text("yellow", "Dostępne opcje Kasowania wpisu:"))
    print("--" * 10)
    print("1 - Skasuj wpis po znanym ID")
    print("2 - Wyszukaj wpis do skasowania ")
    print("3 - Wróć do Menu Bazy danych ")
    print("\n\n")

    return


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
        UsunBaze()  # A tu będzie procedura upewniająca ze chcesz usunac starą bazę i tworząca kopie bezpieczeństwa starej bazy.
    mainBaza.Baza()


def SprawdzenieCzyIsntniejeBaza():
    """
    Sprawdzanie, czy plik bazy danych już istnieje.
    :return:
    """
    try:  # sprawdzanie, czy baza już istnieje
        baza = open(SciezkaBazyGlownej(), "r")
        baza.close()
        return False  # zwraca False, gdy baza istnieje
    except FileNotFoundError:
        return True  # jak bazy nie mam zwraca True


def UtworzBaze():
    """
    Mechanizm tworzenia czystej bazy danych.
    :return:
    """
    # print("ok tworzymy baze wirtualnie poniewaz parcujemy na razie i nie trzeba nam 200 baz :) ")
    con = sqlite3.connect(SciezkaBazyGlownej())
    con.row_factory = sqlite3.Row  # ustawia parametr row_factory w celu umozliwienia dostępu do kolumny nie tylko po indekise ale tez po nazwie
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Sejf")  # jeśli istnieje usuń
    con.commit()
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE Sejf (id INTEGER PRIMARY KEY ASC, Rodzaj_hasła varchar(20) NOT NULL, Login varchar(40) NOT NULL, 
        Hasło varchar(40) NOT NULL, Adres varchar(250) NOT NULL, Data_utworzenia DATE NOT NULL, Dodatkowy_opis varchar(250))""")

    con.close()
    print(color_text('green', 'Utworzono nową bazę danych ! \n'))


def UsunBaze():
    """
    Funkcja usuwająca bazę danych na żądanie użytkownika
    jednocześnie zapobiegająca przypadkowemu usunięciu bazy, przez
    zastosowanie dodatkowego pytania, oraz w przypadku decyzji na usunięcie
    tworząca kopię zapasową kasowanej bazy o nazwie pliku 'zabezpieczenie_bazy(data i godzina usunięcia).db
    :return:
    """
    print("\n\n")
    print(color_text('red',
                     '!!! UWAGA !!! baza juz istnieje !!!! ale ja skasujemy i utworzymy kopię bezpieczenstwa jeśli się upierasz.'))
    print(
        "nadpisaną bazę znajdziesz w katalogu głównym aplikacji pod nazwą  ' zabezpieczenie_bazy + aktuany czas.db',\n ")
    print("\n\n")
    wybor = str.upper(input("Czy jesteś pewien tego kroku ? : (T/N)"))
    match wybor:
        case "T":
            dodatek = time.strftime("%d_%H_%M_%S", time.localtime())
            zabezpieczony = "zabezpieczenie_bazy" + dodatek + ".db"

            copyfile(SciezkaBazyGlownej(), zabezpieczony)
            print("wirtualne nadpisanie opcja w celach testowych wylaczona")

            print()
            print(color_text('red', ' BAZA ZOSTAŁA NADPISANA !\n'))
            UtworzBaze()
        case "N":
            print("\n\n")
            print(color_text('green', 'Ok ! Baza nie nadpisana!\n'))

            return


def Powrot(wywolanie):
    """
    # warunek powrotu do poprzedniej funkcji w zależności skąd została wywołana 1 Głowne menu Bazy
    # 2 z menu kasowania wpisu powtórzone przy każdym case
    :param wywolanie:
    :return:
    """
    if wywolanie == 1:
        WyswietlBaze(0)
    else:
        SkasujWpisMenu()


def WyswietlBaze(wywolanie):
    """
    Funkcja realizująca wyświetlanie rekordów bazy danych.
    :return:
    """
    wynik = SprawdzenieCzyIsntniejeBaza()
    if wynik:
        print(color_text('red', ' Baza nie istnieje, utwórz najpierw bazę!\n'))
        mainBaza.Baza()
    else:

        Menu_wyswietl2()
        wybor = Menu_wybor_opcji1()
        match wybor:
            case "1":
                wyswietlacz.Cala()
                Powrot(wywolanie)
            case "2":
                param = input("Wpisz jakiego serwisu WWW szukamy(Enter dla wszystkich wpisów WWW): ")
                wyswietlacz.WyszukajWWW(param)
                Powrot(wywolanie)
            case "3":
                param = input("Wpisz jakiego serwisu Email szukamy(Enter dla wszystkich wpisów Email): ")
                wyswietlacz.WyszukajMail(param)
                Powrot(wywolanie)
            case "4":
                wyswietlacz.WyszukajNieokreslone()
                Powrot(wywolanie)
            case "5":
                control = True  # sprawdzenie, czy login może być w bazie. Walidacja taka sama jak przy wpisywaniu.
                while control:
                    try:
                        string = input("Wpisz jakiego loginu szukamy: ")
                        x = re.search(r"^[a-zA-Z_\-]+$", string)  # regex dla ciągu ze spacją
                        if x:
                            print(color_text('green', 'prawidłowy\n'))
                            control = False
                        else:
                            raise ZlaWarotsc()
                    except ZlaWarotsc:
                        print(color_text('red', 'Login posiada niedopuszczalny znak  podaj jeszcze raz: \n'))
                wyswietlacz.WyszukajLogin(string)
                Powrot(wywolanie)
            case "6":
                param = input("Jakiego wyrażenia szukamy w opisie: ")
                wyswietlacz.WyszukajOpis(param)
                Powrot(wywolanie)
            case "7":
                control = True
                while control:
                    try:
                        print("wpisanie:2022-12 wyświetli wszystkie wpisy dla grudnia 2022")
                        param = input("Podaj datę(yyyy-mm-dd) powstania wpisu :\n")
                        print()
                        x = re.search(
                            r"^([0-9]{4}((-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]))|(-(0[1-9]|1[0-2]))$))$",
                            param)  # regex dla daty która zaweira rok i mniesiąc lub rok miesiać i dzien
                        if x:
                            control = False
                        else:
                            raise ZlaWarotsc()
                    except ZlaWarotsc:
                        print(color_text('red', 'Prawidłowy format wpisu to yyyy-mm  lub yyyy-mm-dd \n'))
                wyswietlacz.WyszukajData(param)
                Powrot(wywolanie)
            case "8":
                mainBaza.Baza()
            case other:
                print(color_text('red', 'nie dokonano właściwego wyboru\n'))
                return
    return



def MenuDodajWpis():
    """
    Zbieranie parametrów i przekkazanie ich do funkcji samego dodawania.
    Poszczególne operacje:
    podawanie rodzaju wpisu, walidacja tego rodzaju, pytanie o hasło (generowanie, wpisanie czy wklejenie),
    podawanie loginu przypisanego do hasła, adresu usługi i ewentualnie opisu, w przypadku braku opisu, wstawiany jest ciąg
    'brak opisu' w pole opisu.
    :return:
    """
    print(color_text("blue", "Baza Danych"))
    print(color_text("yellow", "Dodawanie wpisu do bazy danych\n"))

    rodzaj_wpisu = ""
    wybor = input("Jaka to usługa ? \n"
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
            print(color_text('red', 'przerwane !!\n'))
            mainBaza.Baza()
            return

    match rodzaj_wpisu:
        case ("Usługa WWW"):  # zalezności od wyboru rodzaju wpis ( czy strona www czy email czy haslojawne typu inne odpowiedni wybór dla pola adres
            adres = walidacjeDlaBazyDanych.SprawdzWWW()

        case ("Usługa Email"):

            adres = walidacjeDlaBazyDanych.SprawdzMaila()

        case other:
            adres = "Usługa niezdefiniowana"

    loginJawny = walidacjeDlaBazyDanych.SprawdzLogin()

    klucz = Klucz()
    login = Szyfrowanie(loginJawny, klucz)

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
            print(color_text('red', 'przerwane !!\n'))
            mainBaza.Baza()
            return

    opis = input("Jeśli chcesz umieścic dodatkowy opis to tutaj:\n"
                 "jeśli nie chcesz opisu lub skończysz pisać naciśnij ENTER.")

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

    con = sqlite3.connect(SciezkaBazyGlownej())
    con.row_factory = sqlite3.Row  # ustawia parametr row_factory w celu umozliwienia dostępu do kolumny nie tylko po indekise ale tez po nazwie
    cur = con.cursor()
    cur.execute('INSERT INTO Sejf VALUES(NULL, ?, ?, ?, ?, ?, ?);', (rodzaj_wpisu, login, haslo, adres, data, opis))
    con.commit()  # wykonanie
    con.close()  # zamknięcie bazy


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
            print(color_text('red', 'nie dokonano właściwego wyboru\n'))
            MenuDodajWpis()


def SkasujWpisMenu():
    Menu_wyswietl_kasowanie()
    wybor = Menu_wybor_opcji_kasowanie()
    match wybor:
        case "1":
            try:
                kasowane = int(input("Podaj ID kasowanego wpisu :\n"))
            except ValueError:
                print (color_text('red',"To nie jest prawidłowe ID"))
                print("\n")
                SkasujWpisMenu()
            con = sqlite3.connect(SciezkaBazyGlownej())  # procedury otwarcia bazy danych ustawienia kursora
            cur = con.cursor()
            wyszukiwanie = f"SELECT * from Sejf where id= {kasowane}"

            sqlite_select_query = wyszukiwanie
            cur.execute(sqlite_select_query)
            records = cur.fetchall()
            if records == []:
                print("\n", color_text('red', "Nie ma wpisu o takim ID, nic nie zostanie skasowane!\n "))
            for row in records:
                print(color_text('red', "Wpis do skasowania !"))
                print('-' * 36)
                print("ID: ", row[0])
                print('-' * 36)
                print("Usługa: ", color_text('red', row[1]))
                print("Login: ", color_text('green', Deszyfruj(row[2])))
                print("Hasło: ", color_text('magenta', Deszyfruj(row[3])))
                print("Adres usługi: ", color_text('yellow', row[4]))
                print("Data utworzenia: ", row[5])
                print("Dodatkowy opis: ", color_text('blue', row[6]))
                print(color_text('red', "-------------------------------------------"))
                print(color_text('red', "Czy jesteś pewien,że chcesz to usunąć ? !!"))
                print(color_text('red', "------------------------------------------"))
                print("\n\n")

                decyzja = input("T/N\n").upper()
                if decyzja == "N":
                    print("\n")
                    print(color_text('green', "Wpis nie został Usunięty !\n"))
                    SkasujWpisMenu()
                elif decyzja == "T":
                    print("\n")
                    kasowany = f"DELETE FROM Sejf WHERE id={kasowane}"
                    print(f"Wpis o ID = {kasowane}")
                    print(color_text('red', "Został bezpowrotnie usuniety!\n\n"))
                    cur.execute(kasowany)
                    con.commit()  # wykonanie
                    con.close()  # zamknięcie bazy
                else:
                    print(color_text('red', "Zły wybór !"))
            SkasujWpisMenu()

        case "2":
            wywolanie = 2
            WyswietlBaze(wywolanie)
