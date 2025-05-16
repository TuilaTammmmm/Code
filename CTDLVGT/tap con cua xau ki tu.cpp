#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmp(const void *a, const void *b) {
    return strcmp(*(char **)a, *(char **)b);
}

void generateSubsets(char *s, int len) {
    int total = 1 << len; // 2^len
    char **subsets = (char **)malloc(sizeof(char*) * total);
    int count = 0;

    for (int mask = 1; mask < total; ++mask) {
        char *subset = (char *)malloc(len + 1);
        int idx = 0;
        for (int i = 0; i < len; ++i) {
            if (mask & (1 << i)) {
                subset[idx++] = s[i];
            }
        }
        subset[idx] = '\0';
        subsets[count++] = subset;
    }

    qsort(subsets, count, sizeof(char*), cmp);

    for (int i = 0; i < count; ++i) {
        printf("%s", subsets[i]);
        if (i != count - 1) printf(" ");
        free(subsets[i]);
    }
    printf("\n");
    free(subsets);
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int n;
        char s[20];
        scanf("%d", &n);
        scanf("%s", s);

        qsort(s, n, sizeof(char), (int(*)(const void*, const void*))strcmp);
        generateSubsets(s, n);
    }
    return 0;
}

