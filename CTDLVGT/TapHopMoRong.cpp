#include <iostream>
using namespace std;
int X[50];
float a[50];
int n, k;
int OK = 1;
void Next_Combination(void)
{
    int i = k;
    while (i > 0 && X[i] == n - k + i)
        i--;
    if (i > 0)
    {
        X[i] = X[i] + 1;
        for (int j = i + 1; j <= k; j++)
            X[j] = X[i] + j - i;
    }
    else
        OK = 0;
}
void result()
{
    for (int i = 1; i <= k; i++)
        cout << a[X[i]] << "\t";
    cout << "\n";
}
void Init(void)
{
    cin >> n >> k;
    for (int i = 1; i <= n; i++)
        cin >> a[i];
    for (int i = 1; i <= k; i++) 
    {
        X[i] = i;
    }
}
int main()
{
    Init();
    while (OK)
    {
        result();
        Next_Combination();
    }
}