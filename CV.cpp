#include <bits/stdc++.h>
using namespace std;

int main(void){
    int t; cin>>t;
    set<char> keys = {'a', 'e', 'i', 'o', 'u'};
    while(t--) {
        int n,count=0;
        cin >> n;
        string s; cin>>s;
        for (int i = 0; i < n; i++)
            if(keys.find(s[i]) == keys.end() && keys.find(s[i+1]) !=keys.end())
                count++;
        cout<<count<<endl;
    }
}
