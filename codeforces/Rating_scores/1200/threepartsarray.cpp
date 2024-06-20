#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <vector>
#include <unordered_map>
#include <map>
#include <climits>

using namespace std;

int main()
{
    int n{};

    cin >> n;

    vector<int> nums;

    int n1 = n;
    int a_i{};
    while (n1--)
    {
        cin >> a_i;
        nums.push_back(a_i);
    }

    map<int, int, greater<int>> leftsums;
    unordered_map<int, int> rightsums;
    int total{0};

    for (int i = 0; i < n; ++i)
    {
        total += nums[i];
    }

    int leftsum{0};
    leftsums[-1] = 0;

    for (int i = 0; i < n; ++i)
    {
        leftsums[leftsum] = i;
        rightsums[total - leftsum] = i + 1;
        leftsum += nums[i];
    }
    int answer{};

    for (auto const &[sum, idx] : leftsums)
    {
        if ((rightsums.find(sum) != rightsums.end()) && rightsums[sum] > idx)
        {
            answer = sum;
            break;
        }
    }
    cout << answer << endl;
}