---
title: 我常用的 mac apps
slug: my-favorite-mac-apps
description: 我常用的 mac apps
tags:
  - mactips
  - startup
  - dev
featured: true
pubDatetime: 2024-10-01T16:31:26+08:00
---

## 开发

### Orbstack

Docker 容器工具

- **备注**:
    - 有 pro 和 enterprise 版本，个人使用免费版够用
    - 轻量、易用、性能高
    - 试用各类开源项目必备
- **价格**: 免费，提供 PRO 版本
- **地址**: [官网](https://orbstack.dev/)

### SwitchHosts

管理、切换多个 hosts 方案的工具

- **价格**: 免费，开源
- **地址**: [GitHub](https://github.com/oldj/SwitchHosts)

### Insomnium

本地优先的 API 调试工具，类似于 postman

- **备注**:
    - 当前已停止维护，但完全够用
    - [insomnia](https://github.com/Kong/insomnia)
      在 [release 2023.5.8](https://github.com/Kong/insomnia/releases/tag/core%402023.5.8) 后引入强制账户登录，Insomnium 是基于此次
      commit 之前的一个 fork，并进行了一些改动
    -
  参考 [Changes in Insomnia 8.0+ regarding needing an account and local/cloud data migration. · Kong/insomnia · Discussion #6590](https://github.com/Kong/insomnia/discussions/6590)
- **价格**: 免费，开源
- **地址**: [GitHub](https://github.com/ArchGPT/insomnium)

## 效率

### Raycast

最好用的启动器，自带窗口管理、剪切板、Snippets、计算器等各种功能，完全替代 Spotlight。

- **备注**：
    - 支持添加自定义脚本
    - 支持插件
    - 个人免费，提供 PRO、Teams 等升级计划，PRO 有 AI 支持
- **价格**: 免费版够用，提供 PRO 版本
- **地址**: [官网](https://www.raycast.com/)

### Homebrew

软件包管理工具

- **备注**:
    - 一些配置
        ```
        # Homebrew 在安装软件时自动清理临时文件和缓存，导致安装速度较慢，可以禁用此功能
        export HOMEBREW_NO_INSTALL_CLEANUP=true 
        # Homebrew 在安装软件时，总是先自动升级自己，可以禁用此功能
        export HOMEBREW_NO_AUTO_UPDATE=true
        ```
- **价格**: 免费，开源
- **地址**: [官网](https://brew.sh/), [GitHub](https://github.com/Homebrew/brew)

### Go2Shell

在 Finder 中启动命令行，并切换到当前目录

- **备注**:
    - 打开配置页面，执行命令 `open -a Go2Shell --args config`
- **价格**: 免费
- **地址**: [官网](https://zipzapmac.com/go2shell), [Mac App Store](https://apps.apple.com/us/app/go2shell/id445770608)

### Ice

菜单栏图标隐藏工具

- **备注**:
    - 相比 Dozer 等其他竞品，增加了 Always Hidden 选项，Option + 鼠标左键，可显示隐藏
    - Homebrew 安装：`brew install jordanbaird-ice`
- **价格**: 免费，开源
- **地址**: [GitHub](https://github.com/jordanbaird/Ice)

### Snipaste

简单易用强大的截图、贴图、标注工具

- **备注**:
    - 支持 Windows、Mac，Linux 开发中
    - 提供 PRO 版本，但免费版本足够用
    - Homebrew 安装：`brew install snipaste`
- **价格**: 免费，提供 PRO 版本
- **地址**: [英文版](https://docs.snipaste.com/), [中文版](https://docs.snipaste.com/zh-cn/)

### Obsidian

本地优先的笔记软件

- **备注**:
    - 跨平台，可使用 iCloud 等进行同步，Mac 和 iPhone 用户很方便
    - 支持 markdown
    - 插件众多
    - 个人免费，有额外付费功能和付费的 Early access
    - 提供 API
- **价格**: 免费，提供 PRO 版本
- **地址**: [官网](https://obsidian.md/)

### RIME | 中州韻輸入法引擎

开源输入法框架，定制型极强，不用担心隐私问题。

- **备注**:
    - Mac 上使用`鼠须管`，iPhone 上使用`仓`
    - 有很多方案和主题，看 [雾凇拼音](https://dvel.me/posts/rime-ice/) 就够
- **价格**: 免费，开源
- **地址**: [官网](https://rime.im/), [GitHub](https://github.com/rime)

### Stats

菜单栏上的系统监控工具，美观、全面

- **价格**: 免费, 开源
- **地址**: [GitHub](https://github.com/exelban/stats)

### Skim

快速好用的 pdf 阅读器

- **价格**: 免费，开源
- **地址**: [官网](https://skim-app.sourceforge.io/), [SourceForge](https://sourceforge.net/projects/skim-app/)

### hyperduck

将链接从 iOS 设备上发送到 Mac，并直接在浏览器中打开

- **备注**:
    - 需 iOS 上也安装对应 app
    -
  参考 [借助 Hyperduck 和 Shortcuts/Raycast 从 iPhone 发送 URL 到 Mac](https://blog.finengine.tech/posts/Send-URL-from-iPhone-to-Mac-with-Hyperduck-and-Shortcuts/)
- **价格**: 免费
- **地址**: [官网](https://sindresorhus.com/hyperduck)

### Bitwarden

跨平台密码管理工具

- **备注**:
    - 支持手机、Mac、Windows、浏览器多平台
    - 个人使用免费，提供 Premium、Families、Teams、Enterprise 等升级计划
    - 开源，支持自部署
- **价格**: 免费，开源
- **地址**: [官网](https://bitwarden.com/), [GitHub](https://github.com/bitwarden)

### Cherry Studio

支持多模型服务的 GPT 客户端

- **价格**: 免费，开源
- **地址**: [官网](https://cherry-ai.com/), [Github](https://github.com/kangfenmao/cherry-studio)

### NetNewsWire

RSS 阅读器，支持多种格式

- **价格**: 免费，开源
- **地址**: [GitHub](https://github.com/Ranchero-Software/NetNewsWire)

### Xnip

截图工具，可以滚动截图

- **价格**: 免费版够用
- **地址**: [官网](https://zh.xnipapp.com/)
  , [Mac App Store](https://apps.apple.com/cn/app/xnip-%E6%88%AA%E5%9B%BE-%E6%A0%87%E6%B3%A8/id1221250572?mt=12)

### Gifski

视频转高质量 GIF 工具

- **价格**: 免费，开源
- **地址**: [GitHub](https://github.com/sindresorhus/Gifski)

### QuickRecorder

开源高性能的 macOS 屏幕录制工具

- **备注**:
    - Homebrew 安装：`brew install lihaoyun6/tap/quickrecorder`
- **价格**: 免费，开源
- **地址**: [GitHub](https://github.com/lihaoyun6/QuickRecorder)

## 终端&命令行

### iTerm2

终端工具

- **价格**: 免费，开源
- **地址**: [官网](https://iterm2.com/), [GitHub](https://github.com/gnachman/iTerm2)

### Oh My Zsh

基于 zsh 命令行的一个扩展工具集，提供了丰富的扩展功能。

- **备注**:
    - 过多的插件会影响速度
    - 我的插件列表：git, autojump
    - 安装`zsh`: `brew install zsh`
    - 安装`ohmyzsh`: `sh -c "$(curl -fsSL https://install.ohmyz.sh/)"`
    - 启用 [autojump](https://github.com/wting/autojump) ，需提前安装：`brew install autojump`
- **价格**: 免费，开源
- **地址**: [GitHub](https://github.com/ohmyzsh/ohmyzsh)

### Starship

轻量、迅速、客制化的高颜值终端主题

- **备注**:
    - Homebrew 安装：`brew install starship`
    - 可搭配 zsh, bash 等使用
    - 开机即用，无须定制就很舒服
- **价格**: 免费，开源
- **地址**: [官网](https://starship.rs/zh-CN/), [GitHub](https://github.com/starship/starship)

### mac-cleanup-py

Python cleanup script for macOS

- **备注**:
    - Homebrew 安装：`brew tap mac-cleanup/mac-cleanup-py && brew install mac-cleanup-py`
    - 配置清理项：`mac-cleanup -c`
- **价格**: 免费，开源
- **地址**: [Github](https://github.com/mac-cleanup/mac-cleanup-py)

## 其他

### Beancount

基于文本文件的复式记账法

- **备注**:
    - Homebrew 安装：`brew tap mac-cleanup/mac-cleanup-py && brew install mac-cleanup-py`
    - 一般搭配 [fava](https://github.com/beancount/fava) 使用
    - 可以将 beancount 内容保存到 github 私有仓库中作为备份，然后在 google colab 中查看
- **价格**: 免费，开源
- **地址**: [Github](https://github.com/beancount/beancount)

### IINA

Mac 上最好的视频播放器

- **备注**:
    - Homebrew 安装：`brew tap iina/homebrew-mpv-iina && brew install mpv-iina`
- **价格**: 免费，开源
- **地址**: [官网](https://iina.io/), [GitHub](https://github.com/iina/iina)

### OSX Watch 屏保

- **价格**: 免费
- **地址**: [官网](https://www.rasmusnielsen.dk/applewatch)
