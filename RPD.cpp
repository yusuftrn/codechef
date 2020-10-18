#include <bits/stdc++.h>
using namespace std;
int sumOf(int p){
    int s=0;
    while(p>0){
        s+=p%10;
        p=p/10;
    }
    return s;
}
int main(void){
    int t; cin>>t;
    while(t--){
        int n; cin>>n;
        int arr[n], p;
        vector<int> v;
        for(int i=0;i<n;i++)
            cin>>arr[i];
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                p = arr[i]*arr[j];
                v.push_back(sumOf(p));
            }
        }
        int size = v.size();
        sort(v.begin(),v.end());
        cout<<v[size-1]<<endl;
    }
}

