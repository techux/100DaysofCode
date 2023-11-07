// Programmed By : Devesh Singh
// Date : 07 November 2023 | 23:45:49
// Title : Pattern 3 - Half pyramid of Number

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n ;

    for (int i=1 ; i<=n ; i++){
        for(int j=1 ; j<=i ; j++){
            cout << j << " " ;
        }
        cout << endl ;
    }
    
    return 0;
}