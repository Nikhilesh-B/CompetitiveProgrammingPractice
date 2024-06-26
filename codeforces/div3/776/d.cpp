#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <climits>

using namespace std;

int find_idx(int target, vector<int> &nums)
{
    int idx{-1};
    int n = nums.size();
    for (int i = 0; i < n; ++i)
    {
        if (nums[i] == target)
        {
            idx = i + 1;
        }
    }
    return idx;
}

vector<int> rotate_left(int amount, vector<int> &nums)
{
    int n = nums.size();
    int amount_right = n - amount;
    vector<int> new_arr(n, 0);
    for (int i = 0; i < n; ++i)
    {
        int new_pos = (i + amount_right) % n;
        new_arr[new_pos] = nums[i];
    }
    return new_arr;
}

void print_arr(vector<int> &nums)
{
    cout << endl;
    for (int n : nums)
    {
        cout << n << " ";
    }
    cout << endl;
}

void process_case(int n, vector<int> &nums)
{
    vector<int> shifts(n, 0);
    for (int rots = 0; rots < n; rots++)
    {
        int target = n - rots;
        int idx = find_idx(target, nums);
        int shift = idx % target;
        nums = rotate_left(shift, nums);
        nums.pop_back();
        shifts[target - 1] = shift;
    }

    for (auto s : shifts)
    {
        cout << s << " ";
    }
    cout << endl;
}

int main()
{
    int t{};
    cin >> t;

    while (t--)
    {
        int n{}, x{};
        vector<int> nums{};
        cin >> n;
        for (int i = 0; i < n; ++i)
        {
            cin >> x;
            nums.push_back(x);
        }
        process_case(n, nums);
    }
}