"""
Obsługa głównego hasła aplikacji.
Sprawdzanie po uruchomieniu aplikacji czy hasło główne istnieje,
jeśli nie wymuszenie jego stworzenia,
możliwość zmiany hasła na nowe po podaniu starego,
w przypadku zagubienia hasła, seria pytań uwierzytelniających,
które umożliwią dostęp do aplikacji i reset hasła
"""

from koloruj import color_text
import sqlite3

def budujHaslo():
    print("\n(hasło składa się z przynajmniej 4 znaków!)\n"
          "mozesz wykorzystać wcześniej wygenerowane hasło zapisane w schowku systemowym ")
    pswd=input("Podaj Nowe hasło główne: \n")
    if len(pswd)<4:
        print (color_text("red","podane hasło jest za krótkie!(min 4 znaki)"))
        budujHaslo()
    else:
        pswd2=input("powtórz hasło.\n")
        if pswd==pswd2:
            print ("podane hasło pasują \n")
        else:
            print(color_text("red","Podane hasła nie pasują do siebie ! Powtórz wprowadzanie hasła(ENTER)\n "))
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
        print (color_text("red","\nBrak Hasła głównego\n"))
        input("Wciśnij ENTER, aby stworzyć hasło główne")
        return True  # jak bazy nie mam zwraca True
    pass

def nowyPlikHasla():
    budujHaslo()
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
        nowyPlikHasla()  # tu będziemy tworzyć nową bazę z master password i polami pytań uwierzytelniających
    else:
        print("jak jest juz haslo to dalej procedujemy")
    exit()