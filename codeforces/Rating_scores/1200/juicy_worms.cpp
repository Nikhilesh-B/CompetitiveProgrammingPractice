#include <iostream>
#include <vector>

using namespace std;

int returnIdx(vector<int> &t, int j)
{
    int lo = 1;
    int hi = t.size() - 1;
    int cand{}, vala{}, valb{};
    while (hi >= lo)
    {
        cand = (hi + lo) / 2;
        valb = t[cand - 1];
        vala = t[cand];
        if (valb < j && j <= vala)
        {
            return cand;
        }
        else if (j <= valb)
        {
            hi = cand - 1;
        }
        else
        {
            lo = cand + 1;
        }
    }
    return -1;
}

int main()
{
    int n{}, m{};
    vector<int> piles;
    vector<int> juicy;
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        int x{};
        cin >> x;
        piles.push_back(x);
    }

    vector<int> totals{0};
    int running_total = 0;
    for (int ps : piles)
    {
        running_total += ps;
        totals.push_back(running_total);
    }

    cin >> m;
    for (int i = 0; i < m; ++i)
    {
        int x{};
        cin >> x;
        juicy.push_back(x);
    }

    for (int j : juicy)
    {
        int idx = returnIdx(totals, j);
        cout << idx << endl;
    }
}
