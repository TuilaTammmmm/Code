#include <iostream>
#include <algorithm>
using namespace std;
struct PhanSo {
    long long tu;
    long long mau;
};

void nhap(PhanSo &p) {
    cin >> p.tu >> p.mau;
}
long long gcd(long long a, long long b) {
    while (b != 0) {
        long long t = b;
        b = a % b;
        a = t;
    }
    return a;
}
void rutgon(PhanSo &p) {
    long long ucln = gcd(p.tu, p.mau);
    p.tu /= ucln;
    p.mau /= ucln;
}

void in(const PhanSo &p) {
    cout << p.tu << "/" << p.mau << std::endl;
}

int main() {
    PhanSo p;
    nhap(p);
    rutgon(p);
    in(p);
    return 0;
}