#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;  // Read the number of elements
    vector<string> numbers(n);

    for (int i = 0; i < n; i++) {
        cin >> numbers[i];  // Read the large numbers as strings
    }

    // Find the smallest number using string comparison
    string min_number = *min_element(numbers.begin(), numbers.end());

    cout << min_number << endl;  // Output the smallest number

    return 0;
}
