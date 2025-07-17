#include <iostream>
using namespace std;

const int MOD = 1e9 + 7;

// Hàm tính lũy thừa nhị phân
long long power(long long a, long long b) {
    long long res = 1;
    a %= MOD;
    while (b > 0) {
        if (b % 2 == 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        b /= 2;
    }
    return res;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        long long N, K;
        cin >> N >> K;
        cout << power(N, K) << endl;
    }
    return 0;
}
