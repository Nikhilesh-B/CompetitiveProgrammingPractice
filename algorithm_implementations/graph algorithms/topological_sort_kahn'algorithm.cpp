// pretty_simple_recursive_implementation;
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
// kahn's algorithm

vector<int> calculate_indegrees(vector<vector<int>> &adj_matrix)
{
    int n = adj_matrix.size();
    int count{};
    vector<int> indegree(n, 0);
    for (int i = 0; i < n; ++i)
    {
        count = 0;
        for (int j = 0; j < n; ++j)
        {
            count += adj_matrix[i][j];
        }
        indegree[i] = count;
    }
    return indegree;
}

vector<int> topological_sort(vector<vector<int>> &adj_matrix)
{
    int n = adj_matrix.size();
    int count = 0;
    vector<int> topsort{};
    vector<int> indegree = calculate_indegrees(adj_matrix);
    deque<int> zero_indegree{};
    for (int i : indegree)
        if (!i)
            zero_indegree.push_back(i);

    while (!zero_indegree.empty() && count < n)
    {
        int u = zero_indegree[0];
        topsort.push_back(u);
        zero_indegree.pop_front();
        count += 1;
        for (int j = 0; j < n; ++j)
        {
            adj_matrix[j][u] -= 1;
            if (!adj_matrix[u][j])
                zero_indegree.push_back(j);
        }
    }
    return topsort;
}

void print_top_sort(vector<int> &top_sort)
{
    cout << "[ ";
    for (int i : top_sort)
    {
        cout << i << "-->";
    }
    cout << "]" << endl;
}

int main()
{
    vector<vector<int>> adj_matrix = {{0, 0, 0},
                                      {1, 0, 0},
                                      {0, 1, 0}};

    vector<int> top_sort = topological_sort(adj_matrix);
    print_top_sort(top_sort);
}
