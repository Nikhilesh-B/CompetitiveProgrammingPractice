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

typedef pair<int, int> ipair;

void printVectorNL(const std::vector<ipair> &vec)
{
    for (const auto &elem : vec)
    {
        std::cout << elem.first << " " << elem.second << std::endl;
    }
}

ipair solve()
{
    int n;
    cin >> n;
    vector<int> a(n, 0);
    for (int i = 0; i < n; ++i)
        cin >> a[i];

    int pos1, pos2, posN;

    for (int i = 0; i < n; ++i)
    {
        int v = a[i];
        if (v == 1)
            pos1 = i;
        else if (v == 2)
            pos2 = i;
        else if (v == n)
            posN = i;
    }

    ipair swap;

    if ((pos1 < posN && posN < pos2) || (pos2 < posN && posN < pos1))
        swap = make_pair(1, 1);
    else if ((pos1 < pos2 && pos2 < posN) || (posN < pos2 && pos2 < pos1))
        swap = make_pair(pos2 + 1, posN + 1);
    else if ((pos2 < pos1 && pos1 < posN) || (posN < pos1 && pos1 < pos2))
        swap = make_pair(pos1 + 1, posN + 1);
    return swap;
}

int main()
{
    int t;
    cin >> t;
    vector<ipair> ans(t, {0, 0});

    for (int i = 0; i < t; ++i)
        ans[i] = solve();

    printVectorNL(ans);
}