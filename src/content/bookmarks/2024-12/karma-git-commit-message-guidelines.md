---
title: Karma 的 Git 提交消息指南：使用 Commitlint 强制执行规范
slug: karma-git-commit-message-guidelines
description: 了解 Karma 对 Git 提交消息的标准，使用 commitlint 和 Angular 配置进行强制执行。这些规范增强了变更日志生成和 Git 历史的导航，确保项目贡献的清晰性和一致性。
tags: 
  - dev
  - tool
  - opensource
pubDatetime: 2024-12-05T19:53:42+08:00
ogImage: 
---

[原文链接](https://karma-runner.github.io/6.4/dev/git-commit-msg.html)

---

In the repository we use and enforce the commit message conventions. The conventions are verified using [commitlint](https://conventional-changelog.github.io/commitlint/) with [Angular config](https://www.npmjs.com/package/@commitlint/config-angular).

## The reasons for these conventions: [#](#the-reasons-for-these-conventions)

* automatic generating of the changelog
* simple navigation through git history (e.g. ignoring style changes)

## Format of the commit message: [#](#format-of-the-commit-message)

```bash
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

## Example commit message: [#](#example-commit-message)

```bash
fix(middleware): ensure Range headers adhere more closely to RFC 2616

Add one new dependency, use `range-parser` (Express dependency) to compute
range. It is more well-tested in the wild.

Fixes #2310
```

## Message subject (first line) [#](#message-subject-first-line)

The first line cannot be longer than 72 characters and should be followed by a blank line. The type and scope should always be lowercase as shown below.

### Allowed `<type>` values: [#](#allowed-type-values)

* **feat** for a new feature for the user, not a new feature for build script. Such commit will trigger a release bumping a MINOR version.
* **fix** for a bug fix for the user, not a fix to a build script. Such commit will trigger a release bumping a PATCH version.
* **perf** for performance improvements. Such commit will trigger a release bumping a PATCH version.
* **docs** for changes to the documentation.
* **style** for formatting changes, missing semicolons, etc.
* **refactor** for refactoring production code, e.g. renaming a variable.
* **test** for adding missing tests, refactoring tests; no production code change.
* **build** for updating build configuration, development tools or other changes irrelevant to the user.

### Example `<scope>` values: [#](#example-scope-values)

* init
* runner
* watcher
* config
* web-server
* proxy
* etc.

The `<scope>` can be empty (e.g. if the change is a global or difficult to assign to a single component), in which case the parentheses are omitted. In smaller projects such as Karma plugins, the `<scope>` is empty.

## Message body [#](#message-body)

Just as in the `<subject>`, use the imperative, present tense: "change" not "changed" nor "changes". Message body should include motivation for the change and contrasts with previous behavior.

### Referencing issues [#](#referencing-issues)

Closed issues should be listed on a separate line in the footer prefixed with "Closes" keyword like this:

```bash
Closes #234
```

or in the case of multiple issues:

```bash
Closes #123, #245, #992
```

### Breaking changes [#](#breaking-changes)

All breaking changes have to be mentioned in footer with the description of the change, justification and migration notes.

```bash
BREAKING CHANGE:

`port-runner` command line option has changed to `runner-port`, so that it is
consistent with the configuration file syntax.

To migrate your project, change all the commands, where you use `--port-runner`
to `--runner-port`.
```

Any commit with the breaking change section will trigger a MAJOR release and appear on the changelog independently of the commit type.

***

This document is based on [Angular Commit Message Format](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#commit). See the [commit history](https://github.com/karma-runner/karma/commits/master) for examples of properly-formatted commit messages.


