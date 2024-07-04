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
    {
        cin >> a[i];
    }

    vector<int> lft(n, a[0]);
    for (int i = 1; i < n; ++i)
    {
        lft[i] = max(a[i - 1], lft[i - 1]);
    }
    int cr = a[k - 1];
    int less_than_k = 0;

    for (int i = 0; i < n; ++i)
    {
        if (cr > a[i] && cr > lft[i])
            less_than_k += 1;
        else if (cr > a[i] && cr >= lft[i])
            less_than_k += 1;
        else if (cr >= a[i] && cr > lft[i])
            continue;
        else if (cr == a[i] && cr == lft[i])
            continue;
        else
            break;
    }

    return less_than_k;
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