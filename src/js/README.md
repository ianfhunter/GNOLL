---
title: JavaScript Setup
published: true
nav_order: 0
---

# Javascript

GNOLL is currently supported in Node as a console level application.
It is **not** supported in the browser yet. 
We appreciate contributions that can change this.

Emscripten does not allow file writing [ref](https://stackoverflow.com/a/54384808), 
at least via the same mechanism as the other languages, 
Output is currently only via stdout.

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
