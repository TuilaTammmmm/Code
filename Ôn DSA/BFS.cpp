#include <bits/stdc++.h>
using namespace std;
vector<int> A[1001];
int visited[1001];
void BFS(int u)
{
    queue<int> q;
    q.push(u);
    visited[u]=true;
    while(!q.empty())
    {
        int u=q.front();q.pop();
        cout<<u<<" ";
        for(int c:A[u])
        {
            if(!visited[c])
            {
                visited[c]=true;
                q.push(c);
            }
        }
    }
}
int main()
{
    int t;
    cin >> t;
    while (t--)
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
            int x, v;
            cin >> x >> v;
            A[x].push_back(v);
            A[v].push_back(x);
        }
        BFS(u);
        cout << "\n";
    }

    return 0;
}