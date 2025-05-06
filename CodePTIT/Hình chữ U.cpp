#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N - 1; i++) {
        cout << "*";
        for (int j = 0; j < N - 2; j++) {
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