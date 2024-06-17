#include <iostream>
using namespace std;

int gcd(int x, int y)
{
    if (y == 0)
    {
        return x;
    }
    else
    {
        return gcd(y, x % y);
    }
}

void maximize(int x)
{
    // cout << "Executed";
    int max_val{-1};
    for (int y = 1; y < x; y++)
    {
        max_val = max(max_val, gcd(x, y) + y);
    }
    cout << max_val << endl;
}

int main()
{
    int t{}, x{};
    cin >> t;
    while (t--)
    {
        cin >> x;
        maximize(x);
    }
}
