# Dice Tower

<img src="https://raw.githubusercontent.com/ianfhunter/DiceTower/main/media/logo.png" height="200" />

# About

DiceTower is a comprehensive grammar-based library for rolling dice. DiceTower parses [Dice Notation](https://en.wikipedia.org/wiki/Dice_notation) for your project, so that you don't have to. Ideal for software or researchers of tabletop gaming.

It's written in C, so it's very fast and portable!

Here's an example of how you might use DiceTower:
```markdown
   Gridon The Brave: I want to steal from the goblin sitting at the bar.
   Dungeon Master: Okay, give me a stealth check!
   Gridon The Brave: Okay, that's a <1d20+5>
   [DiceTower]: 21
   Dungeon Master: Hurrah! You successfully pickpocket the goblin! However, all he had in there were some crummy dice...
```
# Usage

## Install
```
pip install dice_tower
```

## Roll Dice

```
from dicetower import parser as dt;

dt.roll('2')
> 2
```

# Features

DiceTower supports a lot of different notations. Too many to explain here so [we've got a seperate section in our wiki](https://github.com/ianfhunter/dice-tower/wiki/Dice-Roll-Syntaxes).

# Support
If you encounter any issues, please file them in our [Issue Tracker](https://github.com/ianfhunter/dice-tower/issues).

You can vote on prospective new features on [FeatHub](https://feathub.com/ianfhunter/dice)

# License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details.

Individiual licensing arrangements can be made if this is an issue for your project - Contact Me at [LinkedIn](https://www.linkedin.com/in/ianfhunter) to discuss.

# Donate

[Keep this project alive](https://ko-fi.com/ianfhunter)