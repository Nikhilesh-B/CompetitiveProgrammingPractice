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

void remove_val(int b, deque<int> &sa)
{
    auto it = lower_bound(sa.begin(), sa.end(), b);
    if (it != sa.end() && *it == b)
    {
        sa.erase(it);
    }
}

void insert_val(int b, deque<int> &sa)
{
    auto it = lower_bound(sa.begin(), sa.end(), b);
    sa.insert(it, b);
}

void solve()
{
    int n, x;
    cin >> n;
    deque<int> a;
    for (int i = 0; i < n; ++i)
    {
        cin >> x;
        a.push_back(x);
    }

    int max_median = -1;
    deque<int> sorted_a = {a[0], a[0]};
    int i = 0;
    int j = 0;
    while (j < n)
    {
        if (i == j)
        {
            remove_val(a[j], sorted_a);
            j++;
            insert_val(a[j], sorted_a);
        }

        max_median = max(max_median, sorted_a[(sorted_a.size() + 1) / 2 - 1]);

        if (a[i] > a[j])
        {
            remove_val(a[j], sorted_a);
            j++;
            insert_val(a[j], sorted_a);
        }
        else
        {
            remove_val(a[i], sorted_a);
            i++;
            insert_val(a[i], sorted_a);
        }
    }
    cout << max_median << endl;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}