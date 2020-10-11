#include <bits/stdc++.h>
using namespace std;
int main(void) {
    int t; cin>>t;
    while(t--){
        int chef=0,bob=0;
        string s; cin>>s;
        for(int i=0;i<s.length();i++){
            if(s[i]=='1')
                chef++;
            else
                bob++;
        }
        if(chef>bob+1)
            cout<<"WIN"<<endl;
        else
            cout<<"LOSE"<<endl;

    }
}
