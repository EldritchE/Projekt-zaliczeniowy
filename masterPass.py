"""
Obsługa głównego hasła aplikacji.
Sprawdzanie po uruchomieniu aplikacji czy hasło główne istnieje,
jeśli nie, wymuszenie jego stworzenia,
możliwość zmiany hasła na nowe po podaniu starego,
w przypadku zagubienia hasła, seria pytań uwierzytelniających,
które umożliwią dostęp do aplikacji i reset hasła
"""

from koloruj import color_text
import sqlite3
from szyfrowanie import Szyfrowanie, Deszyfruj


class ZlaWarotsc(Exception):
    pass


class StringZamiastInt(Exception):
    pass


def pobierzHaslo():
    con = sqlite3.connect("p.db")
    con.row_factory = sqlite3.Row  # ustawia parametr row_factory w celu umozliwienia dostępu do kolumny nie tylko po indekise ale tez po nazwie
    cur = con.cursor()
    wyszukiwanie = """SELECT * From Mpassword WHERE Haslo not null"""
    sqlite_select_query = wyszukiwanie
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for oldpswdszyfr in records:
        oldpswdbaza = (Deszyfruj(oldpswdszyfr[1]))
    return oldpswdbaza


def sprawdzCzyZnaszHaslo():
    oldpswd = input("Hasło: ")
    con = sqlite3.connect("p.db")
    con.row_factory = sqlite3.Row  # ustawia parametr row_factory w celu umozliwienia dostępu do kolumny nie tylko po indekise ale tez po nazwie
    cur = con.cursor()
    wyszukiwanie = """SELECT * From Mpassword WHERE Haslo not null"""
    sqlite_select_query = wyszukiwanie
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for oldpswdszyfr in records:
        oldpswdbaza = (Deszyfruj(oldpswdszyfr[1]))
    if oldpswdbaza == oldpswd:
        print(color_text("green", "Uwierzytenienie ok\n"))
        return True
    else:
        return False


def sprawdzeniePytan():
    con = sqlite3.connect("p.db")
    con.row_factory = sqlite3.Row  # ustawia parametr row_factory w celu umozliwienia dostępu do kolumny nie tylko po indekise ale tez po nazwie
    cur = con.cursor()
    wyszukiwanie = """SELECT * From Mpassword """
    sqlite_select_query = wyszukiwanie
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for pobrane in records:
        pyt1 = (pobrane[2])
        odp1 = (Deszyfruj(pobrane[3]))
        pyt2 = (pobrane[4])
        odp2 = (Deszyfruj(pobrane[5]))
        print(color_text("cyan", "Pytanie 1:"))
    odpowiedz1 = input(pyt1 + "  :\n")
    if odp1 == odpowiedz1:
        print(color_text("green", "Odpowiedź prawidłowa!Jeszcze jedno pytanie!"))
    else:
        print(color_text("red", "Odpowiedź nie prawidłowa!nie możesz zmienić hasła!"))
        return False
    print(color_text("cyan", "Pytanie 2:"))
    odpowiedz2 = input(pyt2 + "  :\n")
    if odp2 == odpowiedz2:
        print(color_text("green", "Odpowiedź prawidłowa!Możesz zmienić hasło !"))
        return True
    else:
        print(color_text("red", "Odpowiedź nieprawidłowa! Nie możesz zmienić hasła!"))
        return False


def DodawanieWpisu(pswd, pyt1, odp1, pyt2, odp2):
    """
    Procedura dodawania nowego wpisu do bazy danych na podstawie wygenerowanych
     i pobranych danych z funkcji MenuDodajWpis
  .
    :param rodzaj_wpisu:
    :param login:
    :param haslo:
    :param opis:
    :return:
    """

    nowyPlikHasla()
    con = sqlite3.connect("p.db")
    con.row_factory = sqlite3.Row  # ustawia parametr row_factory w celu umozliwienia dostępu do kolumny nie tylko po indekise ale tez po nazwie
    cur = con.cursor()

    cur.execute('INSERT INTO Mpassword VALUES(NULL, ?, ?, ?, ?, ?);', (pswd, pyt1, odp1, pyt2, odp2))
    con.commit()  # wykonanie


