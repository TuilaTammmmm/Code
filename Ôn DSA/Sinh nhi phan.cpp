#include <iostream>
using namespace std;

int X[20], n;
bool OK;

bool isEvenOnes() {
    int count = 0;
    for (int i = 1; i <= n; i++)
        if (X[i] == 1) count++;
    return count % 2 == 0;
}

void print() {
    for (int i = 1; i <= n; i++) {
        cout << X[i];
        if (i < n) cout << " ";
    }
    cout << endl;
}

void Next_Bits_String() {
    int i = n;
    while (i > 0 && X[i]) {
        X[i] = 0;
        i--;
    }
    if (i > 0) X[i] = 1;
    else OK = false;
}

int main() {
    cin >> n;
    OK = true;
    for (int i = 1; i <= n; i++) X[i] = 0;

    while (OK) {
        if (isEvenOnes()) print();
        Next_Bits_String();
    }
    return 0;
}
