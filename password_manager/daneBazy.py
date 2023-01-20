import sys

def CzyUzycBazPrzykladowych():
    return len(sys.argv) > 1 and sys.argv[1] == '--dev'

def SciezkaBazyHasla():
    if CzyUzycBazPrzykladowych():
        return 'przykladowe_db/p.db'
    else:
        return 'db/p.db'

def SciezkaBazyGlownej():
    if CzyUzycBazPrzykladowych():
        return 'przykladowe_db/baza_glowna.db'
    else:
        return 'db/baza_glowna.db'
