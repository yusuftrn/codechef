#include <bits/stdc++.h>
#define lli long long int
using namespace std;

int main(void) {
    int t; cin>>t;
    while(t--){
        int x=0, y=0;
        int n; cin>>n;
        char c =' ', p=' ';
        string s; cin>>s;
       for(int i=0;i<s.length();i++){
           if(s[i]=='L' || s[i]=='R')
               c = 'x';
           else if(s[i]=='U' || s[i] =='D')
               c = 'y';

           if (p == c)
               continue;
           else if(s[i] =='L')
               x-=1;
           else if(s[i]=='R')
               x+=1;
           else if(s[i]=='U')
               y+=1;
           else if(s[i]=='D')
               y-=1;

           if(s[i]=='L' || s[i]=='R')
               p = 'x';
           else if(s[i]=='U' || s[i] =='D')
               p = 'y';
       }
       cout<<x<<" "<<y<<endl;
    }
}
