// Programmed By : Devesh Singh
// Date : 09 November 2023 | 23:34:35
// Title : CPP STL Pairs

// CPP program to illustrate Pair in STL
#include <iostream>
#include <utility>
using namespace std;

int main()
{
	// Pair of Integers
	pair<int, int> number;
	number.first = 100;
	number.second = 69 ;
	cout << number.first << endl ;
	cout << number.second << endl;

	// Pair of characters
	pair<char,char> character ;
	character.first = 'D' ;
	character.second = 'R' ;
	cout << character.first << endl ;
	cout << character.second << endl;

	// Pair of Strings
	pair<string,string> str ;
	str.first = "Devesh" ;
	str.second = "Roshni" ;
	cout << str.first << endl ;
	cout << str.second << endl;

	// Pair of number and character
	pair<char,int> info ;
	info.first = 'Y' ;
	info.second = 1 ;
	cout << info.first << endl ;
	cout << info.second << endl;

	// Pair of String and number 
	pair <string,int> data ;
	data.first = "Devesh" ;
	data.second = 8725 ;
	cout << data.first << endl ;
	cout << data.second << endl ;

    return 0;

}
