#include <iostream>
#include <iomanip>
#define MAX 100
using namespace std;
int X[MAX], n, dem = 0;
bool chuaxet[MAX];
void Result(void)
{
    cout << "\n Ket qua " << ++dem << ":";
    for (int i = 1; i <= n; i++)
        cout << X[i] << setw(3);
}
void Try(int i)
{
    for (int j = 1; j <= n; j++)
    {
        if (chuaxet[j])
        {
            X[i] = j;
            chuaxet[j] = false;
            if (i == n)
                Result();
            else
                Try(i + 1);
            chuaxet[j] = true;
        }
    }
}
int main()
{
    cout << "\n Nhap n=";
    cin >> n;
    for (int i = 1; i <= n; i++)
        chuaxet[i] = true;
    Try(1);
}