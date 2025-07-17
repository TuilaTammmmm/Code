#include <iostream>
#include <set>
#include <algorithm>
#include <sstream>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        string s1, s2;
        getline(cin, s1);
        getline(cin, s2);

        set<string> A, B;
        stringstream ss1(s1), ss2(s2);
        string word;

        while (ss1 >> word) A.insert(word);
        while (ss2 >> word) B.insert(word);

        vector<string> res;

        set_difference(
            A.begin(), A.end(),
            B.begin(), B.end(),
            back_inserter(res)
        );
        
        for (auto &w : res) cout << w << " ";
        cout << endl;
    }
    return 0;
}
