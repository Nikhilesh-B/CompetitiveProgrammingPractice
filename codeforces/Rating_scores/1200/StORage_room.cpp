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

typedef long long ll;

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
    vector<vector<ll>> M(n, vector<ll>(n, 0ll));

    ll value = (1LL << 30) - 1;
    vector<ll> a(n, value);

    // first pass setting all relevant to zero;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            cin >> M[i][j];
            if (i != j)
            {
                a[i] &= M[i][j];
                a[j] &= M[i][j];
            }
        }
    }

    cout << endl;
    printVector(a);

    for (int i = 0; i < n; ++i)
    {
        for (int j = i + 1; j < n; ++j)
        {
            ll check = M[i][j];
            ll a_i = a[i];
            ll a_j = a[j];
            int bitcount = sizeof(check) * 8;
            while (bitcount--)
            {
                bool firstbit = check & 1;
                bool firstbit_i = a_i & 1;
                bool firstbit_j = a_j & 1;
                if (firstbit && !(firstbit_i || firstbit_j))
                {
                    cout << "NO" << endl;
                    return;
                }
                check >>= 1;
                a_i >>= 1;
                a_j >>= 1;
            }
        }
    }

    cout << "YES" << endl;
    printVector(a);
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}