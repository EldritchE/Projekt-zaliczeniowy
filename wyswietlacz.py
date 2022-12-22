"""
Moduł odpowiadający za wyszukiwanie i wyświetlanie
z bazy danych
"""
import sqlite3
from szyfrowanie import Deszyfruj, Szyfrowanie

def WyświetlZadane(wyszukiwanie,wyroznienie=0):
    con = sqlite3.connect("baza_glowna.db")
    cur = con.cursor()

    sqlite_select_query = wyszukiwanie
    cur.execute(sqlite_select_query)
    records = cur.fetchall()


    for row in records:
        if wyroznienie==0:
            print('-'*36)
        print("Id: ", row[0])
        if wyroznienie==0:
            print('-' * 36)
        if wyroznienie==1:
            print('-' * 36)
        print("Rodzaj Hasła: ", row[1])
        if wyroznienie == 1:
            print('-' * 36)
        if wyroznienie == 2:
            print('-' * 36)
        print("Login: ", Deszyfruj(row[2]))
        if wyroznienie == 2:
            print('-' * 36)
        print("Hasło: ", Deszyfruj(row[3]))
        print("Adres usługi: ", row[4])
        print("Data utworzenia: ", row[5])
        print("Dodatkowy opis: ", row[6])
        print("\n")

    con.commit()
    con.close()
    print("Znaleziono:  ", len(records), " rekordów.")
    return

def Cała():
    """Funkcja pobiera i wyświetla dane z calej  bazy."""
    wyszukiwanie="SELECT * from Sejf "
    wyroznienie=0
    WyświetlZadane(wyszukiwanie,wyroznienie)
    return
def WyszukajWWW():
    """Funkcja pobiera i wyświetla dane dla serwisów WWW."""
    wyszukiwanie = "SELECT * from Sejf where Rodzaj_hasła='Usługa WWW'"
    wyroznienie = 1
    WyświetlZadane(wyszukiwanie, wyroznienie)
    return

def WyszukajMail():
    """Funkcja pobiera i wyświetla dane dla serwisów emailowych."""
    wyszukiwanie = "SELECT * from Sejf where Rodzaj_hasła='Usługa Email'"
    wyroznienie = 1
    WyświetlZadane(wyszukiwanie, wyroznienie)
    return


def WyszukajNieokreslone():
    """Funkcja pobiera i wyświetla dane dla serwisów nieokreślonych."""
    wyszukiwanie = "SELECT * from Sejf where Rodzaj_hasła='Inne'"
    wyroznienie = 1
    WyświetlZadane(wyszukiwanie, wyroznienie)
    return


def WyszukajLogin():
    """Funkcja pobiera i wyświetla dane dla podanego loginu."""
    login= Szyfrowanie(input("Podaj poszukiwany login: "))

    wyszukiwanie = f"SELECT * from Sejf where login='{login}'"
    WyświetlZadane(wyszukiwanie)
    wyroznienie = 2
    WyświetlZadane(wyszukiwanie, wyroznienie)
    return


def WyszukajOpis():
    pass


def WyszukajData():
    pass


