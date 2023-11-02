// Problem : https://www.codingninjas.com/studio/problems/nth-fibonacci-number_74156
// Language : C++
// Submission Timestamp : 02 November 2023 | 23:51:31

#include<bits/stdc++.h>
using namespace std;

int main(){

        int a = 0;
        int n;
        cin>>n;
        int sum;
        int b = 1;

        if(n == 1){
                sum = 1;
        }

        for(int i=1 ; i<n ; i++){
                sum = a+b;
                a = b;
                b = sum;
        }
        cout<<sum;

        return 0;
}