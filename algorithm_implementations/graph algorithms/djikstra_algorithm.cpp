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

typedef pair<int, int> ipair;

bool comparePair(ipair p1, ipair p2)
{
    return p1.second < p2.second;
}

int djikstra(vector<vector<int>> &adj_matrix, int source_node_idx, int target_idx)
{
    int n = adj_matrix.size();

    auto comparePair = [](const ipair &p1, const ipair &p2)
    {
        return p1.second > p2.second;
    };

    priority_queue<ipair, vector<ipair>, decltype(comparePair)> pq{};
    pq.push(make_pair(source_node_idx, 0));

    vector<int> dist(adj_matrix.size(), INT_MAX);
    dist[source_node_idx] = 0;

    while (!pq.empty())
    {
        int u = pq.top().first;
        pq.pop();
        for (int i = 0; i < n; ++i)
        {
            int v = i;
            int weight = adj_matrix[u][v];
            if (dist[v] > dist[u] + weight && weight > 0)
            {
                dist[v] = dist[u] + weight;
                pq.push(make_pair(v, dist[v]));
            }
        }
    }
    if (dist[target_idx] != INT_MAX)
        return dist[target_idx];
    return -1;
}

int main()
{
    vector<vector<int>> adj_matrix = {{0, 3, 10},
                                      {3, 0, 6},
                                      {10, 6, 0}};

    int source_node_idx = 0;
    int target_idx = 2;
    int shortest_path = djikstra(adj_matrix, source_node_idx, target_idx);
    if (shortest_path != -1)
    
        cout << "Shortest path has value " << shortest_path << " between source node idx " << source_node_idx << " and target node idx " << target_idx << endl;
    else
        cout << "No path between node with idx" << target_idx << " and node with idx of " << source_node_idx << endl;
}