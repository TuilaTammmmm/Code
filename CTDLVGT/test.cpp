#include <iostream>
#include <iomanip>
#define MAX 100
int X[MAX], Check[MAX], n, k, dem = 0;
bool OK = true;
using namespace std;
void check()
{
    int i = k;
    int j = 0;
    while (i--)
    {
        if (X[i] == Check[i])
            j++;
    }
    if (j == k)
        Next_Combination();
}
void Next_Combination()
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
        OK = false;
}

void Result(void)
{
    for (int i = 1; i <= k; i++)
        cout << X[i] << setw(3);
    cout << endl;
}

int main(void)
{
    int t;
    cin >> t;
    while (t--)
    {
        cin >> n >> k;
        for (int i = 1; i <= k; i++)
            X[i] = i;
        for (int i = 1; i <= k; i++)
            cout << Check[i] << " ";
        while (OK)
        {
            cout << "\n Kết quả " << ++dem << ":";
            for (int i = 1; i <= k; i++)
                cout << X[i] << setw(3);
            Next_Combination();
            check();
        }
    }
}