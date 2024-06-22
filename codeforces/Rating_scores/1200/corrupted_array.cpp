#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <climits>

using namespace std;

typedef long long ll;

ll calculate_sum(vector<int> &b)
{
    ll sum = 0;
    for (int bi : b)
    {
        sum += bi;
    }
    return sum;
}

void output_list(vector<int> &a, int idx1, int idx2)
{
    // print all except the id1 and idx2 items from the list
    for (int j = 0; j < a.size(); ++j)
    {
        if (!(j == idx1 || j == idx2))
        {
            cout << a[j] << " ";
        }
    }
    cout << endl;
}

void process_case(vector<int> &b, int n)
{
    int m = n + 2;
    sort(b.begin(), b.end());

    // output_list(b, 100, 100);

    int cand1 = b[n];
    int cand2 = b[n + 1];

    ll total = calculate_sum(b);

    unordered_map<int, int> seen_elements = {};

    for (int i = 0; i < m; ++i)
    {
        seen_elements[b[i]] = i;
    }

    if (total - cand1 - cand2 == cand1)
    {
        output_list(b, n, n + 1);
        return;
    }
    else
    {
        for (auto &[element, idx] : seen_elements)
        {
            if (total - cand2 - element == cand2)
            {
                output_list(b, idx, n + 1);
                return;
            }
        }
        cout << -1 << endl;
        return;
    }
}

int main()
{
    int t{}, n{};
    unordered_map<int, vector<int>> cases{};
    unordered_map<int, int> n_s{};
    cin >> t;
    for (int c = 0; c < t; c++)
    {
        cin >> n;
        vector<int> nums = {};
        n_s[c] = n;
        for (int j = 0; j < n + 2; j++)
        {
            int x{};
            cin >> x;
            nums.push_back(x);
        }
        cases[c] = nums;
    }

    for (int c = 0; c < t; c++)
    {
        int numbers = n_s[c];
        vector<int> b = cases[c];
        process_case(b, n);
    }
}