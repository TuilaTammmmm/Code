
#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fi;
    fi.open("DATA.in");
    
    map<int, int> mp;
    int x;
    while (fi >> x) {
        mp[x]++;
    }
    fi.close();
    
    for (auto x : mp) {
        cout << x.first << " " << x.second << "\n";
    }
    return 0;
}
