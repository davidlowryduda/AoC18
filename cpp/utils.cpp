#include "utils.h"
#include <fstream>

std::string
read_file(const std::string filename)
{
  std::string contents;
  std::ifstream file(filename, std::ios::in);

  // Check that the file was loaded
  if(!file)
  {
      std::cout << filename << " was not found." << std::endl;
      std::exit(EXIT_FAILURE);
  }

  // Determine the length of the file, resize contents
  file.seekg(0, std::ios::end);
  contents.resize(static_cast<std::size_t> (file.tellg()));

  // Read file into contents
  file.seekg(0, std::ios::beg);
  file.read(&contents[0], contents.size());
  return contents;
}


std::string
read_day(int n)
{
  std::string contents;
  std::string filename = "inputs/input" + std::to_string(n) + ".txt";
  return read_file(filename);
}
