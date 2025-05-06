#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        cout << "*";
    }
    cout << endl;

    for (int i = N - 2; i > 0; i--) {
        for (int j = 0; j < i; j++) {
            cout << " ";
        }
        cout << "*" << endl;
    }

    for (int i = 0; i < N; i++) {
        cout << "*";
    }
    cout << endl;

    return 0;
}