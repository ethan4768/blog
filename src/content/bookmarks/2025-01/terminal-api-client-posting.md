---
title: "darrenburns/posting: 现代终端API客户端，提升开发效率"
slug: terminal-api-client-posting
description: |
  darrenburns/posting 是一款现代化的终端HTTP客户端，类似于Postman和Insomnia，支持键盘操作和SSH使用。请求以简单的YAML文件形式存储，便于阅读和版本控制。它还提供了强大的功能，如自动补全和主题自定义，助力高效开发。
tags: 
  - dev
  - tool
  - api
  - terminal
  - opensource
pubDatetime: 2025-01-06T10:21:03+08:00
ogImage: https://repository-images.githubusercontent.com/806285077/4a45adf3-877e-4898-99f3-11f8f8150286
---

[原文链接](https://github.com/darrenburns/posting)

---

# Posting

[](#posting)

**A powerful HTTP client that lives in your terminal.**

Posting is an HTTP client, not unlike Postman and Insomnia. As a TUI application, it can be used over SSH and enables efficient keyboard-centric workflows. Your requests are stored locally in simple YAML files, so they're easy to read and version control.

[![image](/darrenburns/posting/raw/main/docs/assets/home-image-ad-15aug24.svg)](https://github.com/darrenburns/posting/blob/main/docs/assets/home-image-ad-15aug24.svg)

Some notable features include:

* "jump mode" navigation
* environments/variables
* autocompletion
* syntax highlighting using tree-sitter
* Vim keys
* customizable keybindings
* user-defined themes
* run Python code before and after requests
* extensive configuration
* "open in $EDITOR"
* import curl commands by pasting them into the URL bar
* import OpenAPI specs
* a command palette for quickly accessing functionality

Visit the [website](https://posting.sh) for more information, the roadmap, and the user guide.

## Installation

[](#installation)

Posting can be installed via [uv](https://docs.astral.sh/uv/getting-started/installation/) on MacOS, Linux, and Windows.

`uv` is a single Rust binary that you can use to install Python apps. It's significantly faster than alternative tools, and will get you up and running with Posting in seconds.

You don't even need to worry about installing Python yourself - `uv` will manage everything for you.

```
# quick install on MacOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# install Posting (will also quickly install Python 3.12 if needed)
uv tool install --python 3.12 posting
```

`uv` can also be installed via Homebrew, Cargo, Winget, pipx, and more. See the [installation guide](https://docs.astral.sh/uv/getting-started/installation/) for more information.

Now you can run Posting via the command line:

```
posting
```

`uv` also makes it easy to install additional Python packages into your Posting environment, which you can then use in your pre-request/post-response scripts.

### Prefer `pipx`?

[](#prefer-pipx)

If you'd prefer to use `pipx`, that works too: `pipx install posting`.

Note that Python 3.13 is not currently supported.

## Learn More

[](#learn-more)

Learn more about Posting at <https://posting.sh>.

Posting was built with [Textual](https://github.com/textualize/textual).


