---
title: reflex：使用纯Python构建Web应用程序的开源工具
slug: reflex-web-apps-python
description: reflex是一个开源项目，允许开发者使用纯Python构建Web应用程序。它提供了简单易用的接口，使得Python开发者能够快速创建和部署自己的Web应用。通过在GitHub上贡献代码，您可以参与到reflex的开发中来，推动这个项目的成长和优化。
tags: 
  - opensource
  - dev
  - python
pubDatetime: 2024-11-06T09:46:02+08:00
ogImage: https://repository-images.githubusercontent.com/557075997/b1250dfd-95a2-448d-8221-c8dbe9807e6f
---

[原文链接](https://github.com/reflex-dev/reflex?tab=readme-ov-file)

---

Reflex is a library to build full-stack web apps in pure Python.

Key features:
* **Pure Python** - Write your app's frontend and backend all in Python, no need to learn Javascript.
* **Full Flexibility** - Reflex is easy to get started with, but can also scale to complex apps.
* **Deploy Instantly** - After building, deploy your app with a [single command](https://reflex.dev/docs/hosting/deploy-quick-start/) or host it on your own server.

See our [architecture page](https://reflex.dev/blog/2024-03-21-reflex-architecture/#the-reflex-architecture) to learn how Reflex works under the hood.

## ⚙️ Installation

Open a terminal and run (Requires Python 3.9+):

```bash
pip install reflex
```

## 🥳 Create your first app

Installing `reflex` also installs the `reflex` command line tool.

Test that the install was successful by creating a new project. (Replace `my_app_name` with your project name):

```bash
mkdir my_app_name
cd my_app_name
reflex init
```

This command initializes a template app in your new directory.

You can run this app in development mode:

```bash
reflex run
```

You should see your app running at http://localhost:3000.

Now you can modify the source code in `my_app_name/my_app_name.py`. Reflex has fast refreshes so you can see your changes instantly when you save your code.

