#include <bits/stdc++.h>
using namespace std;

char s[100005];
int main(void){
    cin>>s;
    int i, c, ch, che, chef;
    c=ch=che=chef=0;
    for(i=0; i<strlen(s); i++){
        if(s[i]=='C'){
            c++;
        }
        else if(s[i]=='H'){
            if(c>0){
                c--;
                ch++;
            }
        }
        else if(s[i]=='E'){
            if(ch>0){
                ch--;
                che++;
            }
        }
        else if(s[i]=='F'){
            if(che>0){
                che--;
                chef++;
            }
        }
    }
    cout<<chef<<endl;
}
