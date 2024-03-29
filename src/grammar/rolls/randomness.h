#ifndef __RANDOMNESS_H__
#define __RANDOMNESS_H__

long long arc4random_uniform64(long long upper_bound);

long long get_random_uniformly(void);
double get_random_normally(double mean, double std);

#endif
