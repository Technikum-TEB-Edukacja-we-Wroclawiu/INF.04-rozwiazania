import java.util.Random;

class ArrayOperations {
    private final int[] numbers;
    private final int length;

    ArrayOperations(int length) {
        this.length = length;
        this.numbers = new int[length];

        var rng = new Random();

        for (int i = 0; i < length; i++) {
            this.numbers[i] = rng.nextInt(1, 1001); // [1, 1001)
        }
    }

    /**
     * ******************
     * nazwa metody: printArray
     * opis metody: wypisuje na konsolę wszystkie liczby w tablicy
     * parametry: brak
     * zwracany typ i opis: brak
     * autor: 123456789112
     * ******************
     */
    public void printArray() {
        for (int i = 0; i < length; i++) {
            System.out.println(i + ": " + this.numbers[i]);
        }
    }

    public int findFirst(int needle) {
        for (int i = 0; i < length; i++) {
            if (this.numbers[i] == needle) {
                return i;
            }
        }

        return -1;
    }

    public int printOdd() {
        int counter = 0;
        for (int i = 0; i < length; i++) {
            if (this.numbers[i] % 2 == 1) {
                counter++;
                System.out.println(this.numbers[i]);
            }
        }

        return counter;
    }

    public double average() {
        int sum = 0;
        for (int i = 0; i < length; i++) {
            sum += this.numbers[i];
        }

        return (double) sum / this.length;
    }
}

class Main {
    public static void main(String[] args) {
        var arrayOps = new ArrayOperations(21);

        System.out.println("Wszystkie elementy tablicy:");
        arrayOps.printArray();

        var index_42 = arrayOps.findFirst(42);
        if (index_42 != -1) {
            System.out.println("Liczbę 42 znaleziono na indeksie " + index_42 + ".");
        }

        System.out.println("Liczby nieparzyste w tablicy:");
        var numOdds = arrayOps.printOdd();
        System.out.println("Liczba liczb nieparzystych w tablicy: " + numOdds);

        var avg = arrayOps.average();
        System.out.println("Średnia wartość liczb w tablicy: " + avg);
    }
}