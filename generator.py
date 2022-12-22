"""
Moduł odpowiedzialny za proces i walidacje generowania hasła
na podstawie informacji o wyborach uzytkownika z modułu 'wybórOpcjiGeneratora'.
"""

import random
import re


def Generowanie(dlugosc_hasla, znaki_specjalne, zawiera_liczbe):
    """
    Generator hasła. Zawiera w sobie szereg warunków zawarty w czterech blokach generująco-walidujących
    opartych na decyzjach użytkownika, dotyczących kształtu żądanego hasła, oraz walidację tych warunków
    opartą częściowo na konstrukcjach wyrażeń regularnych (konieczny import biblioteki 're') i zwracający
    hasło pod postacią zmiennej 'haslo'.
    :param dlugosc_hasla:
    :param znaki_specjalne:
    :param zawiera_liczbe:
    :return:
    """
    haslo = ""  # ustawienie zmiennej hasło
    poczatek = 48  # zakres znaków ASCI
    koniec = 123
    if znaki_specjalne == True and zawiera_liczbe == True:  # wersja ze znakami specjalnymi
        czy_jest_znak_specj = False
        while czy_jest_znak_specj == False:
            haslo = ""
            for i in range(dlugosc_hasla):
                znak = random.randint(poczatek, koniec)
                if znak != 62 and znak != 60 and znak != 124:
                    haslo = (haslo + chr(znak))
                    i += 1
                else:
                    znak = znak + random.randint(1, 2)
                    haslo = (haslo + chr(znak))
                    i += 1
            x = re.search(r"(?=(?:.*[!@#$%^&*()\-_=+{};:,.]){1,})",
                          haslo)  # regex dla ciągu zawierającego co najmniej jeden znak specjalny
            y = re.search(r"(?=(?:.*\d){1,})", haslo)  # regex dla ciągu zawierającego co najmniej jedena cyfrę
            if x and y:  # jeżeli oba wary
                czy_jest_znak_specj = True

        return haslo

    if znaki_specjalne == False and zawiera_liczbe == True:  # wersja bez znaków specjalnych ale musi zawierać chociaż jedną cyfrę
        czy_sie_zgadza = False

        while czy_sie_zgadza == False:
            haslo = ""
            i = 1
            while i <= dlugosc_hasla:
                znak = chr(random.randint(poczatek, koniec))
                if znak.isdigit() or znak.isalpha():
                    haslo = (haslo + znak)
                    i += 1
                else:

                    continue
            x = re.search(r"(?=(?:.*\d){1,})", haslo)  # regex dla ciągu zawierającego co najmniej jedena cyfrę
            if x:
                czy_sie_zgadza = True
        return haslo

    if znaki_specjalne == True and zawiera_liczbe == False:  # wersja ze znakami specjalnymi
        czy_jest_znak_specj = False
        while czy_jest_znak_specj == False:
            haslo = ""
            for i in range(dlugosc_hasla):
                znak = random.randint(poczatek, koniec)
                if znak != 62 and znak != 60 and znak != 124:
                    haslo = (haslo + chr(znak))
                    i += 1
                else:
                    znak = znak + random.randint(1, 2)
                    haslo = (haslo + chr(znak))
                    i += 1
            x = re.search(r"(?=(?:.*[!@#$%^&*()\-_=+{};:,.]){1,})",
                          haslo)  # regex dla ciągu zawierającego co najmniej jeden znak specjalny
            y = re.search(r"(?=(?:.*\d){1,})", haslo)  # regex dla ciągu zawierającego co najmniej jedena cyfrę
            if x and not y:
                czy_jest_znak_specj = True

        return haslo

    if znaki_specjalne == False and zawiera_liczbe == False:  # Zawiera tylko litery bez cyfr i znaków specjalnych
        i = 1
        while i <= dlugosc_hasla:
            znak = chr(random.randint(poczatek, koniec))
            if znak.isalpha():
                haslo = (haslo + znak)
                i += 1
            else:
                continue

        return haslo