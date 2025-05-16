#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Hàm đổi chỗ hai ký tự
void swap(char *a, char *b) {
    char temp = *a;
    *a = *b;
    *b = temp;
}

// Hàm sắp xếp xâu theo thứ tự từ điển (bubble sort đơn giản)
void sortString(char *s) {
    int len = strlen(s);
    for (int i = 0; i < len - 1; i++) {
        for (int j = 0; j < len - i - 1; j++) {
            if (s[j] > s[j + 1]) {
                swap(&s[j], &s[j + 1]);
            }
        }
    }
}

// Hàm đệ quy để sinh các tập con
void generateSubsets(char *s, int pos, char *current, int len, int currLen) {
    // Nếu đã duyệt hết xâu, in tập con hiện tại (nếu không rỗng)
    if (pos == len) {
        if (currLen > 0) { // Chỉ in nếu tập con không rỗng
            current[currLen] = '\0'; // Kết thúc chuỗi
            printf("%s ", current);
        }
        return;
    }

    // Trường hợp không chọn ký tự tại vị trí pos
    generateSubsets(s, pos + 1, current, len, currLen);

    // Trường hợp chọn ký tự tại vị trí pos
    current[currLen] = s[pos];
    generateSubsets(s, pos + 1, current, len, currLen + 1);
}

int main() {
    int T;
    scanf("%d", &T); // Đọc số lượng test case

    while (T--) {
        char s[17]; // Xâu tối đa 16 ký tự + 1 ký tự null
        char current[17]; // Lưu tập con hiện tại

        scanf("%s", s); // Đọc xâu trực tiếp

        sortString(s); // Sắp xếp xâu theo thứ tự từ điển

        // Gọi hàm sinh tập con
        generateSubsets(s, 0, current, strlen(s), 0);
        printf("\n"); // In xuống dòng sau mỗi test case
    }

    return 0;
}