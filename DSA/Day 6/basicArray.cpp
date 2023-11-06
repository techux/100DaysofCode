// Programmed By : Devesh Singh
// Date : 06 November 2023 | 23:49:53
// Title : Basic Arrays creation and printing

#include <iostream>
using namespace std;

void printArray(int arr[] , int size){
    for(int i=0 ; i<size ; i++){
        cout<<arr[i] << " " ;
    }
    cout<< endl ;
}

int main() {
    int size = 5 ;
    int arr[5] ;

    cout << "Enter values : " ;
    for (int i=0 ; i<size ; i++){
        cin >> arr[i] ;
    }

    cout << "[Method 1] Values of array are : " << endl ;
    for (int i=0 ; i<size ; i++){
        cout << arr[i] << " ";
    }

    cout << endl << endl << "[Method 2] Printing values of array using function" << endl ;
    printArray(arr,size) ;

    

    return 0;
}