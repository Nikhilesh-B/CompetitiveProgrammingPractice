#include <iostream>
#include <vector>
#include <iomanip>
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

template <typename T>
void printVector(const std::vector<T> &vec)
{
    for (const auto &elem : vec)
    {
        std::cout << elem << " ";
    }
    std::cout << std::endl;
}

void solve()
{
    int n;
    cin >> n;
    vector<int> nums(n, 0);

    for (int i = 0; i < n; ++i)
        nums[i] = i + 1;

    printVector(nums);
}

int main()
{
    int t;
    cin >> t;

    while (t--)
        solve();
}