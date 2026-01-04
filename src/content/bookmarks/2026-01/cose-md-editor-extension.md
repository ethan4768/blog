---
title: "doocs/cose: MD 编辑器的浏览器扩展，一键将文章同步到多个内容平台"
slug: cose-md-editor-extension
description: |
  doocs/cose 是为 doocs/md Markdown 编辑器设计的浏览器扩展，支持一键将文章同步到多个内容平台。插件完全本地运行，不收集、不存储任何用户信息，使用者可在安装扩展后通过 md.doocs.org 或本地开发环境实现多平台分发。已支持的平台包括微信公众号、今日头条、知乎、博客园、百家号、网易号、CSDN、掘金、思否、开源中国、51CTO、InfoQ、简书、腾讯云等。主要特性包括编辑一次即可同步至多平台、自动检测登录状态、同步页签分组管理，以及在微信等平台保持渲染样式并自动保存为草稿。开发者模式测试步骤也提供，若需新增平台或改进同步精准度，可提交 Issue 或 PR。
tags: 
  - opensource
  - dev
  - tool
  - design
  - selfhosted
pubDatetime: 2026-01-04T17:10:48+08:00
ogImage: 
---

[原文链接](https://github.com/doocs/cose)

---

![COSE](/doocs/cose/raw/main/assets/headerLight.svg)

***C**reate **O**nce **S**ync **E**verywhere*

[![License](https://camo.githubusercontent.com/7013272bd27ece47364536a221edb554cd69683b68a46fc0ee96881174c4214c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d626c75652e737667)](https://github.com/doocs/cose/blob/main/LICENSE) [![Chrome Web Store](https://camo.githubusercontent.com/aa0ed8f413c51f11339ba57bf71b8fff16959c0e180ae5b2e324a0e139bc39e2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f496e7374616c6c2d4368726f6d6525323057656225323053746f72652d3432383546343f6c6f676f3d676f6f676c656368726f6d65266c6f676f436f6c6f723d7768697465)](https://chromewebstore.google.com/detail/ilhikcdphhpjofhlnbojifbihhfmmhfk) [![YouTube](https://camo.githubusercontent.com/ecea09e9fbead7e25bf3a79d4ea28a3c750fcf79ffe8e1ca46ef795b4f42e0ad/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f566964656f2d596f75547562652d4646303030303f6c6f676f3d796f7574756265266c6f676f436f6c6f723d7768697465)](https://www.youtube.com/watch?v=KTskiA8Xaj4) [![Bilibili](https://camo.githubusercontent.com/f7641b3fbb0c4cae64f7231b004bcc94d2279f1f7689a9e1fbc9d7c072f94419/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f566964656f2d42696c6962696c692d3030413144363f6c6f676f3d62696c6962696c69266c6f676f436f6c6f723d7768697465)](https://www.bilibili.com/video/BV1ZxqnB1E2C/)

配合 [doocs/md](https://github.com/doocs/md) Markdown 编辑器使用的浏览器扩展，支持一键将文章同步到多个内容平台。

> 本插件完全本地运行，不收集、不存储任何用户信息。**如需添加更多平台或改善同步准确度，欢迎提 [Issue](https://github.com/doocs/cose/issues) 或 [PR](https://github.com/doocs/cose/pulls)**。

## 使用方法

[](#使用方法)

> 点击观看视频：[![Bilibili](https://camo.githubusercontent.com/f7641b3fbb0c4cae64f7231b004bcc94d2279f1f7689a9e1fbc9d7c072f94419/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f566964656f2d42696c6962696c692d3030413144363f6c6f676f3d62696c6962696c69266c6f676f436f6c6f723d7768697465)](https://www.bilibili.com/video/BV1ZxqnB1E2C/) [![YouTube](https://camo.githubusercontent.com/ecea09e9fbead7e25bf3a79d4ea28a3c750fcf79ffe8e1ca46ef795b4f42e0ad/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f566964656f2d596f75547562652d4646303030303f6c6f676f3d796f7574756265266c6f676f436f6c6f723d7768697465)](https://www.youtube.com/watch?v=KTskiA8Xaj4)

1. 先点击安装扩展 [![Chrome Web Store](https://camo.githubusercontent.com/aa0ed8f413c51f11339ba57bf71b8fff16959c0e180ae5b2e324a0e139bc39e2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f496e7374616c6c2d4368726f6d6525323057656225323053746f72652d3432383546343f6c6f676f3d676f6f676c656368726f6d65266c6f676f436f6c6f723d7768697465)](https://chromewebstore.google.com/detail/ilhikcdphhpjofhlnbojifbihhfmmhfk) 然后打开 [md.doocs.org](https://md.doocs.org) 或本地开发环境
2. 编辑 Markdown 内容
3. 点击顶部的 **发布** 按钮
4. 在弹出的对话框中选择要同步的平台
5. 点击 **确定** 开始同步

## 特性

[](#特性)

* 编辑一次，同步到多个平台
* 自动检测各平台登录状态
* 同步的标签页自动归入分组，便于管理
* 微信公众号同步时完整保留渲染样式并自动保存为草稿

## 已支持的平台

[](#已支持的平台)

* 微信公众号
* 今日头条
* 知乎
* 博客园
* 百家号
* 网易号
* CSDN
* 掘金
* 思否
* 开源中国
* 51CTO
* InfoQ
* 简书
* 腾讯云

更多想要添加的平台欢迎提 [Issue](https://github.com/doocs/cose/issues) ！

## 开发者模式测试

[](#开发者模式测试)

1. 克隆或下载本项目
2. 打开 Chrome 浏览器，进入 `chrome://extensions/`
3. 开启右上角的 **开发者模式**
4. 点击 **加载已解压的扩展程序**
5. 选择 `cose` 目录


