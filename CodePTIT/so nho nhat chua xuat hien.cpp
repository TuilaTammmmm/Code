#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> A(n);
        for (int i = 0; i < n; i++)
            cin >> A[i];

        set<int> s;
        for (int x : A)
            if (x > 0)
                s.insert(x);

        int kq = 1;
        for (int x : s)
        {
            if (x == kq)
                kq++;
            else if (x > kq)
                break;
        }
        cout << kq << endl;
    }
}
