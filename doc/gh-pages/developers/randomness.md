---
title: Randomness
published: true
nav_order: 14
parent: Technical Information
---

# Randomness


GNOLL has the following options for random number calculation:

## PCG

The [PCG](https://www.pcg-random.org/) library provides us a more statistically stable, more complex, but still fast! method to gather randomness.

This is the default method.

## ARC4Random

If being cryptographically secure is important to your use case, GNOLL can be configured to use ARC4Random.

To enable this:
- You must install `libbsd-dev`
- build make with `USE_SECURE_RANDOM=1`

The drawback to this method is that it is slower and the statistical quality is not quite as strong as PCG. Though the performance is not very noticable until you are doing very large dice rolls.

An example of Rolling 10000000d10000000:
ARC4Random: : 1.8s
PCG: 0.4s
