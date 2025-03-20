#include <iostream>
#include <iomanip>
#define MAX 100
using namespace std;
int X[MAX], n, k, dem = 0;
void Init()
{ // thiết lập giá trị cho n, k
    cout << "\n Nhập n, k: ";
    cin >> n >> k;
}
void Result(void)
{
    cout << "\n Kết quả " << ++dem << ":"; // đưa ra kết quả
    for (int i = 1; i <= k; i++)
        cout << X[i] << setw(3);
}
void Try(int i)
{ // thuật toán quay lui
    for (int j = X[i - 1] + 1; j <= n - k + i; j++)
    {                   // duyệt trên tập khả năng dành cho xi
        X[i] = j;       // thiết lập thành phần xi là j
        if (i == k)     // nếu xi đã là thành phẩn cuối
            Result();   // ta đưa ra kết quả
        else            // trong trường hợp khác
            Try(i + 1); // ta đi xác định thành phần thứ xi+1
    }
}
int main(void)
{
    Init();
    X[0] = 0;
    Try(1);
}