def budujHaslo():
    print("\n(hasło składa się z przynajmniej 4 znaków!)\n"
          "mozesz wykorzystać wcześniej wygenerowane hasło zapisane w schowku systemowym ")
    pswd = input("Podaj Nowe hasło główne: \n")
    if len(pswd) < 4:
        print(color_text("red", "podane hasło jest za krótkie!(min 4 znaki)"))
        budujHaslo()
    else:
        pswd2 = input("powtórz hasło.\n")
        if pswd == pswd2:
            print("podane hasło pasują \n")
            #     budowa pytan weryfikujących
            pyt1 = input(
                "Podaj pytanie sprawdzające 1, na które tylko ty znasz odpowiedź,\n będzie użyte do weryfikacji w przypadku zagubienia hasła: \n")
            odp1 = input("odpowiedź: \n")
            pyt2 = input(
                "Podaj pytanie sprawdzające 2, na które tylko ty znasz odpowiedź,\n będzie użyte do weryfikacji w przypadku zagubienia hasła: \n")
            odp2 = input("odpowiedź: \n")
            #     zapisanie hasła, pytań sprawdzających, odpowiedzi do bazy ( hasło i odpowiedzi są szyfrowane modułem szyfrowania)

            DodawanieWpisu(Szyfrowanie(pswd), pyt1, Szyfrowanie(odp1), pyt2, Szyfrowanie(odp2))
        else:
            print(color_text("red", "Podane hasła nie pasują do siebie ! Powtórz wprowadzanie hasła(ENTER)\n "))
            input()
            budujHaslo()
    return


def czyJestHaslo():
    """
        Sprawdzanie, czy plik hasła głównego już istnieje.
        :return:
        """
    try:  # sprawdzanie, czy baza już istnieje
        baza = open("p.db", "r")
        baza.close()
        return False  # zwraca False, gdy baza istnieje
    except FileNotFoundError:
        print(color_text("red", "\nBrak Hasła głównego\n"))
        input("Wciśnij ENTER, aby stworzyć hasło główne")
        return True  # jak bazy nie mam zwraca True
    pass


def nowyPlikHasla():
    con = sqlite3.connect("p.db")
    con.row_factory = sqlite3.Row  # ustawia parametr row_factory w celu umozliwienia dostępu do kolumny nie tylko po indekise ale tez po nazwie
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Mpassword")  # jeśli istnieje usuń
    con.commit()
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE Mpassword (id INTEGER PRIMARY KEY ASC, Haslo varchar(40) NOT NULL, pyt1 varchar(250) NOT NULL, 
        odp1 varchar(250) NOT NULL, pyt2 varchar(250) NOT NULL, odp2 varchar(250) NOT NULL)""")

    con.close()

    print(color_text('green', 'utworzono hasło główne ! ! \n'))

    pass


def mPassword():
    wynik_sprawdzenia = czyJestHaslo()
    if wynik_sprawdzenia:
        budujHaslo()  # tu będziemy tworzyć nową bazę z master password i polami pytań uwierzytelniających
    else:
        print("\n\n")
        print(color_text("blue", "Menu Master Password"))
        print(color_text("green", "Dostępne opcje:"))
        print("--" * 10)
        print("1 - Zmień Hasło główne")
        print("2 - Zapomniałem hasła")
        print("3 - Powrót do Menu głównego")
        print("\n\n")
        wybor = 0
        while wybor not in range(1, 4):
            try:  # walidacja właściwego wyboru w menu
                wybor = int(input("Dokonaj wyboru(1,2 lub 3)"))
                if wybor < 1 or wybor > 3:
                    raise ZlaWarotsc()
            except ValueError:
                print("wybór powinien być cyfrą!!")
            except ZlaWarotsc:
                print(f"Niewłaściwy wybór {wybor} nie ma takiej opcji w menu!!")
        match wybor:
            case 1:
                if sprawdzCzyZnaszHaslo() == True:
                    print(color_text("magenta", "Znasz hasło! Zmieniamy na nowe"))
                    budujHaslo()
                    print(color_text("green", "Główne hasło zostało zmienione!"))
                else:
                    print(color_text("red", "\nNIE ZNASZ POPRZEDNIEGO HASŁA ! Nie mozesz dokonać jego zmiany. "
                                            "\nJeśłi zapomiałeś hasła  skorzystaj z opcji odzyskiwania."))
                    mPassword()
            case 2:
                if sprawdzeniePytan() == True:
                    budujHaslo()
                else:
                    mPassword()
            case 3:
                return

            case other:
                mPassword()
    return
