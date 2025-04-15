#include <iostream>
#include <vector>
using namespace std;
vector <int> a;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, dem1 = 0, dem2 = 0;
        cin >> n;
        a.resize(n);
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
            if (a[i] % 2 == 0) dem1++;
            else dem2++;
        }
        cout << dem1 << " " << dem2 << endl;
    }
}