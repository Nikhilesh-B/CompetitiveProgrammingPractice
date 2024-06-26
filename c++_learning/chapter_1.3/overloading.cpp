#include <iostream>

using namespace std;

void print(int x)
{
    cout << "Your integer is " << x << endl;
}

void print(double x)
{
    cout << "Your double is " << x << endl;
}

void print(string s)
{
    cout << "Your string is " << s << endl;
}

int main()
{
    print(42);
    print(1.345);
    print("Hello world!");
}