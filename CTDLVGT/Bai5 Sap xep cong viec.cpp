#include <iostream>
#include <iomanip>
#define MAX 1000
using namespace std;

int Start[MAX], Finish[MAX], n, XOPT[MAX], dem = 0;

void Init()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> Start[i] >> Finish[i];
        XOPT[i] = false;
    }
}

void Sapxep(void)
{
    for (int i = 1; i <= n - 1; i++)
    {
        for (int j = i + 1; j <= n; j++)
        {
            if (Finish[i] > Finish[j])
            {
                int t = Finish[i];
                Finish[i] = Finish[j];
                Finish[j] = t;
                t = Start[i];
                Start[i] = Start[j];
                Start[j] = t;
            }
        }
    }
}
void Result(void)
{
    cout << dem << endl;
    dem=0;
}

void Greedy_Solution(void)
{
    Init();
    Sapxep();
    int i = 1;
    XOPT[i] = true;
    dem = 1;
    for (int j = 2; j <= n; j++)
    {
        if (Finish[i] <= Start[j])
        {
            dem++;
            i = j;
            XOPT[i] = true;
        }
    }
    Result();
}

int main(void)
{
    int t;
    cin >> t;
    while (t--)
    Greedy_Solution();
}