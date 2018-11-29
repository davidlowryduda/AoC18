#include <iostream>
#include "utils.h"

int main()
{
  std::string content;
  content = read_file("test_input.txt");
  //for (auto c : content)
  //{
  //  std::cout << c << "\n";
  //}
  std::cout << content << std::endl;

  std::cout << "\n\n";

  content = read_day(0);
  std::cout << content << std::endl;
}
