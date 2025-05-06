#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        // In khoảng trắng
        for (int j = 0; j < N - i - 1; j++) {
            cout << " ";
        }

        // In các ký tự '*'
        for (int j = 0; j < 2 * i + 1; j++) {
            if (j == 0 || j == 2 * i || (i == N - 1 && j % 2 == 0)) {
                cout << "*";
            } else {
                cout << " ";
            }
        }

        // Xuống dòng
        cout << endl;
    }

    return 0;
}