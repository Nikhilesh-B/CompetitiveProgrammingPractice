#include <iostream>
#include <vector>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <climits>
#include <algorithm>

using namespace std;

// u, v, color
typedef tuple<int, int, int> tint;
typedef pair<int, int> ipair;
// u, #colors, set of colors
typedef tuple<int, int, vector<int>> tuppq;

//v, number of colors, latest color 
typedef tuple<int, int, int> tuppq;


// Custom hash function for tuppq
struct tuppq_hash {
    size_t operator()(const tuppq &t) const {
        size_t seed = 0;
        hash<int> hasher;
        seed ^= hasher(get<0>(t)) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
        seed ^= hasher(get<1>(t)) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
        for (int color : get<2>(t)) {
            seed ^= hasher(color) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
        }
        return seed;
    }
};

// Custom equality function for tuppq
struct tuppq_equal {
    bool operator()(const tuppq &a, const tuppq &b) const {
        return get<0>(a) == get<0>(b) && get<1>(a) == get<1>(b) && get<2>(a) == get<2>(b);
    }
};

int process_case(int n, int m, vector<tint> &edges, int b, int e) {
    auto compare_tuppq = [](const tuppq &a, const tuppq &b) {
        return get<1>(a) > get<1>(b);
    };

    priority_queue<tuppq, vector<tuppq>, decltype(compare_tuppq)> pq(compare_tuppq);
    unordered_set<tuppq, tuppq_hash, tuppq_equal> visited;

    // from node, (to node, color value)
    unordered_map<int, vector<ipair>> edge_map;
    vector<int> min_colors(n, INT_MAX);

    for (const auto &edge : edges) {
        int u = get<0>(edge);
        int v = get<1>(edge);
        int c = get<2>(edge);
        edge_map[u].emplace_back(v, c);
        edge_map[v].emplace_back(u, c);
    }

    vector<int> empty_set;
    pq.emplace(b, 0, empty_set);
    min_colors[b - 1] = 0;


    while (!pq.empty()) {
        auto [u, u_ncol, existing_colors] = pq.top();
        pq.pop();

        if (visited.count(make_tuple(u, u_ncol, existing_colors)))
            continue;
        visited.emplace(u, u_ncol, existing_colors);

        vector<ipair> out_edges = edge_map[u];

        for (const auto &oe : out_edges) {
            int v = oe.first;
            int ec = oe.second;
            int v_ncol = min_colors[v - 1];

            vector<int> color_copy = existing_colors;
            auto it = lower_bound(color_copy.begin(), color_copy.end(), ec);
            if (it == color_copy.end() || *it != ec) {
                color_copy.insert(it, ec);
            }

            if (find(existing_colors.begin(), existing_colors.end(), ec) == existing_colors.end() && 1 + u_ncol <= v_ncol) {
                min_colors[v - 1] = 1 + u_ncol;
                pq.emplace(v, min_colors[v - 1], color_copy);
            } else if (find(existing_colors.begin(), existing_colors.end(), ec) != existing_colors.end() && u_ncol <= v_ncol) {
                min_colors[v - 1] = u_ncol;
                pq.emplace(v, min_colors[v - 1], color_copy);
            }
        }
    }

    return min_colors[e - 1] != INT_MAX ? min_colors[e - 1] : -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t, n, m, b, e;
    cin >> t;
    vector<int> answers;
    while (t--) {
        cin >> n >> m;
        vector<tint> edges;
        for (int i = 0; i < m; ++i) {
            int u, v, c;
            cin >> u >> v >> c;
            edges.emplace_back(u, v, c);
        }
        cin >> b >> e;
        answers.push_back(process_case(n, m, edges, b, e));
    }

    for (const auto &ai : answers)
        cout << ai << endl;

    return 0;
}