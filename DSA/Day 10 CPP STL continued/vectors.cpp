// Programmed By : Devesh Singh
// Date : 10 November 2023 | 23:26:26
// Title : Vectors in STL

#include <bits/stdc++.h>
using namespace std;

int main() {
    vector <int> v ;  // create an integer vector

    v.push_back(10) ;  // Insert into vector
    v.emplace_back(20) ;  // Insert into vector

    cout << v[0] << " "<< v[1] << endl ;


    // vector of pair  ++++++++
    
    vector < pair<int,int> > vec ;
    vec.push_back({5,7}) ;   // insert a pair into the vector
    vec.emplace_back(13,19) ;
    cout << vec[0].first << " " << vec[0].second << endl ;



    // vector with prefilled items

    vector <int> v2(5,100) ;  // 5 times 100 item
    cout << v2[0] << " " << v2[1] << " " << v2[2] << " " << v2[3] << " " << v2[4] << endl ;

    vector <int> v3(5) ;  // Output 5 times 0 or garbage value



    // Access the vector elements
    // Method 1 - Using cout
    cout << v[0] << " "<< v[1] << endl;

    // Method 2 - using at(index_number) function
    cout << v.at(0) << " "<< v.at(1) ;
    
    return 0;
}