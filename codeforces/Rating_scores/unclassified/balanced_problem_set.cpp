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
    int x, n;

    cin >> x >> n;

    int gcd_mx = 1;

    // O(sqrt(n)) algorithm for finding all the square roots
    for (int k = 1; k <= static_cast<int>(sqrt(x)); k++)
    {
        if (x % k == 0)
        {
            int fact1 = k;
            int fact2 = x / k;
            if (x / fact1 >= n)
                gcd_mx = max(gcd_mx, fact1);
            if (x / fact2 >= n)
                gcd_mx = max(gcd_mx, fact2);
        }
    }

    return gcd_mx;
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