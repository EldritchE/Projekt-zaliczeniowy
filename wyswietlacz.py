"""
Moduł odpowiadający za wyszukiwanie i wyświetlanie
z bazy danych
"""
import sqlite3
import pandas
import pandas as pd


def Cała():
    """Funkcja pobiera i wyświetla dane z calej  bazy."""
    con = sqlite3.connect("baza_glowna.db")

    cur = con.cursor()


    cur.execute(
        """
        SELECT Rodzaj_hasła,Login,Hasło,Adres,Data_utworzenia,Dodatkowy_opis FROM Sejf 
        """)
    wpisy = cur.fetchall()
    tabela = pd.DataFrame(wpisy)
    tabela.columns = 'Rodzaj Hasła', 'Login', 'Hasło', 'Adres', 'Data Utworzenia', 'Dodatkowy opis'
    print(tabela)
    # for wpis in wpisy:
    #
    #     print(wpis[0],"\t",wpis[1],"\t",wpis[2],"\t", wpis[3],"\t", wpis[4],"\t",wpis[5],"\t", wpis[6])
    # print()

    con.commit()
    con.close()



def WyszukajWWW():
    pass

def WyszukajMail():
    pass


def WyszukajNieokreslone():
    pass


def WyszukajLogin():
    pass


def WyszukajOpis():
    pass


def WyszukajData():
    pass


