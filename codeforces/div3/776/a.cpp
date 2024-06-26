#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <climits>

using namespace std;

void process_case(string s, char c)
{
    int length = s.length();
    if (length % 2 == 0)
    {
        cout << "NO" << endl;
        return;
    }

    for (int i = 0; i < length; ++i)
    {
        if (s[i] == c && (i + 1) % 2 == 1)
        {
            cout << "YES" << endl;
            return;
        }
    }

    cout << "NO" << endl;
    return;
}

int main()
{
    int t{};
    cin >> t;

    while (t--)
    {
        string s{};
        char c{};
        cin >> s;
        cin >> c;
        process_case(s, c);
    }
}