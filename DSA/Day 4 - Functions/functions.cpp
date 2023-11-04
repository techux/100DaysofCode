// Problem : Learning Functions
// Language : C++
// Submission Timestamp : 04 November 2023 | 23:39:09

#include <iostream>
using namespace std ;

void simple_function(){
    cout << endl << "I am a Simple no return type (void) function " << endl ;
}

int return_function(){
    cout << "I am return type (int) function with no parameter : " ;
    return 17+27 ;
}

void parameterized_function(int x, int y){
    cout << endl << "I am void type parameterized function. Sum : "<< x +y ;
}

int return_parameterised_function(int x, int y){
    cout << endl << "I am int return type parameterised function. Difference : " ;
    return x-y ;
}

int main(){
    simple_function() ;

    cout << return_function() ;

    parameterized_function(10,20) ;

    cout << return_parameterised_function(27,17) ;

    return 0 ;
}