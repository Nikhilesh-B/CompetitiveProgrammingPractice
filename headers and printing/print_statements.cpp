#include <iostream>
#include <vector>
#include <set>

// Template function to print a vector of any type
template <typename T>
void printVector(const std::vector<T> &vec)
{
    for (const auto &elem : vec)
    {
        std::cout << elem << " ";
    }
    std::cout << std::endl;
}

template <typename T>
void printVectorNL(const std::vector<T> &set)
{
    for (const auto &elem : set)
    {
        std::cout << elem << std::endl;
    }
}

template <typename T>
void printSet(const std::set<T> &set)
{
    for (const auto &elem : set)
    {
        std::cout << elem << " ";
    }
    std::cout << std::endl;
}

template <typename T>
void printSetNL(const std::set<T> &set)
{
    for (const auto &elem : set)
    {
        std::cout << elem << std::endl;
    }
}

int main()
{
    // Example usage

    // Vector of integers
    std::vector<int> intVec = {1, 2, 3, 4, 5};
    std::cout << "Integer Vector: ";
    printVector(intVec);

    // Vector of doubles
    std::vector<double> doubleVec = {1.1, 2.2, 3.3, 4.4, 5.5};
    std::cout << "Double Vector: ";
    printVector(doubleVec);

    // Vector of strings
    std::vector<std::string> stringVec = {"Hello", "world", "this", "is", "a", "test"};
    std::cout << "String Vector: ";
    printVector(stringVec);

    return 0;
}