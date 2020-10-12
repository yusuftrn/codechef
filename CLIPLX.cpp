#include <bits/stdc++.h>
using namespace std;

int getMax(int x, int y){
    if(x>y)
        return x;
    else
        return y;
}
int main(void){
    int t; cin>>t;
    while(t--){
        int x, y; cin>>x>>y;
        cout<<getMax(0,x-y)<<endl;
    }
}
