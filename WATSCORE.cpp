#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int t; cin>>t;
    while(t--){
        int n; cin>>n;
        int arr[12] = {0};
        for(int i=0; i<n; i++){
            int a,b;
            cin>>a>>b;
            if(arr[a] < b)
                arr[a] = b;
        }
        int score=0;
        for(int i=0; i<=8; i++){
            score+=arr[i];
        }
        cout<<score<<endl;
    }
}
