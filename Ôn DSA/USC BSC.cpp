#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int a,b;
        cin >>a>>b;
        int gcd=__gcd(a,b);
        long long lcm=(long long)a*b/gcd;
        cout<<lcm<<" "<<gcd;
        cout<<endl;
    }
}