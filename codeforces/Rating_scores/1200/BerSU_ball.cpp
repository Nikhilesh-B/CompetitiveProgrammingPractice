#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <unordered_map>

using namespace std;

void process_case(vector<int> &sa, vector<int> &ba)
{
    int total_pairs = 0;
    unordered_map<int, int> sa_map;
    unordered_map<int, int> ba_map;

    for (int a : sa)
    {
        if (sa_map.find(a) == sa_map.end())
        {
            sa_map[a] = 1;
        }
        else
        {
            sa_map[a] += 1;
        }
    }

    for (int a : ba)
    {
        if (ba_map.find(a) == ba_map.end())
        {
            ba_map[a] = 1;
        }
        else
        {
            ba_map[a] += 1;
        }
    }

    sort(sa.begin(), sa.end());

    for (int a : sa)
    {
        int count = sa_map[a];
        for (int i = -1; i < 2; ++i)
        {
            int candidate = a + i;
            if (count == 0)
            {
                break;
            }
            if (ba_map.find(candidate) != ba_map.end())
            {
                int count_candidate = ba_map[a + i];
                if (count_candidate > count)
                {
                    total_pairs += count;
                    ba_map[a + i] -= count;
                    count = 0;
                }
                else
                {
                    total_pairs += count_candidate;
                    count -= count_candidate;
                    ba_map[a + i] = 0;
                }
            }
        }
    }
    cout << total_pairs;
}

int main()
{
    int n{}, bi{};
    cin >> n;
    vector<int> boys;
    for (int i = 0; i < n; ++i)
    {
        cin >> bi;
        boys.push_back(bi);
    }

    int m{}, gi{};
    cin >> m;
    vector<int> girls;
    for (int i = 0; i < m; ++i)
    {
        cin >> gi;
        girls.push_back(gi);
    }

    vector<int> small_array;
    vector<int> big_array;

    if (n > m)
    {
        small_array = girls;
        big_array = boys;
    }
    else
    {
        small_array = boys;
        big_array = girls;
    }

    process_case(small_array, big_array);
}
