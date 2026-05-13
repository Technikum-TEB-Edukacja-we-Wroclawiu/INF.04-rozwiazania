import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.URI;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException {

		File file = new File("Data.txt");
		List<Song> listOfSongs = loadData(file);
		displaySongCollection(listOfSongs);

	}
	/**
	 *  nazwa: loadData
	 * 	opis: pobiera plik z parametru następnie mapuje jego zawartość do obiektów Song które następnie zapisuje w kolekcji List
	 *  parametry: file - obiekt reprezentujący plik który zawiera informacje o piosenkach
	 *  zwracany typ i opis:  List<Song> - zwracana jest kolekcja List przechowywująca obiekty klasy Song zmapowane wcześniej z pliku tekstowego
	 * 	autor: 123456789112
	 */
	public static List<Song> loadData(File file) throws FileNotFoundException {
		Scanner scanner = new Scanner(file);
		List<Song> listOfSongs = new LinkedList<>();
		int counter = 0;

		while (true) {
			Song song = new Song();
			song.setArtist(scanner.nextLine());
			song.setAlbum(scanner.nextLine());
			song.setSongsNumber(Integer.parseInt(scanner.nextLine()));
			song.setReleaseYear(Integer.parseInt(scanner.nextLine()));
			song.setDownloadNumber(Long.parseLong(scanner.nextLine()));
			listOfSongs.add(song);
			if (scanner.hasNextLine()) {
				scanner.nextLine();
			} else {
				break;
			}

		}
		scanner.close();
		return listOfSongs;
	}
	/**
	 *  nazwa: displaySongCollection
	 * 	opis: wyświetla wszystkie dane z obiektów znadujących się w podanej kolekcji
	 *  parametry: file - obiekt reprezentujący plik który zawiera informacje o piosenkach
	 *  zwracany typ i opis:  brak
	 * 	autor: 123456789112
	 */
	public static void displaySongCollection(List<Song> listOfSongs) {
		for (Song song : listOfSongs) {
			System.out.println(song.toString());
		}
	}
}

class Song {

	private String artist;
	private String album;
	private int songsNumber;
	private int releaseYear;
	private long downloadNumber;
	/**
	 *  nazwa: Song
	 * 	opis: konstruktor bezparametrowy
	 *  parametry: brak
	 *  zwracany typ i opis:  brak
	 * 	autor: 123456789112
	 */
	public Song() {
	}
	/**
	 *  nazwa: setArtist
	 * 	opis: ustawia pole obiektu na podaną w parametrze wartość
	 *  parametry: artist - łańcuch zawierający nazwe artysty
	 *  zwracany typ i opis:  brak
	 * 	autor: 123456789112
	 */
	public void setArtist(String artist) {
		this.artist = artist;
	}
	// nie wiem czy potrzeba przy każdym setterze umieścić podobny komentarz co na górze
	// ale wiem ze nie chce mi się ich pisać xd
	public void setAlbum(String album) {
		this.album = album;
	}

	public void setSongsNumber(int songsNumber) {
		this.songsNumber = songsNumber;
	}

	public void setReleaseYear(int releaseYear) {
		this.releaseYear = releaseYear;
	}

	public void setDownloadNumber(long downloadNumber) {
		this.downloadNumber = downloadNumber;
	}
	/**
	 *  nazwa: toString
	 * 	opis: tworzy Łańcuch reprezentujący dane wszystkich pól znajdujących się w obiekcie
	 *  parametry: brak
	 *  zwracany typ i opis:  String - zwracany jest łańcuch zawierający dane z pól obiektu
	 * 	autor: 123456789112
	 */
	public String toString() {

		return this.artist + "\n" + this.album + "\n" + this.songsNumber + "\n" + this.releaseYear + "\n"
				+ this.downloadNumber + "\n";
	}

}
