#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

string process_case(vector<int> &nums, int x)
{
    int n = nums.size();
    int odd_count{0}, even_count{0};
    for (int j : nums)
    {
        if (j % 2 == 0)
        {
            even_count += 1;
        }
        else
        {
            odd_count += 1;
        }
    }
    bool cond1 = odd_count >= 1;
    bool cond3 = (x % 2 == 0 && even_count > 0) || x % 2 == 1;

    odd_count--;

    int max_even_no_odds = odd_count;
    if (odd_count % 2 == 1)
    {
        max_even_no_odds--;
    }

    bool cond2 = (even_count >= x - 1 - (max_even_no_odds));

    if (cond1 && cond2 && cond3)
    {
        return "YES";
    }

    else
    {
        return "NO";
    }
}

int main()
{
    int t{};
    cin >> t;
    vector<string> answers{};

    while (t--)
    {
        int n{};
        int x{};
        cin >> n;
        cin >> x;
        vector<int> nums{};
        while (n--)
        {
            int y{};
            cin >> y;
            nums.push_back(y);
        }
        answers.push_back(process_case(nums, x));
    }

    for (string ans : answers)
    {
        cout << ans << endl;
    }
}