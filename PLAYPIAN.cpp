#include <bits/stdc++.h>
using namespace std;

int main(){
    int T; cin>>T;
    while(T--){
        string s; cin>>s;
        int flag = 0;
        for(int i=0; i<s.length();i+=2){
            if(s[(i)]== s[(i+1)])
                flag=1;
        }
        if(flag==1)
            cout<<"no"<<endl;
        else
            cout<<"yes"<<endl;
    }
}
