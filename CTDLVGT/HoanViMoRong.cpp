#include <iostream>
using namespace std;
int X[50];
float a[50];
int n, k;
int OK = 1;
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
        int t = X[j];
        X[j] = X[k];
        X[k] = t; // đổi chỗ X[j] cho X[k]
        int r = j + 1, s = n;
        while (r <= s)
        { // lật ngược lại đoạn từ j+1,..,n
            t = X[r];
            X[r] = X[s];
            X[s] = t;
            r++;
            s--;
        }
    }
    else            // nếu là cấu hình cuối cùng
        OK = false; // ta kết thúc duyệt
}
void result()
{
    for (int i = 1; i <= n; i++)
        cout << a[X[i]] << "\t";
    cout << "\n";
}
void Init(void)
{ // thiết lập tập con đầu tiên
    cin >> n >> k;
    for (int i = 1; i <= n; i++)
        cin >> a[i];
    for (int i = 1; i <= n; i++) // tập con đầu tiên là 1, 2, .., k
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
        Next_Permutation();
    }
}