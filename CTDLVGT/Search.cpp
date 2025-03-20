#include <iostream>
using namespace std;
void swap(int *x, int *y){
    int temp = *x; *x = *y; *y = temp;
}
void SelectionSort(int arr[],int M[], int n){
    int i, j, min_idx;
    for (i = 0; i < n-1; i++) {
    min_idx = i;
    for (j = i+1; j < n; j++){
    if (arr[j] < arr[min_idx])
    min_idx = j;
    }
    swap(&arr[min_idx], &arr[i]);
    swap(&M[min_idx], &M[i]);
    }
   }
int SequentialSearch(int A[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (x == A[i])
            return i;
    }
    return -1;
}
int BinarySearch(int A[],int M[], int n, int x) {
    SelectionSort(A,M, n);
    int low = 0;
    int high = n - 1;
    int mid;
    while (low <= high) {
        mid = (low + high) / 2;
        if (x > A[mid])
            low = mid + 1;
        else if (x < A[mid])
            high = mid - 1;
        else
            return mid;
    }
    return -1;
}
int main() {
    int A[] = {5,7,1,2,4,8};
    int n = sizeof(A)/sizeof(A[0]);
    int M[n];
    for (int i = 0; i < n; i++)
    {
        M[i] = i;
    }
    int x;
    cin >> x;   
    int Sequential = SequentialSearch(A, n, x);
    int Binary = BinarySearch(A,M, n, x);
    if (Sequential != -1)
        cout << Sequential << endl;
    if (Binary != -1)
        cout << M[Binary] << endl;
    return 0;
}