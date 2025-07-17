#include <bits/stdc++.h>
#include <algorithm>
using namespace std;
void sort()
{
    int n;
    cin >> n;
    int A[n], B[n];
    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
        B[i] = A[i];
    }
    sort(B, B + n);
    int start = 0;
    int end = n - 1;
    while (start < n && A[start] == B[start])
        start++;
    while (end >= 0 && A[end] == B[end])
        end--;
    cout << start + 1 << " " << end + 1 << endl;
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        sort();
    }
}