from dataclasses import dataclass


@dataclass
class Album:
    artist: str
    album: str
    songsNumber: int
    year: int
    downloadNumber: int


def get_albums(filename: str) -> list[Album]:
    """
    *******
    nazwa funkcji:       get_albums
    opis funkcji:        funkcja odczytuje plik tekstowy w zadanym w zadaniu formacie
                         i tworzy obiekty klasy Album odpowiadające wczytanym danym
    parametry:           filename - nazwa pliku z danymi do wczytania
    zwracany typ i opis: lista obiektów typu Album
    autor:               123456789112
    *******
    """
    albums: list[Album] = []
    with open(filename, encoding='utf8') as f:
        while True:
            artist = f.readline().strip()
            if artist == '':
                break
            album_name = f.readline().strip()
            songs_number = int(f.readline().strip())
            year = int(f.readline().strip())
            download_number = int(f.readline().strip())
            f.readline()

            album = Album(artist, album_name, songs_number, year, download_number)
            albums.append(album)

    return albums


def print_albums(albums: list[Album]) -> None:
    for album in albums:
        print(album.artist)
        print(album.album)
        print(album.songsNumber)
        print(album.year)
        print(album.downloadNumber)
        print()


def main():
    albums = get_albums('Data.txt')
    print_albums(albums)


if __name__ == '__main__':
    main()
