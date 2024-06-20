#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <string>
#include <unordered_map>

using namespace std;

long long combinations_2(int n)
{
    long long nl = (long long)n;
    long long result = ((nl - 1) * nl) / 2;
    return result;
}

long long process_case(vector<int> &a)
{
    unordered_map<int, int> difference_count{};

    for (size_t i = 0; i < a.size(); ++i)
    {
        a[i] = a[i] - i;
    }

    for (int ai : a)
    {
        if (difference_count.find(ai) == difference_count.end())
        {
            difference_count[ai] = 1;
        }
        else
        {
            difference_count[ai] += 1;
        }
    }

    long long total{0};

    for (const auto &[dif, amount] : difference_count)
    {
        if (amount > 1)
        {
            total += combinations_2(amount);
        }
    }

    return total;
}

int main()
{
    vector<long long> answers{};
    int t{};

    cin >> t;

    while (t--)
    {
        int n{};
        cin >> n;
        vector<int> nums{};
        while (n--)
        {
            int x{};
            cin >> x;
            nums.push_back(x);
        }
        long long ans = process_case(nums);
        answers.push_back(ans);
    }

    for (long long ans : answers)
    {
        cout << ans << endl;
    }
}