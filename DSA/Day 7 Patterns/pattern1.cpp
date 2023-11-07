// Programmed By : Devesh Singh
// Date : 07 November 2023 | 23:35:12
// Title : Pattern Problem 1

// Pttern is for n=5 :
// * * * * * 
// * * * * *
// * * * * *
// * * * * *
// * * * * * 

#include <iostream>
using namespace std;

int main() {

    int n ;
    cin >> n ;

    for (int i=0 ; i<n ; i++){
        for(int j=0 ; j<n ; j++){
            cout << "* " ;
        }
        cout << endl ;
    }

    return 0;
}