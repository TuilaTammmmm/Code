#include <iostream>
using namespace std;

// Hàm tính tổng các chữ số của một số nguyên
int sum(int n)
{
    int x = 0;
    while (n > 0) {
        x += n % 10; // Lấy chữ số cuối cùng và cộng vào tổng
        n /= 10;     // Loại bỏ chữ số cuối cùng
    }
    return x; // Trả về tổng các chữ số
}

int main()
{
    int n;
    cin >> n;
    cout << sum(n);
   return 0;
}
