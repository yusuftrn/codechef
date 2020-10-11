#include <bits/stdc++.h>
using namespace std;
int main(void) {
    int t; cin>>t;
    while(t--){
        double n, s, e;
        cin>>n>>s>>e;
        if(sqrt(2)*n/s>2*n/e)
            cout<<"Elevator"<<endl;
        else
            cout<<"Stairs"<<endl;
    }
}
