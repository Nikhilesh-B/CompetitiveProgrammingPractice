#include <iostream>
#include <vector>
#include <iomanip>
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

typedef vector<vector<int>> Matrix;

// Function to print a matrix
void printMatrix(const Matrix &matrix)
{
    for (const auto &row : matrix)
    {
        for (const auto &elem : row)
        {
            cout << elem << " "; // Adjust width for better formatting
        }
        cout << endl;
    }
}

void solve(unordered_set<int> primes)
{
    int n, m;
    cin >> n >> m;

    vector<vector<int>> mat(n, vector<int>(m, 0));

    if (primes.count(n) && primes.count(m))
    {
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
                mat[i][j] = i * m + j + 1;
        }
        vector<int> new_order{n / 2};
        for (int j = 0; j < n / 2; ++j)
        {
            new_order.push_back(j);
            new_order.push_back(n - 1 - j);
        }
        vector<vector<int>> mat_copy(n, vector<int>(m, 0));

        for (int i = 0; i < n; ++i)
        {
            mat_copy[i] = mat[new_order[i]];
        }
        printMatrix(mat_copy);
    }
    else if (primes.count(n))
    {
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
                mat[i][j] = i + j * n + 1;
        }
        printMatrix(mat);
    }
    else if (primes.count(m))
    {
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
                mat[i][j] = i * m + j + 1;
        }
        printMatrix(mat);
    }
    else
    {
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
                mat[i][j] = i + j * n + 1;
        }
        printMatrix(mat);
    }
    cout << endl;
}

int main()
{
    int t;
    cin >> t;

    unordered_set<int> prime_set;
    vector<bool> primes(1000, true);

    for (int i = 2; i < 501; ++i)
    {
        if (primes[i - 1])
        {
            for (int x = 2; x < 1000 / i; x++)
            {
                primes[x * i - 1] = false;
            }
        }
    }
    primes[999] = false;

    for (int i = 0; i < 1000; ++i)
    {
        if (primes[i])
            prime_set.insert(i + 1);
    }
    
    while (t--)
        solve(prime_set);
}