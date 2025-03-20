#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    cout << a + b << endl;
    cout << a - b << endl;
    cout << (long long)a * b << endl;
    cout << a / b << endl;
    cout << a % b << endl;
    cout << fixed << setprecision(2) << (double)a / b;

    return 0;
}