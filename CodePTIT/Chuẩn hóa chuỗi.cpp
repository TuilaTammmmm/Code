#include <iostream>
#include <sstream>
#include <cctype>
using namespace std;

string chuanHoaChuoi(string s) {
    stringstream ss(s);
    string word, result = "";
    while (ss >> word) {
        word[0] = toupper(word[0]);
        for (int i = 1; i < word.length(); i++) {
            word[i] = tolower(word[i]);
        }
        result += word + " ";
    }
    if (!result.empty()) {
        result.pop_back();
    }
    return result;
}

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        string s;
        getline(cin, s);
        cout << chuanHoaChuoi(s) << endl;
    }
    return 0;
}