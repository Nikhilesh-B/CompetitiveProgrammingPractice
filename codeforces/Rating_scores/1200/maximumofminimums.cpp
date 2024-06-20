#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <vector>
#include <unordered_map>
#include <climits> // For INT_MAX and INT_MIN

using namespace std;

int two_case(vector<int> &v, int mn)
{
    int length = v.size();

    vector<int> leftmin = {v[0]};
    deque<int> rightmin = {v[length - 1]};

    int lm = v[0];
    int rm = v[length - 1];

    for (size_t i = 1; i < length; ++i)
    {
        lm = min(lm, v[i]);
        leftmin.push_back(lm);
    }

    for (size_t i = length - 2; i > -1; ++i)
    {
        rm = min(rm, v[i]);
        rightmin.push_front(rm);
    }

    int max_answer = mn;

    for (size_t i = 0; i < length - 1; ++i)
    {
        max_answer = max(max(leftmin[i], rightmin[i]), max_answer);
    }
    return max_answer;
}

int main()
{
    int n{}, k{};
    cin >> n >> k;

    vector<int> values;

    int mn = INT_MAX;
    int mx = INT_MIN;
    

    while (n--)
    {
        int x{};
        cin >> x;
        if (x < mn)
        {
            mn = min(mn, x);
        }
        else if (x > mx)
        {
            mx = max(mx, x);
        }
        values.push_back(x);
    }

    if (k == 1)
    {
        cout << mn << endl;
    }
    else if (k > 2)
    {
        cout << mx << endl;
    }
    else
    {
        cout << two_case(values, mn) << endl;
    }
}
