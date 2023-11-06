// Programmed By : Devesh Singh
// Date : 06 November 2023 | 23:59:39
// Title : Pass By Reference in Arrays

#include <iostream>
using namespace std;

void modify(int arr[]){
    arr[0] = arr[0] + 10 ;
    cout << "Inside function, arr[0] : " << arr[0] << endl ;
}

int main() {
    int size = 5 ;
    int arr[5] = {1,2,3,4,5} ;

    cout << "Before pass by reference, value at arr[0] : " << arr[0] << endl ;

    modify(arr) ;

    cout << "After pass by reference, value at arr[0] : " << arr[0] << endl ;
    
    return 0;
}