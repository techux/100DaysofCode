// Pattern : Pattern 7 - Complete Star Pyramid
// Language : C++
// Timestamp : 08 November 2023 | 13:15:03

// Patern for n=5
//     *    
//    ***   
//   *****  
//  ******* 
// *********

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n ;

    for(int i=0 ; i<n ; i++){
        // print initial space
        for(int j=0 ; j<n-i-1 ; j++){
            cout << " " ;
        }

        // print the stars
        for(int j=0 ; j<2*i+1 ; j++){
            cout << "*" ;
        }

        // print end space
        for (int j=0 ; j<n-i-1 ; j++){
            cout << " " ;
        }

        cout << endl ;
    }

   return 0;
}