// Programmed By : Devesh Singh
// Date : 05 November 2023 | 23:40:26
// Title : Pass by reference and Pass by Value

#include <iostream>
using namespace std;

void pass_by_value(int x) {
    cout << "Inside Function, Value of X is : "<< x << endl;
    x = x+10 ;
    cout << "After incrementing x in function X = " << x << endl ;
}

void pass_by_reference(int &y){
    cout << "Inside value of Y : " << y << endl ;
    y = y+10;
    cout << "After incrementing, Y = " << y << endl ;
}

int main() {
    // Pass by Value
    int x = 10 ;
    cout << "Initialy Value of X = : " << x << endl ;
    pass_by_value(x) ;
    cout << "Outside Function, Value of X is : " << x << endl;

    cout << endl << endl << endl ;
    // Pass by Reference
    int y = 10 ;
    cout << "Initialy Value of Y = : " << y << endl ;
    pass_by_reference(y) ;
    cout << "Outside Function, Value of Y is : " << y << endl;


    return 0;
}