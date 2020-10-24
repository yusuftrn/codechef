#include<bits/stdc++.h>
using namespace std;

int maxSubarray(int arr[], int n, int k){
    int s = 0;
    for (int i=0; i<k; i++)
        s += arr[i];
    int p = s;
    for (int i=k; i<n; i++){
        p += arr[i] - arr[i-k];
        s = max(s, p);
    }
    return s;
}
int main(void){
    int n,k; cin>>n>>k;
    int arr[n];
    for(int i=0;i<n;i++)
        cin>>arr[i];
    cout << maxSubarray(arr, n, k);
}
//https://www.hackerrank.com/contests/inzva-algorithm-program-2019-2020-qualification/challenges/max-subarray
