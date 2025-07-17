#include <bits/stdc++.h>
#include <sstream>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;//1 2
        cin.ignore();
         
        string s;
        getline(cin, s);

        transform(s.begin(), s.end(), s.begin(), ::tolower);

        stringstream ss(s);
        vector<string> kq;
        string word;
        while (ss >> word)
        {
            word[0] = toupper(word[0]);
            kq.push_back(word);
        }


        switch (n)
        {
        case 1:
            cout<<kq[kq.size()-1]<<" ";
            for (int i = 0; i < kq.size()-1; i++)
            {
                cout<<kq[i];
                if(i<kq.size()-1)cout<<" ";
            }
            cout<<endl;
            break;


        case 2:
            for (int i = 1; i < kq.size(); i++)
            {
                cout<<kq[i];
                if(i<kq.size()-1)cout<<" ";
            }
            cout<<" "<<kq[0]<<endl;
            break;
        default:
            break;
        }
    }
}