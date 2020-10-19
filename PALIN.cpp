#include <bits/stdc++.h>
using namespace std;

string s;
void push(int pos){
    s[pos]++;
    if(s[pos]==':'){
        s[pos] == '0';
        if(pos>0)
            push(pos-1);
        else
            s.insert(s.begin(), '1');
    }
}
int main(void){
    int t; cin>>t;
    while(t--){
        cin>>s;
        int sLen = s.length();
        push(sLen-1);
        for(int i=0; i<sLen/2;i++){
            int left=i, right = sLen-i-1;
            while(s[left] != s[right])
                push(right);
        }
        cout<<s<<endl;
    }
}
