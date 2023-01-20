"""
Ładowanie gotowego hasła do schowka systemowego
"""
import pyperclip


def dodajDoSchowka(haslo):
    """
    Zapisywanie zmiennej hasło do schwowka systemowego
    """
    pyperclip.copy(haslo)
