#include <bits/stdc++.h>
using namespace std;
vector<int> A[1001];
bool visited[1001];
void DFS(int u)
{
    visited[u] = true;
    for (int c : A[u])
    {
        if (!visited[c])
        {
            DFS(c);
        }
    }
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
        int count = 0;
        for (int i = 1; i <= n; i++)
        {
            if (!visited[i])
            {
                DFS(i);
                count++;
            }
        }
        cout << count << endl;
    }
}