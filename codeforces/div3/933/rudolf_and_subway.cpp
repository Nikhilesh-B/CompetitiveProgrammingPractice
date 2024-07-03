

#include <iostream>
#include <vector>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <queue>
#include <climits>

using namespace std;

// u, v, color
typedef tuple<int, int, int> tint;
typedef pair<int, int> ipair;
// u, #colors, set of colors
typedef tuple<int, int, vector<int>> tuppq;

int process_case(int n, int m, vector<tint> &edges, int b, int e)
{
    auto compare_tuppq = [](const tuppq &a, const tuppq &b)
    { return get<1>(a) > get<1>(b); };

    priority_queue<tuppq, vector<tuppq>, decltype(compare_tuppq)> pq(compare_tuppq);
    map<pair<int, vector<int>>, bool> visited;

    // from node, (to node, color value)
    unordered_map<int, vector<ipair>> edge_map;
    vector<int> min_colors(n, INT_MAX);

    for (const auto &edge : edges)
    {
        int u = get<0>(edge);
        int v = get<1>(edge);
        int c = get<2>(edge);
        edge_map[u].emplace_back(v, c);
        edge_map[v].emplace_back(u, c);
    }

    vector<int> empty_set = {};
    pq.emplace(b, 0, empty_set);
    min_colors[b - 1] = 0;

    while (!pq.empty())
    {
        tuppq top = pq.top();
        pq.pop();

        int u, u_ncol;
        vector<int> existing_colors;
        tie(u, u_ncol, existing_colors) = top;

        sort(existing_colors.begin(), existing_colors.end());
        if (visited[{u, existing_colors}])
            continue;
        visited[{u, existing_colors}] = true;

        vector<ipair> out_edges = edge_map[u];

        for (const auto &oe : out_edges)
        {
            int v = oe.first;
            int ec = oe.second;
            int v_ncol = min_colors[v - 1];

            vector<int> color_copy = existing_colors;
            if (find(existing_colors.begin(), existing_colors.end(), ec) == existing_colors.end() && 1 + u_ncol <= v_ncol)
            {
                min_colors[v - 1] = 1 + u_ncol;
                color_copy.push_back(ec);
                pq.emplace(v, min_colors[v - 1], color_copy);
            }
            else if (find(existing_colors.begin(), existing_colors.end(), ec) != existing_colors.end() && u_ncol <= v_ncol)
            {
                min_colors[v - 1] = u_ncol;
                pq.emplace(v, min_colors[v - 1], color_copy);
            }
        }
    }
    if (min_colors[e - 1] != INT_MAX)
        return min_colors[e - 1];
    return -1;
}

int main()
{
    int t{}, n{}, m{}, b{}, e{};
    cin >> t;
    vector<int> answers{};
    while (t--)
    {
        cin >> n >> m;
        vector<tint> edges{};
        for (int i = 0; i < m; ++i)
        {
            int u, v, c;
            cin >> u >> v >> c;
            edges.emplace_back(u, v, c);
        }
        cin >> b >> e;
        answers.push_back(process_case(n, m, edges, b, e));
    }

    for (const auto &ai : answers)
        cout << ai << endl;
}