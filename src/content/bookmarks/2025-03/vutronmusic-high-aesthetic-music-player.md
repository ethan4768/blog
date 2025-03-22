---
title: "VutronMusic：高颜值的第三方网易云音乐播放器"
slug: vutronmusic-high-aesthetic-music-player
description: |
  VutronMusic是一个高颜值的第三方网易云播放器，支持流媒体音乐及本地播放，功能包括离线歌单、桌面歌词显示等，兼容Windows、macOS和Linux系统。使用Vue3、TypeScript等技术构建，专为音乐爱好者而生。
tags: 
  - music
  - opensource
pubDatetime: 2025-03-22T19:31:17+08:00
ogImage: https://opengraph.githubassets.com/783fad042332f06e8715854ac33ae710a4a5511497f84654934297bbd3b6e61b/stark81/VutronMusic
---

[原文链接](https://github.com/stark81/VutronMusic)

---

[![Logo](/stark81/VutronMusic/raw/main/buildAssets/icons/icon.png)](https://github.com/stark81/VutronMusic)

## VutronMusic

[](#vutronmusic)

高颜值的第三方网易云播放器

[![LocalMusic](/stark81/VutronMusic/raw/main/images/localMusic.jpg)](https://github.com/stark81/VutronMusic)

## 说明

[](#说明)

* 本项目为本人个人项目，仅用于个人学习研究，请勿用于商业用途。
* 由于本人对better-sqlite3不是那么熟悉，现在即便是安装依赖文件后自动运行post-install，也会导致better-sqlite3没有被准确复制，从而使得安装依赖文件后的第一次运行/打包失败，此时只需再次运行项目，即可正常使&#x7528;**&#x20;(此时， dist-native目录下会出现better-sqlite3文件)**。
* 本项目大部份界面和功能参考 [YesPlayMusic](https://github.com/qier222/YesPlayMusic)，侧边导航栏设计参考"方格音乐"，本地音乐top部分的信息统计参考 [NSMusicS](https://github.com/Super-Badmen-Viper/NSMusicS)。
* 为了减少内存使用，本项目使用虚拟列表来显示绝大部分的列表内容，包括：歌曲列表(单列、固定高度)、评论列表(单列、不固定高度、数量会增减)、探索页面的歌单、歌手列表(多列、不固定高度、数量会增减)等，因此部分列表滚动时可能会发生跳动、闪烁等现象，这些问题还在研究和处理。

## 特点

[](#特点)

* ⚡️ 使用 Vue3 + ts + pinia + fastify + better-sqlite3 进行开发；
* ⚡️ 支持本地歌曲、离线歌单功能，本地歌曲支持读取内嵌封面、内嵌歌词功能，支持线上信息匹配(使用的是匹配接口，非搜索接口)；
* ⚡️ 支持Mac状态栏歌词、TouchBar歌词等；Linux下可通过[media-controls](https://github.com/stark81/media-controls)插件将歌词显示在TopBar里；
* ⚡️ 支持云盘、歌曲评论等功能；

## 配置开发环境

[](#配置开发环境)

```
# 安装依赖，建议使用node21 + python3.9,其他的python版本可能会导致依赖安装失败的问题；
yarn install

# arm64的Mac用户
  使用苹果M系列芯片的用户，在安装依赖前先把buildAssets/builder/config.js文件中的mac.target.arch的值改为['arm64']，然后重新安装依赖即可；

# 运行
yarn run dev（开发）
yarn run build（构建）
```

## 开源许可

[](#开源许可)

本项目仅供个人学习研究使用，禁止用于商业及非法用途。

基于 [MIT license](https://opensource.org/licenses/MIT) 许可进行开源。

## 截图

[](#截图)

[![home-screenShot](/stark81/VutronMusic/raw/main/images/home.jpg)](https://github.com/stark81/VutronMusic/blob/main/images/home.jpg) [![explore-screenShot](/stark81/VutronMusic/raw/main/images/explore.jpg)](https://github.com/stark81/VutronMusic/blob/main/images/explore.jpg) [![library-screenShot](/stark81/VutronMusic/raw/main/images/library.jpg)](https://github.com/stark81/VutronMusic/blob/main/images/library.jpg) [![likepage-screenShot](/stark81/VutronMusic/raw/main/images/like-page.jpg)](https://github.com/stark81/VutronMusic/blob/main/images/like-page.jpg) [![local-music-screenShot](/stark81/VutronMusic/raw/main/images/local-music.jpg)](https://github.com/stark81/VutronMusic/blob/main/images/local-music.jpg) [![playlist-screenShot](/stark81/VutronMusic/raw/main/images/playlists.jpg)](https://github.com/stark81/VutronMusic/blob/main/images/playlists.jpg) [![playpage-screenShot](/stark81/VutronMusic/raw/main/images/play-page.jpg)](https://github.com/stark81/VutronMusic/blob/main/images/play-page.jpg) [![comment-screenShot](/stark81/VutronMusic/raw/main/images/comment-page.jpg)](https://github.com/stark81/VutronMusic/blob/main/images/comment-page.jpg) [![search-screenShot](/stark81/VutronMusic/raw/main/images/search-lyric.jpg)](https://github.com/stark81/VutronMusic/blob/main/images/search-lyric.jpg) [![user-screenShot](/stark81/VutronMusic/raw/main/images/user.jpg)](https://github.com/stark81/VutronMusic/blob/main/images/user.jpg) [![mv-screenShot](/stark81/VutronMusic/raw/main/images/mv.jpg)](https://github.com/stark81/VutronMusic/blob/main/images/mv.jpg) [![tray-lyric-screenShot](/stark81/VutronMusic/raw/main/images/tray-TouchBar-lyric.jpg)](https://github.com/stark81/VutronMusic/blob/main/images/tray-TouchBar-lyric.jpg) [![media-controls-screenShot](/stark81/VutronMusic/raw/main/images/media-control-lyric.png)](https://github.com/stark81/VutronMusic/blob/main/images/media-control-lyric.png)


