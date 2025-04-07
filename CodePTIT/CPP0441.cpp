
#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

void TestCase()
{
    int n, x;
    cin >> n >> x;
    int a[n];
    for (auto &so : a) cin >> so;
    for (int i = 0; i < n; ++i) {
        if (a[i] == x) {
            cout << i + 1 << endl;
            return;
        }
    }
    cout << "-1\n";
}

int main()
{
    int T;
    cin >> T;
    while (T--) TestCase();
    return 0;
}
