import sys
from dataclasses import dataclass
from PyQt6.QtWidgets import QMainWindow, QApplication

from ui import Ui_MainWindow


@dataclass
class Album:
    artist: str
    album: str
    songsNumber: int
    year: int
    downloadNumber: int


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.albums: list[Album] = []
        self.load_albums()
        self.which_album = 0
        self.show_album()

        self.left.clicked.connect(self.prev)
        self.right.clicked.connect(self.next)
        self.btn_download.clicked.connect(self.download)

    def load_albums(self):
        with open('Data.txt', encoding='utf8') as f:
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
                self.albums.append(album)

        print(self.albums)

    def show_album(self):
        a = self.albums[self.which_album]
        self.lbl_band.setText(a.artist)
        self.lbl_album.setText(a.album)
        self.lbl_num_songs.setText(f"{a.songsNumber} utworów")
        self.lbl_year.setText(f"{a.year}")
        self.lbl_downloads.setText(f"{a.downloadNumber}")

    def prev(self):
        self.which_album -= 1
        if self.which_album == -1:
            self.which_album = len(self.albums) - 1
        self.show_album()

    def next(self):
        self.which_album += 1
        if self.which_album == len(self.albums):
            self.which_album = 0
        self.show_album()

    def download(self):
        self.albums[self.which_album].downloadNumber += 1
        self.show_album()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
