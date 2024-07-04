#include <iostream>
#include <vector>
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
    double n, d, h;
    cin >> n >> d >> h;

    vector<double> y(n);
    for (int i = 0; i < n; i++)
        cin >> y[i];
    sort(y.begin(), y.end());
    double tr_area = 1 / 2 * d * h;
    double to_area = n * tr_area;
    double overlap = 0.0;

    for (int i = 1; i < n; i++)
    {
        int y1{y[i]}, y2{y[i + 1]};
        if (y2 - y1 < h)
        {
            double overlap_height = h - (y2 - y1);
            double overlap_area = d / 2 * h * pow(overlap_height, 2);
            to_area -= overlap_area;
        }
    }
    cout << to_area << endl;
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
