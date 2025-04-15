#include <bits/stdc++.h> // Thư viện chuẩn bao gồm tất cả các thư viện cần thiết
using namespace std;
typedef long long LL; // Định nghĩa kiểu dữ liệu LL là long long

// Hàm tính ước chung lớn nhất (GCD) của hai số a và b
LL gcd(LL a, LL b)
{
    while (b > 0) { // Lặp cho đến khi b bằng 0
        LL x = a % b; // Lấy phần dư của a chia b
        a = b;        // Gán b cho a
        b = x;        // Gán phần dư cho b
    }
    return a; // Trả về ước chung lớn nhất
}

// Hàm giải quyết bài toán cho mỗi test case
void solve()
{
    LL n; // Biến lưu giá trị đầu vào
    cin >> n; // Nhập giá trị n từ người dùng
    LL r = 1; // Biến lưu kết quả, khởi tạo bằng 1
    for (LL i = 1; i <= n; ++i) { // Lặp từ 1 đến n
        LL g = gcd(r, i); // Tính GCD của r và i
        r = r * i / g;    // Tính bội chung nhỏ nhất (LCM) của r và i
    }
    cout << r << endl; // In kết quả ra màn hình
}

int main()
{
    int t; // Biến lưu số lượng test case
    cin >> t; // Nhập số lượng test case từ người dùng
    while (t--) // Lặp qua từng test case
        solve(); // Gọi hàm solve để xử lý
    return 0; // Kết thúc chương trình
}
