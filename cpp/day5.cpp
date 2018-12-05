/*
 * Solve day 5.
 *
 * On the right are notes to myself about cpp, revealing what I do and don't
 * know about the language.
 */

#include "utils.h"


bool related(char a, char b)
{
  int diff = a - b;
  if (diff == 32 || diff == -32){
    return true;
  }
  return false;
}


std::string collapse_once(std::string s)
{
  s = s + "1";
  std::string out = "";
  char a;
  char b;
  for (unsigned int i = 0; i < s.length() - 1; ++i){
    a = s[i];
    b = s[i+1];
    if (!related(a, b)) out += a;
    else ++i;
  }
  return out;
}


std::string collapse_maximally(std::string line)
{
  std::string cline = collapse_once(line);
  while (cline != line){
    line = cline;
    cline = collapse_once(line);
  }
  return cline;
}


std::string remove_pair(std::string line, char c)
{
  char C = (int)c + 32;
  std::string out = "";
  for (auto l : line){
    if (l != c && l != C) out.push_back(l);
  }
  return out;
}



void part1(std::string content)
{
  std::string line;
  std::istringstream input(content);
  std::getline(input, line); // input is only one line
  std::cout << collapse_maximally(line).length() << std::endl;
}


void part2(std::string content)
{
  std::string line;
  std::istringstream input(content);
  std::getline(input, line);
  std::string alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  int record = 9999;
  std::string scomp = "";
  int icomp = 0;
  for (auto l : alpha){
    std::string scomp = remove_pair(line, l);
    icomp = collapse_maximally(scomp).length();
    if (icomp < record) record = icomp;
  }
  std::cout << record << std::endl;
}


int main()
{
  std::string content;
  content = read_file("inputs/input5.txt");
  part1(content);
  part2(content);
}
