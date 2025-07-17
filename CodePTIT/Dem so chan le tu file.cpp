#include <bits/stdc++.h>
using namespace std;
ifstream infile("data.in");
void dem()
{
    int n;
    infile>>n;
    int chan=0;
    int le=0;
    for (int i = 0; i < n; i++)
    {
        int x;
        infile>>x;
        if(x%2==0)chan++;
        else le++;
    }
    cout<<chan<<" "<<le<<endl;
}
int main(){
    int t;
    infile>>t;
    while(t--)
    {
        dem();
    }
    return 0;
}