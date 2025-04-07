
#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fi;
    fi.open("VANBAN.in");

    set<string> se;
    string s;
    while (fi >> s) {
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        se.insert(s);
    }
    fi.close();

    for (auto s : se) {
        cout << s << endl;
    }
    return 0;
}
