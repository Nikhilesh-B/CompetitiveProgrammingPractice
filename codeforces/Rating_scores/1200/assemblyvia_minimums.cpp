#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <vector>
#include <unordered_map>
#include <climits>

using namespace std;

string process_case(int n, vector<int> &ma)
{
    string rstr = "";
    vector<int> indx_positions = {};

    int running_idx = -1;
    for (int i = 0; i < n - 1; ++i)
    {
        running_idx += (n - 1 - i);
        indx_positions.push_back(running_idx);
    }

    sort(ma.begin(), ma.end());

    vector<int> rarr = {};

    for (int pos : indx_positions)
    {
        rarr.push_back(ma[pos]);
    }
    rarr.push_back(ma[ma.size() - 1]);

    for (int mv : rarr)
    {
        rstr += (to_string(mv) + " ");
    }

    return rstr;
}

int main()
{
    int t{};
    cin >> t;
    int x{}, n{};

    vector<string> answers = {};

    while (t--)
    {
        vector<int> minarr = {};
        cin >> n;

        for (int i = 0; i < n * (n - 1) / 2; ++i)
        {
            cin >> x;
            minarr.push_back(x);
        }

        answers.push_back(process_case(n, minarr));
    }

    for (string sa : answers)
    {
        cout << sa << endl;
    }
}