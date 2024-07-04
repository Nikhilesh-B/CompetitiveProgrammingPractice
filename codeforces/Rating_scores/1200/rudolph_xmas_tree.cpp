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

double solve()
{
    double n, d, h;
    cin >> n >> d >> h;

    vector<double> y(n);
    for (int i = 0; i < n; i++)
    {
        cin >> y[i];
    }

    double tr_area = 0.5 * d * h;
    double to_area = n * tr_area;

    for (int i = 0; i < n - 1; i++)
    { 
        double y1 = y[i];
        double y2 = y[i + 1];
        if (y2 - y1 < h)
        {
            double overlap_height = h - (y2 - y1);
            double overlap_area = (d / (2 * h)) * pow(overlap_height, 2);
            to_area -= overlap_area;
        }
    }

    return to_area;
}

int main()
{
    ios::sync_with_stdio(false); // Synchronize C and C++ standard streams
    cin.tie(nullptr);            // Untie cin from cout for performance (optional)

    int t;
    cin >> t;

    vector<double> results(t); // Vector to store the results of each test case

    for (int i = 0; i < t; i++)
    {
        results[i] = solve();
    }

    // Print all results after taking in all inputs
    for (const auto &result : results)
    {
        cout << fixed << setprecision(7) << result << endl;
    }

    return 0;
}