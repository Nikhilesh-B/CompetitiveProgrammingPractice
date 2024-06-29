#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <set>
#include <climits>

using namespace std;

typedef long long ll;

ll process_case(ll n, ll x, vector<ll> &s)
{
    sort(s.begin(), s.end());
    for (ll i = 0; i < n; ++i)
    {
        if (i == 0)
            continue;
        s[i] += s[i - 1];
    }
    auto it_lower = lower_bound(s.begin(), s.end(), x);
    if (it_lower != s.begin() && !binary_search(s.begin(), s.end(), x))
        --it_lower;

    ll found_idx{};
    if (it_lower == s.begin())
        found_idx = 0;
    else
        found_idx = it_lower - s.begin();

    int number_to_take[found_idx + 1];
    ll total = 0;
    ll days_passed = 0;
    for (ll i = found_idx; i > -1; --i)
    {
        if (i == found_idx)
            number_to_take[i] = max((x - s[i]) / (i + 1) + 1, 0ll);
        else
            number_to_take[i] = max((x - s[i]) / (i + 1) - days_passed + 1, 0ll);
        days_passed += number_to_take[i];
    }

    for (ll i = 0; i < found_idx + 1; ++i)
    {
        total += (number_to_take[i] * (i + 1));
    }

    return total;
};

int main()
{
    int t{};
    cin >> t;

    vector<ll> answers{};

    ll n{}, x{}, a{};
    while (t--)
    {
        vector<ll> shops{};
        cin >> n >> x;
        for (int i = 0; i < n; i++)
        {
            cin >> a;
            shops.push_back(a);
        }
        answers.push_back(process_case(n, x, shops));
    }

    for (ll ans : answers)
    {
        cout << ans << endl;
    }
}
