// Programmed By : Devesh Singh
// Date : 07 November 2023 | 23:49:08
// Title : Pattern 4 - Half Pyramid of number part 2

// Pattern for n=5 is
// 1 
// 2 2 
// 3 3 3 
// 4 4 4 4 
// 5 5 5 5 5 

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i=1 ; i<=n ; i++){
        for(int j=1 ; j<=i ; j++){
            cout << i << " " ;
        }
        cout << endl ;
    }
    
    return 0;
}