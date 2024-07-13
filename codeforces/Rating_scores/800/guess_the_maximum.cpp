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
void printVectorNL(const std::vector<T> &set)
{
    for (const auto &elem : set)
    {
        std::cout << elem << std::endl;
    }
}

int solve()
{
    int n;
    cin >> n;
    vector<int> a(n, 0);
    for (int i = 0; i < n; ++i)
        cin >> a[i];

    int mn_max = INT_MAX;

    for (int i = 0; i < n - 1; ++i)
        mn_max = min(mn_max, max(a[i], a[i + 1]));

    return mn_max - 1;
}

int main()
{
    int t;
    cin >> t;
    vector<int> answers(t, 0);

    for (int i = 0; i < t; ++i)
        answers[i] = solve();

    printVectorNL(answers);
}