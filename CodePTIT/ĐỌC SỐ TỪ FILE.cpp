#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

string units[] = {"khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"};

string teens[] = {"muoi", "muoi mot", "muoi hai", "muoi ba", "muoi bon", "muoi lam", "muoi sau", "muoi bay", "muoi tam", "muoi chin"};

string tens[] = {"", "", "hai muoi", "ba muoi", "bon muoi", "nam muoi", "sau muoi", "bay muoi", "tam muoi", "chin muoi"};

string readUnit(int n) {
    return units[n];
}

string readTwoDigits(int n) {
    if (n < 10) {
        return readUnit(n);
    } else if (n < 20) {
        return teens[n - 10];
    } else {
        int ten = n / 10;
        int unit = n % 10;
        if (unit == 0) {
            return tens[ten];
        } else {
            return tens[ten] + " " + readUnit(unit);
        }
    }
}

string readThreeDigits(int n) {
    int hundred = n / 100;
    int remainder = n % 100;
    string result = readUnit(hundred) + " tram";
    if (remainder > 0) {
        if (remainder < 10) {
            result += " linh " + readUnit(remainder);
        } else {
            result += " " + readTwoDigits(remainder);
        }
    }
    return result;
}

string readLargeNumber(int n) {
    if (n == 0) return "khong";
    if (n < 1000) return readThreeDigits(n);

    string result = "";
    int billion = n / 1000000000;
    n %= 1000000000;
    int million = n / 1000000;
    n %= 1000000;
    int thousand = n / 1000;
    n %= 1000;

    if (billion > 0) {
        result += readLargeNumber(billion) + " ty";
        if (million > 0 || thousand > 0 || n > 0) {
            result += " ";
        }
    }

    if (million > 0) {
        result += readThreeDigits(million) + " trieu";
        if (thousand > 0 || n > 0) {
            result += " ";
        }
    }

    if (thousand > 0) {
        result += readThreeDigits(thousand) + " nghin";
        if (n > 0) {
            result += " ";
        }
    }

    if (n > 0) {
        result += readThreeDigits(n);
    }

    return result;
}

int main() {
    ifstream inputFile("data.in");
    if (inputFile.is_open()) {
        int numTestCases;
        inputFile >> numTestCases;
        inputFile.ignore();

        for (int i = 0; i < numTestCases; ++i) {
            int n;
            inputFile >> n;
            inputFile.ignore();
            cout << readLargeNumber(n) << endl;
        }
        inputFile.close();
    } else {
        cout << "Khong the mo file data.in" << endl;
    }
    return 0;
}