// Problem : https://www.codingninjas.com/studio/problems/sum-of-even-odd_624650
// Language : C++
// Submission Timestamp : 03 November 2023 | 23:38:30

#include<iostream>
using namespace std;

int main() {
	int n;
    cin>>n;

    int even = 0;
    int odd =0;

    while(n){
        int digit= n%10;
        if(digit%2==0){
            even+=digit;
        }
        else{
            odd+=digit;
        }
        n=n/10;
    }

    cout<<even<<" "<<odd;
}
