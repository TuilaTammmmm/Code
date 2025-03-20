#include <iostream>
#include <iomanip>
#define MAX 100
int X[MAX], n, k, dem = 0;
bool OK = true;
using namespace std;

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
        OK = false;
}

int main(void)
{
    cin >> n >> k;
    for (int i = 1; i <= k; i++)
        X[i] = i;
    while (OK)
    {
        cout << "\n Kết quả " << ++dem << ":";
        for (int i = 1; i <= k; i++)
            cout << X[i] << setw(3);
        Next_Combination();
    }
}