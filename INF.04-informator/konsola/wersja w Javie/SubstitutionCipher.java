import java.util.HashMap;
import java.util.Map;

public class SubstitutionCipher {

    private Map<Character, Character> dict = new HashMap<>();

    public SubstitutionCipher(){
        dict.put('g','a');
        dict.put('a', 'g');
        dict.put('d','e');
        dict.put('e', 'd');
        dict.put('r', 'y');
        dict.put('y', 'r');
        dict.put('p', 'o');
        dict.put('o', 'p');
        dict.put('l', 'u');
        dict.put('u', 'l');
        dict.put('k', 'i');
        dict.put('i', 'k');
    }


    /* ******************************************************************************************
     * nazwa funkcji:       encryptText
     *
     * parametry wejściowe: text - napis, który należy zaszyfrować
     * wartość zwracana:    zaszyfrowany tekst
     * opis funkcji:        Funkcja szyfruje podany tekst szyfrem przestawieniowym gaderypoluki,
     *                      który zamienia pary liter g-a, d-e, r-y, p-o, l-u, k-i między sobą
     *                      (g na a, a na g itp.).
     * autor:               970526xxxxx
     ***************************************************************/
    public String encryptText(String text){
        StringBuilder stringBuilder = new StringBuilder();
        for(Character c: text.toLowerCase().toCharArray()){
            Character encryptC = dict.get(c);
            if(encryptC == null)
                encryptC = c;
            stringBuilder.append(encryptC);
        }
        return stringBuilder.toString();
    }
}
