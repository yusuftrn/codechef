#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int t; cin>>t;
    while(t--) {
        int i,j,n;
        cin >> n;
        string fir[n];
        string sec[n];
        for  (i=0; i < n; i++)
            cin >> fir[i] >> sec[i];
        for(i=0; i<n;i++){
            int f=0;
            for(j=0;j<n;j++){
                if(fir[i].compare(fir[j])==0 && i!=j){
                    f=1;
                    break;
                }
            }
            if(f==1)
                cout<<fir[i]<<" "<<sec[i]<<endl;
            else
                cout<<fir[i]<<endl;
        }
    }
}
