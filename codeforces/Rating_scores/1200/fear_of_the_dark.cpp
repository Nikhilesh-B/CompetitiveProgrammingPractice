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

typedef pair<double, double> dpair;

void printVectorNL(const vector<double> &vec)
{
    for (const auto &elem : vec)
    {
        std::cout << fixed << setprecision(20) << elem << std::endl;
    }
}

// double distance(double x0, double y0, double x1, double y1)
// {
//     return sqrt(pow((x1 - x0), 2) + pow((y1 - y0), 2));
// }

double distance(dpair c, dpair d)
{
    double x0 = c.first;
    double y0 = c.second;
    double x1 = d.first;
    double y1 = d.second;
    return sqrt(pow((x1 - x0), 2) + pow((y1 - y0), 2));
}

double solve()
{
    double px, py, ax, ay, bx, by;
    cin >> px >> py >> ax >> ay >> bx >> by;

    dpair o = {0.0, 0.0};
    dpair p = make_pair(px, py);
    dpair a = make_pair(ax, ay);
    dpair b = make_pair(bx, by);

    double OA = distance(o, a);
    double OB = distance(o, b);
    double PA = distance(p, a);
    double PB = distance(p, b);
    double half_AB = distance(a, b) / 2.0;

    if (OA >= OB && PA >= PB)
    {
        return max(OB, PB);
    }
    else if (OA <= OB && PA <= PB)
    {
        return max(OA, PA);
    }
    else
    {
        return max(max(min(OA, OB), min(PA, PB)), half_AB);
    }
}

int main()
{
    int t;
    cin >> t;

    vector<double> answers(t, 0);

    for (int i = 0; i < t; ++i)
    {
        answers[i] = solve();
    }

    printVectorNL(answers);
}