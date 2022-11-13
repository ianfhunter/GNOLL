#include <iostream>
#include <fstream>
#include <assert.h>
#include <string.h>
#include "shared_header.h"

int roll_full_options(
    char* roll_request, 
    char* log_file, 
    int enable_verbosity, 
    int enable_introspection,
    int enable_mocking,
    int mocking_type,
    int mocking_seed
);

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
    0
  );
  assert(err_code);

  std::ifstream myfile; 
  myfile.open(fn);
  std::string mystring;
  if ( myfile.is_open() ) { 
    myfile >> mystring;
    std::cout << mystring; 
  }else{
    return 1;
  }
  return 0;
}
