#include <iostream>
#include <vector>
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

void solve()
{
    string a, b;
    cin >> a >> b;
    int la, lb;
    la = a.length();
    lb = b.length();

    int i = 0;
    int j = 0;
    int k = 0;

    int mx_inorder = 0;
    int sq = 0;
    while (j < lb && i < lb)
    {
        while (k < la)
        {
            if (a[k] == b[j])
            {
                sq += 1;
                j++;
            }
            k++;
        }
        mx_inorder = max(mx_inorder, sq);
        sq = 0;
        k = 0;
        i++;
        j = i;
    }
    int rval = lb + (la - mx_inorder);

    cout << rval << endl;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}