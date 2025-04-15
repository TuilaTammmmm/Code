#include <iostream>
#include <string>
using namespace std;

int main() {
    string target = "iloveptit";
    
    char c;
    cin >> c;

    if (target.find(c) != string::npos) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}