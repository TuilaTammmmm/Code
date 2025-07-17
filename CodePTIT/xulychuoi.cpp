#include <bits/stdc++.h>
using namespace std;

int main() {
    string s, line;
    while (getline(cin, line)) {
        s += line + " ";
    }

    string tmp = "";
    vector<string> cau;

    for (char c : s) {
        tmp += c;
        if (c == '.' || c == '?' || c == '!') {
            tmp.erase(tmp.size()-1,1);
            cau.push_back(tmp);
            tmp = "";
        }
    }

    for (auto &x : cau) {
        stringstream ss(x);
        string tu, ketqua = "";
        while (ss >> tu) {
            ketqua += tu + " ";
        }
        if (!ketqua.empty()) ketqua.pop_back();

        transform(ketqua.begin(), ketqua.end(), ketqua.begin(), ::tolower);
        if (!ketqua.empty()) ketqua[0] = toupper(ketqua[0]);

        cout << ketqua << endl;
    }
    return 0;
}
