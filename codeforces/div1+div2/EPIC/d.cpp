#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <unordered_set>
#include <list>
#include <map>
#include <set>
#include <climits>
#include <queue>

using namespace std;

int process_case(int n, vector<int> &a)
{
    map<int, int> counts;
    for (auto ai : a)
    {
        if (counts.find(ai) == counts.end())
            counts[ai] = 1;
        else
            counts[ai] += 1;
    }
    int x = 0;
    int alice_val = counts.begin()->first;
    int bob_val{};
    int prev_val = -INT_MAX;

    while (true)
    {
        prev_val = alice_val;
        if (counts[alice_val] > 0)
        {
            counts[alice_val] -= 1;
            x += 1;
            if (counts[alice_val] == 0)
                counts.erase(alice_val);
        }

        auto it = counts.upper_bound(alice_val);
        if (it != counts.end())
        {
            bob_val = it->first;
            counts[bob_val] -= 1;
            if (counts[bob_val] == 0)
            {
                counts.erase(bob_val);
                it = counts.upper_bound(bob_val);
                if (it != counts.end())
                    alice_val = it->first;
                else
                    return x;
            }
            else
            {
                alice_val = bob_val;
            }
        }
        else
            return x;
    }
    return x;
}

int main()
{
    int t{}, n{}, x;
    cin >> t;

    vector<int> answers{};

    while (t--)
    {
        vector<int> a{};
        cin >> n;
        for (int i = 0; i < n; ++i)
        {
            cin >> x;
            a.push_back(x);
        }
        answers.push_back(process_case(n, a));
    }

    for (auto ans : answers)
    {
        cout << ans << endl;
    }
}