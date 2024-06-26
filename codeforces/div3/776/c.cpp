#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <climits>

using namespace std;

bool customComparator2(const tuple<int, int, int> &a, const tuple<int, int, int> &b)
{
    return get<1>(a) < get<1>(b); // Sort by first element
}

bool customComparator(const pair<int, int> &a, const pair<int, int> &b)
{
    return a.first < b.first; // Sort by first element
}

void process_case(int n, int m, vector<tuple<int, int, int>> pos_weights)
{
    sort(pos_weights.begin(), pos_weights.end(), customComparator2);

    int answer = 0;
    vector<pair<int, int>> positions_idx = {};
    for (int i = 0; i < 2 * n; ++i)
    {
        answer += get<1>(pos_weights[i]);
        pair<int, int> insertpair{};
        insertpair.first = get<0>(pos_weights[i]);
        insertpair.second = get<2>(pos_weights[i]);
        positions_idx.push_back(insertpair);
    }
    sort(positions_idx.begin(), positions_idx.end(), customComparator);
    cout << answer << endl;
    for (int j = 0; j < positions_idx.size() / 2; ++j)
    {
        cout << positions_idx[j].second << " " << positions_idx[2 * n - 1 - j].second << endl;
    }
}

int main()
{
    int t{};
    cin >> t;

    vector<int> answers{};

    while (t--)
    {
        int m{}, n{};
        tuple<int, int, int> pos_weight{};
        vector<tuple<int, int, int>> pos_weights{};
        cin >> n >> m;
        for (int j = 0; j < m; ++j)
        {
            cin >> get<0>(pos_weight) >> get<1>(pos_weight);
            get<2>(pos_weight) = j + 1;
            pos_weights.push_back(pos_weight);
        }
        process_case(n, m, pos_weights);
    }
}