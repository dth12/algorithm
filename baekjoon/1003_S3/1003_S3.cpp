#include <bits/stdc++.h>
using namespace std;

vector<int> v;

void add_case(vector<int>& vec, int target_size) {
    while (vec.size() < target_size) {
        int size = vec.size();
        int zero = vec[size - 2] + vec[size - 4];
        int one = vec[size - 1] + vec[size - 3];

        vec.push_back(zero);
        vec.push_back(one);
    }
    return;
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int tc;
    cin >> tc;

    v.push_back(1);
    v.push_back(0);
    v.push_back(0);
    v.push_back(1);
    v.push_back(1);
    v.push_back(1);

    for (int t = 0; t < tc; t++) {
        int n;
        cin >> n;

        int target_size = 2 * (n + 1);
        int size = v.size();
        if (size < target_size) {
            add_case(v, target_size);
        }

        cout << v[target_size - 2] << " " << v[target_size - 1] << '\n';
    }
}