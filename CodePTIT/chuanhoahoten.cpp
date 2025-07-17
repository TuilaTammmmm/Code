#include <bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    getline(cin,s);
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    stringstream ss(s);
    vector<string> kq;
    string word;
    while (ss >> word)
    {
        word[0]=toupper(word[0]);
        kq.push_back(word);
    }
    string ten=kq.back();

    for (int i = 0; i < ten.size(); i++)
    {
        ten[i]=toupper(ten[i]);
    }

    for (int i = 0; i < kq.size()-1; ++i) {
        cout << kq[i];
        if(i<kq.size()-2)
        {
            cout<<" ";
        }
    }
    cout<<", "<<ten;
}