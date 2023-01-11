"""
Moduł Menu obsługi bazy danych

Zawiera następujące funkcje:
Wyświetlanie menu
oraz moduł obsługujący wybory użytkownika, oraz ich walidację.

"""
import mainBaza
from koloruj import color_text


def Menu_wyswietl():
    """
    Wyświetlanie Menu Bazy danych.
    :return:
    """
    print(color_text("blue", "Baza Danych"))
    print(color_text("yellow", "Dostępne opcje Bazy Danych:"))
    print("--" * 10)
    print("1 - Dodaj nowy wpis do bazy zgromadzonych haseł i loginów")
    print("2 - Wyszukaj w bazie ")
    print("3 - Utwórz nową bazę danych (!!!)\n    ----!!!UAWAGA! w opcji 3 ryzyko nadpisania poprzedniej bazy!!!----")
    print("4 - Wróć do Menu głównego")
    print("\n\n")

    return


def Menu_wyswietl2():
    """
    Wyświetlanie Menu Bazy danych.
    :return:
    """
    print(color_text("blue", "Baza Danych"))
    print(color_text("yellow", "Dostępne opcje Wyświetlania:"))
    print("--" * 10)
    print("1 - Wyświetl całą bazę danych ")
    print("2 - Szukaj w adresach www")
    print("3 - Szukaj w adresach emial")
    print("4 - Szukaj w nieokreslonych")
    print("5 - Szukaj po loginie")
    print("6 - Szukaj po opisie ")
    print("7 - Szukaj po dacie utworzenia")
    print("8 - Wróć do Menu Bazy Danych")
    print("\n\n")

    return


def Menu_wybor_opcji1():
    """
    Funkcja realizująca wybory użytkownika z walidacją tych wyborów.
        :return:
    """
    wybor = input("Dokonaj wyboru(1,2,3,4,5,6,7, lub 8)\n")
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
        case "4":
            # print("wybrano 4")
            return wybor
        case "5":
            # print("wybrano 5")
            return wybor
        case "6":
            # print("wybrano 6")
            return wybor
        case "7":
            # print("wybrano 7")
            return wybor
        case "8":
            # print("wybrano 8")
            return wybor
        case other:
            print(color_text('red', 'nie dokonano właściwego wyboru\n'))
            Menu_wybor_opcji1()
    mainBaza.Baza()


def Menu_wybor_opcji():
    """
    Funkcja realizująca wybory użytkownika z walidacją tych wyborów.
        :return:
    """
    wybor = input("Dokonaj wyboru(1,2,3 lub 4)")
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
        case "4":
            # print("wybrano 4")
            return wybor
        case other:
            print(color_text('red', 'nie dokonano właściwego wyboru\n'))
            mainBaza.Baza()
