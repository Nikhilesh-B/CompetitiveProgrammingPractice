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
typedef pair<int, ll> ipair;
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
    int n, m, h;
    cin >> n >> m >> h;

    vector<vector<int>> t(n, vector<int>(m, 0));

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            cin >> t[i][j];

    vector<ipair> pp(n, {0, 0ll});

    for (int i = 0; i < n; ++i)
    {
        vector<int> problems = t[i];
        sort(problems.begin(), problems.end());
        ll time = 0;
        int solved = 0;
        ll penalty = 0;
        for (auto p : problems)
        {
            if (time + p <= h)
            {
                solved++;
                time += p;
                penalty += time;
            }
            else
                break;
        }
        pp[i] = make_pair(solved, penalty);
    }

    ipair ru_score = pp[0];

    auto sort_ipair = [](ipair p1, ipair p2)
    {
        if (p1.first != p2.first)
            return p1.first > p2.first;
        else
            return p1.second < p2.second;
    };

    sort(pp.begin(), pp.end(), sort_ipair);

    int ridx = -1;

    for (int i = 0; i < n; ++i)
    {
        if (pp[i] == ru_score)
        {
            ridx = i;
            break;
        }
    }

    return ridx + 1;
}

int main()
{
    int t;
    cin >> t;
    vector<int> places(t);
    for (int i = 0; i < t; i++)
        places[i] = solve();
    printVectorNL(places);
}