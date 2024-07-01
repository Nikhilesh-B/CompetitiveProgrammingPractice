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

int process_case(int n, vector<int> &h)
{
    vector<int> seconds(n, -1);

    for (int i = h.size() - 1; i > -1; --i)
    {
        if (i == h.size() - 1)
        {
            seconds[i] = h[i];
        }
        else
        {
            if (h[i + 1] < h[i])
            {
                int time_to_level = h[i] - h[i + 1];
                int wait_time = seconds[i + 1] - h[i + 1];
                if (time_to_level > wait_time)
                {
                    seconds[i] = h[i];
                }
                else
                    seconds[i] = seconds[i + 1] + 1;
            }
            else
                seconds[i] = seconds[i + 1] + 1;
        }
    }
    int mx = -1;
    for (auto s : seconds)
        mx = max(s, mx);
    return mx;
}

int main()
{
    int t{}, n{}, x;
    cin >> t;

    vector<int> answers{};

    while (t--)
    {
        vector<int> h{};
        cin >> n;
        for (int i = 0; i < n; ++i)
        {
            cin >> x;
            h.push_back(x);
        }
        answers.push_back(process_case(n, h));
    }

    for (auto ans : answers)
    {
        cout << ans << endl;
    }
}