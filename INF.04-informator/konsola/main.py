"""
/* ****************************************************************************
 * nazwa funkcji:       encrypt
 *
 * parametry wejściowe: cleartext — tekst jawny do zaszyfrowania
 * wartość zwracana:    szyfrogram utworzony zgodnie z algorytmem
                        GADERYPOLUKI
 * opis funkcji:        funkcja przyjmuje tekst jawny i zwraca
                        szyfrogram utworzony zgodnie z algorytmem
                        GADERYPOLUKI; uwzględniana jest wielkość liter,
                        znaki spoza słownika podstawieniowego nie są zmieniane.
 * autor:               961009xxxxx
 * ***************************************************************************/
"""
def encrypt(cleartext: str) -> str:
    # ga de ry po lu ki
    substitution = {'g': 'a', 'd': 'e', 'r': 'y', 'p': 'o', 'l': 'u', 'k': 'i',
                    'a': 'g', 'e': 'd', 'y': 'r', 'o': 'p', 'u': 'l', 'i': 'k'}
    cleartext_list = list(cleartext)
    encrypted_list = []
    for letter in cleartext_list:
        letter_lower = letter.lower()
        if letter not in substitution and letter_lower not in substitution:
            encrypted_list.append(letter)
            continue

        if letter.isupper():
            encrypted_list.append(substitution[letter_lower].upper())
        else:
            encrypted_list.append(substitution[letter])

    return ''.join(encrypted_list)


if __name__ == '__main__':
    assert encrypt("PROGRAM") == "OYPAYGM"

    user_input = input("Wprowadź tekst do zaszyfrowania: ")
    encrypted_text = encrypt(user_input)
    print(f"Zaszyfrowany tekst: {encrypted_text}")
