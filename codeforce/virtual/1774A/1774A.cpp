#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int ntc;
    cin >> ntc;

    for (int tc = 0; tc < ntc; tc++) {
        string str;
        int n;
        int total = 0;

        cin >> n >> str;

        for (int i = 0; i < n; i++) {
            int d = str[i] - '0';

            if (i == 0) {
                total += d;
                continue;
            }

            if (total == 1) {
                if (d == 1) total = 0;
                cout << "-";
            } else {
                if (d == 1) total = 1;
                cout << "+";
            }
        }

        cout << '\n';
    }
}