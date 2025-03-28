#include <iostream>
#include <iomanip>
#define MAX 100
using namespace std;
int X[MAX], n, k;
bool OK=true;
void Next_Combination() {
    int i = k;
    while (i > 0 && X[i] == n - k + i) {
        i--;
    }
    if (i > 0) {
        X[i] = X[i] + 1;
        for (int j = i + 1; j <= k; j++) {
            X[j] = X[i] + j - i;
        }
    } else {
        OK = false;
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        cin >> n >> k;
        for (int i = 1; i <= k; i++) {
            cin >> X[i];
        }
        Next_Combination();
        if (OK) {
            for (int i = 1; i <= k; i++) {
                cout << X[i] << " ";
            }
        } else {
            for (int i = 1; i <= k; i++) {
                X[i] = i;
                cout << X[i] << " ";
            }
        }
        cout << endl;
    }
    return 0;
}