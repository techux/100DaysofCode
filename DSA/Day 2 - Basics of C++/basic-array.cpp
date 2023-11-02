// Programmed By : Devesh Singh
// Date : 02 November 2023 | 23:38:01
// Title : Practicing basic of array with Striver

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
    
    int arr[size] ;

    cout << "Enter values " << endl ;

    for (int i=0 ; i<size ; i++){
        cin >> arr[i];
    }

    printArray(arr,5) ;
    
    return 0;
}