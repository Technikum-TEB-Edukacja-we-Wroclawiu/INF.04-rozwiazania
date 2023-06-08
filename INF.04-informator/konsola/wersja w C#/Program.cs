using System;
using System.Collections.Generic;

namespace INF._04_informator_gaderypoluki
{
    class Program
    {
        private readonly Dictionary<char, char> substitutionDictionary = new()
        {
            { 'g', 'a' },
            { 'd', 'e' },
            { 'r', 'y' },
            { 'p', 'o' },
            { 'l', 'u' },
            { 'k', 'i' },
            { 'a', 'g' },
            { 'e', 'd' },
            { 'y', 'r' },
            { 'o', 'p' },
            { 'u', 'l' },
            { 'i', 'k' }
        };

        /* ******************************************************************************************
         * nazwa funkcji:       Encrypt
         * 
         * parametry wejściowe: textToEncrypt - napis, który należy zaszyfrować
         * wartość zwracana:    zaszyfrowany tekst 
         * opis funkcji:        Funkcja szyfruje podany tekst szyfrem przestawieniowym gaderypoluki,
         *                      który zamienia pary liter g-a, d-e, r-y, p-o, l-u, k-i między sobą
         *                      (g na a, a na g itp.).
         * autor:               961009xxxxx
         * ******************************************************************************************/
        string Encrypt(string textToEncrypt)
        {
            string encryptedText = "";

            foreach (char character in textToEncrypt)
            {
                char tmpChar;
                if(substitutionDictionary.TryGetValue(character, out tmpChar))
                {
                    encryptedText += tmpChar;
                } 
                else if (Char.IsUpper(character) && substitutionDictionary.TryGetValue(Char.ToLower(character), out tmpChar))
                {
                    encryptedText += Char.ToUpper(tmpChar);
                } 
                else
                {
                    encryptedText += character;
                }
            }

            return encryptedText;
        }

        static void Main()
        {
            Program p = new();

            Console.Write("Podaj tekst do zaszyfrowania: ");
            string textToEncrypt = Console.ReadLine();
            string encryptedText = p.Encrypt(textToEncrypt);
            Console.WriteLine("Zaszyfrowany tekst: {0}", encryptedText);
        }
    }
}
