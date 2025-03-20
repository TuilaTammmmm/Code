#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    if (b == 0) {
        cout << "0";
    } else {
        cout << a + b << " ";                      // Tổng
        cout << a - b << " ";                      // Hiệu
        cout << a * b << " ";                      // Tích
        cout << fixed << setprecision(2) << (float)a / b << " "; // Chia kết quả thực
        cout << a % b;                             // Chia phần dư
    }

    return 0;
}