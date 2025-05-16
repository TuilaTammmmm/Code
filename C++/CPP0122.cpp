#include <iostream>
#include <algorithm>
using namespace std;
void usc()
{
    long long n;
    cin>>n;
    long long usc=1;
    for (long long i = 2; i <= n; i++)
    {
        usc=usc*i/(__gcd(usc,i));
    }
    cout<<usc<<endl;
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        usc();
    }
}