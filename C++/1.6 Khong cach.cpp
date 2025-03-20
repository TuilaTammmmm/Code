#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int tinh_khoang_cach(int x1, int y1, int x2, int y2){
    return sqrt(pow(x1-x2,2)+pow(y1-y2,2));
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        double kc=tinh_khoang_cach(x1, y1, x2, y2);
        cout << setprecision(4) << fixed << kc << endl;
    }
    return 0;
}