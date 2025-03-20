#include <iostream>
#include <iomanip>
#include <sstream>
using namespace std;

struct SinhVien {
    string hoTen;
    string lop;
    string ngaySinh;
    float gpa;
};
void chuanHoaNgaySinh(string &ngaySinh) {
    stringstream ss(ngaySinh);
    string token;
    string ngay, thang, nam;
    getline(ss, ngay, '/');
    getline(ss, thang, '/');
    getline(ss, nam, '/');
    if (ngay.length() == 1) ngay = "0" + ngay;
    if (thang.length() == 1) thang = "0" + thang;
    ngaySinh = ngay + "/" + thang + "/" + nam;
}
void nhap(SinhVien &a) {
    getline(cin, a.hoTen);
    getline(cin, a.lop);
    getline(cin, a.ngaySinh);
    cin >> a.gpa;
    chuanHoaNgaySinh(a.ngaySinh);
}
void in(const SinhVien &a) {
    cout << "B20DCCN001" << " " << a.hoTen << " " << a.lop << " " << a.ngaySinh << " " << fixed << setprecision(2) << a.gpa << endl;
}
int main() {
    struct SinhVien a;
    nhap(a);
    in(a);
    return 0;
}
