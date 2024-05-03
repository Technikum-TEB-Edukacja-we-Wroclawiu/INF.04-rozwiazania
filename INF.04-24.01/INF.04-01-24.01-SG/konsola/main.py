def pesel_gender(pesel: str) -> str:
    return 'K' if int(pesel[9]) % 2 == 0 else 'M'


def pesel_validate(pesel: str) -> bool:
    """
    ******************************************
    nazwa funkcji: pesel_validate
    opis funkcji: weryfikuje poprawność wprowadzonego numeru PESEL
    parametry: pesel - 11-znakowy napis zawierający wyłącznie cyfry - numer PESEL do weryfikacji
    zwracany typ i opis: bool — True, jeśli podany PESEL jest poprawny, False w p.p.
    autor: 123456789112
    ******************************************
    """
    digits = [int(digit) for digit in pesel]
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    S = sum([a * b for a, b in zip(digits[:10], weights)])
    M = S % 10
    if M == 0:
        R = 0
    else:
        R = 10 - M

    return R == digits[-1]


if __name__ == '__main__':
    pesel = '55030101193'
    pesel = input('Wprowadź numer PESEL: ')
    print('Kobieta' if pesel_gender(pesel) == 'K' else 'Mężczyzna')
    print('Suma kontrolna', 'zgodna' if pesel_validate(pesel) else 'niepoprawna')
