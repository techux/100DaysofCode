// Programmed By : Devesh Singh
// Date : 07 November 2023 | 23:52:06
// Title : Pattern 5 - Inverted Half Phyramid

// Pattern for n=5 is :
// * * * * * 
// * * * * 
// * * * 
// * * 
// * 

#include <iostream>
using namespace std;

int main() {
    int n; 
    cin >> n ;

    for (int i=0 ; i<n ; i++){
        for (int j=n ; j>i ; j--){
            cout << "* " ;
        }
        cout << endl ;
    }
    
    return 0;
}