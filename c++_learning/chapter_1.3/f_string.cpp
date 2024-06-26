#include <iostream>

using namespace std;

double cube(double num)
{
    return num * num * num;
}

double square(double num)
{
    return num*num;    
}

void print_cube_square(double cube, double square)
{
    string result = format("Cube:{}, Square:{}", cube, square);
    cout << result << endl;
}

int main()
{
    double og_num = 1.5;
    double cube = cube(og_num);
    double square = square(og_num)
    print_cube_square(cube, square);
    return 0;
}