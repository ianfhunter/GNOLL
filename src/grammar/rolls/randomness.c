#include "external/pcg-c/include/pcg_variants.h"
#include "rolls/randomness.h"
#include <limits.h>
#include <stdint.h>
#include <stdio.h>
#include <math.h>
#include <stdbool.h>

#if USE_SECURE_RANDOM == 1
#include <bsd/stdlib.h>
#endif

extern pcg64_random_t rng;

#if USE_SECURE_RANDOM == 1
long long arc4random_uniform64() {
    int64_t random_value;    
    random_value = (((int64_t)arc4random_uniform(INT_MAX)) << 32) | arc4random_uniform(INT_MAX);
    return random_value;
}
#endif

long long get_random_uniformly(void){
    long long value;
    #if USE_SECURE_RANDOM == 1
        value = (long long)arc4random_uniform64();
    #else
        value = (long long)pcg64_boundedrand_r(&rng, LLONG_MAX);
    #endif
    return value;
}


double get_random_normally(double mean, double std) { 
    /* Box-Muller. */
    // Not Cryptographically Secure yet.
    static double cached = 0.0;
    double res;
    if (cached == 0.0) {
        double x, y, r;
        do {
            x = 2.0 * (double)pcg64_boundedrand_r(&rng, LLONG_MAX) / (double)ULLONG_MAX - 1;
            y = 2.0 * (double)pcg64_boundedrand_r(&rng, LLONG_MAX) / (double)ULLONG_MAX - 1;
            r = x * x + y * y;
        } while (r == 0.0 || r > 1.0);

        double d = sqrt(-2.0 * log(r) / r);

        double n1 = x * d;
        double n2 = y * d;

        res = n1 * std + mean;
        cached = n2;
    }
    else {
        res = cached * std + mean;
        cached = 0.0;
    }

    if(res < -3 || res > 0){
        // If outlier beyond bounds, reroll.
        // TODO: Catch Recusion Limit!!
        return get_random_normally(mean, std);
    }

    // The rest of the function only calculates one half
    bool other_side = (bool)pcg64_boundedrand_r(&rng, 2);
    if (other_side){
        return res*-1;
    }

    return res;
}
