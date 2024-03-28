---
title: JavaScript Setup
published: true
nav_order: 0
---

# Javascript

GNOLL is currently supported in Node as a console level application and as a browser package.

Emscripten does not allow file writing [ref](https://stackoverflow.com/a/54384808), 
at least via the same mechanism as the other languages, 
Output is currently only via stdout.

## Setup

### Pre-Requisites

```bash
sudo apt-get install emscripten nodejs
```

### Run (Console)

```bash
make javascript
```

```bash
node build/js/a.out.js
```

### Run (Browser)

Build with `make all jsweb`
Start a web server (e.g. `python3 -m http.server 8003 &> /dev/null &`)
Load index.html (http://localhost:8003/index.html in the previous example).
Provide notation in the textbox and press the "Roll" button. Output is printed to a separate div.
