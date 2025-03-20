#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        long long N;
        cin >> N;
        cout << fixed << setprecision(15) << 1.0 / N << endl;
    }

    return 0;
}