"""
Moduł szyfrowanie Szyfrem Cezara o  kluczu 26
Moduł stworzony przeze mnie na potrzeby inmnych zajęć, funkcje zbędne do
prawidłowego działania w aplikacji hasła, zostały zakomentowane.

"""


def Klucz():  # pobranie warości klucza od użytkownika z walidacją wprowadzonych danych
    klucz = 26
    return klucz
    # try:
    #     klucz = int(input("podaj klucz szyfrujący"))
    #     if klucz < 1 or klucz >= 26:
    #         print("podaj liczbe z zakresu 1-25 ")
    #         Klucz()
    # except:
    #     ValueError
    #     print("podaj liczbe z zakresu 1-25 ")
    #     Klucz()


def Deszyfruj(wynik,
              klucz=26):  # deszyfrowanie przez przestawienie kolejnych liter na litery przesunięte o klucz w lewo

    wynik2 = ""
    ciag = wynik
    for i in range(len(ciag)):  # pętla po kolejnych znakach ciagu

        wynik2 += chr(ord(ciag[i]) - klucz)  # zapisuje ostatni wyraz z ciag jako pierwszy w str wynik

    return wynik2


def Szyfrowanie(ciag,
                klucz=26):  # szyfrowanie przez przestawienie kolejnych liter na litery przesunięte o klucz w prawo

    wynik = ""
    for i in range(len(ciag)):  # pętla po kolejnych znakach ciagu

        wynik += chr(ord(ciag[i]) + klucz)  # zapisuje ostatni wyraz z ciag jako pierwszy w str wynik
        wynik2 = wynik
    return wynik

# def Wydruk(ciag,klucz,wynik):
#     print("Ciąg :",ciag," pozaszyfrowaniu szyfrem Cezara kluczem :",klucz,"wygląda tak : ",wynik)


# def Main():
#     ciag = input("Wprowaź ciąg znaków do zaszyfrowania :")
#     Klucz()
#     Szyfrowanie(ciag, klucz)
#     Wydruk(ciag,klucz,wynik)
#     print("wcisnij Enter żeby zdeszyfrować ciąg :",wynik , " kluczem :",klucz)
#     input()
#     Deszyfruj(wynik,klucz)
#     print ("Po deszyfracji kluczem ",klucz, "ciag ",wynik, "ma postać początkową niezaszyfrowaną",wynik2)
#
# Main()
