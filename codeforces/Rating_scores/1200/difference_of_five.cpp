#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    int n{};
    vector<int> skills{};

    cin >> n;

    while (n--)
    {
        int x{};
        cin >> x;
        skills.push_back(x);
    }

    sort(skills.begin(), skills.end());

    int i = 0;
    int j = 0;
    int max_size = 1;

    while (i < skills.size())
    {
        if (skills[j] - skills[i] <= 5)
        {
            max_size = max(max_size, (j - i + 1));
            j++;
            if (j == skills.size())
            {
                break;
            }
        }
        else
        {
            i++;
            if (j < i)
            {
                j = i;
            }
        }
    }
    cout << max_size << endl;
}