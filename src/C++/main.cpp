#include <iostream>
#include <fstream>
#include <string>
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
  const char* fn = strdup("out.dice");
  
  remove(fn);

  int err_code = roll_full_options(
    strdup("1d20"),
    strdup("out.dice"),
    0,
    0,
    0,
    0,
    0
  );
  if(err_code){return err_code;}

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
