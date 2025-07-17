#include <bits/stdc++.h>
using namespace std;
string A="1";
void nhandoi()
{
    int N=2;
    while(N<=50)
    {
        char c=N+'0';
        string B=A;
        A=B+c+B;
        N++;
    }
}
int main(){
    nhandoi();
    int t;
    cin>>t;
    while(t--)
    {
        int N,K;
        cin>>N>>K;
        cout<<A[K-1]<<endl;
    }
}