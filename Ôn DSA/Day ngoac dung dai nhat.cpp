#include <bits/stdc++.h>
using namespace std;
#include <bits/stdc++.h>
using namespace std;

void count(string s)
{
    int dem = 0;
    stack<char> ss;
    for (char c : s)
    {
        if (c == '(')
        {
            ss.push(c);
        }
        else
        {
            if (!ss.empty())
            {
                char top = ss.top();
                if (c == ')' && top == '(')
                {
                    dem += 2;
                    ss.pop();
                }
            }
        }
    }
    cout << dem << endl;
}

int main(){
    int t;cin>>t;
    cin.ignore();
    while(t--)
    {
        string s;
        getline(cin,s);
        count(s);
    }
}