#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <set>
#include <climits>

using namespace std;

void process_case(int n, vector<int> &arr)
{
    vector<int> MEX_LEFT = vector<int>(n, 0);
    vector<int> MEX_RIGHT = vector<int>(n, 0);

    set<int> left_not_seen = {};
    set<int> right_not_seen = {};

    for (int i = 0; i < n + 1; i++)
    {
        left_not_seen.insert(i);
        right_not_seen.insert(i);
    }

    for (int i = 0; i < n; i++)
    {
        left_not_seen.erase(arr[i]);
        MEX_LEFT[i] = *left_not_seen.begin();
    }

    for (int i = n - 1; i > -1; --i)
    {
        right_not_seen.erase(arr[i]);
        MEX_RIGHT[i] = *right_not_seen.begin();
    }
    for (int j = 1; j < n; ++j)
    {
        if (MEX_LEFT[j - 1] == MEX_RIGHT[j])
        {
            cout << 2 << endl;
            cout << 1 << " " << j << endl;
            cout << j + 1 << " " << n << endl;
            return;
        }
    }
    cout << -1 << endl;
};

int main()
{
    int t{};
    cin >> t;

    int n{}, x{};
    while (t--)
    {
        vector<int> arr{};
        cin >> n;
        for (int i = 0; i < n; i++)
        {
            cin >> x;
            arr.push_back(x);
        }
        process_case(n, arr);
    }
}
