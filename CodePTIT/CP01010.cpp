#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

void TestCase()
{
    int n;
    cin >> n;
    int a[n + 1];
    f[0] = 0;
    for (int i = 1; i <= n; ++i)
    {
        cin >> a[i];
        f[i] = f[i - 1] + a[i];
    }
    for (int i = 1; i <= n; ++i)
    {
        int sL = f[i - 1];
        int sR = f[n] - sL - a[i];
        if (sL == sR)
        {
            cout << i << endl;
            return;
        }
    }
    cout << "-1\n";
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;
    while (T--)
        TestCase();
    return 0;
}
