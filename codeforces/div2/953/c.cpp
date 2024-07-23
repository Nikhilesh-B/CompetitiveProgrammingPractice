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
    ll n, k;
    cin >> n >> k;

    vector<ll> a(n, 0);

    if (k % 2)
    {
        cout << "NO" << endl;
        return;
    }

    if (n % 2 == 0)
    {
        if (k > ((n - 1) * n / 2))
        {
            cout << "NO" << endl;
            return;
        }
        else
        {
            for (int i = 1; i < n + 1; ++i)
            {
                a[i - 1] = i;
            }

            ll current = 0;

            while (k > 0)
            {
                ll val = n - current * 2 - 1;
                ll idx = n / 2;

                if (k == 2 && 2 * val != 2)
                {
                    ll tmp = a[idx];
                    a[idx] = a[idx - 1];
                    a[idx - 1] = tmp;
                }
                else if (k == 4 && 2 * val != 4)
                {
                    ll tmp1 = a[idx];
                    ll tmp2 = a[idx + 1];
                    a[idx] = a[idx - 1];
                    a[idx - 1] = tmp1;
                    a[idx + 1] = a[idx + 2];
                    a[idx + 2] = tmp2;
                }
                else if (2 * val <= k)
                {
                    ll tmp = a[current];
                    a[current] = a[n - current - 1];
                    a[n - current - 1] = tmp;
                    k -= 2 * val;
                }
                current += 1;
            }
            cout << "YES" << endl;
            printVector(a);
            ll dif = 0;
            vector<ll> a_cp(n, 0);
            for (int i = 1; i < n + 1; ++i)
            {
                a_cp[i - 1] = i;
            }

            for (int i = 0; i < n; ++i)
            {
                dif += abs(a[i] - a_cp[i]);
            }
            cout << "DIFFERENCE IS " << dif << endl;
        }
    }

    else
    {
        if (k > ((n - 1) * (n + 1) / 2))
        {
            cout << "NO" << endl;
            return;
        }
        else
        {
            for (int i = 1; i < n + 1; ++i)
            {
                a[i - 1] = i;
            }

            ll current = 0;

            while (k > 0)
            {
                ll val = n - current * 2 - 1;
                ll idx = n / 2;

                if (k == 2 && 2 * val != 2)
                {
                    ll tmp = a[idx];
                    a[idx] = a[idx - 1];
                    a[idx - 1] = tmp;
                }
                else if (k == 4 && 2 * val != 4)
                {
                    ll tmp1 = a[idx];
                    ll tmp2 = a[idx + 1];
                    a[idx] = a[idx - 1];
                    a[idx - 1] = tmp1;
                    a[idx + 1] = a[idx + 2];
                    a[idx + 2] = tmp2;
                }
                else if (2 * val <= k)
                {
                    ll tmp = a[current];
                    a[current] = a[n - current - 1];
                    a[n - current - 1] = tmp;
                    k -= 2 * val;
                }
                current += 1;
            }
            cout << "YES" << endl;
            printVector(a);
            ll dif = 0;
            vector<ll> a_cp(n, 0);
            for (int i = 1; i < n + 1; ++i)
            {
                a_cp[i - 1] = i;
            }

            for (int i = 0; i < n; ++i)
            {
                dif += abs(a[i] - a_cp[i]);
            }
            cout << "DIFFERENCE IS " << dif << endl;
        }
    }
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