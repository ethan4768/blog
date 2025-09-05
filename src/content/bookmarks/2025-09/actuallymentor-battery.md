---
title: "actuallymentor/battery：管理 Apple Silicon Mac 电池充电状态的 CLI/GUI 工具"
slug: actuallymentor-battery
description: |
  actuallymentor/battery 是一个用于管理 Apple Silicon (M1, M2, M3) Mac 电池充电的工具。它可以将电池电量限制在80%，从而延长电池寿命，免费且开源，支持命令行和图形用户界面操作，适合长期插电的用户。
tags: 
  - macos
  - tool
pubDatetime: 2025-09-05T20:06:02+08:00
ogImage: https://opengraph.githubassets.com/dc75b3f4ee2ceb9f630c5c1e7294d2c11e416328a268868ba8bf1bfc42151ecb/actuallymentor/battery
---

[原文链接](https://github.com/actuallymentor/battery)

---

# Battery charge limiter for Apple Silicon Macbook devices适用于 Apple Silicon Macbook 设备的电池充电限制器

[](#battery-charge-limiter-for-apple-silicon-macbook-devices)

[![](/actuallymentor/battery/raw/main/screenshots/tray.png)](https://github.com/actuallymentor/battery/blob/main/screenshots/tray.png)This tool makes it possible to keep a chronically plugged in Apple Silicon Macbook at `80%` battery, since that will prolong the longevity of the battery. It is free and open-source and will remain that way.该工具可以将长期插入的 Apple Silicon Macbook 保持在 `80%` 的电池电量，因为这将延长电池的使用寿命。它是免费和开源的，并且将保持这种状态。

> Want to know if this tool does anything or is just a placebo? Read [this excellent article](https://batteryuniversity.com/article/bu-808-how-to-prolong-lithium-based-batteries). TL;DR: keep your battery cool, keep it at 80% when plugged in, and discharge it as shallowly as feasible.想知道这个工具有什么作用还是只是安慰剂？阅读[这篇优秀的文章 ](https://batteryuniversity.com/article/bu-808-how-to-prolong-lithium-based-batteries)。TL;DR：保持电池凉爽，插入电源时保持在 80%，并尽可能浅地放电。

### Requirements  要求

[](#requirements)

This is an app for Apple Silicon Macs. It will not work on Intel macs. Do you have an older Mac? Consider the free version of the [Al Dente](https://apphousekitchen.com/) software package. It is a good alternative and has a premium version with many more features.这是一款适用于 Apple Silicon Mac 的应用程序。它不适用于英特尔 Mac。你有一台旧的 Mac 吗？考虑 [Al Dente](https://apphousekitchen.com/) 软件包的免费版本。这是一个不错的选择，并且有一个具有更多功能的高级版本。

### Installation  安装

[](#installation)

* Option 1: install the app through brew with `brew install battery`选项 1：使用 `brew 安装电池`通过 brew 安装应用程序
* Option 2: [download the app dmg version here](https://github.com/actuallymentor/battery/releases/)选项 2：[ 在此处下载应用程序 dmg 版本](https://github.com/actuallymentor/battery/releases/)
* Option 3: install ONLY the command line interface (see section below)选项 3：仅安装命令行界面（请参阅以下部分）

When installing via brew or dmg, opening the macOS app is required to complete the installation.通过 brew 或 dmg 安装时，需要打开 macOS 应用才能完成安装。

The first time you open the app, it will ask for your administator password so it can install the needed components. Please note that the app:首次打开应用程序时，它会要求您输入管理员密码，以便安装所需的组件。请注意，该应用程序：

* Discharges your battery until it reaches 80%, **even when plugged in**即使已**插入电源，也会**将电池放电直至达到 80%
* Disables charging when your battery is above 80% charged当您的电池电量超过 80% 时禁用充电
* Enables charging when your battery is under 80% charged当您的电池电量低于 80% 时启用充电
* Keeps the limit engaged even after rebooting即使在重新启动后仍保持限制启用
* Keeps the limit engaged even after closing the tray app即使在关闭托盘应用程序后也能保持限制
* Also automatically installs the `battery` command line tool. If you want a custom charging percentage, the CLI is the only way to do that.还会自动安装`电池`命令行工具。如果您想要自定义充电百分比，CLI 是唯一的方法。

Do you have questions, comments, or feature requests? [Open an issue here](https://github.com/actuallymentor/battery/issues) or [Tweet at me](https://twitter.com/actuallymentor).你有问题、意见或功能请求吗？[ 在此处提出问题](https://github.com/actuallymentor/battery/issues)或[向我发推文 ](https://twitter.com/actuallymentor)。

***

## 🖥 Command-line version  🖥 命令行版本

[](#-command-line-version)

> If you don't know what a "command line" is, ignore this section. You don't need it.如果您不知道什么是“命令行”，请忽略此部分。你不需要它。

The GUI app uses a command line tool under the hood. Installing the GUI automatically installs the CLI as well. You can also separately install the CLI.GUI 应用程序在后台使用命令行工具。安装 GUI 也会自动安装 CLI。您也可以单独安装 CLI。

The CLI is used for managing the battery charging status for Apple Silicon Macbooks. Can be used to enable/disable the Macbook from charging the battery when plugged into power.CLI 用于管理 Apple Silicon Macbook 的电池充电状态。可用于在插入电源时启用/禁用 Macbook 为电池充电。

### Installation  安装

[](#installation-1)

One-line installation:  单线安装：

```
curl -s https://raw.githubusercontent.com/actuallymentor/battery/main/setup.sh | bash
```

This will:  这将：

1. Download the precompiled `smc` tool in this repo (built from the [hholtmann/smcFanControl](https://github.com/hholtmann/smcFanControl.git) repository)在此存储库中下载预编译的 `smc` 工具（从 [hholtmann/smcFanControl](https://github.com/hholtmann/smcFanControl.git) 存储库构建）
2. Install `smc` to `/usr/local/bin`将 `smc` 安装到 `/usr/local/bin`
3. Install `battery` to `/usr/local/bin`将`电池`安装到 `/usr/local/bin`

### Usage  用法

[](#usage)

Example usage:  用法示例：

```
# This will enable charging when your battery dips under 80, and disable it when it exceeds 80
battery maintain 80
```

After running a command like `battery charging off` you can verify the change visually by looking at the battery icon:运行命令（如`电池充电关闭 `）后，您可以通过查看电池图标直观地验证更改：

[![Battery not charging](/actuallymentor/battery/raw/main/screenshots/not-charging-screenshot.png)](https://github.com/actuallymentor/battery/blob/main/screenshots/not-charging-screenshot.png)

After running `battery charging on` you will see it change to this:运行`电池充电`后，您会看到它更改为：

[![Battery charging](/actuallymentor/battery/raw/main/screenshots/charging-screenshot.png)](https://github.com/actuallymentor/battery/blob/main/screenshots/charging-screenshot.png)

For help, run `battery` without parameters:如需帮助，请运行`不`带参数的电池：

```
Battery CLI utility v1.0.1

Usage:

  battery status
    output battery SMC status, % and time remaining

  battery maintain LEVEL[1-100,stop]
    reboot-persistent battery level maintenance: turn off charging above, and on below a certain value
    eg: battery maintain 80
    eg: battery maintain stop

  battery charging SETTING[on/off]
    manually set the battery to (not) charge
    eg: battery charging on

  battery adapter SETTING[on/off]
    manually set the adapter to (not) charge even when plugged in
    eg: battery adapter off

  battery calibrate
    calibrate the battery by discharging it to 15%, then recharging it to 100%, and keeping it there for 1 hour

  battery charge LEVEL[1-100]
    charge the battery to a certain percentage, and disable charging when that percentage is reached
    eg: battery charge 90

  battery discharge LEVEL[1-100]
    block power input from the adapter until battery falls to this level
    eg: battery discharge 90

  battery visudo
    ensure you don't need to call battery with sudo
    This is already used in the setup script, so you should't need it.

  battery update
    update the battery utility to the latest version

  battery reinstall
    reinstall the battery utility to the latest version (reruns the installation script)

  battery uninstall
    enable charging, remove the smc tool, and the battery script
```

## FAQ & Troubleshooting  常见问题和故障排除

[](#faq--troubleshooting)

### Why does this exist?  为什么会这样？

[](#why-does-this-exist)

I was looking at the Al Dente software package for battery limiting, but I found the [license too limiting](https://github.com/davidwernhart/AlDente/discussions/558) for a poweruser like myself.我正在查看用于电池限制的 Al Dente 软件包，但我发现它适合像我这样的高级用户。

I would actually have preferred using Al Dente, but decided to create a command-line utility to replace it as a side-project on holiday. A colleague mentioned they would like a GUI, so I spend a few evenings setting up an Electron app. And voila, here we are.实际上，我更喜欢使用 Al Dente，但决定创建一个命令行实用程序来替换它作为假期的副项目。一位同事提到他们想要一个 GUI，所以我花了几个晚上设置一个 Electron 应用程序。瞧，我们来了。

### "It's not working"  “它不起作用”

[](#its-not-working)

If you used one of the earlier versions of the `battery` utility, you may run into [path/permission issues](https://github.com/actuallymentor/battery/issues/8). This is not your fault but mine. To fix it:如果您使用了早期版本的`电池`实用程序之一，则可能会遇到[路径/权限问题 ](https://github.com/actuallymentor/battery/issues/8)。这不是你的错，而是我的错。要解决它，请执行以下作：

```
sudo rm -rf ~/.battery
binfolder=/usr/local/bin
sudo rm -v "$binfolder/smc" "$binfolder/battery"
```

Then reopen the app and things should work. If not, [open an issue](https://github.com/actuallymentor/battery/issues/new/choose) and I'll try to help you fix it.然后重新打开应用程序，一切应该可以正常工作。如果没有，请[打开一个问题 ](https://github.com/actuallymentor/battery/issues/new/choose)，我会尽力帮助您解决它。

### A note to Little Snitch users给 Little Snitch 用户的说明

[](#a-note-to-little-snitch-users)

This tool calls a number of urls, blocking all of them will only break auto-updates.该工具调用多个 URL，阻止所有 URL 只会破坏自动更新。

1. `unidentifiedanalytics.web.app` is a self-made app that tracks app installations, I use it to see if enough people use the app to justify spending time on it. It tracks only how many unique ip addresses open the app.`unidentifiedanalytics.web.app` 是一个跟踪应用程序安装的自制应用程序，我用它来查看是否有足够的人使用该应用程序来证明花时间在它上面是合理的。它仅跟踪打开应用程序的唯一 IP 地址数。
2. `icanhazip.com` is used to see if there is an internet connection`icanhazip.com` 用于查看是否有互联网连接
3. `github.com` is used both as a liveness check and as the source of updates for the underlying command-line utility`github.com` 既用作活跃度检查，也用作底层命令行实用程序的更新源
4. `electronjs.org` hosts the update server for the GUI`electronjs.org` 托管 GUI 的更新服务器

All urls are called over `https` and so not leak data. Unidentified Analytics keeps track of unique ip addresses that open the app, but nothing else.所有 url 都是通过 `https` 调用的，因此不会泄露数据。Unidentified Analytics 会跟踪打开应用程序的唯一 IP 地址，但不会跟踪其他任何地址。

### What distinguishes this project from Optimized Charging?这个项目与优化充电有什么区别？

[](#what-distinguishes-this-project-from-optimized-charging)

Optimized Charging, a feature that is built into MacOS, aims to ensure the longevity and health of your battery. It does so by "delaying charging the battery past 80% when it predicts that you’ll be plugged in for an extended period of time, and aims to charge the battery before you unplug," as explained in [Apple's user guide](https://support.apple.com/en-ca/guide/mac-help/mchlfc3b7879/mac#:~:text=Optimized%20Battery%20Charging%3A%20To%20reduce,the%20battery%20before%20you%20unplug.).优化充电是 MacOS 内置的一项功能，旨在确保电池的使用寿命和健康。正如 [Apple 用户指南](https://support.apple.com/en-ca/guide/mac-help/mchlfc3b7879/mac#:~:text=Optimized%20Battery%20Charging%3A%20To%20reduce,the%20battery%20before%20you%20unplug.)中所解释的那样，它通过“当它预测您将长时间插入电源时将电池充电延迟超过 80%，并旨在在您拔下电源之前为电池充电”来做到这一点。

Additionally, Optimized Charging uses machine learning to decide when the battery should be held at 80%, and when it should become fully charged. If your Mac is not plugged in on a regular schedule, optimized charging will not work as intended.此外，优化充电使用机器学习来决定何时应将电池保持在 80% 以及何时应充满电。如果您的 Mac 没有定期接通电源，优化充电将无法按预期工作。

This app is a similar alternative to Optimized Charging, giving the user control over when it is activated, what percentage the battery should be held at, and more.此应用程序是优化充电的类似替代方案，让用户可以控制何时激活、电池应保持多少百分比等。

### How do I support this project?我该如何支持这个项目？

[](#how-do-i-support-this-project)

Do you know how to code? Open a pull-request for a feature with the label [help wanted (PR welcome)](https://github.com/actuallymentor/battery/labels/help%20wanted%20%28PR%20welcome%29).你知道如何编码吗？打开具有标签 help [wanted （PR welcome）](https://github.com/actuallymentor/battery/labels/help%20wanted%20%28PR%20welcome%29) 的功能的拉取请求。

Do you have an awesome feature idea? [Add a feature request](https://github.com/actuallymentor/battery/issues/new/choose)你有一个很棒的功能创意吗？[ 添加功能请求](https://github.com/actuallymentor/battery/issues/new/choose)

Do you just want to keep me motivated to update the app? [Tweet at me](https://twitter.com/actuallymentor)你只是想让我有动力更新应用程序吗？给[我发推文](https://twitter.com/actuallymentor)


