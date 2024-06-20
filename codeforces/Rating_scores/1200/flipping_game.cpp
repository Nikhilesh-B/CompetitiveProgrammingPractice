#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int count_ones(vector<int> &a, int i, int j)
{
    int ones = 0;
    for (int idx = i; idx < j + 1; idx++)
    {
        if (a[idx] == 1)
        {
            ones += 1;
        }
    }
    return ones;
}

int count_zeros(vector<int> &a, int i, int j)
{
    int zs = 0;
    for (int idx = i; idx < j + 1; idx++)
    {
        if (a[idx] == 0)
        {
            zs += 1;
        }
    }
    return zs;
}

int main()
{
    int n{};
    vector<int> nums{};

    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        int x{};
        cin >> x;
        nums.push_back(x);
    }

    int og_ones = count_ones(nums, 0, nums.size() - 1);
    int max_delta = -1;

    int ones{}, zeros{};
    for (int i = 0; i < n; ++i)
    {
        for (int j = i; j < n; ++j)
        {
            ones = count_ones(nums, i, j);
            zeros = count_zeros(nums, i, j);
            max_delta = max(max_delta, zeros - ones);
        }
    }
    cout << og_ones + max_delta << endl;
}
