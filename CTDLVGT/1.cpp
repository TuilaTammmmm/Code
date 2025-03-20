#include <iostream>
#include <iomanip>
#define MAX 100
using namespace std;
int X[MAX], n, dem = 0;
bool OK = true;
void Init(void) {
    cin >> n;
    for (int i = 1; i <= n; i++)
        X[i] = 0;
}
void Result(void) {
    cout <<"\n"<<++dem << ":";
    for (int i = 1; i <= n; i++)
        cout << X[i] << setw(3);
}
void Next_Bits_String(void) {
    int i = n;
    while (i > 0 && X[i]) {
        X[i] = 0;
        i--;
    }
    if (i > 0)
        X[i] = 1;
    else
        OK = false;
}
int main(void) {
    Init();
    while (OK) {
        Result();
        Next_Bits_String();
    }
}
