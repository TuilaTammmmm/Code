
#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

void TestCase()
{
    int n, k;
    cin >> n >> k;
    int a[n];
    for (auto &x : a)
        cin >> x;
    sort(a, a + n);
    int d = 0;
    for (int i = 0; i < n; ++i)
    {
        if (a[i] > k / 2)
            break;
        if (l != n)
        {
            d += u - l;
        }
    }
    cout << d << endl;
}

int main()
{
    int T;
    cin >> T;
    while (T--)
        TestCase();
    return 0;
}
