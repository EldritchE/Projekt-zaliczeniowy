"""
---------------------------------
Główny moduł obsługi bazy danych.
--------------------------------
Zawiera funkcje realizującą wyboru użytkownika
w funkcji Baza.
Wywołuje wyświetlanie Menu obsługi bazy danych i
realizuje odwołania do poszczególnych działań na Bazie

"""
from menuBaza import Menu_wyswietl, Menu_wybor_opcji
from baza import UtworzNowaBaze, WyswietlBaze, MenuDodajWpis,SkasujWpisMenu


def Baza():
    """
    Wyświetlanie menu bazy danych z modułu 'menuBaza' funkcją Menu_Wyświetl
    otrzymana zmienna wybór jest walidowana w strukturze 'match - case'
    i następuje skok do wybranej funkcjonalności.
    :return:
    """
    Menu_wyswietl()
    wybor = Menu_wybor_opcji()
    match wybor:
        case "1":
            MenuDodajWpis()
        case "2":
            SkasujWpisMenu()
        case "3":
            wywolanie = 1
            WyswietlBaze(wywolanie)
        case "4":
            UtworzNowaBaze()
        case "5":
            pass
