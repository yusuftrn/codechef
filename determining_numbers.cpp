#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin>>n;
    int num[n],arr[1000],h=0;
    for(int i=0;i<n;i++)
        cin>>num[i];
    sort(num,num+n);
    for(int i=0;i<n;i++){
        if(num[i]!=num[i+1]&&num[i]!=num[i-1]){
            arr[h]=num[i];
            h++;
        }
    }
    sort(arr,arr+2);
    cout<<arr[0]<<" "<<arr[1];
}
