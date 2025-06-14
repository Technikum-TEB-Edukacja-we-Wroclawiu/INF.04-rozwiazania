package bibliotekaDlaLancuchow;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		System.out.println("podaj tekst w którym zostaną policzone samogłoski i usunięte powtórzenia");
		String providedInput=scanner.nextLine();
		System.out.println("liczba samogłosek: "+StringTools.countVowels(providedInput));
		System.out.println("tekst po usunięciu powtórzeń: "+StringTools.deleteRepetitions(providedInput));
	}

}

class StringTools{
	/**
	 *  nazwa: countVowels
	 * 	opis: liczy samogłoski w podanym tekscie a następnie zwraca ich liczbe
	 *  parametry: text - typ łańcuchowy przechowywujący tekst w którym trzeba policzyć samogłoski
	 *  zwracany typ i opis: int - liczba samogłosek w tekście 	
	 * 	autor: 123456789112
	 */
	public static int countVowels(String text) {
		final String vowels="aąeęiouóyAĄEĘIOUÓY";
		int numberOfVowels=0;
		if(text!=null && text!="") {
			for(int i=0;i<text.length();i++) {
				for(int j=0;j<vowels.length();j++) {
					if(text.charAt(i)==vowels.charAt(j)) numberOfVowels++;
				}
			}
		}
		return numberOfVowels;
	}
	/**
	 *  nazwa: deleteRepetitions
	 * 	opis: usuwa powtórzenia znaków znajdujących się obok siebie w podanym tekscie np. z słowa Abbba;;; zwróci Aba;
	 *  parametry: text - typ łańcuchowy przechowywujący tekst z którego trzeba usunąć powtórzenia
	 *  zwracany typ i opis: String - tekst oczyszczony z powtórzeń 	
	 * 	autor: 123456789112
	 */
	public static String deleteRepetitions(String text) {
		String cleanedText="";
		if(text!=null && text!="") {
			cleanedText+=""+text.charAt(0);
			for(int i=1;i<text.length();i++) {
				if(cleanedText.charAt(cleanedText.length()-1)!=text.charAt(i)) {
					cleanedText+=text.charAt(i);
				}
			}
		}
	
		return cleanedText;
	}
	
}
