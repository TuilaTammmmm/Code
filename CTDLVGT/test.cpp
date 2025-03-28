#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#define MAX 100
using namespace std;

char X[MAX];
char T[MAX];
int n, m, dem = 0;
bool OK = true;

void Init() {
    string S;
    cin >> S;
    n = S.length();

    m = 0;
    bool used[256] = {false};
    for (int i = 0; i < n; i++) {
        if (!used[S[i]]) {
            T[m] = S[i];
            used[S[i]] = true;
            m++;
        }
    }

    sort(T, T + m);

    for (int i = 1; i <= n; i++) {
        X[i] = T[i - 1];
    }
}

void Result() {
    for (int i = 1; i <= n; i++) {
        cout << X[i];
    }
    cout << " ";
}

void Next_Permutation() {
    int j = n - 1;
    while (j > 0 && X[j] >= X[j + 1]) {
        j--;
    }
    if (j > 0) {
        int k = n;
        while (X[j] >= X[k]) {
            k--;
        }
        char t = X[j];
        X[j] = X[k];
        X[k] = t;

        int r = j + 1, s = n;
        while (r <= s) {
            t = X[r];
            X[r] = X[s];
            X[s] = t;
            r++;
            s--;
        }
    } else {
        OK = false;
    }
}

void Generate_Permutations(string S) {
    n = S.length();

    m = 0;
    bool used[256] = {false};
    for (int i = 0; i < n; i++) {
        if (!used[S[i]]) {
            T[m] = S[i];
            used[S[i]] = true;
            m++;
        }
    }

    sort(T, T + m);

    for (int i = 1; i <= n; i++) {
        X[i] = T[i - 1];
    }

    OK = true;
    dem = 0;
    while (OK) {
        Result();
        Next_Permutation();
    }
    cout << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        string S;
        cin >> S;
        Generate_Permutations(S);
    }
    cout << endl;
    return 0;
}