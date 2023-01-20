"""
Główny moduł programu.

        Zawiera odwołania do poszczególnych elementów aplikacji
        takich jak, generator haseł, moduł obsługi bazy danych.

"""

from .wyborOpcjiGeneratora import Wybor
from .mainBaza import Baza
from .koloruj import color_text
from . import masterPass
from .masterPass import pobierzHaslo


class ZlaWarotsc(Exception):
    pass


class StringZamiastInt(Exception):
    pass

def Wejscie(licznik):
    if licznik == 0:
        print(color_text("red", "Nie znasz Hasła! Do widzenia!"))

        exit()
    pobpswd = pobierzHaslo()
    pswd = input(color_text("blue", "Wprowdadź hasło główne:\n"))
    if pobpswd == pswd:
        MenuGlowne()
    else:
        print(color_text("red", "Hasło nieprawidłowe! pozostło "), licznik - 1, color_text("red", "prób\n"))
        licznik -= 1
        Wejscie(licznik)
    return


def MenuGlowne():
    """
        Główna pętla aplikacji
    """
    print("\n\n")
    print(color_text("blue", "Menu główne"))
    print(color_text("green", "Dostępne opcje:"))
    print("--" * 10)
    print("1 - Wygeneruj nowe hasło o podanych parametrach \n     na użytek bierzący")
    print("2 - Przejdź do menu zarządzania bazą danych\n     zgromadzonych haseł i loginów")
    print("3 - Ustaw - zresetuj hasło główne")
    print("4 - Zakończ działanie programu")
    print("\n\n")
    wybor = 0
    while wybor not in range(1, 5):
        try:  # walidacja właściwego wyboru w menu
            wybor = int(input("Dokonaj wyboru(1,2,3 lub 4)"))
            if wybor < 1 or wybor > 4:
                raise ZlaWarotsc()
        except ValueError:
            print("wybór powinien być cyfrą!!")
        except ZlaWarotsc:
            print(f"Niewłaściwy wybór {wybor} nie ma takiej opcji w menu!!")
    match wybor:
        case 1:
            Wybor()
            MenuGlowne()
        case 2:
            Baza()
            MenuGlowne()
        case 3:
            masterPass.mPassword()
            MenuGlowne()
        case 4:
            print(color_text("blue", "Dziękuję za skorzystanie z programu ! Do widzenia !!\n\nEldritch."))
            exit()
        case other:
            MenuGlowne()


def main():
    print(color_text("yellow",
                     "Witaj w programie do generowania haseł i nie tylko (wersja rozwojowa, na ile pozwolą umiejętności :D"))
    print("--" * 50)
    licznik = 3
    Wejscie(licznik)


if __name__ == '__main__':
    main()
