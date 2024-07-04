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
    cout << endl;
    for (const auto &elem : vec)
    {
        std::cout << elem << " ";
    }
    std::cout << std::endl;
}

template <typename T>
void printVectorNL(const std::vector<T> &vec)
{
    for (const auto &elem : vec)
    {
        std::cout << elem << std::endl;
    }
}

int solve()
{
    int n, k;
    cin >> n >> k;
    vector<int> a(n, 0);

    for (int i = 0; i < n; ++i)
        cin >> a[i];

    int r = a[k - 1];
    int num_higher = 0;
    vector<int> hi{};

    for (int i = 0; i < n; ++i)
    {
        if (a[i] > r || i == k - 1)
        {
            hi.emplace_back(i);
            num_higher += 1;
        }
    }

    if (num_higher == 1)
    {
        return n - 1;
    }
    else
    {
        return max(max(hi[0] - 1, 0), hi[1] - (hi[0] ? hi[0] : hi[0] + 1));
    }
}

int main()
{
    int t;
    cin >> t;
    vector<int> ans(t, 0);

    for (int i = 0; i < t; ++i)
        ans[i] = solve();

    printVectorNL(ans);
}