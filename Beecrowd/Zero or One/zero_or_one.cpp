#include <iostream>

using namespace std;

int main() {
    int A = 0, B = 0, C = 0;

    while (cin >> A >> B >> C) {
        if (A != B && A != C)
            cout << "A";
        else if (B != A && B != C)
            cout << "B";
        else if (C != A && C != B)
            cout << "C";
        else
            cout << "*";
        cout << endl;
    }
}