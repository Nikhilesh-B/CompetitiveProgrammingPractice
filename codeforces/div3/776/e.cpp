#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <climits>

using namespace std;

void insert_in_order(vector<pair<int, int>> &interval_idxs, pair<int, int> insertpair)
{
    int insertion_idx = 0;
    int lo = 0;
    int hi = interval_idxs.size() - 1;

    while (lo <= hi)
    {
        int cand = (hi + lo) / 2;
        if (interval_idxs[cand].first < insertpair.first)
        {
            lo = cand + 1;
            insertion_idx = cand;
        }
        else if (interval_idxs[cand].first > insertpair.first)
        {
            hi = cand - 1;
        }
        else
        {
            insertion_idx = cand;
            break;
        }
    }
    cout << "insertion idx" << insertion_idx;
    interval_idxs.insert(interval_idxs.begin() + insertion_idx, insertpair);
}

void print_interval_idxs(vector<pair<int, int>> &interval_idxs)
{
    cout << "[";
    for (auto a : interval_idxs)
    {
        cout << "(" << a.first << "," << a.second << ")";
    }
    cout << "]" << endl;
}

void print_points(vector<int> &lst)
{
    cout << "[";
    for (auto a : lst)
    {
        cout << a << ", ";
    }
    cout << "]" << endl;
}

int process_case(int n, int d, vector<int> &dates)
{
    vector<pair<int, int>> interval_idxs{};
    print_points(dates);
    int length = dates.size();
    for (int i = 0; i < length - 1; ++i)
    {
        pair<int, int> insertpair;
        insertpair.first = dates[i + 1] - dates[i];
        insertpair.second = i;
        insert_in_order(interval_idxs, insertpair);
    }
    print_interval_idxs(interval_idxs);

    int mu = interval_idxs[0].first;

    if (interval_idxs.size() == 2)
    {
        return (d - 1) / 2;
    }

    if (interval_idxs[0].first == interval_idxs[2].first)
        return mu;
    else if (interval_idxs[0].first == interval_idxs[1].first)
    {
        if (abs(interval_idxs[0].second - interval_idxs[1].second) == 1)
            return 2 * mu + 1;
        else
            return mu;
    }
    else
        return (interval_idxs[interval_idxs.size() - 1].first - 1) / 2;
}

int main()
{
    int t{};
    cin >> t;
    vector<int> answers;
    while (t--)
    {
        int n{}, d{}, x{};
        vector<int> dates{1};
        cin >> n >> d;
        for (int i = 0; i < n; ++i)
        {
            cin >> x;
            dates.push_back(x);
        }
        dates.push_back(d);
        answers.push_back(process_case(n, d, dates));
    }

    for (int a : answers)
    {
        cout << a << endl;
    }
}