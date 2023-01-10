"""
Główny moduł programu.

        Zawiera odwołania do poszczególnych elementów aplikacji
        takich jak, generator haseł, moduł obsługi bazy danych.

"""

import sys
from wyborOpcjiGeneratora import Wybor
from mainBaza import Baza
from koloruj import color_text


class ZlaWarotsc(Exception):
    pass


class StringZamiastInt(Exception):
    pass


def MenuGlowne():
    """
        Główna pętla aplikacji
    """
    print("\n\n")
    print(color_text("green","Dostępne opcje:"))
    print("--" * 10)
    print("1 - Wygeneruj nowe hasło o podanych parametrach \n     na użytek bierzący")
    print("2 - Przejdź do menu zarządzania bazą danych\n     zgromadzonych haseł i loginów")
    print("3 - trzecia opcja narazie też nieznana")
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
            pass
        case 4:
            sys.exit()
        case other:
            MenuGlowne()


print("--" * 50)
print(color_text("yellow","Witaj w programie do generowania haseł i nie tylko (wersja rozwojowa, na ile pozwolą umiejętności :D"))
print("--" * 50)
MenuGlowne()
