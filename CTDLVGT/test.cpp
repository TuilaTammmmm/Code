#include <iostream>
#include <queue>
using namespace std;

const int MAX = 100;
int A[MAX][MAX]; // Ma trận kề
bool visited[MAX];
int V; // Số đỉnh

void DFS(int u) {
    visited[u] = true;
    cout << u << " ";

    for (int v = 1; v <= V; v++) {
        if (A[u][v] == 1 && !visited[v]) {
            DFS(v);
        }
    }
}

void BFS(int start) {
    queue<int> q;
    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int u = q.front(); q.pop();
        cout << u << " ";

        for (int v = 1; v <= V; v++) {
            if (A[u][v] == 1 && !visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }
}
int main() {
    cout << "Nhap so dinh V: ";
    cin >> V;

    cout << "Nhap ma tran ke " << V << " x " << V << ":\n";
    for (int i = 1; i <= V; i++) {
        for (int j = 1; j <= V; j++) {
            cin >> A[i][j];
        }
    }

    int start=1;

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
