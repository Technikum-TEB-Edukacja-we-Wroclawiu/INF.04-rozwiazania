import random
import string

"""
nazwa funkcji: generate_password
opis funkcji: funkcja generująca 12-znakowe hasło
parametry: brak
zwaracany typ i opis: string – wygenerowane hasło
autor: 00000000000
"""
def generate_password() -> str:
    lower_letters = [char for char in string.ascii_lowercase]
    upper_letters = [char for char in string.ascii_uppercase]
    digits = [char for char in string.digits]
    special = [char for char in '!@#$%^&*()_+']
    polish_letters = [char for char in 'ąęłńóśżźĄĘŁŃÓŚŻŹ']
    password = (random.choices(lower_letters, k=3) + random.choices(upper_letters, k=3) + random.choices(digits, k=2) +
                random.choices(special, k=2) + random.choices(polish_letters, k=2))
    random.shuffle(password)
    return ''.join(password)

if __name__ == '__main__':
    for i in range(5):
        print(f'Hasło {i+1}: {generate_password()}')
