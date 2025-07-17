#include <bits/stdc++.h>
using namespace std;
vector<int> A[1001];
bool visited[1001];
int DFS(int u)
{
    visited[u] = true;
    int count=1;
    for (int c : A[u])
    {
        if (!visited[c])
        {
            count+=DFS(c);
        }
    }
    return count;
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, m;
        cin >> n >> m;
        for (int i = 1; i <= n; i++)
        {
            A[i].clear();
            visited[i] = false;
        }
        for (int i = 0; i < m; i++)
        {
            int x, y;
            cin >> x >> y;
            A[x].push_back(y);
            A[y].push_back(x);
        }
        int maxf= 0;
        for (int i = 1; i <= n; i++)
        {
            if (!visited[i])
            {
                int count =DFS(i);
                maxf=max(maxf,count);
            }
        }
        cout << maxf << endl;
    }
}