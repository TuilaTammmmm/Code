#include <bits/stdc++.h>
using namespace std;

int n;
vector<string> s(n);

string check() {
    string min = s[0];
    for (int i = 1; i < s.size(); i++) {
        if (s[i]+'0' < min+'0')
            min = s[i];
    }
    return min;
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> s[i];
    string smallest = check();
    cout << smallest;
    return 0;
}

