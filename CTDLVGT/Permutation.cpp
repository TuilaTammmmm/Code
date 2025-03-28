#include <iostream>
#include <iomanip>
#define MAX 100
int X[MAX], n, dem = 0;
bool OK = true;
using namespace std;
void Next_Permutation(void)
{                                    // sinh ra hoán vị kế tiếp
    int j = n - 1;                   // xuất phát từ vị trí j = n-1
    while (j > 0 && X[j] > X[j + 1]) // tìm chỉ số j sao cho X[j] < X[j+1]
        j--;
    if (j > 0)
    {                       // nếu chưa phải hoán vị cuối cùng
        int k = n;          // xuất phát từ vị trí k = n
        while (X[j] > X[k]) // tìm chỉ số k sao cho X[j] < X[k]
            k--;
        int t = X[j];X[j] = X[k];X[k] = t; // đổi chỗ X[j] cho X[k]
        int r = j + 1, s = n;
        while (r <= s)
        {
            t = X[r];X[r] = X[s];X[s] = t;
            r++;s--;
        }
    }
    else
        OK = false;
}
int main(void)
{
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin>>X[i];
    while (OK)
    {
        cout << "\n Kết quả " << ++dem << ":";
        for (int i = 1; i <= n; i++)
            cout << X[i] << setw(3);
        Next_Permutation();
    }
}
