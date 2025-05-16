#include <stdio.h>
#include <string.h>

int N;
char s[20];

int isPhatLoc(char s[]) {
    if (s[0] != '8' || s[N - 1] != '6') return 0;

    for (int i = 0; i < N - 1; i++) {
        if (s[i] == '8' && s[i + 1] == '8') return 0;
    }

    for (int i = 0; i <= N - 4; i++) {
        if (s[i] == '6' && s[i + 1] == '6' && s[i + 2] == '6' && s[i + 3] == '6')
            return 0;
    }

    return 1;
}

void Try(int i) {
    for (char c = '6'; c <= '8'; c += 2) {
        s[i] = c;
        if (i == N - 1) {
            if (isPhatLoc(s)) {
                s[N] = '\0';
                printf("%s\n", s);
            }
        } else {
            Try(i + 1);
        }
    }
}

int main() {
    scanf("%d", &N);
    Try(0);
    return 0;
}
