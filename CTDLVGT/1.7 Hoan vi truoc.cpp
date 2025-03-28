#include <iostream>
#include <iomanip>
#define MAX 100
int X[MAX], n, dem = 0;
bool OK = true;
using namespace std;
void Next_Permutation(void)
{
    int j = n - 1;
    while (j > 0 && X[j] > X[j + 1])
        j--;
    if (j > 0)
    {
        int k = n;
        while (X[j] > X[k])
            k--;
        int t = X[j];
        X[j] = X[k];
        X[k] = t;
        int r = j + 1, s = n;
        while (r <= s)
        {
            t = X[r];
            X[r] = X[s];
            X[s] = t;
            r++;
            s--;
        }
    }
    else
        OK = false;
}
int main(void)
{
    int t;
    cin >> t;
    while (t--)
    {
        cin >> n;
        for (int i = 1; i <= n; i++)
        {
            cin >> X[i];
        }
        Next_Permutation();
        if (OK)
        {
            for (int i = 1; i <= n; i++)
                cout << X[i] << " ";
            cout << endl;
        }
        else
        {
            for (int i = n; i <= 1; i++)
            {
                X[i] = i;
                cout << X[i] << " ";
            }
            cout << endl;
        }
    }
}
