#include <iostream>
using namespace std;
int main(){
    int t;
    cin >> t;
    for(int i=1;i<=t;i++){
        int n;
        cin >> n;
        int dem=0;
        for (int i = 0; i < 9; i++)
        {
            int Num=n%10;
            if (Num!=0 && Num != 6 && Num !=8)
            {
                dem++;
                cout << "NO" << endl;
                break;            
            }
            n=n/10;
        }
        if (dem==0)
        {
            cout << "YES" << endl;
        }
    }
    return 0;
}