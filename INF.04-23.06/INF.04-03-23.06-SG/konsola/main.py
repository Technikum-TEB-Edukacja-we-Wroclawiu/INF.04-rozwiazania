"""
**********************************************************
  nazwa klasy: Film
  pola:        _title - tytuł filmu
               _number_of_rentals - liczba wypożyczeń
  metody:      set_title, brak zwracanej wartości - ustawia tytuł filmu
               get_title, str - zwraca ustawiony tytuł filmu
               get_number_of_rentals, int - zwraca liczbę wypożyczeń filmu
               rent, brak zwracanej wartości - zwiększa liczbę wypożyczeń filmu
  informacje:  funkcja reprezentuje część logiki systemu wirtualnej
               wypożyczalni filmów
  autor:       961009xxxxx
**********************************************************
"""
class Film:
    def __init__(self):
        self._title: str = ""
        self._number_of_rentals: int = 0

    def set_title(self, title) -> None:
        self._title = title

    def get_title(self) -> str:
        return self._title

    def get_number_of_rentals(self) -> int:
        return self._number_of_rentals

    def rent(self) -> None:
        self._number_of_rentals += 1


if __name__ == '__main__':
    film = Film()
    print(f"Stan pól: _title: '{film.get_title()}'; _number_of_rentals: {film.get_number_of_rentals()}")

    film.set_title("To jest nowy tytuł filmu")
    print(f"Nowy tytuł: {film.get_title()}")

    print(f"Liczba wypożyczeń przed zwiększeniem: {film.get_number_of_rentals()}")
    film.rent()
    print(f"Liczba wypożyczeń po zwiększeniu: {film.get_number_of_rentals()}")
