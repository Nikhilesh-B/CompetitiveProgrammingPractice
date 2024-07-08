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

// small, big
// depends on where we are placing the modulo in the code;
int find_gcd(int x, int y)
{
    if (y == 0)
        return x;
    else
        return find_gcd(y, x % y);
}

int main()
{
    int x, y;
    // numbers to find gcd of
    x = 3;
    y = 17;

    cout << find_gcd(x, y);
}