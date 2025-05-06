#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define MAX 100
int A[MAX][MAX];
int mark[MAX];
int n;
void Nhap()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            cin >> A[i][j];
        }
    }
}

void DFS(int u)
{
    mark[u] = 1;
    cout << u << " ";
    for (int v = 1; v <= n; v++)
    {
        if (A[u][v] == 1 && mark[v] == 0)
        {
            DFS(v);
        }
    }
}

void BFS(int u)
{
    queue<int> Queue;
    mark[u] = 1;
    Queue.push(u);
    while (!Queue.empty())
    {
        int x = Queue.front();
        Queue.pop();
        cout << x << " ";
        for (int v = 1; v <= n; v++)
        {
            if (A[x][v] == 1 && mark[v] == 0)
            {
                mark[v] = 1;
                Queue.push(v);
            }
        }
    }
}

int main()
{
    int u;
    Nhap();
    cin >> u;
    fill(mark, mark + MAX, 0);
    DFS(u);
    cout << endl;
    fill(mark, mark + MAX, 0);
    BFS(u);
    cout << endl;
    return 0;
}