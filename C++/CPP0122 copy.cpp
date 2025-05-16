#include <iostream>
using namespace std;
typedef long long ll;
ll gcd(ll a, ll b)
{
    while (b > 0)
    {
        ll x = a % b;
        a = b;
        b = x;
    }
    return a;
}
ll usc()
{

    ll n;
    cin >> n;
    ll usc = 1;
    for (ll i = 1; i <= n; i++)
    {
        ll temp = gcd(usc, i);
        usc = usc * i / temp;
    }
    cout << usc << endl;
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        usc();
    }
}