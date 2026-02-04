#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

vector<int> adj[1001];
bool visited[1001];
int Duondi[1001];

void bfs(int s, int t) {
    queue<int> q;
    q.push(s);
    visited[s] = true;
    Duondi[s] = -1;

    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                Duondi[v] = u;
                q.push(v);
            }
        }
    }

    if (!visited[t]) {
        cout << -1 << endl;
        return;
    }

    vector<int> path;
    for (int v = t; v != -1; v = Duondi[v])
        path.push_back(v);
    reverse(path.begin(), path.end());

    for (int v : path)
        cout << v << " ";
    cout << endl;
}

int main() {
    int test;
    cin >> test;
    while (test--) {
        int n, m, s, t;
        cin >> n >> m >> s >> t;

        for (int i = 1; i <= n; i++) {
            adj[i].clear();
            visited[i] = false;
        }

        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        bfs(s, t);
    }

    return 0;
}
