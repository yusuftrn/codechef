#include <bits/stdc++.h>
using namespace std;

int matchCount(int n){
    int stick = 0;
    if(n == '0')
        stick =6;
    else if(n == '1')
        stick =2;
    else if(n == '2')
        stick =5;
    else if(n == '3')
        stick =5;
    else if(n == '4')
        stick =4;
    else if(n == '5')
        stick =5;
    else if(n == '6')
        stick =6;
    else if(n == '7')
        stick =3;
    else if(n == '8')
        stick =7;
    else if(n == '9')
        stick =6;
    return stick;
}

int main(void){
    int t; cin>>t;
    while(t--){
        int x,y,c=0;
        cin>>x>>y;
        int sum = x+y;
        string s = to_string(sum);
        for(int i=0; i<s.length();i++){
            c += matchCount(s[i]);
        }
        cout<<c<<endl;
    }
}MATCHES
