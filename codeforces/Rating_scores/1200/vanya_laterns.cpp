#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip> // For fixed and setprecision

using namespace std;

void process_case(vector<int> &lp)
{
    double dist{};
    double min_radius = -1;
    for (size_t i = 0; i < lp.size() - 1; ++i) // Use size_t for the loop counter
    {
        if (i == 0 || i == lp.size() - 2)
        {
            dist = (double)(lp[i + 1] - lp[i]);
        }
        else
        {
            dist = (lp[i + 1] - lp[i]) / 2.0;
        }
        min_radius = max(min_radius, dist);
    }
    cout << fixed << setprecision(10) << min_radius;
}

int main()
{
    int n{};
    int l{}, a{};

    cin >> n;
    cin >> l;
    vector<int> lamposts{0};
    for (int i = 0; i < n; ++i)
    {
        cin >> a;
        lamposts.push_back(a);
    }
    lamposts.push_back(l);
    sort(lamposts.begin(), lamposts.end());
    process_case(lamposts);
}