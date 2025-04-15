#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// Hàm so sánh hai số lớn dưới dạng chuỗi
bool isSmaller(const string& num1, const string& num2) {
    if (num1.length() < num2.length()) {
        return true;
    }
    if (num1.length() > num2.length()) {
        return false;
    }
    return num1 < num2;
}

int main() {
    int n;
    cin >> n;
    cin.ignore(); // Đọc bỏ ký tự newline sau khi đọc n

    string smallest_num;
    for (int i = 0; i < n; ++i) {
        string current_num;
        cin >> current_num;
        if (i == 0) {
            smallest_num = current_num;
        } else {
            if (isSmaller(current_num, smallest_num)) {
                smallest_num = current_num;
            }
        }
    }

    cout << smallest_num << endl;

    return 0;
}