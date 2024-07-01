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

typedef pair<vector<int>, int> cpair;

bool no_zeros_relevant_zeros(vector<int> &a)
{
    int n = a.size();
    for (int i = 0; i < n; ++i)
    {
        int ai = a[i];
        if (ai == 0 && i != n - 1)
            return false;
    }
    return true;
}

cpair update_vector_a(vector<int> &os, int ops)
{
    vector<int> new_vector = {};
    int n = os.size();
    int save_idx = -1;

    for (int i = n - 2; i > -1; --i)
    {
        int osi = os[i];
        if (osi == 0)
        {
            save_idx = i;
            break;
        }
    }

    for (int j = 0; j < n; ++j)
    {
        if (j < save_idx)
            new_vector.push_back(os[j]);
        else if (j > save_idx + 1)
            new_vector.push_back(os[j] - 2);
    }
    ops += 1;
    return make_pair(new_vector, ops);
}

int process_case(int n, vector<int> &a)
{
    vector<int> os{};
    int ops = 0;
    for (int i = 0; i < n; ++i)
    {
        os.push_back(a[i] - (i + 1));
    }
    while (!no_zeros_relevant_zeros(os))
    {
        cpair rpair = update_vector_a(os, ops);
        ops = rpair.second;
        os = rpair.first;
    }

    return ops;
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