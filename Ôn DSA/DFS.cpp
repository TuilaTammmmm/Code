#include <bits/stdc++.h>
using namespace std;
vector<int> A[1001];
bool visited[1001];
void DFS(int u)
{
    visited[u]=true;
    cout<<u<<" ";
    for(int c:A[u])
    {
        if(!visited[c])
        {
            DFS(c);
        }
    }
}
int main()
{
    int n, m, u;
    cin >> n >> m >> u;
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
    DFS(u);
    cout << endl;
}