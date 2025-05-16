#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
using namespace std;

#define MAX 100
int X[MAX], n, k, dem = 0;
bool OK = true;

void Next_Combination(void)
{
    int i = k;
    while (i > 0 && X[i] == n - k + i)
        i--;
    if (i > 0)
    {
        X[i] = X[i] + 1;
        for (int j = i + 1; j <= k; j++)
            X[j] = X[i] + j - i;
    }
    else
        OK = false;
}

// Hàm sinh tất cả các tập con của xâu ký tự S
void generateSubsets(string &S, string current, int index, vector<string> &result) {
    if (index == S.length()) {
        if (!current.empty()) {
            result.push_back(current);
        }
        return;
    }

    // Không chọn ký tự hiện tại
    generateSubsets(S, current, index + 1, result);

    // Chọn ký tự hiện tại
    generateSubsets(S, current + S[index], index + 1, result);
}

int main(void)
{
    // Phần sinh tổ hợp
    cin >> n >> k;
    for (int i = 1; i <= k; i++)
        X[i] = i;
    while (OK)
    {
        cout << "\n Kết quả " << ++dem << ":";
        for (int i = 1; i <= k; i++)
            cout << X[i] << setw(3);
        Next_Combination();
    }

    // Phần sinh tập con
    int T;
    cin >> T; // Số lượng test
    while (T--) {
        string S;
        cin >> S;

        // Sắp xếp xâu ký tự để đảm bảo thứ tự từ điển
        sort(S.begin(), S.end());

        vector<string> subsets;
        generateSubsets(S, "", 0, subsets);

        // Sắp xếp kết quả để đảm bảo thứ tự từ điển
        sort(subsets.begin(), subsets.end());

        // In kết quả
        for (const string &subset : subsets) {
            cout << subset << " ";
        }
        cout << endl;
    }

    return 0;
}