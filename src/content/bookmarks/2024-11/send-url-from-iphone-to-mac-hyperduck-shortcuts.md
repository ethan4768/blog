---
title: 通过 Hyperduck 和快捷指令将 iPhone URL 发送至 Mac
slug: send-url-from-iphone-to-mac-hyperduck-shortcuts
description: 使用 Hyperduck 和快捷指令，将 iPhone 上的 URL 发送到 Mac，并在默认浏览器中打开。本文详细介绍了如何配置和使用这些工具，满足自动化需求，让你的工作效率更高。
tags: 
  - i-o-stips
  - mac-tips
  - tool
  - automation
  - awesome
pubDatetime: 2024-11-26T18:03:52+08:00
ogImage: https://blog.finengine.tech/posts/%E5%80%9F%E5%8A%A9-hyperduck-%E5%92%8C-shortcuts-raycast-%E4%BB%8E-i-phone-%E5%8F%91%E9%80%81-url-%E5%88%B0-mac.png
---

[原文链接](https://blog.finengine.tech/posts/Send-URL-from-iPhone-to-Mac-with-Hyperduck-and-Shortcuts/)

---

## 需求[](#需求)

当我用手机刷 twitter 或其他网站时，经常会发现一些有趣的内容，但有时在手机上不太方便深入研究，于是便借助各项工具暂存以便从 Mac 上进行查看。但经常发生的情况是，要不是在收藏夹吃灰，要不就是需要每次手动打开页面并手动删除暂存内容。 我自己使用过的方法有：

1. Pocket
2. 微信收藏、微信文件传输助手
3. 各类笔记工具：Notes、Obsidian
4. Safari 阅读列表
5. iCloud 标签页

这些方法并不如意，我的诉求有：

1. 手机分享的页面能够自动在 mac 上打开页面，避免在收藏夹或笔记中吃灰
2. 能够对某些页面 URL 进行一些处理，比如将 x.com 转为 twitter.com，删除跟踪
3. 可以有个存档

无意中发现一个 app [Hyperduck](https://sindresorhus.com/hyperduck) 比较符合需求，是著名的 Sindre Sorhus 开发，他是 github 上 star 数第一的个人，奉行一个 app 专注于一件事并做好它。关于作者的事迹很多，大家有兴趣可以自行查找，个人认为是一个非常专注、热爱分享、懂得拒绝的人。关于 Hyperduck 的使用，我进行了咨询，作者很快给出了建议，下面介绍下 Hyperduck 并附上我的方案。

## Hyperduck 介绍[](#hyperduck-介绍)

> Send links from your iOS/visionOS devices to your Mac

Hyperduck 将链接从 iOS 设备上发送到 Mac，并直接在浏览器中打开。 需要注意的是，Hyperduck 使用 iCloud 进行同步，所以速度和稳定性主要取决于 iCloud，从我在国内的体验上看，大约会延迟 1 \~ 5 秒。

### 配置[](#配置)

1. 分别在 iPhone/iPad 和 Mac 上下载 hyperduck
2. 在 iOS 系统上，Settings › Apple ID › iCloud › Apps Using iCloud，将 Hyperduck 开启
3. 在 macOS 系统上，我没有做任何操作即可使用。官方设置中，System Settings › Apple ID › iCloud › iCloud Drive › Apps syncing to iCloud Drive，将 Hyperduck 开启，但我没有找到 Hyperduck 这一项。
4. 有问题可以查看 [Hyperduck Troubleshooting](https://sindresorhus.com/hyperduck#troubleshooting) 解决。

### 基本功能[](#基本功能)

设置完成后，然后在 Safari、twitter 或其他网页的分享中，可以看到“Send to Mac”选项，点击后就可以在 Mac 的默认浏览器中打开此页面，非常方便。

![](https://images.finengine.tech/2024/02/2c318c099e1b7f45f6f624f2491fcca8.jpeg)

如果希望能够控制哪些 URL 可以使用特定浏览器或 APP 打开，可以使用 Sindre Sorhus 的另一个 app [Velja](https://sindresorhus.com/velja)，这个 app 可以根据 URL 和规则判断使用哪个浏览器或 APP 打开页面。

除了直接在分享中进行“Send to Mac”外，Hyperduck 还在快捷指令中增加了两个选项，“Send URLs to Mac”和“Run Shortcut on Mac”，可以在一定程度上从 iOS 设备远程控制 Mac。

### 快捷指令-Send URLs to Mac[](#快捷指令-send-urls-to-mac)

这个操作可以直接将一个 URL 发送到 Mac 并自动打开，还可以调用 Mac 上 Raycast 提供的 [deeplink](https://manual.raycast.com/deeplinks)。 使用方法，在 iOS 设备上新建快捷指令，选择“Send URLs to Mac”，然后将 `URLs` 部分替换为 Raycast deeplink 即可。在 Raycast 中可以很方便获取 deeplink。

![](https://images.finengine.tech/2024/02/213e7246b28f97427651d8aa7c35c615.jpeg)

比如：

1. 撒花，本质上是在 Raycast 中执行 `confetti` 指令。

   * Raycast deeplink：`raycast://confetti`
   * Shortcut 示例：[撒花！via Raycast deeplink](https://www.icloud.com/shortcuts/b973981d8f7a42dba3b9bc0dfca421da)

2. 远程锁定 Mac，本质上是在 Raycast 中执行 `Lock Screen` 指令。

   * Raycast deeplink：`raycast://extensions/raycast/system/lock-screen`
   * Shortcut 示例：[Lock Mac Screen(via Raycast deeplink)](https://www.icloud.com/shortcuts/e0042e8e013b428b989a16bcdeee1263)

### 快捷指令-Run Shortcut on Mac[](#快捷指令-run-shortcut-on-mac)

这个操作可以远程执行 Mac 上的快捷指令。 使用方法，在 iOS 设备上新建快捷指令，选择“Run Shortcut on Mac”，然后将 `Shortcut` 部分替换为 Mac 上的快捷指令名称即可。所以要完成一个动作，需要先在 Mac 上设置好要执行的快捷指令，然后在 iOS 设备上新建快捷指令。

比如：

1. 远程锁定 Mac，快捷指令同样可以完成此功能

   * Mac Shortcut：[锁定屏幕](https://www.icloud.com/shortcuts/6887c50a26154ca9be06c9ed1a7736c0)
   * iOS Shortcut：[Lock Mac Screen(via Shortcut)](https://www.icloud.com/shortcuts/d72fc7791b82426a8d8b99e5f1e8397e)

2. 远程开启屏保

   * Mac Shorcut：[启动屏保](https://www.icloud.com/shortcuts/61e38da477154790bf7ad061340bb7b1)
   * iOS Shortcut：[Open Screen Saver](https://www.icloud.com/shortcuts/f34f4a0a560e4d3f9e4c4e0044bd2e22)

初次执行，可能会遇到一些权限申请的情况，始终允许即可。

![](https://images.finengine.tech/2024/02/1418b96a800421d1b68829bba461446e.jpeg)

## 最终方案[](#最终方案)

使用 Hyperduck 的基础功能就可以实现第一个诉求，自动在 mac 上打开分享的页面。但想要实现第 2 个诉求，我曾寄希望于 Sindre Sorhus 的另一个 app [Velja](https://sindresorhus.com/velja)，但它目前不支持自行对 URL 进行转换。邮件咨询过作者后，作者给的答复是：

> A URL transform feature is coming to Velja in the next few months.

并建议可以考虑使用 Hyperduck 提供的“Run Shortcut on Mac”快捷指令来实现。

在经过一番折腾后，最终采用了快捷指令的方案。原因 Raycast deeplink 需要自己写插件，而且不完全通用 (有些人可能没有安装 Raycast)。

最终方案如下：

第一步，在 Mac 上创建快捷指令 [Open URL](https://www.icloud.com/shortcuts/2227f8d7a9024ea1aa58859a7dc9a321)，完成以下功能

1. 接收传入的 URL
2. 对 URL 进行处理，比如将 x.com 转为 twitter.com
3. 将 URL 追加到 Apple Notes 指定的备忘录中
4. 使用浏览器打开 URL

![](https://images.finengine.tech/2024/02/0b4f1b905eac8940e1c49384e3a88152.jpeg)

可以根据自己的需要进行修改，比如修改追加的备忘录，URL 转换等。

第二步，在 iOS 设备上创建快捷指令 [Open on Mac](https://www.icloud.com/shortcuts/74e33923ffee4f20acfcf1a874a98431)，完成以下功能

1. 从共享表单中获取 URL
2. Run “Open URL” Shortcut on Mac

第三步，最后调整下分享中“Open on Mac”顺序到自己舒服的位置。

![](https://images.finengine.tech/2024/02/db787776a703dd762074196f33b382b3.jpeg)

如此就完成了！🎉🎉

## 参考内容[](#参考内容)

1. [Hyperduck — Sindre Sorhus](https://sindresorhus.com/hyperduck) Hyperduck 官网
2. [Automation April：Hyperduck Leverages the Power of URL Schemes to Control Your Mac from an iPhone or iPad - MacStories](https://www.macstories.net/reviews/automation-april-hyperduck-leverages-the-power-of-url-schemes-to-control-your-mac-from-an-iphone-or-ipad/) MacStroies 网站对 Hyperduck 的介绍
3. [Raycast Deeplinks](https://manual.raycast.com/deeplinks)


