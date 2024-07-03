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

// u, v, color
typedef tuple<int, int, int> tint;

typedef pair<int, int> ipair;

// u, #colors, set of colors.
typedef tuple<int, int, unordered_set<int>> tuppq;

int process_case(int n, int m, vector<tint> &edges, int b, int e)
{
    auto compare_tuppq = [](const tuppq &a, const tuppq &b)
    { return get<1>(a) > get<1>(b); };

    priority_queue<tuppq, vector<tuppq>, decltype(compare_tuppq)> pq;
    map<tint, int> visited;

    // from node, (to node, color value)
    unordered_map<int, vector<ipair>> edge_map;
    vector<int> min_colors(n, INT_MAX);

    for (tint edge : edges)
    {
        int u = get<0>(edge);
        int v = get<1>(edge);
        int c = get<2>(edge);
        edge_map[u].emplace_back(v, c);
        edge_map[v].emplace_back(u, c);
    }

    unordered_set<int> empty_set = {};
    pq.push(make_tuple(b, 0, empty_set));
    min_colors[b - 1] = 0;

    while (!pq.empty())
    {
        tuppq top = pq.top();

        int u, u_ncol;
        unordered_set<int> existing_colors;

        tie(u, u_ncol, existing_colors) = top;
        pq.pop();

        vector<ipair> out_edges = edge_map[u];

        for (auto oe : out_edges)
        {
            int v = oe.first;
            int ec = oe.second;
            tint tint_edge = make_tuple(u, v, ec);
            int v_ncol = min_colors[v - 1];

            if (visited.find(tint_edge) == visited.end())
                visited[tint_edge] = 1;
            else if (visited[tint_edge] == 1)
                visited[tint_edge] += 1;
            else
                continue;

            unordered_set<int> color_copy = existing_colors;
            if (existing_colors.find(ec) == existing_colors.end() && 1 + u_ncol <= v_ncol)
            {
                min_colors[v - 1] = 1 + u_ncol;
                color_copy.insert(ec);
                pq.emplace(v, min_colors[v - 1], color_copy);
            }

            else if (existing_colors.find(ec) != existing_colors.end() && u_ncol <= v_ncol)
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
        tint edge{};
        for (int i = 0; i < m; ++i)
        {
            cin >> get<0>(edge);
            cin >> get<1>(edge);
            cin >> get<2>(edge);
            edges.push_back(edge);
        }
        cin >> b >> e;
        answers.push_back(process_case(n, m, edges, b, e));
    }

    for (auto ai : answers)
        cout << ai << endl;
}