#include <bits/stdc++.h>
#include <sstream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    cin.ignore();
    while(t--)
    {
        string s;
        getline(cin,s);
        stringstream ss(s);
        string tu;
        vector<string> kq;
        while(ss>>tu)
        {
            kq.push_back(tu);
        }
        for (int i = kq.size()-1; i>=0; i--) {
            cout << kq[i];
            if(i>0)
            cout<<" ";
        }
        cout << endl;
    }
}