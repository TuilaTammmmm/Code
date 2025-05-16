#include <stdio.h>
#define MAX 16

int X[MAX], n;
int count1s()
{
    int dem = 0;
    for (int i = 0; i < n; i++)
        if (X[i] == 1)
            dem++;
    return dem;
}

void Print()
{
    if (count1s() % 2 == 0)
    {
        for (int i = 0; i < n; i++)
        {
            printf("%d", X[i]);
            if (i < n - 1)
                printf(" ");
        }
        printf("\n");
    }
}

void GenerateBinaryStrings(int i)
{
    for (int j = 0; j <= 1; j++)
    {
        X[i] = j;
        if (i == n - 1)
            Print();
        else
            GenerateBinaryStrings(i + 1);
    }
}

int main()
{
    scanf("%d", &n);
    if (n <= 2 || n >= 16)
        return 0;
    GenerateBinaryStrings(0);
    return 0;
}