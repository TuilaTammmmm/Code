#include <bits/stdc++.h>
using namespace std;
void Sum()
{
    int n;
    cin >> n;
    double S = 0;
    for (int i = 1; i <= n; i++)
    {
        S += 1.0/i;
    }
    cout << setprecision(4) << fixed << S;
}
int main()
{
    Sum();
    return 0;
}