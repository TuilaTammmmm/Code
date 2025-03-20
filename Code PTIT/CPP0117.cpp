#include <iostream>
using namespace std;
int SumOfDigits(int x){
    int S = 0;
    while (x != 0)
    {
        int mod = x % 10;
        S += mod;
        x = x / 10;
    }
    return S;
}
int FinalDigit(int x)
{
    while (x >= 10)
    {
        x = SumOfDigits(x);
    }
    return x;
}
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int x;
        cin >> x;
        cout << FinalDigit(x) << endl;
    }
    return 0;
}
