#include <bits/stdc++.h>
using namespace std;

string num_to_text(int n) {
    vector<string> donvi = {"khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"};
    if (n < 10) return donvi[n];
    if (n == 10) return "muoi";
    if (n < 20) return "muoi " + donvi[n%10];
    int chuc = n/10;
    int dv = n%10;
    if (dv == 0) return donvi[chuc] + " muoi";
    return donvi[chuc] + " muoi " + donvi[dv];
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        cout << num_to_text(n) << endl;
    }
    return 0;
}
