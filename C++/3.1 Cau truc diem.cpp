#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

struct Point {
    double x, y;
} A, B;

void input(Point &p) {
    cin >> p.x >> p.y;
}

double distance(const Point &p1, const Point &p2) {
    return sqrt(pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2));
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        input(A);
        input(B);
        cout << fixed << setprecision(4) << distance(A, B) << endl;
    }
    return 0;
}