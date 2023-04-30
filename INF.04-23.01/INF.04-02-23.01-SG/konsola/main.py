# ******
# Klasa:    Notatka
# Opis:     Klasa reprezentująca notatki. Każda notatka ma swój tytuł i opis.
# Pola:     __id - unikalny identyfikator notatki
#           _tytul - tytuł notatki
#           _tresc - treść notatki
#           __liczba_notatek - statyczne pole informujące o liczbie utworzonych notatek;
#                              nowe notatki otrzymują __id równy temu polu (po jego inkrementacji)
# Autor:    961009xxxxx
# ******
class Notatka:
    __liczba_notatek = 0

    def __init__(self, tytul: str, tresc: str):
        Notatka.__liczba_notatek += 1
        self.__id: int = Notatka.__liczba_notatek
        self._tytul: str = tytul
        self._tresc: str = tresc

    def wyswietl(self):
        print(f"Tytuł: {self._tytul}\nTreść: {self._tresc}")

    def diagnostyka(self):
        print(f"{Notatka.__liczba_notatek};{self.__id};{self._tytul};{self._tresc}")


if __name__ == '__main__':
    notatka1 = Notatka("Pierwsza notatka", "Oto treść pierwszej notatki")
    notatka2 = Notatka("Druga notatka", "To jest treść drugiej notatki")
    notatka1.wyswietl()
    notatka1.diagnostyka()
    notatka2.wyswietl()
    notatka2.diagnostyka()
