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

```bash
make all jsbundle
```

Start a web server. For example:

```bash
python3 -m http.server 8003 &> /dev/null &
```

Load index.html (http://localhost:8003/index.html in the previous example) in your browser.

Provide notation in the textbox and press the "Roll" button.
The output of GNOLL is printed to a separate div.

Include gnoll.bundle.js in your own webpages for your own projects
