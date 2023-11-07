// Programmed By : Devesh Singh
// Date : 07 November 2023 | 23:56:50
// Title : Pattern 6 - Inverter Number Pyramid

// Pattern for n=5 is :
// 1 2 3 4 5 
// 1 2 3 4 
// 1 2 3 
// 1 2 
// 1 

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n ;

    for(int i=n ; i>=1 ; i--){
        for (int j=1 ; j<=i ; j++){
            cout << j << " " ;
        }
        cout << endl ;
    }
    
    return 0;
}