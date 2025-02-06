---
title: "MediaGo：跨平台视频提取工具，支持流媒体和B站下载"
slug: mediago-video-extraction-tool
description: |
  MediaGo是一个支持视频下载的跨平台工具，能轻松提取流媒体内容、m3u8文件和B站视频，同时提供Windows和Mac桌面客户端。此工具还支持批量下载和Docker部署，极大地方便用户在PC及移动设备之间切换观看。
tags: 
  - video
  - tool
  - download
pubDatetime: 2025-02-06T10:02:06+08:00
ogImage: https://opengraph.githubassets.com/f234e3356b46bc93710167ea4677656ca74c2fce7a294af8476562e724dba211/caorushizi/mediago
---

[原文链接](https://github.com/caorushizi/mediago)

---

# MediaGo

[](#mediago)

[快速开始](https://downloader.caorushizi.cn/guides.html?form=github)  •  [官网](https://downloader.caorushizi.cn?form=github)  •  [文档](https://downloader.caorushizi.cn/documents.html?form=github)  •  [Discussions](https://github.com/caorushizi/mediago/discussions)\


[English](https://github.com/caorushizi/mediago/blob/master/README.en.md)   •   [日本語](https://github.com/caorushizi/mediago/blob/master/README.jp.md)

[![GitHub Downloads (all assets, all releases)](https://camo.githubusercontent.com/36cc46595d8a868bd561a1816b360719e8be484340a038e76b3c4dcf7930562c/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f63616f72757368697a692f6d65646961676f2f746f74616c)](https://camo.githubusercontent.com/36cc46595d8a868bd561a1816b360719e8be484340a038e76b3c4dcf7930562c/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f63616f72757368697a692f6d65646961676f2f746f74616c)[![GitHub Downloads (all assets, latest release)](https://camo.githubusercontent.com/a9387fe1903728baa8e1e5d6808147e8a98fc8dd5e38d75bcfd4db9b5ecc85c1/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f63616f72757368697a692f6d65646961676f2f6c61746573742f746f74616c)](https://camo.githubusercontent.com/a9387fe1903728baa8e1e5d6808147e8a98fc8dd5e38d75bcfd4db9b5ecc85c1/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f63616f72757368697a692f6d65646961676f2f6c61746573742f746f74616c)[![GitHub Repo stars](https://camo.githubusercontent.com/f46403966ac2432bdd7a2670228b097581393ee191a5fd7f68685295ae958fe0/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f63616f72757368697a692f6d65646961676f)](https://camo.githubusercontent.com/f46403966ac2432bdd7a2670228b097581393ee191a5fd7f68685295ae958fe0/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f63616f72757368697a692f6d65646961676f)[![GitHub forks](https://camo.githubusercontent.com/b4b795c8ae5165dc8a4b187ec46fcb29dc08dfbc98a31faeb3ce8281cb045457/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f63616f72757368697a692f6d65646961676f)](https://camo.githubusercontent.com/b4b795c8ae5165dc8a4b187ec46fcb29dc08dfbc98a31faeb3ce8281cb045457/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f63616f72757368697a692f6d65646961676f)\
[![caorushizi%2Fmediago | Trendshift](https://camo.githubusercontent.com/40c78f37b1a4d23d3eac630e9bed97ec7f99c6bd98f9d915f95cd5ed1e71ddd7/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7265706f7369746f726965732f3131303833)](https://trendshift.io/repositories/11083)

***

## Intro

[](#intro)

本项目支持 m3u8 视频在线提取工具 流媒体下载 m3u8 下载。

* **✅  无需抓包**： 使用软件自带浏览器可以轻松嗅探网页中的视频资源，通过嗅探到的资源列表选择自己想要下载的资源，简单快速。
* **📱  移动播放**： 可以轻松无缝的在 PC 和移动设备之前切换，下载完成后即可使用手机观看视频。
* **⚡️  批量下载**： 支持同时下载多个视频和直播资源，高速带宽不闲置。
* **🎉  支持 docker 部署**： 支持 docker 部署 web 端，方便快捷。

## Quickstart

[](#quickstart)

运行代码需要 node 和 pnpm，node 需要在官网下载安装，pnpm 可以通过`npm i -g pnpm`安装。

## 运行代码

[](#运行代码)

```
# 代码下载
git clone https://github.com/caorushizi/mediago.git

# 安装依赖
pnpm i

# 开发环境
pnpm dev

# 打包运行
pnpm release

# 构建 docker 镜像
docker buildx build -t caorushizi/mediago:latest .

# docker 启动
docker run -d --name mediago -p 8899:8899 -v /root/mediago:/root/mediago registry.cn-beijing.aliyuncs.com/caorushizi/mediago
```

## Releases

[](#releases)

### v3.0.0 (2024.10.7 发布)

[](#v300-2024107-发布)

#### 软件下载

[](#软件下载)

* [【mediago】 windows(安装版) v3.0.0](https://github.com/caorushizi/mediago/releases/download/v3.0.0/mediago-setup-win32-x64-3.0.0.exe)
* [【mediago】 windows(便携版) v3.0.0](https://github.com/caorushizi/mediago/releases/download/v3.0.0/mediago-portable-win32-x64-3.0.0.exe)
* [【mediago】 macos arm64（apple 芯片） v3.0.0](https://github.com/caorushizi/mediago/releases/download/v3.0.0/mediago-setup-darwin-arm64-3.0.0.dmg)
* [【mediago】 macos x64（intel 芯片） v3.0.0](https://github.com/caorushizi/mediago/releases/download/v3.0.0/mediago-setup-darwin-x64-3.0.0.dmg)
* [【mediago】 linux v3.0.0](https://github.com/caorushizi/mediago/releases/download/v3.0.0/mediago-setup-linux-amd64-3.0.0.deb)
* 【mediago】 docker v3.0 `docker run -d --name mediago -p 8899:8899 -v /root/mediago:/root/mediago registry.cn-beijing.aliyuncs.com/caorushizi/mediago:v3.0.0`

### docker 宝塔面板一键部署（推荐）

[](#docker-宝塔面板一键部署推荐)

1. 安装宝塔面板，前往 [宝塔面板](https://www.bt.cn/new/download.html?r=dk_mediago) 官网，选择正式版的脚本下载安装

2. 安装后登录宝塔面板，在菜单栏中点击 `Docker`，首次进入会提示安装`Docker`服务，点击立即安装，按提示完成安装

3. 安装完成后在应用商店中找到`MediaGo`，点击安装，配置域名等基本信息即可完成安装

### 软件截图

[](#软件截图)

[![首页](https://camo.githubusercontent.com/078ad757f064eeb3e383e617509dca55e5dd035e72838670a53a9b1fe70fd385/68747470733a2f2f7374617469632e7a6979696e672e736974652f696d616765732f686f6d652e706e67)](https://camo.githubusercontent.com/078ad757f064eeb3e383e617509dca55e5dd035e72838670a53a9b1fe70fd385/68747470733a2f2f7374617469632e7a6979696e672e736974652f696d616765732f686f6d652e706e67)

### 重要更新

[](#重要更新)

* 支持 docker 部署 web 端
* 更新桌面端 UI

### 更新日志

[](#更新日志)

* 更新桌面端 UI
* 支持 docker 部署 web 端
* 新增视频播放，支持桌面端和移动端播放
* 修复 mac 打开无法展示界面的问题
* 优化了批量下载的交互
* 添加了 windows 的便携版（免安装哦）
* 优化了下载列表，支持页面中多个视频的嗅探
* 支持收藏列表手动导入导出
* 支持首页下载列表导出
* 优化了【新建下载】表单的交互逻辑
* 支持 UrlScheme 打开应用，并添加下载任务
* 修复了一些 bug 并提升用户体验

## 软件截图

[](#软件截图-1)

[![首页](https://camo.githubusercontent.com/078ad757f064eeb3e383e617509dca55e5dd035e72838670a53a9b1fe70fd385/68747470733a2f2f7374617469632e7a6979696e672e736974652f696d616765732f686f6d652e706e67)](https://camo.githubusercontent.com/078ad757f064eeb3e383e617509dca55e5dd035e72838670a53a9b1fe70fd385/68747470733a2f2f7374617469632e7a6979696e672e736974652f696d616765732f686f6d652e706e67)

[![首页-dark](https://camo.githubusercontent.com/a73c7b0c6c2ba9d9e9437e03bc0423e12bc0c11949530736adcd6cb89dd603e8/68747470733a2f2f7374617469632e7a6979696e672e736974652f696d616765732f686f6d652d6461726b2e706e67)](https://camo.githubusercontent.com/a73c7b0c6c2ba9d9e9437e03bc0423e12bc0c11949530736adcd6cb89dd603e8/68747470733a2f2f7374617469632e7a6979696e672e736974652f696d616765732f686f6d652d6461726b2e706e67)

[![设置页面](https://camo.githubusercontent.com/b41dc65efff4708c1f6efef7e84b8398086f1dcac043633c73710930332be0ef/68747470733a2f2f7374617469632e7a6979696e672e736974652f696d616765732f73657474696e67732e706e67)](https://camo.githubusercontent.com/b41dc65efff4708c1f6efef7e84b8398086f1dcac043633c73710930332be0ef/68747470733a2f2f7374617469632e7a6979696e672e736974652f696d616765732f73657474696e67732e706e67)

[![资源提取](https://camo.githubusercontent.com/99673482cce444711cb7298d587e0da22a09110ccc14c509827750a7208a2f88/68747470733a2f2f7374617469632e7a6979696e672e736974652f696d616765732f62726f777365722e706e67)](https://camo.githubusercontent.com/99673482cce444711cb7298d587e0da22a09110ccc14c509827750a7208a2f88/68747470733a2f2f7374617469632e7a6979696e672e736974652f696d616765732f62726f777365722e706e67)

## 技术栈

[](#技术栈)

* react <https://react.dev/>
* electron <https://www.electronjs.org>
* koa <https://koajs.com>
* vite <https://cn.vitejs.dev>
* antd <https://ant.design>
* tailwindcss <https://tailwindcss.com>
* shadcn <https://ui.shadcn.com/>
* inversify <https://inversify.io>
* typeorm <https://typeorm.io>

## 鸣谢

[](#鸣谢)

* N\_m2u8DL-CLI 来自于 <https://github.com/nilaoda/N_m3u8DL-CLI>
* N\_m3u8DL-RE 来自于 <https://github.com/nilaoda/N_m3u8DL-RE>
* mediago 来自于 <https://github.com/caorushizi/hls-downloader>


