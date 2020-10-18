#include <bits/stdc++.h>
using namespace std;

int main(void){
    int t; cin>>t;
    while(t--){
        vector<int> a;
        while(true){
            int n; cin>>n;
            a.push_back(n);
            char c =getchar();
            if(c!=' ')
                break;
        }
        int size = a.size() -1;
        sort(a.begin(), a.end());
        if(size!=a[size])
            cout<<a[size]<<endl;
        else
            cout<<a[size-1]<<endl;
    }
}

