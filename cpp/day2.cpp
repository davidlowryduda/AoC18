/*
 * Solve day 2.
 *
 * On the right are notes to myself about cpp, revealing what I do and don't
 * know about the language.
 */

#include "utils.h"


/*
 * digest_line --- return a count of each letter appearing in input word
 */
std::unordered_map<char, int>
digest_line(std::string word)
{
  std::unordered_map<char, int> seen;
  for (char c : word)
  {
    seen[c] += 1;
  }
  return seen;
}


/*
 * contains_value --- returns True if key is in the unordered_map
 */
bool contains_value(std::unordered_map<char, int> map, int rep)
{
  for (auto iter = map.begin(); iter != map.end(); ++iter)
  {
    if (iter->second == rep)    // the map is a bunch of std::pair<char, int>
    {                           // Thus to access the int, one uses second to
      return true;              // get the int part. This is the same as
    }                           // (*iter).second.
  }
  return false;
}



void part1(std::string content)
{
  int doubles {0};
  int triples {0};
  std::string line;
  std::istringstream input(content);

  while (std::getline(input, line))
  {
    std::unordered_map<char, int> seen = digest_line(line);
    if (contains_value(seen, 2)) { doubles += 1; }
    if (contains_value(seen, 3)) { triples += 1; }
  }
  std::cout << doubles * triples << std::endl;
}


/*
 * distance --- compute naive Hamming distance between word1 and word2
 */
int distance(std::string word1, std::string word2)
{
  int ndiffs {0};
  for (uint i = 0; i < word1.length(); ++i)
  {
    if (word1[i] != word2[i]) { ndiffs += 1; }
  }
  return ndiffs;
}


/*
 * common_substring --- return common substring between word1 and word2
 */
std::string common_substring(std::string word1, std::string word2)
{
  std::string res = "";
  for (uint i = 0; i < word1.length(); ++i)
  {
    if (word1[i] == word2[i]) { res += word1[i]; }
  }
  return res;
}


void part2(std::string content)
{
  std::string line;
  std::istringstream input(content);
  while (std::getline(input, line))
  {
    std::string line2;
    std::istringstream input2(content);

    while (std::getline(input2, line2))
    {
      if (distance(line, line2) == 1)
      {
        std::cout << common_substring(line, line2) << std::endl;
        return;
      }
    }
  }
}


int main()
{
  std::string content;
  content = read_file("inputs/input2.txt");
  part1(content);
  part2(content);
}
