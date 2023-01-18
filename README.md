# Projekt-zaliczeniowy Przedmiot Python zaawansowany.

Robert Jaworski 81591



Aplikacja o funkcjonalności menadżera i generatora haseł.
-



- Postawowa funkcjonalność:
  -

-  **_1: Generowanie hasła_** na bierzące potrzeby użytkownika na postawie zadanych parametrów. Czyli, czy hasło ma zawierać znaki
  specjalne, cyfry, jaka ma być wymagana długość hasła. Aplikacja narzuca pewne zasady tworzenia hasła:
  (minimalna długość hasła = 4 znaki,maksymalna długość generowanego hasła przyjęto na 40 znaków, z założenia aplikacja 
  używa małych i wielkich liter z automatu nie pytając o to użytkownika.
    -     Dodatkowo, po utworzeniu oczekiwanego hasła, aplikacja z automatu zapisuje hasło w schowku systemowym,
          o czym informuje, do wykorzystania w samej aplikacji, jak również po za nią, w intuicyjny sposób w jaki korzysta 
          się ze skrótu klawiszowego ctrl+V, lub menu kontekstowego myszki.


- **_2: Opcje Bazy Danych_** gromadzącej utworzone hasła do róznego rodzaju serwisów i usług, gdzie wymagane są login i hasło
    -       jeśli baza danych haseł nie istnieje, uzytkownik z automatu jest przenoszony do opcji tworzenia bazy danych

  
  - **Dodanie wpisu** do bazy danych:  umozliwia stworzenie nowego wpisu serwis-login-hasło-opis
  - **Wyszukiwanie informacji** w bazie danych 
  
  
                1) wyświetlanie zawartości całej bazy dnaych
                2) szukanie wpisów po zadanym adresie www
                3) szukanie po zadanym adresie email
                4) szukanie po wpisach nieokreślonych
                5) szukanie po loginie
                6) szukanie po opisie
                7) szukanie po dacie utworzenia (wpisanie tylko rou i miesiąca, wyświetla wpisy z danego miesiąca)
                8) powrót do menu bazy danych
  
  - **Utworzenie nowej bazy danych**

        z mechanizmem zabezpieczenia poprzedniej bazy przed utratą w postaciu utorzenia pliku 'zabezpieczenie_bazy(aktualny czass).db'
  - **Powrót do menu głownego**



- **_3: Ustaw- zresetuj hasło główne_**
- **Zmiana hasła głównego**

      typowy mechanizm zabezpeieczający przed zmianą hasła (podanie strego hasła, następnie powtórzenie 2 dwukrotne nowego
- **Zapomniałem hasła**

      typowy mechanizm zabezpeieczający przed utratą hasła, oparty na 2 pytaniach zabezpieczających
      zapamietanych przy tworzeniu hasła
  

- Informacje ogólne:
  -
 - hasło startowe '1111'
 - załączona baza danych z przykładowymi wpisami