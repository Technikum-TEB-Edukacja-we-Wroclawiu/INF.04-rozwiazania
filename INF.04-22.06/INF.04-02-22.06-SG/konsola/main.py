class Osoba:
    instances: int = 0  # pole statyczne

    def __init__(self, id: int = 0, name: str = ""):
        self.__id: int = id  # utworzenie pola w instancji (!) klasy
        self.__name: str = name
        Osoba.instances += 1  # zmiana wartości pola statycznego

    def copy(self, person: "Osoba"):
        self.__id = person.__id
        self.__name = person.__name
        # nie zwiększamy self.instances,
        # bo wcześniej na pewno będzie wywołane
        # self.__init__

    def print_name(self, other_name: str):
        if self.__name == "":
            print("Brak danych")
        else:
            print(f"Cześć {other_name}, mam na imię {self.__name}")


if __name__ == '__main__':
    print(f"Liczba zarejestrowanych osób to {Osoba.instances}")
    person1 = Osoba()

    tmp_id = int(input("Wprowadź id nowej osoby: "))
    tmp_name = input("Wprowadź imię nowej osoby: ")
    person2 = Osoba(tmp_id, tmp_name)

    person3 = Osoba()
    person3.copy(person2)

    for p in [person1, person2, person3]:
        p.print_name("Jan")

    print(f"Liczba zarejestrowanych osób to {Osoba.instances}")
