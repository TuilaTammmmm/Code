#include <iostream>
#include <sstream>
#include <cctype>
using namespace std;
string chuanhoatu(string u)
{
    if(u.empty()) return "";
    u[0]=toupper(u[0]);
    for(int i=1;i<u.size();i++)
        u[i]=tolower(u[i]);
    return u;
}
int main()
{
    string s;
    getline(cin,s);
    stringstream ss(s);
    string u, kq="";
    while(ss>>u)
    {
        kq+=chuanhoatu(u)+" ";
    }
    if(!kq.empty())
    kq.pop_back();
    cout<<kq;
}