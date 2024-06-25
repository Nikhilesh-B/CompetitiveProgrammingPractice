#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <climits>

using namespace std;

typedef long long ll;

int process_case(ll x, ll y, ll k)
{
    while (x != 1 && x + k >= (x / y + 1) * y)
    {
        long long next_multiple = (x / y + 1) * y;
        k -= (next_multiple - x);
        x = next_multiple;
        while (x % y == 0)
        {
            x /= y;
        }
    }
    if (x == 1)
        return x + k % (y - 1);
    else
        return x + k % y;
}

void solve()
{
    long long x, y, k;
    cin >> x >> y >> k;
    while (k > 0 && x != 1)
    {
        long long ost = (x / y + 1) * y - x;
        ost = max(1ll, ost);
        ost = min(ost, k);
        x += ost;
        while (x % y == 0)
        {
            x /= y;
        }
        k -= ost;
    }
    cout << x + k % (y - 1) << '\n';
}

int main()
{
    int t;
    cin >> t;

    vector<ll> answers;

    while (t--)
    {
        // solve();
        ll x{}, y{}, k{};
        cin >> x >> y >> k;
        answers.push_back(process_case(x, y, k));
    }

    for (ll ans : answers)
    {
        cout << ans << endl;
    }
}
