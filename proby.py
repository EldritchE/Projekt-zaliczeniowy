"""
Plik to testowania podręcznych rozwiązań :)
"""

import sqlite3 # importujemy moduł sqlite3 do obsługi baz SQLite3
# utworzenie połączenia z bazą przechowywaną
# na dysku w katalogu(C:\Users\wojciech.moszczynski\PycharmProjects)
# lub w pamięci (':memory:')
con = sqlite3.connect('hotelEwa.db')
con.row_factory = sqlite3.Row
cur = con.cursor()
# instrukcja ustawia właściwość row_factory na wartość sqlite3.Row,
# aby możliwy był dostęp do kolumn (pól tabel) nie tylko przez
# indeksy, ale również przez nazwy. Jest to bardzo przydatne
# podczas odczytu danych.
# dostęp do kolumn przez indeksy i przez nazwy
# Aby móc wykonywać operacje na bazie,
# potrzebujemy obiektu tzw. kursora, tworzymy go poleceniem cur=
# utworzenie obiektu kursora
# I tyle potrzeba, żeby rozpocząć pracę z bazą ######
# Teraz baza jest pusta, bez tabel
##### TWORZENIE TABEL W PUSTEJ BAZIE #####
cur.execute("DROP TABLE IF EXISTS pokoje;")
cur.execute("""
    CREATE TABLE IF NOT EXISTS pokoje (
        id INTEGER PRIMARY KEY ASC,
        numer_pokoju number(2,0) NOT NULL,
        rodzaj_pokoju varchar(20) DEFAULT ''
    )""")
# Powyższe polecenia SQL-a tworzą trzy tabele.
# Tabela “pokoje” przechowuje numer i rodzaj pokoju.
# do każdego pokoju może być przypisanych wielu gości hotelowych.
# tabela “goście” zawiera pola przechowujące imię i nazwisko
# gościa oraz identyfikator pokoju hotelowego (pole “pokoje_id”, tzw. klucz obcy),
# do której przypisany jest gość.
# typ danych w bazie Number(P,S)
# P oznacza ilość cyfr w całej liczbie,
# S oznacza ilość miejsc po przecinku.
cur.executescript("""
    DROP TABLE IF EXISTS goście;
    CREATE TABLE IF NOT EXISTS goście (
        id INTEGER PRIMARY KEY ASC,
        imie varchar(250) NOT NULL,
        nazwisko varchar(250) NOT NULL,
        pokoje_id INTEGER NOT NULL,
        FOREIGN KEY(pokoje_id) REFERENCES pokoje(id)
    )""")
# ZOSTAŁY UTWORZONE PUSTE TABELE klasa i uczeń
# Po wykonaniu wprowadzonego kodu w katalogu w bazie hotelEwa.db
# teraz tworze tabelę terminów, w których pokoje były wynajmowane
cur.executescript("""
    DROP TABLE IF EXISTS daty;
    CREATE TABLE IF NOT EXISTS daty (
        id INTEGER PRIMARY KEY ASC,
        data_pocz date NOT NULL,
        data_koniec date NOT NULL,
        pokoje_id INTEGER NOT NULL,
        FOREIGN KEY(pokoje_id) REFERENCES pokoje(id)
    )""")
#### WSTAWIANIE DANYCH DO BAZY ##########
# wstawiamy PIERWSZE rekordy danych do tabeli pokoje (rekordy: numer i profil)

