#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        char n;
        cin >> n;
        if (n >= 'A' && n <= 'Z') {
            n += 32; 3
            cout << n << endl;
        } else if (n >= 'a' && n <= 'z') {
            n -= 32;
            cout << n << endl;
        }
    }
}