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

// val, idx
typedef pair<int, int> ipair;

void print_deque(deque<ipair> state)
{
    cout << "[ ";
    for (auto pi : state)
    {
        cout << "(val= " << pi.first << ", idx=" << pi.second << ") ";
    }
    cout << "]" << endl;
}

int process_sub_case(int m, int d, vector<int> &ci)
{
    deque<ipair> state{};
    for (int i = 0; i < m; ++i)
    {
        // cout << "P1 " << endl;
        // print_deque(state);

        // cout << "INDEX" << i << endl;
        if (i == 0)
        {
            state.push_back(make_pair(1, 0));
            continue;
        }
        ipair topvalue = state[0];
        int val = topvalue.first;
        int idx = topvalue.second;
        int newval = val + (ci[i] + 1);

        if (abs(i - idx) - 1 == d)
            state.pop_front();

        while (!state.empty() && state[state.size() - 1].first >= newval)
            state.pop_back();

        state.push_back(make_pair(newval, i));
        // // cout << "P2 " << endl;
        // print_deque(state);
    }
    while (state[0].second != m - 1)
        state.pop_front();

    return state[0].first;
}

int process_case(int n, int m, int k, int d, vector<vector<int>> &c)
{
    deque<int> answers{};

    for (int i = 0; i < n; ++i)
    {
        vector<int> cse = c[i];
        int val1 = process_sub_case(m, d, cse);
        // reverse(cse.begin(), cse.end());
        // int val2 = process_sub_case(m, d, cse);
        answers.push_back(val1);
    }

    int rval = 0;
    sort(answers.begin(), answers.end());
    while (k--)
    {
        rval += answers[0];
        answers.pop_front();
    }
    return rval;
}

int main()
{
    int t{};
    cin >> t;
    vector<int> answers{};
    while (t--)
    {
        int n{}, m{}, k{}, d{}, x{};
        cin >> n >> m >> k >> d;
        vector<vector<int>> channels{};
        for (int i = 0; i < n; i++)
        {
            vector<int> lst{};
            for (int i = 0; i < m; ++i)
            {
                cin >> x;
                lst.push_back(x);
            }
            channels.push_back(lst);
        }
        answers.push_back(process_case(n, m, k, d, channels));
    }
    for (auto ans : answers)
    {
        cout << ans << endl;
    }
}