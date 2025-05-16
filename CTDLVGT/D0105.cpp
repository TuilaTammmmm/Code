#include <stdio.h>

int X[50];
float a[50];
int n, k;
int OK = 1;

void Next_Combination() {
    int i = k;
    while (i > 0 && X[i] == n - k + i)
        i--;
    if (i > 0) {
        X[i] = X[i] + 1;
        for (int j = i + 1; j <= k; j++)
            X[j] = X[i] + j - i;
    } else {
        OK = 0;
    }
}

void result() {
    for (int i = 1; i <= k; i++)
        printf("%.0f\t", a[X[i]]);
    printf("\n");
}

void Init() {
    scanf("%d%d", &n, &k);
    for (int i = 1; i <= n; i++) {
        a[i] = i;
        X[i] = i;
    }
}

int Cnk(int n, int k) {
    if (k == 0 || k == n) return 1;
    if (k > n) return 0;
    int res = 1;
    for (int i = 1; i <= k; i++) {
        res = res * (n - i + 1) / i;
    }
    return res;
}

void solve() {
    Init();
    int C[50];
    C[0] = 0;
    for (int i = 1; i <= k; i++) {
        scanf("%d", &C[i]);
    }
    int ans = 1;
    for (int i = 1; i <= k; i++) {
        for (int j = C[i - 1] + 1; j < C[i]; j++) {
            ans += Cnk(n - j, k - i);
        }
    }
    printf("%d\n", ans);
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        solve();
    }
    return 0;
}
