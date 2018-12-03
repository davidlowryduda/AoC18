/*
 * Solve day 3.
 *
 * On the right are notes to myself about cpp, revealing what I do and don't
 * know about the language.
 */

#include "utils.h"

/*
 * initialize_fabric --- set all entries in fabric to 0
 */
void initialize_fabric(int (&arr)[1000][1000])
{
  for (int i=0; i<1000; ++i)
  {
    for (int j=0; j<1000; ++j)
    {
      arr[i][j] = 0;
    }
  }
}


struct parsed_line
{
  std::string id;
  int x;
  int y;
  int width;
  int height;
};

/*
 * parse_line --- parse a line into a `parsed_line`
 *
 * A line is of the form
 *     #id @ x,y: widthxheight
 */
parsed_line
parse_line(std::string line)
{
  int found = line.find("@");
  std::string id = line.substr(0, found-1);
  int found2 = line.find(",");
  int x = std::stoi(line.substr(found+1, found2));
  found = found2;
  found2 = line.find(":");
  int y = std::stoi(line.substr(found+1, found2));
  found = found2;
  found2 = line.find("x");
  int width = std::stoi(line.substr(found+1, found2));
  int height = std::stoi(line.substr(found2+1));
  parsed_line pline = {id, x, y, width, height};
  return pline;
}


/*
 * register_rectangle --- add data from rectangle data (in pline) to arr
 *
 * Store the number of times each part of the array is covered by a rectangle.
 */
void register_rectangle(parsed_line pline, int (&arr)[1000][1000])
{
  for (int i = pline.x; i < pline.x + pline.width; ++i)
  {
    for (int j = pline.y; j < pline.y + pline.height; ++j)
    {
      arr[i][j] += 1;
    }
  }
}

/*
 * no_overlap --- returns true if the rectangle overlaps with no other
 *                rectangle.
 *
 * It is assumed that this is run after all rectangles are registered with
 * `register_rectangle`.
 */
bool no_overlap(parsed_line pline, int (&arr)[1000][1000])
{
  for (int i = pline.x; i < pline.x + pline.width; ++i)
  {
    for (int j = pline.y; j < pline.y + pline.height; ++j)
    {
      if (arr[i][j] != 1)
      {
        return false;
      }
    }
  }
  std::cout << pline.id << std::endl;
  return true;
}

void part1(std::string content, int (&arr)[1000][1000])
{
  std::string line;
  std::istringstream input(content);
  parsed_line pline;
  int count = 0;
  while (std::getline(input, line))
  {
    pline = parse_line(line);
    register_rectangle(pline, arr);
  }
  for (int i = 0; i < 1000; ++i)
  {
    for (int j = 0; j < 1000; ++j)
    {
      if (arr[i][j] > 1) ++count;
    }
  }
  std::cout << count << std::endl;
}


void part2(std::string content, int (&arr)[1000][1000])
{
  std::string line;
  std::istringstream input(content);
  parsed_line pline;
  while (std::getline(input, line))
  {
    pline = parse_line(line);
    if (no_overlap(pline, arr)) return;
  }
}


int main()
{
  std::string content;
  content = read_file("inputs/input3.txt");
  int fabric[1000][1000];
  initialize_fabric(fabric);
  part1(content, fabric);
  part2(content, fabric);
}
