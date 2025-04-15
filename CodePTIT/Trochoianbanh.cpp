#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    string s;
    cin >> s;

    int g_pos = -1, t_pos = -1;

    for (int i = 0; i < n; i++) {
        if (s[i] == 'G') g_pos = i;
        if (s[i] == 'T') t_pos = i;
    }

    if (g_pos > t_pos) swap(g_pos, t_pos);

    bool can_reach = true;
    for (int i = g_pos; i <= t_pos; i += k) {
        if (s[i] == '#') {
            can_reach = false;
            break;
        }
        if (i == t_pos) {
            cout << "YES" << endl;
            return 0;
        }
    }

    cout << "NO" << endl;
    return 0;
}