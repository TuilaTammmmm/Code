#include <bits/stdc++.h>
using namespace std;
const int Max = 1000000;
bool prime[Max + 1];
void SieveOfEratosthenes() {
    fill(prime, prime + Max + 1, true);
    prime[0] = prime[1] = false;
    for (int p = 2; p * p <= Max; p++) {
        if (prime[p]) {
            for (int i = p * p; i <= Max; i += p)
                prime[i] = false;
        }
    }
}
bool check_tang_giam(int i) {
    string s = to_string(i);
    bool tang = true, giam = true;
    for (size_t j = 1; j < s.size(); j++) {
        if (s[j] <= s[j - 1]) tang = false;
        if (s[j] >= s[j - 1]) giam = false;
    }
    
    return tang || giam;
}
int main() {
    SieveOfEratosthenes();
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int max = (int)pow(10, n) - 1;
        int min = (int)pow(10, n - 1);
        int dem = 0;
        for (int i = min; i <= max; i++) {
            if (prime[i] && check_tang_giam(i)) {
                dem++;
            }
        }
        cout <<dem << endl;
    }
    return 0;
}
