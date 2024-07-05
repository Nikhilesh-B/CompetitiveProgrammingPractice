#include <iostream>
#include <vector>
#include <iomanip>
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

ll solve()
{
    int n;
    cin >> n;

    vector<ll> a(n);
    for (int i = 0; i < n; ++i)
        cin >> a[i];

    reverse(a.begin(), a.end());

    ll total_splits = 0;
    ll cmax = a[0];

    for (int i = 1; i < n; ++i)
    {
        double divnto = static_cast<double>(a[i]) / static_cast<double>(cmax);
        ll divntoi = a[i] / cmax;

        if (!(a[i] % cmax))
            total_splits += divntoi - 1;
        else if (divnto > 2.0)
        {
            total_splits += divntoi - 1 + 1;
            ll leftover = a[i] - (divntoi - 1) * cmax;
            cmax = min(leftover / 2, leftover - (leftover / 2));
        }
        else if (divnto > 1.0)
        {
            total_splits += 1;
            cmax = min(a[i] / 2, a[i] - (a[i] / 2));
        }
        else
        {
            cmax = a[i];
        }
    }
    return total_splits;
}

int main()
{
    ios::sync_with_stdio(false); // Disable synchronization with C I/O
    cin.tie(nullptr);            // Untie cin from cout for faster input

    int t;
    cin >> t;
    vector<ll> answers(t);
    for (int i = 0; i < t; ++i)
        answers[i] = solve();

    for (auto ans : answers)
        cout << ans << endl;

    return 0;
}