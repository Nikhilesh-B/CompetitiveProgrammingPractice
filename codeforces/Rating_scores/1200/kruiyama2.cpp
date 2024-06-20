#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

vector<ll> getleftcosts(vector<ll> &c)
{
    vector<ll> leftcosts{};
    ll leftsum = 0;
    for (ll j : c)
    {
        leftsum += j;
        leftcosts.push_back(leftsum);
    }
    return leftcosts;
}

vector<ll> getrightcosts(vector<ll> &c)
{
    vector<ll> rightcosts{};
    ll rightsum = 0;
    for (ll j = c.size() - 1; j >= 0; --j)
    {
        rightsum += c[j];
        rightcosts.push_back(rightsum);
    }
    reverse(rightcosts.begin(), rightcosts.end());
    return rightcosts;
}

int main()
{
    ll n{}, m{};

    vector<ll> costs;

    cin >> n;
    for (ll i = 0; i < n; ++i)
    {
        ll x{};
        cin >> x;
        costs.push_back(x);
    }

    vector<ll> sorted_costs = costs; // Correctly assign sorted_costs
    sort(sorted_costs.begin(), sorted_costs.end());

    ll total = 0;
    for (ll c : costs)
    {
        total += c;
    }

    vector<ll> leftcosts = getleftcosts(costs);
    vector<ll> rightcosts = getrightcosts(costs);

    vector<ll> leftcostssrt = getleftcosts(sorted_costs);
    vector<ll> rightcostssrt = getrightcosts(sorted_costs);

    cin >> m;
    ll type{}, l{}, r{}, ans{};

    while (m--)
    {
        cin >> type >> l >> r;
        ans = total;
        if (type == 0)
        {
            if (l > 1)
            {
                ans -= leftcosts[l - 2]; // Adjusted for 0-based indexing
            }
            if (r < costs.size())
            {
                ans -= rightcosts[r]; // Adjusted for 0-based indexing
            }
            cout << ans << endl;
        }
        else
        {
            if (l > 1)
            {
                ans -= leftcostssrt[l - 2]; // Adjusted for 0-based indexing
            }
            if (r < costs.size())
            {
                ans -= rightcostssrt[r]; // Adjusted for 0-based indexing
            }
            cout << ans << endl;
        }
    }

    return 0;
}