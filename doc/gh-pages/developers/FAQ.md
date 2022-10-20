---
title: FAQs
published: true
nav_order: 14
parent: Technical Information
---

# FAQ

Have a Feature Request? [File it for us to look at](https://github.com/ianfhunter/GNOLL/issues). We also have a place for [Discussion](https://github.com/ianfhunter/GNOLL/discussions).

> Q: How can I use unicode, emojis and other strange characters in GNOLL?

GNOLL does not support special characters natively, due to limitations of dependant libraries and significant additional complexity. Our recommendation is to use a representative string for these characters. e.g. 🐺 could be input to GNOLL as WOLF.

> Q: How can I use GNOLL to draw cards out of a deck?

GNOLL does not support tracking the state of internal counters between executions and/or statements, so cannot remove cards from a pool. We recommend doing passing reduced options to GNOLL from your script as cards/dice sides are revealed.
