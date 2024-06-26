#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <climits>

using namespace std;

void print_matrix(const vector<vector<int>> &matrix)
{
    for (const auto &row : matrix)
    {
        for (int val : row)
        {
            cout << val << " ";
        }
        cout << endl;
    }
}

vector<int> return_neighbors(int r, int c, int rows, int cols, const std::vector<std::vector<int>> &matrix)
{
    vector<int> neigh_vals{};
    vector<pair<int, int>> possible_neighs = {{r - 1, c}, {r + 1, c}, {r, c - 1}, {r, c + 1}};

    for (const auto &neigh : possible_neighs)
    {
        int nr = neigh.first;
        int nc = neigh.second;
        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols)
        {
            neigh_vals.push_back(matrix[nr][nc]);
        }
    }

    return neigh_vals;
}

bool greater_than_all(int val, vector<int> other_vals)
{
    for (int ovs : other_vals)
    {
        if (val <= ovs)
        {
            return false;
        }
    }
    return true;
}

void make_modification(vector<vector<int>> &matrix)
{
    int rows = matrix.size();
    int cols = matrix[0].size();
    bool flag = true;
    for (int r = 0; r < rows; ++r)
    {
        for (int c = 0; c < cols; ++c)
        {
            vector<int> rn = return_neighbors(r, c, rows, cols, matrix);
            sort(rn.begin(), rn.end());
            if (greater_than_all(matrix[r][c], rn))
            {
                matrix[r][c] = rn[rn.size() - 1];
            }
        }
    }
}

void take_intput(vector<vector<int>> &matrix)
{
    int rows = matrix.size();
    int cols = matrix[0].size();
    for (int r = 0; r < rows; ++r)
    {
        for (int c = 0; c < cols; ++c)
        {
            cin >> matrix[r][c];
        }
    }
}

int main()
{
    int t{};

    cin >> t;

    int n{}, m{};
    for (int j = 0; j < t; ++j)
    {
        cin >> n >> m;
        vector<vector<int>> matrix(n, vector<int>(m));
        take_intput(matrix);
        make_modification(matrix);
        print_matrix(matrix);
    }
}