#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <climits>

using namespace std;

vector<int> find_primes_less_than(int x)
{
    int nums[x];
    for (int i = 0; i < x; ++i)
    {
        nums[i] = 0;
    }

    int x_sqrt = sqrt(x);

    for (int n = 2; n < x_sqrt + 1; ++n)
    {
        int j = 2;
        while (j * n <= x)
        {
            nums[j * n - 1] = 1;
            ++j;
        }
    }

    vector<int> primes = {};

    for (int i = 1; i < x; ++i)
    {
        if (nums[i] == 0)
        {
            primes.push_back(i + 1);
        }
    }
    return primes;
}

vector<int> prime_factorization(int x)
{
    vector<int> primes = find_primes_less_than(x);
    vector<int> factorization = {};

    while (x != 1)
    {
        for (int p : primes)
        {
            if (x % p == 0)
            {
                x /= p;
                factorization.push_back(p);
                break;
            }
        }
    }
    sort(factorization.begin(), factorization.end());

    return factorization;
}

int find_product(vector<int> &factiors)
{
    int answer = 1;
    for (int f : factiors)
    {
        answer *= f;
    }
    return answer;
}

vector<int> find_neighbors(vector<int> &factors, vector<int> &ns)
{
    unordered_map<int, int> nums = {};
    vector<int> neighbors = {};
    for (int n : ns)
    {
        if (nums.find(n) != nums.end())
        {
            nums[n] += 1;
        }
        else
        {
            nums[n] = 1;
        }
    }

    for (int f : factors)
    {
        if (nums.find(f) == nums.end())
        {
            neighbors.push_back(f);
        }
        else
        {
            if (nums[f] > 1)
            {
                nums[f] -= 1;
            }
            else
            {
                nums.erase(f);
            }
        }
    }
    return neighbors;
}

int find_closest_val(vector<int> &factors, int mv)
{
    int closest_val = 1;

    deque<vector<int>> our_matrix = {};
    for (int f : factors)
    {
        vector<int> apnd_lst = {f};
        if (f < mv)
        {
            closest_val = max(f, closest_val);
        }
        our_matrix.push_back(apnd_lst);
    }

    while (our_matrix.size() != 0)
    {
        // fmt::print("matrix:", our_matrix);
        vector<int> node = our_matrix.front();
        our_matrix.pop_front();
        vector<int> neighbors = find_neighbors(factors, node);
        int product = find_product(node);
        for (int n : neighbors)
        {
            if (closest_val < product * n && product * n <= mv)
            {
                closest_val = product * n;
            }

            if (product * n < mv)
            {
                vector<int> node_copy = node;
                node_copy.push_back(n);
                vector<int> new_addition = node_copy;
                our_matrix.push_back(new_addition);
            }
        }
    }
    return closest_val;
}

void process_case(int x, int n)
{
    int max_val = x / n;
    vector<int> factorization = prime_factorization(x);
    int closest_val = find_closest_val(factorization, max_val);
    cout << closest_val << endl;
}

int main()
{
    int t{};
    cin >> t;
    int x{}, n{};

    while (t--)
    {
        cin >> x >> n;
        process_case(x, n);
    }
}