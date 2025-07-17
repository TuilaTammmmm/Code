#include <bits/stdc++.h>
using namespace std;
void dem()
{
    int n;
    cin>>n;
    int chan=0;
    int le=0;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin>>x;
        if(x%2==0)chan++;
        else le++;
    }
    cout<<chan<<" "<<le<<endl;
}
int main(){
    int t;
    cin>>t;
    while(t--)
    {
        dem();
    }
    return 0;
}