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
void printVectorNL(const std::vector<T> &vec)
{
    for (const auto &elem : vec)
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

    sort(a.begin(), a.end());

    if (a[0] < 0)
        return a[0];
    else
        return a[a.size() - 1];
}

int main()
{
    int t;
    cin >> t;

    vector<int> answers(t, 0);

    for (int i = 0; i < t; ++i)
    {
        answers[i] = solve();
    }

    printVectorNL(answers);
}