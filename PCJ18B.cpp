#include <bits/stdc++.h>
using namespace std;
int main(void){
  int t; cin>>t;
  while(t--){
    int n; cin>>n;
    int i=0, s=0;
    while(i<n){
      s+=(n-i)*(n-i);
      i+=2;
    }
    cout<<s<<endl;
  }
}
