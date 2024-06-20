#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <vector>
#include <unordered_map>
#include <climits> 

using namespace std;

void process_case(int n, int k, int x, vector<int> &lvls)
{
    sort(lvls.begin(), lvls.end());
    vector<int> differences{};
    int dif{};
    for (int i = 0; i < n - 1; ++i)
    {
        dif = lvls[i + 1] - lvls[i];
        if (dif > x)
        {
            differences.push_back(dif);
        }
    }

    sort(differences.begin(), differences.end());

    int len_difs = differences.size();

    double incremental_dif = {};
    int no_dif_avoided = 0;

    for (int j = 0; j < len_difs; ++j)
    {
        incremental_dif = differences[j];
        if (ceil(incremental_dif / (2 * x)) <= k)
        {
            k = k - ceil(incremental_dif / (2 * x));
            no_dif_avoided += 1;
            if (k == 0)
            {
                break;
            }
        }
        else
        {
            break;
        }
    }
    int answer = 1 + len_difs - no_dif_avoided;
    cout << answer << endl;
}

int main()
{
    int n{}, k{}, x{};
    cin >> n >> k >> x;

    vector<int> levels{};

    for (int i = 0; i < n; ++i)
    {
        int lvl{};
        cin >> lvl;
        levels.push_back(lvl);
    }

    process_case(n, k, x, levels);
}