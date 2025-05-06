#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int tens = n / 10;
    int units = n % 10;
    int result = tens - units;
    cout << result << endl;
    return 0;
}