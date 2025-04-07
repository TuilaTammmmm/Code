#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

void TestCase()
{
    long long n, k;
    cin >> n >> k;
    long long r = 0;
    for (int i = 1; i <= n; ++i)
        r += i % k;
    cout << (r == k) << endl;
}

int main()
{
    int T;
    cin >> T;
    while (T--)
        TestCase();
    return 0;
}