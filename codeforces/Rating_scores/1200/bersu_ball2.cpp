#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <unordered_map>

using namespace std;

void process_case(vector<int> &b, vector<int> &g)
{
    int bl = b.size();
    int gl = g.size();
    int i = 0;
    int j = 0;
    int total_couples = 0;

    while (i < bl && j < gl)
    {
        if (abs(b[i] - g[j]) <= 1)
        {
            total_couples += 1;
            i++;
            j++;
        }
        else if (b[i] > g[j])
        {
            j++;
        }
        else
        {
            i++;
        }
    }
    cout << total_couples;
}

int main()
{
    int n{}, bi{};
    cin >> n;
    vector<int> boys;
    for (int i = 0; i < n; ++i)
    {
        cin >> bi;
        boys.push_back(bi);
    }

    int m{}, gi{};
    cin >> m;
    vector<int> girls;
    for (int i = 0; i < m; ++i)
    {
        cin >> gi;
        girls.push_back(gi);
    }

    sort(boys.begin(), boys.end());
    sort(girls.begin(), girls.end());

    process_case(boys, girls);
}