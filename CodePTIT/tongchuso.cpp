#include <iostream>
using namespace std;

int sum(int n)
{
    int x = 0;
    while (n > 0) {
        x += n % 10;
        n /= 10;
    }
    return x;
}

int main()
{
    int n;
    cin >> n;
    cout << sum(n);
   return 0;
}
