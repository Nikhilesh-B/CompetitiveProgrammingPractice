#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

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

vector<ll> getrightcosts(vector<ll> &c, int total)
{
    vector<ll> rightcosts{};
    ll rightsum = 0;
    for (ll j = c.size() - 1; j > -1; --j)
    {
        rightsum += c[j];
        rightcosts.push_back(rightsum);
    }
    reverse(rightcosts.begin(), rightcosts.end());
    return rightcosts;
}

int main()
{
    int n{}, m{};

    vector<ll> costs;

    cin >> n;
    for (int i = 0; i < n; ++i)
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
    vector<ll> rightcosts = getrightcosts(costs, total);

    vector<ll> leftcostssrt = getleftcosts(sorted_costs);
    vector<ll> rightcostssrt = getrightcosts(sorted_costs, total);

    cin >> m;
    int type{}, l{}, r{};
    ll ans;

    vector<ll> answers{};

    while (m--)
    {
        cin >> type >> l >> r;
        l--;
        r--;
        ans = total;
        if (type == 1)
        {
            if (l > 0)
            {
                ans -= leftcosts[l - 1];
            }
            if (r < costs.size() - 1)
            {
                ans -= rightcosts[r + 1];
            }
        }

        else
        {
            if (l > 0)
            {
                ans -= leftcostssrt[l - 1];
            }
            if (r < costs.size() - 1)
            {
                ans -= rightcostssrt[r + 1];
            }
        }
        answers.push_back(ans);
    }

    for (ll s : answers)
    {
        cout << s << endl;
    }
}