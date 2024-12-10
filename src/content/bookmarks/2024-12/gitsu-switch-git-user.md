---
title: gitsu：轻松切换 Git 用户的命令行工具
slug: gitsu-switch-git-user
description: gitsu 是一个轻量级的命令行工具，灵感来自于 Git-User-Switch，旨在简化 Git 用户的切换过程。支持多种用户管理功能，如添加、修改和选择用户，提升开发效率。
tags: 
  - dev
  - tool
  - opensource
pubDatetime: 2024-12-10T10:18:19+08:00
ogImage: https://opengraph.githubassets.com/30b3fd399a5cb994845e94bcee996a7b83c6ca7a26607e6e04e4fa2c63a87e75/matsuyoshi30/gitsu
---

[原文链接](https://github.com/matsuyoshi30/gitsu?tab=readme-ov-file)

---

# gitsu

[](#gitsu)

A simple cli tool for switching git user easily inspired by [Git-User-Switch](https://github.com/geongeorge/Git-User-Switch)

[![screenshot](/matsuyoshi30/gitsu/raw/main/images/demo.gif)](https://github.com/matsuyoshi30/gitsu/blob/main/images/demo.gif)[![screenshot](https://github.com/matsuyoshi30/gitsu/raw/main/images/demo.gif) ](https://github.com/matsuyoshi30/gitsu/blob/main/images/demo.gif)     [](https://github.com/matsuyoshi30/gitsu/blob/main/images/demo.gif)

## Installation

[](#installation)

Binary releases are [here](https://github.com/matsuyoshi30/gitsu/releases).

**Homebrew**

```
brew install matsuyoshi30/gitsu/gitsu
```

**Go (Not recommended)**

```
go get github.com/matsuyoshi30/gitsu
```

#### Requirements

[](#requirements)

* Go 1.16 \~

## Usage

[](#usage)

```
USAGE:
   git su [global options] command [command options] [arguments...] # via Homebrew
   gitsu [global options] command [command options] [arguments...]  # via go get

COMMANDS:
   delete, d  Delete existing user
   modify, m  Modify existing user
   select, s  Select existing user
   reset, r   Remove all saved user profiles
   init, i    Initialize user config by providing an alias
   add, a     Add new user
   help, h    Shows a list of commands or help for one command
```

## LICENSE

[](#license)

[MIT](https://github.com/matsuyoshi30/gitsu/blob/main/LICENSE)


