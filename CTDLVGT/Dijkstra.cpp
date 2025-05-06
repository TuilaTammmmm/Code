#include <stdio.h>
#include <limits.h>
#define MAX 100

int minDistance(int dist[], int sptSet[], int n) {
    int min = INT_MAX, min_index = -1;
    for (int v = 1; v <= n; v++) {
        if (!sptSet[v] && dist[v] <= min) {
            min = dist[v];
            min_index = v;
        }
    }
    return min_index;
}

void printSolution(int dist[], int n) {
    for (int i = 1; i <= n; i++) {
        if (dist[i] != INT_MAX)
            printf("%d ", dist[i]);
    }
    printf("\n");
}

void dijkstra(int graph[MAX][MAX], int src, int n) {
    int dist[MAX], sptSet[MAX];
    for (int i = 1; i <= n; i++) {
        dist[i] = INT_MAX;
        sptSet[i] = 0;
    }
    dist[src] = 0;
    for (int count = 1; count <= n - 1; count++) {
        int u = minDistance(dist, sptSet, n);
        if (u == -1)
            break;
        sptSet[u] = 1;
        for (int v = 1; v <= n; v++) {
            if (!sptSet[v] && graph[u][v] != INT_MAX && dist[u] != INT_MAX &&
                dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }
    printSolution(dist, n);
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n, m, graph[MAX][MAX], src;
        scanf("%d %d %d", &n, &m, &src);
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                graph[i][j] = (i == j) ? 0 : INT_MAX;
            }
        }
        for (int i = 1; i <= m; i++) {
            int dau, cuoi, trongso;
            scanf("%d %d %d", &dau, &cuoi, &trongso);
            if (dau < 1 || dau > n || cuoi < 1 || cuoi > n || trongso < 0) {
                return 1;
            }
            if (graph[dau][cuoi] > trongso) {
                graph[dau][cuoi] = trongso;
                graph[cuoi][dau] = trongso;
            }
        }
        dijkstra(graph, src, n);
    }
    return 0;
}