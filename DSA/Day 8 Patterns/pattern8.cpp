// Pattern : Pattern 8 - Inverted full Star Pyramid
// Language : C++
// Timestamp : 08 November 2023 | 13:39:47

// Patern for n=5
// *********
//  *******
//   *****
//    ***
//     *


#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n ;

    for (int i=n ; i>0 ; i--){
        // print spaces
        for(int j=0 ; j<n-i ; j++){
            cout << " ";
        }

        // print Stars
        for(int j=0 ; j<2*i-1 ; j++){
            cout << "*";
        }
        
        // print spaces
        for(int j=0 ; j<n-i+1 ; j++){
            cout << " ";
        }

        cout << endl ;

    }

    

   return 0;
}