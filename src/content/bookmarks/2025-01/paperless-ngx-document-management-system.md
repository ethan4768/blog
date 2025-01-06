---
title: "Paperless-ngx: 社区支持的文档管理系统，扫描、索引并归档您的实体文档"
slug: paperless-ngx-document-management-system
description: |
  Paperless-ngx 是一个开源文档管理系统，可以将实体文档转变为可搜索的在线档案，帮助您减少纸张使用。作为原项目的官方继任者，Paperless-ngx 鼓励社区共同参与，支持持续的开发和改进。
tags: 
  - dev
  - opensource
  - tool
  - documentmanagement
pubDatetime: 2025-01-06T09:55:12+08:00
ogImage: https://opengraph.githubassets.com/6997a4fbd284f1c94cd234e302ed1b7f70420f5118e5ca9e947071fe1ab22f3e/paperless-ngx/paperless-ngx
---

[原文链接](https://github.com/paperless-ngx/paperless-ngx)

---

[![ci](https://github.com/paperless-ngx/paperless-ngx/workflows/ci/badge.svg)](https://github.com/paperless-ngx/paperless-ngx/actions)[![Crowdin](https://camo.githubusercontent.com/b4d22f491bb4b1d8ad8a983ceb4f48a5949011efee978bd4dc55f7da2c5b62e1/68747470733a2f2f6261646765732e63726f7764696e2e6e65742f70617065726c6573732d6e67782f6c6f63616c697a65642e737667)](https://crowdin.com/project/paperless-ngx)[![Documentation Status](https://camo.githubusercontent.com/dd4b21124dd1bb6047a8f020a121a6a6470d73cecdf157148b065302891c8f3c/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6465706c6f796d656e74732f70617065726c6573732d6e67782f70617065726c6573732d6e67782f6769746875622d70616765733f6c6162656c3d646f6373)](https://docs.paperless-ngx.com)[![codecov](https://camo.githubusercontent.com/cf6273f9644bbff06a4e657ea5df3cb6dc0b3912a3d1363d7e61e69a2ecb1414/68747470733a2f2f636f6465636f762e696f2f67682f70617065726c6573732d6e67782f70617065726c6573732d6e67782f6272616e63682f6d61696e2f67726170682f62616467652e7376673f746f6b656e3d564b364f55504a335459)](https://codecov.io/gh/paperless-ngx/paperless-ngx)[![Chat on Matrix](https://camo.githubusercontent.com/a4bcabdcd3cebf74e7e63e9b9d7b5ed6f10ce2b743bfbb82be6dded7604fd58b/68747470733a2f2f6d61747269782e746f2f696d672f6d61747269782d62616467652e737667)](https://matrix.to/#/%23paperlessngx%3Amatrix.org)[![demo](https://camo.githubusercontent.com/22156630cd900a247bc6c9417b69d9d63e869bedcae993b905bdd8382487c1f7/68747470733a2f2f63726f6e69746f722e696f2f6261646765732f7665374974592f70726f64756374696f6e2f5735455f42396a6b656c47395a6244694e48555051455648334d592e737667)](https://demo.paperless-ngx.com)

![](https://github.com/paperless-ngx/paperless-ngx/raw/main/resources/logo/web/png/Black%20logo%20-%20no%20background.png)

# Paperless-ngx

[](#paperless-ngx)

Paperless-ngx is a document management system that transforms your physical documents into a searchable online archive so you can keep, well, *less paper*.

Paperless-ngx is the official successor to the original [Paperless](https://github.com/the-paperless-project/paperless) & [Paperless-ng](https://github.com/jonaswinkler/paperless-ng) projects and is designed to distribute the responsibility of advancing and supporting the project among a team of people. [Consider joining us!](#community-support)

Thanks to the generous folks at [DigitalOcean](https://m.do.co/c/8d70b916d462), a demo is available at [demo.paperless-ngx.com](https://demo.paperless-ngx.com) using login `demo` / `demo`. *Note: demo content is reset frequently and confidential information should not be uploaded.*

* [Features](#features)

* [Getting started](#getting-started)

* [Contributing](#contributing)

  * [Community Support](#community-support)
  * [Translation](#translation)
  * [Feature Requests](#feature-requests)
  * [Bugs](#bugs)

* [Related Projects](#related-projects)

* [Important Note](#important-note)

This project is supported by:\
[![](https://camo.githubusercontent.com/c7974ce4b77cd11d4cf48978920c7009153ea17c134891bd3eeca760444fa909/68747470733a2f2f6f70656e736f757263652e6e7963332e63646e2e6469676974616c6f6365616e7370616365732e636f6d2f6174747269627574696f6e2f6173736574732f5356472f444f5f4c6f676f5f686f72697a6f6e74616c5f626c61636b5f2e737667)](https://m.do.co/c/8d70b916d462)

# Features

[](#features)

![](https://raw.githubusercontent.com/paperless-ngx/paperless-ngx/main/docs/assets/screenshots/documents-smallcards.png)

A full list of [features](https://docs.paperless-ngx.com/#features) and [screenshots](https://docs.paperless-ngx.com/#screenshots) are available in the [documentation](https://docs.paperless-ngx.com/).

# Getting started

[](#getting-started)

The easiest way to deploy paperless is `docker compose`. The files in the [`/docker/compose` directory](https://github.com/paperless-ngx/paperless-ngx/tree/main/docker/compose) are configured to pull the image from GitHub Packages.

If you'd like to jump right in, you can configure a `docker compose` environment with our install script:

```
bash -c "$(curl -L https://raw.githubusercontent.com/paperless-ngx/paperless-ngx/main/install-paperless-ngx.sh)"
```

More details and step-by-step guides for alternative installation methods can be found in [the documentation](https://docs.paperless-ngx.com/setup/#installation).

Migrating from Paperless-ng is easy, just drop in the new docker image! See the [documentation on migrating](https://docs.paperless-ngx.com/setup/#migrating-to-paperless-ngx) for more details.

### Documentation

[](#documentation)

The documentation for Paperless-ngx is available at [https://docs.paperless-ngx.com](https://docs.paperless-ngx.com/).

# Contributing

[](#contributing)

If you feel like contributing to the project, please do! Bug fixes, enhancements, visual fixes etc. are always welcome. If you want to implement something big: Please start a discussion about that! The [documentation](https://docs.paperless-ngx.com/development/) has some basic information on how to get started.

## Community Support

[](#community-support)

People interested in continuing the work on paperless-ngx are encouraged to reach out here on github and in the [Matrix Room](https://matrix.to/#/#paperless:matrix.org). If you would like to contribute to the project on an ongoing basis there are multiple [teams](https://github.com/orgs/paperless-ngx/people) (frontend, ci/cd, etc) that could use your help so please reach out!

## Translation

[](#translation)

Paperless-ngx is available in many languages that are coordinated on Crowdin. If you want to help out by translating paperless-ngx into your language, please head over to <https://crwd.in/paperless-ngx>, and thank you! More details can be found in [CONTRIBUTING.md](https://github.com/paperless-ngx/paperless-ngx/blob/main/CONTRIBUTING.md#translating-paperless-ngx).

## Feature Requests

[](#feature-requests)

Feature requests can be submitted via [GitHub Discussions](https://github.com/paperless-ngx/paperless-ngx/discussions/categories/feature-requests), you can search for existing ideas, add your own and vote for the ones you care about.

## Bugs

[](#bugs)

For bugs please [open an issue](https://github.com/paperless-ngx/paperless-ngx/issues) or [start a discussion](https://github.com/paperless-ngx/paperless-ngx/discussions) if you have questions.

# Related Projects

[](#related-projects)

Please see [the wiki](https://github.com/paperless-ngx/paperless-ngx/wiki/Related-Projects) for a user-maintained list of related projects and software that is compatible with Paperless-ngx.

# Important Note

[](#important-note)

> Document scanners are typically used to scan sensitive documents like your social insurance number, tax records, invoices, etc. **Paperless-ngx should never be run on an untrusted host** because information is stored in clear text without encryption. No guarantees are made regarding security (but we do try!) and you use the app at your own risk. **The safest way to run Paperless-ngx is on a local server in your own home with backups in place**.


