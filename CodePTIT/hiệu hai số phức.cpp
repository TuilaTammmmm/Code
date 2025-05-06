#include <iostream>
using namespace std;

class SoPhuc {
private:
    int phanThuc;
    int phanAo;

public:
    SoPhuc(int thuc = 0, int ao = 0) : phanThuc(thuc), phanAo(ao) {}

    friend istream& operator>>(istream& is, SoPhuc& sp) {
        is >> sp.phanThuc >> sp.phanAo;
        return is;
    }

    friend ostream& operator<<(ostream& os, const SoPhuc& sp) {
        if (sp.phanAo >= 0)
            os << sp.phanThuc << " + " << sp.phanAo << "i";
        else
            os << sp.phanThuc << " - " << -sp.phanAo << "i";
        return os;
    }

    SoPhuc operator-(const SoPhuc& other) const {
        return SoPhuc(phanThuc - other.phanThuc, phanAo - other.phanAo);
    }
};

int main() {
    SoPhuc p(2, 3), q(4, 5);
    cin >> p >> q;
    cout << p - q;
    return 0;
}