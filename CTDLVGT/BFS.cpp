#include <bits/stdc++.h>
using namespace std;

const int N = 200;

bool visited[N + 1][N + 1];

int n, m, a[N + 1][N + 1];

const int hx[4] = {-1, 0, 0, 1};
const int hy[4] = {0, -1, 1, 0};
// trái, trên, phải, dưới
void bfs(int i, int j)
{
    queue<pair<int, int>> q; // giá trị đầu của từng pair để lưu chỉ số hàng, giá trị sau lưu chỉ số cột.
    q.push(make_pair(i, j));
    visited[i][j] = true; // đã thăm vị trí có tọa độ (i, j)
    while (q.size())
    {                                 // trong khi q chưa rỗng
        pair<int, int> u = q.front(); // u là phần tử ở đầu hàng đợi q
        q.pop();                      // xóa u
        for (int i = 0; i < 4; i++)
        { // for các hướng kề u
            int dx = hx[i] + u.first;
            int dy = hy[i] + u.second; // dx, dy chính là tọa độ mới vừa được loang ra từ u
            if (dx < 1 || dx > m || dy < 1 || dy > n)
            { // nếu như tọa độ thu được nằm ở ngoài lưới -> không xét
                continue;
            }
            if (a[dx][dy] == 0 || visited[dx][dy] == true)
            { // nếu giá trị của tọa độ (dx, dy) là 0 hoặc tọa độ này đã thăm -> không xét
                continue;
            }
            q.push(make_pair(dx, dy)); // đẩy (dx, dy) vào queue để xét tiếp
            visited[dx][dy] = true;    // đã thăm vị trí có tọa độ (dx, dy)
        }
    }
}

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> m >> n;
    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            cin >> a[i][j];
        }
    }
    memset(visited, false, sizeof(visited)); // gán tất cả phần tử ở mảng visited = false tức là chưa có đỉnh nào được thăm
    int cnt = 0;
    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (a[i][j] == 1 && visited[i][j] == false)
            { // nếu như tọa độ (i, j) có giá trị bằng 1 và chưa được thăm, ta sẽ bắt đầu BFS ở đây.
                bfs(i, j);
                ++cnt;
            }
        }
    }
    cout << cnt;
    return 0;
}