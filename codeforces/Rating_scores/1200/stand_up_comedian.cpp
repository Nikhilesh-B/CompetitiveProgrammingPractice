#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <deque>
#include <unordered_map>
#include <climits>

using namespace std;

void process_case(int a1, int a2, int a3, int a4)
{
    int bob{a1}, eve{a1};
    int tj = a1;

    int increment{};
    while (bob > -1 && eve > -1)
    {
        if (a2 > 0 || a3 > 0)
        {
            if (a2 > 0 && a3 > 0)
            {
                if (bob > 0 && eve > 0)
                {
                    if (bob < eve)
                    {
                        increment = bob;
                        bob = 0;
                        eve += increment;
                        tj += increment;
                        a2 -= increment;
                    }
                    else
                    {
                        increment = eve;
                        eve = 0;
                        bob += increment;
                        tj += increment;
                        a3 -= increment;
                    }
                }
                else if (bob > 0)
                {
                    increment = bob;
                    bob = 0;
                    eve += increment;
                    tj += increment;
                    a2 -= increment;
                }
                else if (eve > 0)
                {
                    increment = eve;
                    eve = 0;
                    bob += increment;
                    tj += increment;
                    a3 -= increment;
                }
                else
                {
                    tj += 1;
                    eve = -1;
                }
            }
            else if (a2 > 0)
            {
                if (bob > 0)
                {
                    increment = bob;
                    bob = 0;
                    eve += increment;
                    tj += increment;
                    a2 -= increment;
                }
                else
                {
                    tj += 1;
                    bob = -1;
                }
            }
            else
            {
                if (eve > 0)
                {
                    increment = eve;
                    eve = 0;
                    bob += increment;
                    tj += increment;
                    a3 -= increment;
                }
                else
                {
                    tj += 1;
                    eve = -1;
                }
            }
        }
        else
        {
            increment = min(bob, min(eve, a4)) + 1;
            tj += increment;
            bob -= increment;
            eve -= increment;
            a4 -= increment;
        }
    }
}

int main()
{
    int t{};
    int a1{}, a2{}, a3{}, a4{};
    cin >> t;

    while (t--)
    {
        cin >> a1 >> a2 >> a3 >> a4;
        process_case(a1, a2, a3, a4);
    }
}