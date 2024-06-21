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

void process_case(int x, int n)
{
    int max_val = x / n;
    while (true)
    {
        if (x % max_val == 0)
        {
            break;
        }
        else
        {
            max_val--;
        }
    }
    cout << max_val << endl;
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