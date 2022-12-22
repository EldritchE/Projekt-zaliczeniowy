import re
class ZlaWarotsc(Exception):
    pass

def SprawdzMaila():
    control=True
    while control:
        try:
            string = input("Podaj adres email :")
            string = string.lower()
            x = re.search(r"(\w+\.?|-?\w+?)+@\w+\.?-?\w+?(\.\w{2,3})+", string)  # regex dla ciągu bedącego adresem email
            if x:
                print("prawidłowy\n")
                control=False
            else:
                raise ZlaWarotsc()
        except ZlaWarotsc:
            print("zly adres email! Podaj jeszce raz: \n")
    return string

def SprawdzWWW():
    control=True
    while control:
        try:
            string = input("Podaj adres WWW :")
            string=string.lower()
            x = re.search(r"^www.[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}$", string)  # regex dla ciągu bedącego adresem WWW
            if x:
                print("prawidłowy\n")
                control=False
            else:
                raise ZlaWarotsc()
        except ZlaWarotsc:
            print("zly adres WWW!(prawidłowa postać :'www.nazwa.com') Podaj jeszce raz: \n")
    return string

def SprawdzLogin():  #sprawdzanie czy login nie ma baiłych znaków
    control = True
    while control:
        try:
            string = input("Login :")
            x = re.search(r"^[a-zA-Z_\-]+$", string)  # regex dla ciągu z spacją
            if x:
                print("prawidłowy\n")
                control = False
            else:
                raise ZlaWarotsc()
        except ZlaWarotsc:
            print("Login posiada niedopuszczalny znak  podaj jeszcze raz: \n")
    return string



def SprawdzHasloJesliZReki():
    control = True
    while control:
        try:
            string = input("Wpisz swoje hasło:\n")
            x = re.search(r"\s{1,}", string)  # regex dla ciągu z spacją
            if x:
                print("prawidłowy\n")
                control = False
            else:
                raise ZlaWarotsc()
        except ZlaWarotsc:
            print("Login posiada niedopuszczalny znak  podaj jeszcze raz: \n")
    return string

