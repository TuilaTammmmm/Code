#include <iostream>
using namespace std;

int findUnique(int a, int b, int c) {
    if (a == b) return c;
    if (a == c) return b;
    return a;
}

int main() {
    int x1, y1, x2, y2, x3, y3;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
    int x4 = findUnique(x1, x2, x3);
    int y4 = findUnique(y1, y2, y3);
    cout << x4 << " " << y4;
    return 0;
}