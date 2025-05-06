#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int reverseNumber(int n) {
    string s = to_string(n);
    reverse(s.begin(), s.end());
    return stoi(s);
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;

        int reversedN = reverseNumber(n);

        if (__gcd(n, reversedN) == 1) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}