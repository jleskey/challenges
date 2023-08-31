#include <iostream>
#include <string>

using namespace std;

// Since we know the number has to be between 1 and 10 (inclusive),
// it must be higher than 0 and less than 11. These make good
// default values.
int KNOWN_LOW = 0,
    KNOWN_HIGH = 11;

// We assume honesty until something doesn't add up.
bool HONESTY_ASSUMPTION = true;

int main() {
    // We use our sesible defaults.
    int tooLow = KNOWN_LOW, tooHigh = KNOWN_HIGH;
    bool honest = HONESTY_ASSUMPTION;

    int lastNumber = 0;
    string lastResponse = "";

    cin >> lastNumber;

    while (lastNumber != 0) {
        cin.ignore();
        getline(cin, lastResponse);

        if (lastResponse == "right on") {
            if (lastNumber <= tooLow || lastNumber >= tooHigh) {
                honest = false;
            }
            cout << "Stan " << (honest ? "may be honest" : "is dishonest") << endl;
            // New game!
            tooLow = KNOWN_LOW;
            tooHigh = KNOWN_HIGH;
            honest = HONESTY_ASSUMPTION;
        }
        else if (lastResponse == "too low" && lastNumber < tooHigh) {
            if (lastNumber > tooLow)
                tooLow = lastNumber;
        }
        else if (lastResponse == "too high" && lastNumber > tooLow) {
            if (lastNumber < tooHigh)
                tooHigh = lastNumber;
        }
        else {
            honest = false;
        }

        cin >> lastNumber;
    }
}