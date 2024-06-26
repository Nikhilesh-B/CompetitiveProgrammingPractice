#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <climits>

using namespace std;

int process_case(vector<int> &a, int n, int k)
{
    int moves = 0;
    for (int i = 0; i < n / 2; ++i)
    {
        if ((abs(a[i] - a[n - 1 - i]) % k == 0))
        {
            moves += (abs(a[i] - a[n - 1 - i]) / k);
        }
        else
        {
            return -1;
        }
    }
    return moves;
}

int main()
{
    vector<int> answers{};
    int t{};

    cin >> t;

    int k{}, n{};
    for (int i = 0; i < t; ++i)
    {
        cin >> n >> k;
        vector<int> a;
        for (int j = 0; j < n; ++j)
        {
            int x{};
            cin >> x;
            a.push_back(x);
        }
        answers.push_back(process_case(a, n, k));
    }

    for (int ans : answers)
    {
        cout << ans << endl;
    }
}