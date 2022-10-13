## Scripts

[![status](https://joss.theoj.org/papers/c704c5148e622d32403948320c5e96a1/status.svg)](https://joss.theoj.org/papers/c704c5148e622d32403948320c5e96a1)
[![TTRPG compatibility rate](https://img.shields.io/badge/Popular%20TTRPG%20compatibility-96.875%25-green)](https://img.shields.io/badge/Popular%20TTRPG%20compatibility-96.875%25-green)
[![GitHub license](https://img.shields.io/github/license/ianfhunter/GNOLL.svg)](https://github.com/ianfhunter/GNOLL/blob/master/LICENSE)
![GitHub last commit](https://img.shields.io/github/last-commit/ianfhunter/GNOLL.svg)  [![Donate](https://img.shields.io/badge/Donate-Paypal-yellow.svg)](https://paypal.me/ianfhunter)

- [Sitemap](#sitemap)
- [Roadmaps Meta](#roadmaps-meta)
- [Content Skeleton](#content-skeleton)

## Sitemap

Generates the sitemap with all the pages and guides

```shell
npm run meta:sitemap
```

## Roadmaps Meta

Generates the `content/roadmaps.json` file by combining the `content/raodmaps/**/meta.json` content in each roadmap

```shell
npm run meta:roadmaps
```

## Content Skeleton

This command is used to create the content folders and files for the interactivity of the roadmap. You can use the below command to generate the roadmap skeletons inside a roadmap directory:

```shell
npm run roadmap-content [frontend|backend|devops|...]
```

For the content skeleton to be generated, we should have proper grouping, and the group names in the project files. You can follow the steps listed below in order to add the meta information to the roadmap. 

For languages other than Python/C/C++ call the corresponding make target after the commands above.

## 🐛 Issues / Bugs / FAQs / Feature Requests

If you encounter any issues or have any ideas, please file them in our [Issue Tracker](https://github.com/ianfhunter/GNOLL/issues).

## ✋ Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## 🔢 Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/ianfhunter/gnoll/tags).

## 🤹 Authors / Contributers / Attributions

* **Ian Hunter** - *Main Developer* - [Ianfhunter](https://github.com/ianfhunter/)

See also the list of [contributors](https://github.com/ianfhunter/gnoll/contributors) who participated in this project.

## 📃 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details.

Individual licensing arrangements can be made if this is an issue for your project - Contact Me at [LinkedIn](https://www.linkedin.com/in/ianfhunter) to discuss.

## 👏 Acknowledgments

* **Billie Thompson** - *README & Contribution Templates* - [PurpleBooth](https://github.com/PurpleBooth)

## 🏗️ Built With

* [Lex & Yacc](http://dinosaur.compilertools.net/) - Grammar Lexing & Parsing
* [uthash](https://troydhanson.github.io/uthash/userguide.html) - C hashtable lib
* Love! 💖

## 💰 Donate

[Keep this project alive](https://ko-fi.com/ianfhunter)
