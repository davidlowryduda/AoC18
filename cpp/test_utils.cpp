#include <iostream>
#include "utils.h"

int main()
{
  std::string content;
  content = read_file("test_input.txt");
  for (auto c : content)
  {
    std::cout << c << "\n";
  }
  std::cout <<  std::endl;
}
