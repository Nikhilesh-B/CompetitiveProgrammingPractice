#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <string>
#include <unordered_map>

using namespace std;

int relevant_length(vector<int> &sorted, int idx)
{
    int lo = 0;
    int hi = sorted.size() - 1;
    int length = sorted.size();

    int import_position{};
    while (hi >= lo)
    {
        int cand = (hi + lo) / 2;
        if (cand == 0)
        {
            return length;
        }
        if (sorted[cand - 1] < idx && idx <= sorted[cand])
        {
            import_position = cand;
            break;
        }
        else if (idx <= sorted[cand - 1])
        {
            hi = cand - 1;
        }

        else
        {
            lo = cand + 1;
        }
    }
    return length - import_position;
}

int process_case(vector<int> &a)
{
    int length = a.size();
    int fnum = a[0];
    int total_matches = 0;

    unordered_map<int, vector<int>> differences{};

    int dif{};
    for (int i = 1; i < length; ++i)
    {
        dif = (a[i] - fnum) - i;
        if (differences.find(dif) == differences.end())
        {
            vector<int> idxs = {i};
            differences[dif] = idxs;
        }
        else
        {
            differences[dif].push_back(i);
        }
        if (dif == i)
        {
            total_matches += 1;
        }
    }

    for (int i = 1; i < length; ++i)
    {
        int dif_fnum = a[i] - fnum;
        int dif_idx = i;
        int desired_dif = dif_fnum - dif_idx;
        vector<int> relevant_difs = differences[desired_dif];
        total_matches += (relevant_length(relevant_difs, i));
    }

    return total_matches;
}

int main()
{
    vector<int> answers{};
    int t{};

    cin >> t;

    while (t--)
    {
        int n{};
        cin >> n;
        vector<int> nums{};
        while (n--)
        {
            int x{};
            cin >> x;
            nums.push_back(x);
        }
        int ans = process_case(nums);
        answers.push_back(ans);
    }

    for (int ans : answers)
    {
        cout << ans << endl;
    }
}
