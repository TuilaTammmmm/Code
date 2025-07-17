#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    cin.ignore();
    while (t--)
    {
        int N,K;
        cin >> N>>K;
        vector<int> A(N);
        for(int i=0;i<N;i++)cin>>A[i];
        auto temp = find(A.begin(), A.end(), K);
        if (temp != A.end())
            cout << temp - A.begin()+1 << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}
