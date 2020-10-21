#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int n,t;
    string s;
    cin>>t;
    while(t--){
        cin>>n; cin>>s;
        bool _h=1, _t=0, v=1;
        int _ch=0, _ct=0;
        for(int i=0; i<n; i++){
            if( s[i]=='.' )
                continue;
            else if( s[i]=='H' && _h==1 )
                _t=1, _h=0, _ch++;
            else if( s[i]=='T' && _t==1 )
                _t=0, _h=1, _ct++;
            else
                v=0;
        }
        if( v==0 || _ch!=_ct)
            cout<<"Invalid"<<endl;
        else
            cout<<"Valid"<<endl;
    }
}
