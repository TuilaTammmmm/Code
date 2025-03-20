#include <iostream>
using namespace std;
void Sum()
{
    int n;
    cin >> n;
    long long r = (long long)n * (n + 1) / 2;
    cout << r << endl;
}
int main()
{
    int T;
    cin >> T;
    while (T--)
        Sum();
    return 0;
}