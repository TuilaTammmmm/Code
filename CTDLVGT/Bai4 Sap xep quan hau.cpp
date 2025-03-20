#include <iostream>
#include <iomanip>
#define MAX 100
using namespace std;
int X[MAX], n, dem = 0;
bool cot[MAX], dcxuoi[MAX], dcnguoc[MAX];
void Init()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cot[i] = true;
    }
    for (int i = 1; i < 2 * n; i++)
    {
        dcxuoi[i] = true;
        dcnguoc[i] = true;
    }
}
void Result(void)
{
    cout << dem;
}
void Try(int i)
{
    for (int j = 1; j <= n; j++)
    {
        if (cot[j] && dcxuoi[i - j + n] && dcnguoc[i + j - 1])
        {
            X[i] = j;
            cot[j] = false;
            dcxuoi[i - j + n] = false;
            dcnguoc[i + j - 1] = false;
            if (i == n)
                dem++;
            else
                Try(i + 1);
            cot[j] = true;
            dcxuoi[i - j + n] = true;
            dcnguoc[i + j - 1] = true;
        }
    }
}
int main(void)
{
    int t;
    cin >> t;
    while (t--)
    {
        Init();
        Try(1);
        Result();
    }
}