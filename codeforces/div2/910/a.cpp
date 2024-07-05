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

void solve()
{
    int n, k;
    cin >> n >> k;
    string str;
    cin >> str;

    vector<int> from_left(n, 0);

    int rn_b = 0;
    for (int i = n - 1; i > -1; --i)
    {
        from_left[i] = rn_b;
        if (str[i] == 'B')
            rn_b += 1;
    }

    if (rn_b == k)
    {
        cout << 0 << endl;
        return;
    }

    for (int i = 0; i < n; ++i)
    {
        if (i + 1 + from_left[i] == k)
        {
            cout << "1" << endl;
            cout << i + 1 << " B" << endl;
            return;
        }

        else if (from_left[i] == k)
        {
            cout << "1" << endl;
            cout << i + 1 << " A" << endl;
            return;
        }
    }

    cout << "2" << endl;
    cout << n << " A" << endl;
    cout << k << " B" << endl;
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