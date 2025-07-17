#include <bits/stdc++.h>
#include <algorithm>
using namespace std;
int nhap(int A[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
    }
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int A[n], B[n];
        nhap(A, n);
        nhap(B, n);
        int m=2*n;
        vector<int> C(m);
        vector<int> D(m);
        set_union(A, A + n, B, B + n, back_inserter(C));
        set_intersection(A, A + n, B, B + n, back_inserter(D));
        for (int i = 0; i < m; i++)
        {
            cout << C[i] << " ";
        }
        for (int i = 0; i < m; i++)
        {
            cout << D[i] << " ";
        }
    }
}