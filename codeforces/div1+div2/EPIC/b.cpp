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

typedef long long ll;

ll process_case(int n, vector<int> &a)
{
    vector<int> defecits{};
    vector<int> greatest_seen_to_left(n, a[0]);
    for (int i = 1; i < n; ++i)
        greatest_seen_to_left[i] = max(greatest_seen_to_left[i - 1], a[i - 1]);

    for (int i = 1; i < n; ++i)
    {
        if (greatest_seen_to_left[i] > a[i])
            defecits.push_back(greatest_seen_to_left[i] - a[i]);
    }

    sort(defecits.begin(), defecits.end());

    ll total_coins = 0;
    ll current_made_up = 0;

    for (int i = 0; i < defecits.size(); ++i)
    {
        if (defecits[i] > current_made_up)
        {
            total_coins += (defecits.size() - i + 1) * (defecits[i] - current_made_up);
            current_made_up = defecits[i];
        }
    }

    return total_coins;
}

int main()
{
    int t{}, n{}, x;
    cerr << "Hello this is a test";
    cin >> t;

    vector<ll> answers{};

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