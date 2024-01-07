# INF.04-02-22.06-SG

## Ważne

To rozwiązanie powstawało na zajęciach [kwalifikacyjnego kursu zawodowego INF.04](https://teb.pl/kierunki/d/projektowanie-i-testowanie-aplikacji/).

Zadanie **w Angularze** zostało **rozbudowane** o następujące elementy:

- dodawanie kursu do listy (zgodnie z treścią zadania program ma działać dla każdej listy, nie tylko tej 3-elementowej),
- wyświetlanie komunikatów o stanie na stronie, nie tylko w konsoli (tam też).

Zadanie **w React'cie** jest zrobione "czysto".

## Informacje o rozwiązaniu

System operacyjny: Windows 11 Pro wersja 22H2

Nazwy środowisk programistycznych: Visual Studio Code, PyCharm 2023.1 (Professional Edition)

Języki programowania / frameworki / biblioteki: TypeScript, Angular, React, Bootstrap; Python

## Aplikacja konsolowa

![mobile1.png](testy/konsola1.png)
Rysunek 1. Przedstawiono działanie aplikacji konsolowej zgodnie z testem opisanym w częsci III arkusza. Wynik programu widoczny jest w prawej części okna IDE.

## Aplikacja webowa

### Rozwiązanie w Angularze

![web1.png](testy/web1.png)
Rysunek 2. Stan początkowy.

![web2.png](testy/web2.png)
Rysunek 3. Wprowadzono poprawne dane do formularza, ale jeszcze go nie zatwierdzono.

![web3.png](testy/web3.png)
Rysunek 4. Zatwierdzono formularz z poprawnymi danymi.

![web4.png](testy/web4.png)
Rysunek 5. Zmieniono dane w formularzu na niepoprawne (nieistniejący numer kursu) i zatwierdzono.

### Rozwiązanie w React'cie

![web5.png](testy/web5.png)
Rysunek 6. Stan początkowy.

![web6.png](testy/web6.png)
Rysunek 7. Uzupełniono pola "imię i nazwisko" oraz "numer kursu" poprawnymi danymi.

![web7.png](testy/web7.png)
Rysunek 8. Kliknięto przycisk "Zapisz do kursu".

![web8.png](testy/web8.png)
Rysunek 9. Zmieniono numer kursu na niepoprawny i kliknięto "Zapisz do kursu".
