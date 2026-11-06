import java.util.LinkedList;
import java.util.Random;
import java.util.Scanner;

public class main {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		diceGame();
		
		while(true) {
			System.out.println("Jeszcze raz? (t/n)");
			String decision=sc.nextLine();
			if(decision.equals("t")) {
				diceGame();
			}else if(decision.equals("n")) {
				break;
			}
			
		}
		
	}
	/**
	 *  nazwa: diceGame()
	 * 	opis: rozpoczyna gre pobierajac informacje od uzytkownika o liczbie rzutów następnie wywoluje funkcje wyswietlajaca wynik
	 *  parametry: brak
	 *  zwracany typ i opis: brak   	
	 * 	autor: 123456789112
	 */
	public static void diceGame() {
		Scanner sc = new Scanner(System.in);
		while(true) {
			
			System.out.println("Ile kostek chcesz rzucić?(3-10)");
			int rollsNumber=sc.nextInt();
			if(rollsNumber>=3 && rollsNumber<=10) {
				int score=giveResult(rollDice(rollsNumber));
				System.out.println("Liczba uzyskanych punktów:"+score);
				break;
			}
		}
	}
	/**
	 *  nazwa: rollDice
	 * 	opis: symuluje proces rzutu koscmi losujac podana przez użytkownika liczbe wartosci reprezentujacych oczka na kostce
	 *  parametry: liczbaRzutow - liczba rzutów kostką do wykonania
	 *  zwracany typ i opis: int[] - tablica reprezentująca wszystkie wylosowane liczby w trakcie rzutu kostką  	
	 * 	autor: 123456789112
	 */
	public static int[] rollDice(int rollsNumber) {
		Random random = new Random();
		int[] diceArray= new int[rollsNumber];
		for(int i=0;i<rollsNumber;i++) {
			int rolledDice=(int)(Math.random()*5)+1;
			diceArray[i]=rolledDice;
			System.out.println("Kostka "+i+":"+rolledDice);
		}
		return diceArray;
		
	}
	/**
	 *  nazwa: giveResult
	 * 	opis: Oblicza wynik końcowy wszystkich rzutów kostką a następnie podaje wynik w wiadomosci dla uzytkownika
	 *  parametry: losoweLiczby - tablica przechowująca wszystkie wartości wyrzucone kostką 
	 *  zwracany typ i opis: brak	
	 * 	autor: 123456789112
	 */
	public static int giveResult(int[] diceArray) {
		LinkedList<Integer>checkedNumbers=new LinkedList<Integer>();
		int score=0;
		for(int i=0;i<diceArray.length;i++) {
			if(!checkedNumbers.contains(diceArray[i])) {
				checkedNumbers.add(diceArray[i]);
				int occurrencesNumber=1;
				for(int j=i+1;j<diceArray.length;j++) {
					
					if(diceArray[j]==diceArray[i]) {
						occurrencesNumber++;
					}
				}
				if(occurrencesNumber>=2) {
					score+=occurrencesNumber*diceArray[i];
				}
			}
		}
		return score;
	
	}

}
