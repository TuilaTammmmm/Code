#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("data.in", "r", stdin);
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int a[n];
        int cnt1 = 0, cnt2 = 0;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            if (a[i] % 2 == 0) 
                cnt1++;
            else 
                cnt2++;
        }
        cout << cnt1 << " " << cnt2 << endl;
    }
    return 0;
}