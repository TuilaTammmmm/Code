#include <iostream>
#include <iomanip>
#define MAX 100
using namespace std;
int X[MAX], n, dem = 0;
bool chuaxet[MAX];
float a[MAX];
void Init()
{
    cout << "\n Nhap n=";
    cin >> n;
    for (int i = 1; i <= n; i++)
        chuaxet[i] = true;
    cout << "\n Nhap mang a[]=";
    for (int i = 1; i <= n; i++)
        cin >> a[i];
}
void Result(void)
{
    cout << "\n Ket qua " << ++dem << ":";
    for (int i = 1; i <= n; i++)
        cout << a[X[i]] << setw(3);
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
    Init();
    Try(1);
}