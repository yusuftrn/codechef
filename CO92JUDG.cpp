#include <bits/stdc++.h>
using namespace std;
int main(void) {
    int t;  cin>>t;
    while(t--){
        int n; cin>>n;
        int i, a[n], b[n], sumA=0, sumB=0;
        for(i=0; i<n; i++){
            cin>>a[i];
        }
        for(i=0; i<n; i++){
            cin>>b[i];
        }
        sort(a,a+n);
        sort(b,b+n);
        for(i=0;i<n-1; i++){
            sumA += a[i];
            sumB += b[i];
        }
        if(sumA<sumB)
            cout<<"Alice"<<endl;
        else if(sumA>sumB)
            cout<<"Bob"<<endl;
        else
            cout<<"Draw"<<endl;
    }
}
