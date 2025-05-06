#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

bool isPrime(int num) {
    if (num < 2) return false;
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) return false;
    }
    return true;
}

int main() {
    int N, M;
    cin >> N >> M;

    vector<vector<int>> matrix(N, vector<int>(M));
    int maxPrime = -1;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> matrix[i][j];
            if (isPrime(matrix[i][j])) {
                maxPrime = max(maxPrime, matrix[i][j]);
            }
        }
    }

    if (maxPrime == -1) {
        cout << "NOT FOUND" << endl;
    } else {
        cout << maxPrime << endl;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (matrix[i][j] == maxPrime) {
                    cout << "Vi tri [" << i << "][" << j << "]" << endl;
                }
            }
        }
    }

    return 0;
}