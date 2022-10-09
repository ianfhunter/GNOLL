#ifndef __SAFE_FNS_H__
#define __SAFE_FNS_H__

#include <stdio.h>
#include <stdlib.h>
#include "shared_header.h"

void * safe_malloc(size_t size);
void * safe_calloc(size_t nitems, size_t size);
FILE * safe_fopen(const char *filename, const char *mode);

#endif
