#include <bits/stdc++.h>
using namespace std;
struct NhanVien {
    char maNV[10] = "00001";
    char hoTen[50];
    char ngaySinh[15];
    char gioiTinh[5];
    char chucVu[20];
    char diaChi[50];
    char maSoThue[15];
    char ngayKyHopDong[15];
};
void nhap(NhanVien &a) {
    cin.getline(a.hoTen, 50);
    cin.getline(a.gioiTinh, 5);
    cin.getline(a.ngaySinh, 15);
    cin.getline(a.diaChi, 50);
    cin.getline(a.maSoThue, 15);
    cin.getline(a.ngayKyHopDong, 15);
}
void in(const NhanVien &a) {
    cout << a.maNV << " " << a.hoTen << " " << a.gioiTinh << " " << a.ngaySinh << " " 
         << a.diaChi << " " << a.maSoThue << " " << a.ngayKyHopDong << endl;
}
int main() {
    struct NhanVien a;
    nhap(a);
    in(a);
    return 0;
}