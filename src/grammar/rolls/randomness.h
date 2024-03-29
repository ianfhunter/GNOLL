#ifndef __RANDOMNESS_H__
#define __RANDOMNESS_H__

#if USE_SECURE_RANDOM == 1
long long arc4random_uniform64(long long upper_bound);
#endif

long long get_random_uniformly(void);
double get_random_normally(double mean, double std);

#endif
