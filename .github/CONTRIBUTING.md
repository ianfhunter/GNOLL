# Contributing

First off, thank you for considering contributing to GNOLL.

We're so happy you're considering contributing! Thank you! We hope this document will make it easier to do that.

Following these guidelines helps to communicate that you respect the time of the developers managing and developing this open source project. In return, they should reciprocate that respect in addressing your issue, assessing changes, and helping you finalize your pull requests.

## Process
Please assign yourself to a ticket, or request this, so anyone looking doesn't work on the same thing! Clone the code, make your changes, add a test & create a PR! We'll try to review it as soon as we can

## Change Identified

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change. 

Please note we have a [Code of Conduct](CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.

## Pull Request Process

 1. Ensure any temporary dependencies are removed before submission.

 2. Update the README.md with details of changes to the interface, this includes new environment 
   variables, exposed ports, useful file locations and container parameters.

 3. Increase the version numbers in any examples files and the README.md to the new version that this
   Pull Request would represent. The versioning scheme we use is [SemVer](http://semver.org/).

 4. You may merge the Pull Request in once you have recieved a positive code review.

 ## Scope
GNOLL is specifically designed to be a library for Dice Notation. What that means is, that we are looking for contributions that expand, improve or simplify parsing that notation. TTRPG character creation/storage, Encounter tracking or any other game mechanics are **out of scope** and are best handled as a wrapper around GNOLL in a seperate repository.

Similarly, GNOLL is not overly concerned about the graphical display of the results, but the actual results themselves. We may only consider these contributions on a per-case basis.

## What kinds of contributions we want

GNOLL is an open source project and we love to receive contributions from our community — you! There are many ways to contribute, from writing tutorials or blog posts, improving the documentation, submitting bug reports and feature requests or writing code which can be incorporated into GNOLL itself.

## What contributions we do NOT want

Please don't push standards and suggestions that have already been marked as `won't fix` unless the content is significantly different to what has already been discussed.

Please don't ask for timeline estimates nor for support in another projects codebase. It is reasonably simple to minimize failing test cases for us to debug issues, and we encourage you do so.

## Ground Rules

### Leadership
 * The [main author](https://github.com/ianfhunter/) has final decision and override authority for this project. This includes acceptance/denial/postphonement of features and contributions, ownership of financial contributions, enforcement of policies and discussion with third-parties. 

### Guidelines
 * Do work on branches and create Pull Requests to the master branch when ready.
 * Work cannot be merged unless passing all tests and build regressions.
 * Ensure that your code is sufficiently tested. Try not to reduce our code test coverage if possible
 * Ensure that the scope of your changes have been correctly advertised and any short-comings, alternatives or future work communicated for triage
 * Keep Pull Requests as small as possible to facilitate quick reviews

## Your First Contribution

Unsure where to begin contributing to Dice? You can start by looking through the issues marked `Good First Issue`. These should only require introductory knowledge

Experienced? We could use your help with `Help Wanted` Issues.

Extremely Green? Here are some tutorials to get you up and running on how to create your first Pull Request [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github).

## New Language Support
We would love it if you added a language not yet on our list. We have two things for you to observe first though.

 1. Please add a test so we will know if it breaks!
 2. Try to use the existing C code, if you think there is no way to do this, please mention it in our issues/discussion tab so we can discuss alternatives. We'd really like to avoid duplicating files!
 3. Provide both a passing case AND a failing case to show our exit codes being used.

## Reporting security vulnerabilities or other sensitive issues

If you find a security vulnerability, do NOT open an issue. Contact the maintainer instead.

In order to determine whether you are dealing with a security issue, ask yourself these two questions:
  * Can I access something that's not mine, or something I shouldn't have access to?
  * Can I disable something for other people?

If the answer to either of those two questions are "yes", then you're probably dealing with a security issue. Note that even if you answer "no" to both questions, you may still be dealing with a security issue, so if you're unsure

Known, unaddressed vulnerabilities will be hilighted on the main readme. Additionally, resolved dependencies for previous versions will be mentioned in a SECURITY.md file

## C Guidelines
As much as possible, try to keep logic *out* of the .lex and .yacc files and in functions imported from other files.

GNOLL should ideally never crash and we control this by:

  * Writing errors to the global `gnoll_errno`
  * Checking this value is == 0 before doing any work in your function.
  * All functions that can cause memory/io issues should use safe equivilents in safe_functions.h . Where a function can produce an error code, they should immediately return.

## Code review process
The author will looks at Pull Requests on a regular basis. Feedback will be given as fast as possible, larger changes may take more time to review

## Community

Currently there are not enough people using the project to warrant a chat system. However, we can do this when we gain steam.

## Code Style Guidelines

This will be appended as we add language support

  * **Python** - [PEP8](https://www.python.org/dev/peps/pep-0008/)
