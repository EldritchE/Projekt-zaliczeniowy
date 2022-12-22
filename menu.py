"""

Moduł odpowiedzialny za utworzenie menu głównego

"""


def Menu_wyswietl():
    """
    Fyunkcja wyświetlania opcji Menu Głównego:
    :return:
    """
    print("\n\n")
    print("Dostępne opcje:")
    print("--" * 10)
    print("1 - Wygeneruj nowe hasło o podanych parametrach \n     na użytek bierzący")
    print("2 - Przejdź do menu zarządzania bazą danych\n     zgromadzonych haseł i loginów")
    print("3 - trzecia opcja narazie też nieznana")
    print("0 - Zakończ działanie programu")
    print("\n\n")
    return


def Menu_wybor_opcji():
    """
    Wybór opcji Menu głównego: z walidacją.
    :return:
    """
    wybor = input("Dokonaj wyboru(1,2,3 lub 0)")
    match wybor:
        case "1":
            print()
            return wybor
        case "2":
            print()
            return wybor
        case "3":
            print()
            return wybor
        case "0":
            print()
            return wybor
        case other:
            print("nie dokonano właściwego wyboru\n")
