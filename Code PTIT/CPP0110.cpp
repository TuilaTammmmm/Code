#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    while (n--) {
        string str;
        cin >> str;
        auto p = str.find("084");
        if (p != string::npos) {
            str.erase(p, 3);
        }
        cout << str << endl;
    }
    return 0;
}