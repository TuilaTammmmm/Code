#include <iostream>
using namespace std;
int main(){
    int t;
    cin >> t;
    for(int i=1;i<=t;i++){
        int n;
        cin >> n;
        int s=0;
        for(int j=1;j<=n;j++){
            s += j;
        }
        cout << s << endl;
    }
}