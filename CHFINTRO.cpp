#include <bits/stdc++.h>
using namespace std;

int main(void){
    int n, R;
    cin>>n>>R;
    while(n--){
        int r;
        cin>>r;
        if(R>r)
            cout<<"Bad boi"<<endl;
        else
            cout<<"Good boi"<<endl;
    }
}

