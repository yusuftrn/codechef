#include <bits/stdc++.h>
using namespace std;

int Tn;
string s;
bool ok;

int main (int argc, char * const argv[]) {
    cin >> Tn;
    assert(1 <= Tn && Tn <= 100);
    while (Tn--) {
        cin >> s;
        for(char i : s) {
            assert('A' <= i && i <= 'Z');
        }
        assert(2 <= s.length() && s.length() <= 100);
        bool ok = true;
        for(int i = 0; i < s.length(); i++)
            if (s[i] != s[i % 2]) {
                ok = false;
                break;
            }
        if (s[0] == s[1])
            ok = false;
        if (ok)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}
TICKETS5
