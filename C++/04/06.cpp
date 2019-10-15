#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int main() {
    vector<string> words;
    for (string temp; cin >> temp;) {
        words.push_back(temp);
    }
    cout << "Number of words: " << words.size() << "\n";
    for (int i = 0; i < words.size(); i++) {
        if (words[i] == "Broccoli") {
            words[i] = "BLEEP";
        }
    }
    sort(words.begin(), words.end());
    for (int i = 0; i < words.size(); i++) {
        if (i == 0 || words[i - 1] != words[i]) {
            cout << words[i] << "\n";
        }
    }
    return 0;
}