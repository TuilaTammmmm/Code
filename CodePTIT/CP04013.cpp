
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int sl;
    cin >> sl;
    for (int i = 0; i < sl; ++i)
    {
        int x;
        cin >> x;
        if (x >= 0)
            a[n++] = x;
        else
            b[m++] = x;
    }
    sort(a, a + n, greater<int>());
    sort(b, b + m);

    vector<int> res;
    if (m >= 2)
    {
        res.push_back(b[0] * b[1]);
        if (n >= 1)
            res.push_back(res.back() * a[0]);
    }
    if (n >= 2)
    {
        res.push_back(a[0] * a[1]);
        if (n >= 3)
            res.push_back(res.back() * a[2]);
    }
    sort(res.rbegin(), res.rend());
    cout << res[0];
    return 0;
}