cur.execute('INSERT INTO pokoje VALUES(NULL, ?, ?);', ('2', 'jedynka'))
cur.execute('INSERT INTO pokoje VALUES(NULL, ?, ?);', ('3', 'dwójka'))
cur.execute('INSERT INTO pokoje VALUES(NULL, ?, ?);', ('4', 'dwójka'))
cur.execute('INSERT INTO pokoje VALUES(NULL, ?, ?);', ('5', 'trójka'))
cur.execute('INSERT INTO pokoje VALUES(NULL, ?, ?);', ('6', 'jedynka'))
cur.execute('INSERT INTO pokoje VALUES(NULL, ?, ?);', ('7', 'trójka'))
# wykonujemy zapytanie SQL, które pobierze id pokoju "1" z tabeli "pokoje".
cur.execute('SELECT id FROM pokoje WHERE numer_pokoju = ?', ('1',))
pokoje_id = cur.fetchone()[0]
# wypełnianie tabeli goście
# "goście_hotelu" zawiera tuple z danymi poszczególnych uczniów
# Wartość NULL w poleceniach SQL-a i None w tupli z danymi gości
# odpowiadające kluczom głównym umieszczamy po to, aby baza danych
# utworzyła je automatycznie. Można by je pominąć, ale wtedy w poleceniu
# wstawiania danych musimy wymienić nazwy pól, np.
goście_hotelu = (
    (None, 'Tomasz', 'Pająk', 1),
    (None, 'Jan', 'Boniecki', 4),
    (None, 'Piotr', 'Kalisiak', 7),
    (None, 'Ewa', 'Szpada', 5),
    (None, 'Darek', 'Kopacz', 6),
    (None, 'Piotr', 'Błacha', 3),
    (None, 'Jan', 'Ropa', 4),
    (None, 'Stanisław','Hammer', 3),
    (None, 'Aleksandra','Kmieć', 5),
)
cur.executemany('INSERT INTO goście VALUES(?,?,?,?)', goście_hotelu)
# kiedy jest pokoje_id to domyślnie wstawia się 1, ponieważ nie znamy numeru pokoju
# wstawiamy rekordy z tupli goście_hotelowi do tabeli goście
# wstawiania danych musimy wymienić nazwy pól, np.
# Data w formacie YYYY-MM-DD, gdzie YYYY to rok, MM to miesiąc, DD to dzień.
# wypełniamy kolejną tabelę z datami w których były wynajmowane pokoje
terminy = (
    (None, '2018-5-22', '2018-5-23', 1),
    (None, '2018/5/20', '2018/5/22', 4),
    (None, '2018/5/20', '2018/5/24', 3),
    (None, '2018/5/18', '2018/5/20', 3),
    (None, '2018/5/18', '2018/5/20', 4),
    (None, '2018/5/18', '2018/5/19', 5),
    (None, '2018/5/21', '2018/5/23', 6),
    (None, '2018/5/20', '2018/5/22', 7),
)
cur.executemany('INSERT INTO daty VALUES(?,?,?,?)', terminy)
# zatwierdzamy zmiany w bazie
con.commit()
############## POBIERANIE DANYCH ###################
# pobieranie danych z bazy czyli DRUKOWANIE
# Pobieranie danych (czyli kwerenda) wymaga polecenia SELECT języka SQL.
# Definiujemy własną funkcję czytajdane() która wykonuje
# zapytanie SQL pobierające wszystkie dane
# z dwóch powiązanych tabel: “goście”, “pokoje” .
## Na zielono i w potrójnych cudzysłowach są orginalne zapytania SQL
print("Goście hotelowi wg pokojów")
def czytajdane():
    """Funkcja pobiera i wyświetla dane z bazy."""
    cur.execute(
        """
        SELECT goście.id,imie,nazwisko,numer_pokoju FROM goście,pokoje 
        WHERE goście.pokoje_id=pokoje.id
        """)
# rekordy zwrócone przez metodę .fetchall(), zapisujemy w
# zmiennej goście w postaci tupli
# odczytujemy w pętli for jako listę goście_hotelu
    goście_hotelu = cur.fetchall()
    for goście in goście_hotelu:
        print(goście['id'], goście['imie'], goście['nazwisko'], goście['numer_pokoju'])
    print()
czytajdane() # Instrukcja uruchamia drukowanie zgodnie z funkcją czytajdane()
# wynik zapytania to wszystkie trzy osoby z tupli 'goście'
def czytajDATY():
    """Funkcja pobiera i wyświetla dane z bazy."""
    cur.execute(
        """
        SELECT daty.id,data_pocz,data_koniec FROM daty 
        """)
# rekordy zwrócone przez metodę .fetchall(), zapisujemy w
# zmiennej goście w postaci tupli
# odczytujemy w pętli for jako listę goście_hotelu
    print("WYDRUK DAT POBYTU")
    daty_hotelu = cur.fetchall()
    for daty in daty_hotelu:
        print(daty['id'], daty['data_pocz'], daty['data_koniec'])
    print()
czytajDATY()# Instrukcja uruchamia drukowanie zgodnie z funkcją czytajdane()
########## Modyfikacja i usuwanie danych #######################
# zmiana pokoju gościa o identyfikatorze 2
cur.execute('SELECT id FROM pokoje WHERE numer_pokoju = ?', ('2',))
pokoje_id = cur.fetchone()[0]
cur.execute('UPDATE goście SET pokoje_id=? WHERE id=?', (pokoje_id, 2))
# zmieniono pokój drugiego goscia w bazie
# przekazywane w tupli (zwróć uwagę na dodatkowy przecinek(!))
# usunięcie gościa o identyfikatorze 3
cur.execute('DELETE FROM goście WHERE id=?', (3,))
czytajdane()
cur.close() # Na koniec zamykamy połącznie z bazą
            # dzięki czemu zapisujemy dokonane zmiany i
            # zwalniamy zarezerwowane przez skrypt zasoby.