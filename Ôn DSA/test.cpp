#include <bits/stdc++.h>
using namespace std;

set<string> result;

void permute(string s, int l, int r) {
    if (l == r) result.insert(s);
    else {
        for (int i = l; i <= r; i++) {
            swap(s[l], s[i]);
            permute(s, l + 1, r);
            swap(s[l], s[i]); // backtrack
        }
    }
}

int main() {
    string s = "aab";
    permute(s, 0, s.size() - 1);
    for (auto &x : result) cout << x << "\n";
}
