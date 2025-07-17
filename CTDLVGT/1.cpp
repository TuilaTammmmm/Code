#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int MAX = 100;
vector<int> adj[MAX]; // Danh sách kề
bool visited[MAX];    // Mảng đánh dấu đã thăm

void addEdge(int u, int v) {
    adj[u].push_back(v);
    adj[v].push_back(u); // Nếu là đồ thị vô hướng
}

void DFS(int u) {
    visited[u] = true;
    cout << u << " ";
    for (int v : adj[u]) {
        if (!visited[v]) DFS(v);
    }
}

void BFS(int start) {
    queue<int> q;
    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int u = q.front(); q.pop();
        cout << u << " ";
        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }
}

int main() {
    int V, E;
    cout << "Nhap so dinh V và so canh E: ";
    cin >> V >> E;

    cout << "Nhap " << E << " canh (dinh u v):\n";
    for (int i = 0; i < E; ++i) {
        int u, v;
        cin >> u >> v;
        addEdge(u, v);
    }

    int start;
    cout << "Nhap dinh bat dau: ";
    cin >> start;

    cout << "DFS: ";
    fill(visited, visited + MAX, false);
    DFS(start);
    cout << endl;

    cout << "BFS: ";
    fill(visited, visited + MAX, false);
    BFS(start);
    cout << endl;

    return 0;
}
