#include <iostream>
using namespace std;

class SoPhuc {
private:
    long long phanThuc;
    long long phanAo;

public:
    SoPhuc(long long thuc = 0, long long ao = 0) : phanThuc(thuc), phanAo(ao) {}

    friend istream& operator>>(istream& is, SoPhuc& sp) {
        is >> sp.phanThuc >> sp.phanAo;
        return is;
    }

    friend ostream& operator<<(ostream& os, const SoPhuc& sp) {
        os << sp.phanThuc << " + " << sp.phanAo << "i";
        return os;
    }

    SoPhuc operator+(const SoPhuc& other) const {
        return SoPhuc(phanThuc + other.phanThuc, phanAo + other.phanAo);
    }
};

int main() {
    SoPhuc p(2, 3), q(4, 5);
    cin >> p >> q;
    cout << p + q;
    return 0;
}