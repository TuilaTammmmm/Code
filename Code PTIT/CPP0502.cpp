#include <bits/stdc++.h>
#include <iomanip>
using namespace std;
struct ThiSinh {
    char hoTen[50];
    char ngaySinh[11];
    float diemMon1;
    float diemMon2;
    float diemMon3;
    float tongDiem;
};
void nhap(ThiSinh &A) {
    cin.getline(A.hoTen, 50);
    cin.getline(A.ngaySinh, 11);
    cin >> A.diemMon1 >> A.diemMon2 >> A.diemMon3;
    A.tongDiem = A.diemMon1 + A.diemMon2 + A.diemMon3;
}
void in(const ThiSinh &A) {
    cout << A.hoTen << " " << A.ngaySinh << " " << fixed << setprecision(1) << A.tongDiem << endl;
}
int main(){
    struct ThiSinh A;
    nhap(A);
    in(A);
    return 0;
}