#include <iostream>

using namespace std;

double cube(double num)
{
    return num * num * num;
}

// this worked to give us our cube
void print_cube(double cube)
{
    cout << "Your cube is ";
    cout << cube;
    cout << endl;
}

int main()
{
    double result = cube(1.5);
    print_cube(result);
}