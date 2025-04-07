
#include <bits/stdc++.h>
using namespace std;

void solve(vector<int> &a, int n) {
    vector<int> L(n), R(n);
    stack<int> st;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && a[st.top()] >= a[i]) {
            st.pop();
        }
        if (st.empty())
            L[i] = 0;
        else
            L[i] = st.top() + 1;
        st.push(i);
    }

    while (!st.empty()) {
        st.pop();
    }

    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && a[st.top()] >= a[i]) {
            st.pop();
        }
        if (st.empty())
            R[i] = n - 1;
        else
            R[i] = st.top() - 1;
        st.push(i);
    }
    
    for (int i = 0; i < n; ++i) {
        a[i] = R[i] - L[i] + 1;
    }
}

void TestCase() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> a(n, vector<int>(m, 0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> a[i][j];
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (i > 0 && a[i][j] != 0)
                a[i][j] += a[i - 1][j];
        }
    }

    int res = 0;
    for (int i = 0; i < n; ++i) {
        vector<int> b(a[i].begin(), a[i].end());
        solve(b, m);
        for (int j = 0; j < m; ++j) {
            res = max(res, min(a[i][j], b[j]));
        }
    }
    cout << res << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    while (T--) {
        TestCase();
    }
    return 0;
}
