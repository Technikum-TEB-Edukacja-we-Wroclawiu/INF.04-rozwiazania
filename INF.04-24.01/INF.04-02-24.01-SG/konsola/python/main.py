class StringHelper:
    """
    ****************************
    klasa: StringHelper
    opis: klasa reprezentuje bibliotekę metod działających na napisach
    metody: count_vowels - zwraca liczbę samogłosek w podanym tekście
            remove_duplicates - zwraca tekst z usuniętymi powtórzeniami znaków występującymi obok siebie
    autor: 123456789112
    ****************************
    """
    def count_vowels(text: str) -> int:
        counter = 0
        vowels = "aąeęiouóyAĄEĘIOUÓY"
        for char in text:
            if char in vowels:
                counter += 1

        return counter

    def remove_duplicates(text: str) -> str:
        ret = text[0]  # HACK tbh
        for char in text:
            if char == ret[-1]:
                continue
            ret += char

        return ret


if __name__ == '__main__':
    text = input("Wprowadź napis: ")
    print(f"Liczba samogłosek: {StringHelper.count_vowels(text)}")
    print(f"Tekst bez powtórzeń: {StringHelper.remove_duplicates(text)}")
