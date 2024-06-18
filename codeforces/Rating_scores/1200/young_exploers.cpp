#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

void process_case(vector<int> &es, int n)
{
    int max_groups = 0;
    sort(es.begin(), es.end());

    int i{0}, j{0};

    while (i < n && j < n)
    {
        if (j - i + 1 >= es[j])
        {
            max_groups += 1;
            i = j;
            i++;
            j++;
        }
        else
        {
            j++;
        }
    }
    cout << max_groups << endl;
}

int main()
{
    int t{};
    cin >> t;
    unordered_map<int, vector<int>> cases;
    unordered_map<int, int> n_s;

    for (int i = 0; i < t; i++)
    {
        vector<int> nums{};
        int n{}, x{};
        cin >> n;
        n_s[i] = n;
        for (int j = 0; j < n; j++)
        {
            cin >> x;
            nums.push_back(x);
        }
        cases[i] = nums;
    }
    for (int i = 0; i < t; i++)
    {
        process_case(cases[i], n_s[i]);
    }
}