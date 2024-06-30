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

int process_case(int n, int m, int k, vector<int> &b, vector<int> &c)
{
    int total_combs = 0;
    for (int bf : b)
    {
        for (int cf : c)
        {
            if (bf + cf <= k)
                total_combs += 1;
        }
    }
    return total_combs;
}

int main()
{
    int t{};
    cin >> t;
    vector<int> answers{};
    while (t--)
    {
        int n{}, m{}, k{}, x{};
        cin >> n >> m >> k;
        vector<int> b{};
        vector<int> c{};
        for (int i = 0; i < n; ++i)
        {
            cin >> x;
            b.push_back(x);
        }
        for (int i = 0; i < m; ++i)
        {
            cin >> x;
            c.push_back(x);
        }

        answers.push_back(process_case(n, m, k, b, c));
    }

    for (int a : answers)
    {
        cout << a << endl;
    }
}