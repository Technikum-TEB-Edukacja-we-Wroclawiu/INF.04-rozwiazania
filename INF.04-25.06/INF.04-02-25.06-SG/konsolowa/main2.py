# INF.04-02-25.06-SG
class Caesar:
    @staticmethod
    def cipher(cleartext: str, key: int) -> str:
        if key == 0:
            return cleartext

        key = key % 26

        encrypted = ""

        for char in cleartext:
            if char not in "qwertyuiopasdfghjklzxcvbnm":
                encrypted += char
            else:
                new_char = ord(char) + key
                if new_char > ord('z'):
                    new_char -= 26
                encrypted += chr(new_char)

        return encrypted


if __name__ == '__main__':
    text_to_cipher = input("Wprowadź tekst do zaszyfrowania: ")
    text_key = int(input("Wprowadź klucz: "))

    print(f"Tekst zaszyfrowany: {Caesar.cipher(text_to_cipher, text_key)}")
