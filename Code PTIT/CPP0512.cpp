#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
struct PhanSo
{
	long long int tu, mau;
};

void process(PhanSo A, PhanSo B)
{
	long long int a = A.tu, b = B.tu, c = A.mau, d = B.mau;
	long long int bc = A.mau * B.mau / __gcd(A.mau, B.mau); // Tìm bội chung nhỏ nhất của mẫu số

	A.tu = A.tu * bc / A.mau; // Quy đồng tử số A
	B.tu = B.tu * bc / B.mau; // Quy đồng tử số B

	PhanSo C;
	long long int x = (A.tu + B.tu);
	long long int y = bc;
	long long int t1 = x * x / __gcd(x * x, y * y);
	long long int m1 = y * y / __gcd(x * x, y * y);
	cout << t1 << "/" << m1 << " ";

	PhanSo D;
	D.tu = a * b * x * x;  // Tử số của phân số tích
	D.mau = c * d * y * y; // Mẫu số của phân số tích
	long long int t2 = D.tu / __gcd(D.tu, D.mau);
	long long int m2 = D.mau / __gcd(D.tu, D.mau);
	cout << t2 << "/" << m2 << endl;
}
int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		PhanSo A;
		PhanSo B;
		cin >> A.tu >> A.mau >> B.tu >> B.mau;
		process(A, B);
	}
}