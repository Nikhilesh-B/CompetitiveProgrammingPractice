#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <climits>

using namespace std;

string process_case(int x1, int y1, int x2, int y2)
{
    if (x1 == y1)
    {
        return "YES";
    }
    else if (x1 > y1)
    {
        if (y2 >= x2)
            return "NO";
        else
            return "YES";
    }
    else
    {
        if (x2 >= y2)
            return "NO";
        else
            return "YES";
    }
}

int main()
{
    int t{};

    cin >> t;

    vector<string> answers;

    while (t--)
    {
        int x1{}, y1{}, x2{}, y2{};
        cin >> x1 >> y1 >> x2 >> y2;
        answers.push_back(process_case(x1, y1, x2, y2));
    }
    for (string ans : answers)
    {
        cout << ans << endl;
    }
}