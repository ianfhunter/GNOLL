# Contributing

First off, thank you for considering contributing to Dice.

Following these guidelines helps to communicate that you respect the time of the developers managing and developing this open source project. In return, they should reciprocate that respect in addressing your issue, assessing changes, and helping you finalize your pull requests.

## Change Identified

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change. 

Please note we have a [CODE_OF_CONDUCT.md](code of conduct), please follow it in all your interactions with the project.

## Pull Request Process

1. Ensure any temporary dependencies are removed before submission.
2. Update the README.md with details of changes to the interface, this includes new environment 
   variables, exposed ports, useful file locations and container parameters.
3. Increase the version numbers in any examples files and the README.md to the new version that this
   Pull Request would represent. The versioning scheme we use is [SemVer](http://semver.org/).
4. You may merge the Pull Request in once you have recieved a positive code review.
# Introduction

### What kinds of contributions we want

Dice is an open source project and we love to receive contributions from our community — you! There are many ways to contribute, from writing tutorials or blog posts, improving the documentation, submitting bug reports and feature requests or writing code which can be incorporated into Dice itself.

### What contributions we do NOT want

Please don't push standards and suggestions that have already been marked as `won't fix` unless the content is significantly different to what has already been discussed.

Please don't ask for timeline estimates nor for support in another projects codebase. It is reasonably simple to minimize failing test cases for us to debug issues, and we encourage you do so.

# Ground Rules

## Guidelines
 * Do work on branches and create Pull Requests to the master branch when ready.
 * Work cannot be merged unless passing all tests and build regressions.
 * Ensure that your code is sufficiently tested. Try not to reduce our code test coverage if possible
 * Ensure that the scope of your changes have been correctly advertised and any short-comings, alternatives or future work communicated for triage
 * Keep Pull Requests as small as possible to facilitate quick reviews


# Your First Contribution

Unsure where to begin contributing to Dice? You can start by looking through the issues marked `Good First Issue`. These should only require introductory knowledge

Experienced? We could use your help with `Help Wanted` Issues.

Extremely Green? Here are some tutorials to get you up and running on how to create your first Pull Request [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github).


Small contributions such as fixing spelling errors, where the content is small enough to not be considered breaking, can be merged by a reviewer without waiting for regression.

As a rule of thumb, changes are obvious fixes if they do not introduce any new functionality or creative thinking. As long as the change does not affect functionality, some likely examples include the following:
* Spelling / grammar fixes
* Typo correction, white space and formatting changes
* Comment clean up
* Bug fixes that change default return values or error codes stored in constants
* Adding logging messages or debugging output
* Changes to ‘metadata’ files like Gemfile, .gitignore, build scripts, etc.
* Moving source files from one directory or package to another (that are not referenced)

# Reporting security vulnerabilities or other sensitive issues

If you find a security vulnerability, do NOT open an issue. Contact the maintainer instead.

In order to determine whether you are dealing with a security issue, ask yourself these two questions:
 * Can I access something that's not mine, or something I shouldn't have access to?
 * Can I disable something for other people?

If the answer to either of those two questions are "yes", then you're probably dealing with a security issue. Note that even if you answer "no" to both questions, you may still be dealing with a security issue, so if you're unsure

Known, unaddressed vulnerabilities will be hilighted on the main readme. Additionally, resolved dependencies for previous versions will be mentioned in a SECURITY.md file

# Code review process
The author will looks at Pull Requests on a regular basis. Feedback will be given as fast as possible, larger changes may take more time to review

# Community

Currently there are not enough people using the project to warrant a chat system. However, we can do this when we gain steam.

# Code Style Guidelines

This will be appended as we add language support

 * **Python** - [PEP8](https://www.python.org/dev/peps/pep-0008/)
