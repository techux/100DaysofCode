// Problem : https://www.codingninjas.com/studio/problems/find-character-case_58513
// Platform : Coding Ninjas
// Language : C++

#include<iostream>
using namespace std;

int main() {
	char ch ;

	cin >> ch ;

	if ((int)ch>=65 && (int)ch<=90){
		cout << 1 ;
	} else 
	if ((int)ch>=97 && (int)ch<=122){
		cout << 0 ;
	} else {
		cout << -1 ;
	}
	
}
