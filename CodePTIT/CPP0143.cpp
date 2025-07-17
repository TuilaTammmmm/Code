
#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

vector<long long> f;
void fibo()
{
    f.push_back(0);
    f.push_back(1);
    f.push_back(1);
    for (int i = 3; i <= 92; ++i)
        f.push_back(f[i - 1] + f[i - 2]);
}
int main()
{

    fibo();
    int T;
    cin >> T;
    while (T--)
        int n;
        cin >> n;
        cout << f[n] << endl;
    return 0;
}
