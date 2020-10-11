#include <bits/stdc++.h>
using namespace std;
int main(void){
  int n; cin>>n;
  while(n--){
    int f=0;
    string s;
    cin>>s;
    for(int i=0;i<s.length(); i++){
      if(s[i] =='>'){
        s[i]='<';
      }
      else if(s[i]=='<'){
        s[i]='>';
      }
    }
    for(int i=0;i<=s.length()-1; i++){
      if(s[i] == '>' && s[i+1]=='<'){
        f++;
      }
    }
    cout<<f<<endl;
  }
}
