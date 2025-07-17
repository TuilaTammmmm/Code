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
        int A[n];
        for (int i = 0; i < n; i++)
            cin >> A[i];
        
        sort(A, A + n);

        int temp = 999999;
        for (int i = 1; i < n; i++)
        {
            int x = A[i] - A[i - 1];
            if (x < temp) temp = x;
        }
        cout << temp << endl;
    }
}
