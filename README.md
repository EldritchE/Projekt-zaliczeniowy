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

  
  - **Dodanie wpisu** do bazy danych:
    -      umożliwia stworzenie nowego wpisu serwis-login-hasło-opis
  - **Usunięcie wpisu** z bazy danych:  
    -      umożliwia usunięcie dowolnego wpisu z bazy danych po podaniu ID wpisu. Z tego menu istnieje wejscie
           do menu przeszukiwania, celem odnalezienia ID
  - **Wyszukiwanie informacji** w bazie danych 
  
        
                1) wyświetlanie zawartości całej bazy dnaych 
                2) szukanie wpisów po zadanym adresie www    (wpis www jest wyrózniony)
                3) szukanie po zadanym adresie email         (wpis email jest wyrózniony)
                4) szukanie wpisów o nieokreślonym rodzaju serwisu
                5) szukanie po loginie                       (wpis login jest wyrózniony)
                6) szukanie po opisie                        (wpis opisu jest wyrózniony)
                7) szukanie po dacie utworzenia (wpisanie tylko roku i miesiąca, wyświetla wpisy z danego miesiąca)
                8) powrót do menu bazy danych
  
  - **Utworzenie nowej bazy danych**

        z mechanizmem zabezpieczenia poprzedniej bazy przed utratą w postaciu utorzenia pliku 'zabezpieczenie_bazy(aktualny czass).db'
  - **Powrót do menu głownego**



- **_3: Ustaw- zresetuj hasło główne_**
- **Zmiana hasła głównego**

      typowy mechanizm zabezpieczający przed zmianą hasła (podanie strego hasła, następnie powtórzenie 2 dwukrotne nowego
- **Zapomniałem hasła**

      typowy mechanizm zabezpieczający przed utratą hasła, oparty na 2 pytaniach zabezpieczających
      zapamietanych przy tworzeniu hasła
  

- Informacje ogólne:
  -
 - projekt pisany w Pycharmie
 - został przygotowany plik Dockerfile
 - aplikacja posiada dwa tryby uruchomienia
 - przez plik run.sh uruchamiamy standardową aplikację bez bazy danych i bez hasła głównego 
 - przez run-dev.sh z przykładową bazą danych i ustawionym hasłem głównym hasło startowe '_1111_'
        odpowiedz na 1 pytanie sprawdzające przy zmianie hasła '_ja_'
        odpowiedz na 2 pytanie sprawdzające przy zmianie hasła '_tak_'

 - dane do logowania do repozytorium GiHub do projektu : ************************************
 - Dostęp do repozytorium przewidziano do 20 lutego 2023, 
 - Projekt powstał w dwóch repozytoriach, ze względu na awarię pierwszego zostało utworzone drugie :)
 - załączono plik 'requirements.txt'
