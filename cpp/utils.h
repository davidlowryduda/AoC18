/*
 * utils.h --- Common utilities
 *
 * Includes the basic libraries, and defines convenient utility functions
 * that may be useful.
 */

#ifndef UTILS_H
#define UTILS_H

#include <iostream>
#include <string>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <stdexcept>
#include <sstream>
#include <unordered_map>
#include <set>
#include <array>


/*
 * read_day --- Read input file for day <n>
 */
std::string
read_day(int n);


/*
 * read_file --- Read contents of file
 */
std::string
read_file(const std::string filename);


#endif /* UTILS_H */
