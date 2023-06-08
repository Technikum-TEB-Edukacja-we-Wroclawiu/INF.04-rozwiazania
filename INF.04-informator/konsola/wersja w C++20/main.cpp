#include <iostream>
#include <map>
#include <string>

using namespace std;

class Gaderypoluki {
private:
	map<char, char> substitutions{
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

public:
	/* ******************************************************************************************
	* nazwa funkcji:       encryptText
	*
	* parametry wejściowe: textToEncrypt - napis, który należy zaszyfrować
	* wartość zwracana:    zaszyfrowany tekst
	* opis funkcji:        Funkcja szyfruje podany tekst szyfrem przestawieniowym gaderypoluki,
	*                      który zamienia pary liter g-a, d-e, r-y, p-o, l-u, k-i między sobą
	*                      (g na a, a na g itp.).
	* autor:               961009xxxxx
	***************************************************************/
	string encryptText(string textToEncrypt) {
		string encryptedText = "";
		for (char c : textToEncrypt) {
			if (auto tmpChar = substitutions.find(c); tmpChar != substitutions.end()) {
				encryptedText += tmpChar->second;
			}
			else if (auto tmpChar = substitutions.find(tolower(c)); tmpChar != substitutions.end()) {
				encryptedText += toupper(tmpChar->second);
			}
			else {
				encryptedText += c;
			}
		}

		return encryptedText;
	}
};

int main()
{
	Gaderypoluki gaderypoluki;

	cout << "Wprowadź tekst do zaszyfrowania: ";
	string textToEncrypt;
	getline(cin, textToEncrypt);
	cout << "Zaszyfrowany tekst: " << gaderypoluki.encryptText(textToEncrypt);
}
