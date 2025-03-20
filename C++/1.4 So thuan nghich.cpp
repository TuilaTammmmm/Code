#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main()
{
    int t;
    cin >> t;
    cin.ignore();
    while (t--)
    {
        string n;
        getline(cin, n);
        string m = n;
        reverse(m.begin(), m.end());
        if (m == n)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}