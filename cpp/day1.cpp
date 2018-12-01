/*
 * Solve day 1.
 *
 * On the right are notes to myself about cpp, revealing what I do and don't
 * know about the language.
 */

#include "utils.h"

void part1(std::string content)
{
  long long total = 0;
  std::string line;
  std::istringstream input(content);      // streams have convenient line-by
                                          // line readers
  std::string op;
  int num = 0;
  while (std::getline(input, line))
  {
    op = line[0];
    num = std::stoi(line.substr(1));
    if (op == "+")      { total += num; }
    else if (op == "-") { total -= num; }
    else {
      throw std::invalid_argument("Operation not recognized.");
    }
  }
  std::cout << total << std::endl;
}


void part2(std::string content)
{
  int num = 0;
  int * pval;
  long long total = 0;
  std::string line;
  std::string op;
  std::unordered_map<long long, int> seen;
  for (int i = 0; i < 1000; ++i) // Don't cycle input > 1000 times
  {
    std::istringstream input(content);
    while (std::getline(input, line))
    {
      op = line[0];
      num = std::stoi(line.substr(1));
      if (op == "+")      { total += num; }
      else if (op == "-") { total -= num; }
      else {
        throw std::invalid_argument("Operation not recognized.");
      }

      pval = &seen[total];
      if (*pval == 0) { (*pval)++; }
      else if (*pval > 0)
      {
        std::cout << total << std::endl;
        return;
      }
    }
  }
}


int
main()
{
  std::string content;
  content = read_file("inputs/input1.txt");
  part1(content);
  part2(content);
}
