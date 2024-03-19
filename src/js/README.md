---
title: JavaScript Setup
published: true
nav_order: 0
---

# Javascript

GNOLL is currently supported in Node as a console level application, **not** a browser script. (Though, we would appreciate contributers that know how to make it happen).

Emscripten does not allow file writing [ref](https://stackoverflow.com/a/54384808), at least via the same mechanism as the other languages, so output is currently only via stdout. 

## Setup

### Pre-Requisites
```bash
sudo apt-get install emscripten nodejs
```

### Build
```bash
make javascript
```

### Run
```bash
node build/js/a.out.js
```
