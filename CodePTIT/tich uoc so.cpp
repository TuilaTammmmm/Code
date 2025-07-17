#include <bits/stdc++.h>
using namespace std;
void uoc()
{
    int n;
    cin>>n;
    int total=1;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin>>x;
        total*=x;
    }
    int tichuoc=1;
    for (int i = 0; i < total; i++)
    {
        if(total%i==0)
        {
            tichuoc*=i;
        }
    }
    cout<<tichuoc;
}
int main(){
    uoc();
}