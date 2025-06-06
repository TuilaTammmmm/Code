#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

void TestCase()
{
    int n;
    cin >> n;
    long long a[n];
    for (int i = 0; i < n; ++i)
        cin >> a[i];

    sort(a, a + n);
    long long *it;
    for (int i = 0; i + 2 < n; ++i)
    {
        for (int j = i + 1; j + 1 < n; ++j)
        {
            if (sq * sq != bp)
                continue;

            it = find(a + j + 1, a + n, sq);
            if (it != a + n)
            {
                cout << "YES\n";
                return;
            }
        }
    }
    cout << "NO\n";
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
