#include <iostream>

using namespace std;

void process_case(int n, int m, int a, int b)
{
    double p_pt_multi{};
    int price{0};
    p_pt_multi = (double)b / m;

    if (p_pt_multi < a)
    {
        price += n / m * b;
        int leftover = n % m;
        if (b < leftover * a)
        {
            price += b;
        }
        else
        {
            price += leftover * a;
        }
    }
    else
    {
        price = n * a;
    }
    cout << price;
}

int main()
{
    int n{}, m{}, a{}, b{};
    cin >> n >> m >> a >> b;
    process_case(n, m, a, b);
}
