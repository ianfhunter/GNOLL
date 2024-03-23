#include <iostream>
#include <fstream>
#include <assert.h>
#include <string.h>
#include "shared_header.h"

int main()
{
  const char* fn = "out.dice";
  
  remove(fn);

  int err_code = roll_full_options(
    strdup("1d20"),
    strdup(fn),
    0,
    0,
    0,
    0,
    0,
    0
  );
  assert(err_code == 0);

  std::ifstream myfile; 
  myfile.open(fn);
  if ( myfile.is_open() ) { 
    std::string mystring;
    myfile >> mystring;
    std::cout << mystring; 
  }else{
    return 1;
  }
  return 0;
}
