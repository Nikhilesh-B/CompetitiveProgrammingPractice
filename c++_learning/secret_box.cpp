#include <iostream>
#include <vector>
#include <tuple>
using namespace std;

typedef long long ll;

int main()
{
    int t{};
    vector<vector<ll,ll,ll,ll>> problem_specs{};
    cin >> t;

    int x{};
    while (t--)
    {
        cin >> x;
        problem_specs.push_back(x);
    }
}
