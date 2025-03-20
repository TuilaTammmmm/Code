#include <iostream>
#include <iomanip>
#define MAX 100
using namespace std;

int X[MAX], n, dem = 0;
bool cot[MAX], dcxuoi[MAX], dcnguoc[MAX];

// Hàm in kết quả
void Result(void)
{
    cout << "\n Ket qua " << ++dem << ":";
    for (int i = 1; i <= n; i++)
        cout << X[i] << setw(3);
}
void Try(int i)
{
    for (int j = 1; j <= n; j++) // Duyệt qua các cột
    {
        // Kiểm tra xem có thể đặt quân hậu tại vị trí (i, j) không
        if (cot[j] && dcxuoi[i - j + n] && dcnguoc[i + j - 1])
        {
            X[i] = j; // Đặt quân hậu tại cột j
            cot[j] = false; // Đánh dấu cột j đã bị chiếm
            dcxuoi[i - j + n] = false; // Đánh dấu đường chéo xuôi đã bị chiếm
            dcnguoc[i + j - 1] = false; // Đánh dấu đường chéo ngược đã bị chiếm
            if (i == n) // Nếu đã đặt đủ n quân hậu
                Result(); // In kết quả
            else
                Try(i + 1); // Thử đặt quân hậu tiếp theo
            // Quay lui: bỏ đánh dấu để thử các trường hợp khác
            cot[j] = true;
            dcxuoi[i - j + n] = true;
            dcnguoc[i + j - 1] = true;
        }
    }
}

int main(void)
{
    cin >> n;
    for (int i = 1; i <= n; i++)// Khởi tạo các cột chưa bị chiếm
    {
        cot[i] = true;
    }
    for (int i = 1; i < 2 * n; i++) // Khởi tạo các đường chéo chưa bị chiếm
    {
        dcxuoi[i] = true;
        dcnguoc[i] = true;
    }
    Try(1);
}