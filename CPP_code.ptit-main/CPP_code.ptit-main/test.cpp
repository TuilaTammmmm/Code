#include <iostream>
#include <cmath>
using namespace std;
bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        for (int i = n; i <= m; i++) {
            if (isPrime(i)) cout << i << " ";
        }
        cout << "\n";
    }
    return 0;
}