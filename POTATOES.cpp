#include <bits/stdc++.h>
using namespace std;

bool isPrime(int n){
    if(n == 0 || n == 1)
        return false;
    for(int i=2; i<n; i++)
        if(n%i == 0)
            return false;
    return true;
}

int  main(){
    int t,x,y,i;
    cin>>t;
    while(t--){
        cin>>x>>y;
        int sum, i;
        sum = x+y; i = sum+1;
        while(true){
            if(isPrime(i)==1){
                break;
            }
            i++;
        }
        cout<<i-sum<<"\n";
    }
}
