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

int gcd(int x, int y)
{
    if (x == 0)
        return y;
    else
        return gcd(y % x, x);
}

string process_case(int n, int m, int k, vector<vector<int>> &heights)
{
    ll imbalance = 0;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
            imbalance += heights[i][j];
    }

    vector<ll> potential_steps{};

    ll sum = 0;
    for (int i = 0; i < k; ++i)
    {
        for (int j = 0; j < k; ++j)
        {
            sum = 0;
            for (int r = 0; r < k; ++r)
            {
                for (int c = 0; c < k; ++c)
                {
                    sum += heights[r][c];
                }
            }
            potential_steps.push_back(sum);
        }
    }

    for (auto potential_step : potential_steps)
    {
        if (imbalance % potential_step == 0)
        {
            return "YES";
        }
    }
    return "NO";
}
int main()
{
    int t;
    cin >> t;
    vector<string> answers;
    while (t--)
    {
        int n{}, m{}, k{}, x{};
        cin >> n >> m >> k;
        vector<vector<int>> heights(n, vector<int>(m, 0));
        vector<vector<int>> snow(n, vector<int>(m, 0));
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
                cin >> heights[i][j];
        }
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
                cin >> snow[i][j];
        }
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
                if (snow[i][j] == 0)
                    heights[i][j] *= -1;
        }
        answers.push_back(process_case(n, m, k, heights));
    }

    for (string ans : answers)
    {
        cout << ans << endl;
    }
}
