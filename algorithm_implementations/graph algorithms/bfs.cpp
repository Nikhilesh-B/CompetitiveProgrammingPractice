// BFS implementation to find a specific node
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <climits>

using namespace std;

vector<int> dfs_find_neighbors(vector<vector<int>> &adj_matrix, int node_idx)
{
    vector<int> neighbors = {};
    int node_size = adj_matrix.size();

    for (int i = 0; i < node_size; ++i)
    {
        if (adj_matrix[node_idx][i] == 1 && i != node_idx)
        {
            neighbors.push_back(i);
        }
    }
    return neighbors;
}

int dfs_find_values(vector<vector<int>> &adj_matrix, unordered_map<int, int> &values, int source_node_idx, int target)
{
    deque<int> fifo_quque = {source_node_idx};
    unordered_set<int> explored = {};

    while (fifo_quque.size())
    {
        int expand_node_idx = fifo_quque[0];
        fifo_quque.pop_front();
        vector<int> neighbors = dfs_find_neighbors(adj_matrix, expand_node_idx);
        explored.insert(expand_node_idx);
        for (int n : neighbors)
        {
            if (values[n] == target)
                return n;
            if (explored.find(n) == explored.end())
                fifo_quque.push_back(n);
        }
    }
    return -1;
}

int main()
{
    int n = 3;
    vector<vector<int>> adj_matrix = {{1, 1, 1},
                                      {1, 1, 1},
                                      {1, 1, 1}};
    unordered_map<int, int> values = {{0, 10}, {1, 9}, {2, 3}};
    int target = 3;
    int source_node_idx = 0;
    int index_of_value = dfs_find_values(adj_matrix, values, source_node_idx, target);
    if (index_of_value != -1)
        cout << "Target value of " << target << " found at index " << index_of_value << " from source node with index " << source_node_idx << " and value of " << values[source_node_idx] << endl;
    else
        cout << "Target value of " << target << " not reachable from source node with index " << source_node_idx << " and value of " << values[source_node_idx] << endl;
}
