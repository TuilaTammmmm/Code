#include <iostream>
#include <iomanip>
#define MAX 100
using namespace std;
int X[MAX], n, dem = 0;
bool OK = true;
void Result(void)
{
    for (int i = 1; i <= n; i++)
        cout << X[i];
    cout << endl;
}
void Next_Bits_String(void)
{
    int i = n;
    while (i > 0 && X[i])
    {
        X[i] = 0;
        i--;
    }
    if (i > 0)
        X[i] = 1;
    else
        OK = false;
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string binary;
        cin >> binary;
        n = binary.length();
        for (int i = 0; i < n; i++)
        {
            X[i + 1] = binary[i] - '0';
        }
        Next_Bits_String();
        Result();
    }
}