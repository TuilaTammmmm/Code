#include <iostream>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int found = 1;
        for (int p = 2; p * p <= n; p++) {
            if (n % p == 0) {
                found = 0;
                break;
            }
        }
        if(found==1) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
}