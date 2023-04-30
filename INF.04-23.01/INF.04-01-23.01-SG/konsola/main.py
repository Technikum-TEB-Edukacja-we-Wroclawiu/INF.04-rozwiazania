"""
*******************************************
nazwa funkcji:       gcd
opis funkcji:        funkcja wyznacza największy wspólny dzielnik (ang. greatest
                     common divider) dwóch parametrów a i b zgodnie z algorytmem
                     Euklidesa.
parametry:           a - pierwsza liczba
                     b - druga liczba
zwracany typ i opis: int - liczba całkowita będąca największym wspólnym dzielnikiem
                     liczb a i b
autor:               961009xxxxx
*******************************************
"""
def gcd(_a: int, _b: int) -> int:
    while _a != _b:
        if _a > _b:
            _a = _a - _b
        else:
            _b = _b - _a

    return _a


def read_number(name: str) -> int:
    """
    Funkcja wczytująca liczbę całkowitą dodatnią zgodnie z wymaganiami z arkusza.
    :param name: Nazwa liczby do wczytania
    :return: Wprowadzona z klawiatury wartość jako liczba całkowita
    """
    while True:
        try:
            tmp = int(input(f"Wprowadź liczbę {name}: "))
            if tmp < 0:
                raise ValueError
            break
        except ValueError:
            print("Należy wprowadzić liczbę całkowitą dodatnią")

    return tmp


if __name__ == '__main__':
    a = read_number("a")
    b = read_number("b")
    gcd_a_b = gcd(a, b)
    print(f"Największy wspólny dzielnik liczb {a} i {b} to {gcd_a_b}.")
