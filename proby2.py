class ZlaWarotsc(Exception):
    pass
class StringZamiastInt(Exception):
    pass
def funkcja1():
    input("funkcja 1")
    return
def funkcja2():
    input("funkcja 2")
    Menu1()
def Menu1():
    print("opcja 1")
    print ("opcja 2")
    print ("opcja 3")
    print ("wyjscie 4")
    wybor=0
    while wybor not in range(1,5):

        try:
            wybor = int(input("wybierz: "))
            if wybor <1 or wybor>4:
                raise ZlaWarotsc()
        except ValueError:
            # raise StringZamiastInt
            print ("wybór powinien być cyfrą!!")
        except ZlaWarotsc:
            print (f"Niewłaściwy wybór {wybor} nie ma takiej opcji w menu!!")
    match (wybor):
        case 1:
            funkcja1()
        case 2:
            funkcja2()




Menu1()
print("jak to widzisz to tutaj wyskoczył program z funcji 1 lub 2")