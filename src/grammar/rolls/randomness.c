

#include "external/pcg_basic.h"
#include "rolls/randomness.h"
#include <limits.h>
#include <stdint.h>
#include <stdio.h>
#include <math.h>

#if USE_SECURE_RANDOM == 1
#include <bsd/stdlib.h>
#endif

extern pcg32_random_t rng;

int get_random_uniformly(){
    int value;
    #if USE_SECURE_RANDOM == 1
        value = (int)arc4random_uniform(INT_MAX);
    #else
        value = (int)pcg32_boundedrand_r(&rng, INT_MAX);
    #endif
    return value;
}


double get_random_normally(double mean, double std) { /* Box-Muller. */
    // Not Cryptographically Secure yet.
    static double cached = 0.0;
    double x, y, r, res;

    // printf("Mean: %f, std: %f\n", mean, std);
    if (cached == 0.0) {
        do {
            x = 2.0 * (int)pcg32_boundedrand_r(&rng, INT_MAX) / UINT32_MAX - 1;
            y = 2.0 * (int)pcg32_boundedrand_r(&rng, INT_MAX) / UINT32_MAX - 1;
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
    // -3 to 0
    // now -6 to 0
    // res -= 3;

    if(res < -3 || res > 0){
        // If outlier beyond bounds, reroll.
        // TODO: Catch Recusion Limit!!
        return get_random_normally(mean, std);
    }

    // The rest of the function only calculates one half
    int other_side = (int)pcg32_boundedrand_r(&rng, 2);
    if (other_side){
        return res*-1;
    }

    return res;
}
