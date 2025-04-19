import java.util.Scanner;

class Device {
    /**
     * ******
     * nazwa: display
     * opis: metoda wyświetla podany komunikat w konsoli
     * parametry: `message` - komunikat do wyświetlenia
     * zwracany typ i opis: brak
     * autor: 123456789112
     * ******
     */
    public void display(String message) {
        System.out.println(message);
    }
}

class WashingMachine extends Device {
    private int program = 0;

    public int setProgram(int program) {
        if (program >= 1 && program <= 12) {
            this.program = program;
        } else {
            this.program = 0;
        }

        return this.program;
    }
}

class Vacuum extends Device {
    private boolean status = false;
    public void on() {
        if(!status) {
            status = true;
            display("Odkurzacz włączono");
        }
    }
    public void off() {
        if(status) {
            status = false;
            display("Odkurzacz wyłączono");
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        WashingMachine washingMachine = new WashingMachine();
        Vacuum vacuum = new Vacuum();

        System.out.print("Podaj numer prania (1..12): ");
        int program = sc.nextInt();
        if(washingMachine.setProgram(program) == program) {
            System.out.println("Program został ustawiony");
        } else {
            System.out.println("Podano niepoprawny numer programu");
        }

        vacuum.on();
        vacuum.on();
        vacuum.on();

        vacuum.display("Odkurzacz wyładował się");

        vacuum.off();
    }
}