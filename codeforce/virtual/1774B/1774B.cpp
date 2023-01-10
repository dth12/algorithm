#include <bits/stdc++.h>
using namespace std;

int arr[100001];

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int tc;
    cin >> tc;
    for (int c = 0; c < tc; c++) {
        int n, m, k;
        cin >> n >> m >> k;

        int max_num = n / k + 1;
        int count = n % k;
        
        for (int i = 0; i < m; i++) {
            int color_num;
            cin >> color_num;
            
            if (color_num == max_num) count--;
            if (color_num > max_num) count = -100;
        }

        if (count >= 0) {
            cout << "YES" << '\n';
        } else {
            cout << "NO" << '\n';
        }
    }
}