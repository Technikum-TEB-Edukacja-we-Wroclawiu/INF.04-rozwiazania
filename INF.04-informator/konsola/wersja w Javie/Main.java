import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        SubstitutionCipher substitutionCipher = new SubstitutionCipher();

        System.out.println("Podaj tekst do zaszyforwania: ");
        String text = scanner.nextLine();
        String encryptText = substitutionCipher.encryptText(text);
        System.out.println("Tekst zaszyfrowany: "+encryptText);
    }
}