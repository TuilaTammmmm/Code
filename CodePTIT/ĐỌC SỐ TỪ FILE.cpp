#include <bits/stdc++.h>
#include <algorithm>
#include <math.h>
#include <iostream>
using namespace std;

string res(char s)
{
    if (s == '1') return "mot";
    if (s == '2') return "hai";
    if (s == '3') return "ba";
    if (s == '4') return "bon";
    if (s == '5') return "nam";
    if (s == '6') return "sau";
    if (s == '7') return "bay";
    if (s == '8') return "tam";
    if (s == '9') return "chin";
}

int main()
{
    freopen("data.in", "r", stdin);
    int tc;
    cin >> tc;
    while (tc--) 
 
    {
        string n;
        cin >> n;
        if (n == "0") cout << "khong" << endl;
        else if (n == "100") cout << "mot tram" << endl;
        else if (n.size() == 1) cout << res(n[0]) << endl;
        else if (n == "10") cout << "muoi" << endl;
        else if (n.size() == 2 && n[1] == '0' && n[1] != '1') 
 
        {
            string tmp = "";
            tmp += res(n[0]) + " ";
            tmp += "muoi";
            cout << tmp << endl;
            
        }
        else if (n.size() == 2 && n[1] != 0 && n[0] == '1') 
 
        {
            string tmp = "";
            tmp += "muoi ";
            if (n[1] == '5') tmp += "lam";
            else tmp += res(n[1]);
            cout << tmp << endl;
            
        }
        else 
        {
            string tmp = "";
            tmp += res(n[0]);
            tmp += " muoi ";
            if (n[1] == '5') tmp += "lam";
            else tmp += res(n[1]);
            cout << tmp << endl;
            
        }
        
    }
    return 0;
}
