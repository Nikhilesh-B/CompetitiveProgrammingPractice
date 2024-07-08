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
void printSet(const std::set<T> &set)
{
    for (const auto &elem : set)
    {
        std::cout << elem << " ";
    }
    std::cout << std::endl;
}

// O(sqrt(x)) way to find factors;
int main()
{
    // number to find all factors for
    int x = 100;

    set<int> factors;

    for (int k = 1; k <= static_cast<int>(sqrt(x)); k++)
    {
        if (!(x % k))
        {
            factors.insert(k);
            factors.insert(x / k);
        }
    }

    printSet(factors);
}