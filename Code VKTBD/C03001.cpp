#include <iostream>
#include <string>
using namespace std;
int sumOfDigits(const string& number) {
    int sum = 0;
    for (char digit : number) {
        sum += digit - '0';
    }
    return sum;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        string number;
        cin >> number;
        if (sumOfDigits(number) % 10 == 0) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}