#include <bits/stdc++.h>
#define lli long long int
using namespace std;

int main(void) {
    int t; cin>>t;
    while(t--){
        lli a, b;
        cin >> a >>b;
        int c = 1;
        int sum=0;
        while(a!=0 || b!=0){
            lli l=a%10;
            lli m=b%10;
            sum += (((a+b)%10) * c);
            c *= 10;
            a/=10;
            b/=10;
        }
        cout<<sum<<endl;
    }
}
