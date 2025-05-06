#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> A(n);

    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    set<int> uniqueNumbers(A.begin(), A.end());

    for (int num : uniqueNumbers) {
        cout << num << " ";
    }

    return 0;
}