#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double a, b;
    cin >> a >> b;
    if (a == 0) {
        if (b == 0) {
            cout << "Vo so nghiem" << endl;
        } else {
            cout << "Vo nghiem" << endl;
        }
    } else {
        double x = -b / a;
        cout << fixed << setprecision(2) << x << endl;
    }
    return 0;
}