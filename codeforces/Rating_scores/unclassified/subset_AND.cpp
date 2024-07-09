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

int main()
{
    int n, k, q;
    cin >> n >> k >> q;

    vector<int> a(n, 0);

    for (int i = 0; i < n; ++i)
        cin >> a[i];

    unordered_map<int, vector<int>> bitstores;

    for (int sft = 0; sft < 30; ++sft)
    {
        vector<int> lastzero(n, -1);
        for (int j = 0; j < n; ++j)
        {
            int aj = a[j];
            if (((aj >> sft) & 1) == 0)
                lastzero[j] = j;
            else if (j != 0)
                lastzero[j] = lastzero[j - 1];
        }
        bitstores[sft] = lastzero;
    }

    for (int i = 0; i < q; ++i)
    {
        int l, r;
        int count = 0;
        cin >> l >> r;
        l--;
        r--;

        for (int sft = 0; sft < 30; ++sft)
        {
            int k_bit = (k >> sft) & 1;
            vector<int> last_zero = bitstores[sft];

            if (k_bit == 0 && last_zero[r] < l)
            {
                cout << "NO" << endl;
                break;
            }
            else if (k_bit == 1 && last_zero[r] >= l)
            {
                cout << "NO" << endl;
                break;
            }
            else
                count += 1;
        }
        if (count == 30)
        {
            cout << "YES" << endl;
        }
    }
}