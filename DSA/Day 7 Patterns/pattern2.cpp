// Programmed By : Devesh Singh
// Date : 07 November 2023 | 23:39:31
// Title : Pattern 2 - Half Pyramid of star

// Pattern for n=5 is

// * 
// * * 
// * * * 
// * * * * 
// * * * * * 

#include <iostream>
using namespace std;


int main() {
    int n ;
    cin >> n ;

    for (int i=1 ; i<=n ; i++){
        for(int j=0 ; j<i ; j++){
            cout << "* " ;
        }
        cout << endl ;
    }
    
    return 0;
}