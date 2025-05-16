#include <stdio.h>
#include <stdlib.h>

int X[50];
float a[50];
int n, k;
int OK = 1;

int compare(const void *a, const void *b) {
    float fa = *(float*)a;
    float fb = *(float*)b;
    if (fa < fb) return -1;
    if (fa > fb) return 1;
    return 0;
}

void remove_duplicates() {
    int new_n = 1;
    for (int i = 2; i <= n; i++) {
        if (a[i] != a[new_n]) {
            new_n++;
            a[new_n] = a[i];
        }
    }
    n = new_n;
}

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
    scanf("%d %d", &n, &k);
    for (int i = 1; i <= n; i++)
        scanf("%f", &a[i]);

    for (int i = 1; i <= k; i++)
        X[i] = i;

    qsort(a + 1, n, sizeof(float), compare);

    remove_duplicates();
}

int main() {
    Init();
    while (OK) {
        result();
        Next_Combination();
    }
    return 0;
}
