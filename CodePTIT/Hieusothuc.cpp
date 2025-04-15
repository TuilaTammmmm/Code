#include <iostream>
using namespace std;

struct SoPhuc {
    int thuc;
    int ao;

    SoPhuc(int t = 0, int a = 0) : thuc(t), ao(a) {}

    SoPhuc operator+(const SoPhuc& other) const {
        return SoPhuc(thuc + other.thuc, ao + other.ao);
    }

    SoPhuc operator-(const SoPhuc& other) const {
        return SoPhuc(thuc - other.thuc, ao - other.ao);
    }

    friend istream& operator>>(istream& in, SoPhuc& sp) {
        in >> sp.thuc >> sp.ao;
        return in;
    }

    friend ostream& operator<<(ostream& out, const SoPhuc& sp) {
        out << sp.thuc;
        if (sp.ao >= 0) {
            out << " + " << sp.ao << "i";
        } else {
            out << " - " << -sp.ao << "i";
        }
        return out;
    }
};

int main() {
    SoPhuc p(2, 3), q(4, 5);
    cin >> p >> q;
    cout << p - q;
    return 0;
}