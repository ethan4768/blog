---
title: "MusicBrainz Picard: 跨平台音乐标记工具，支持多种音频格式"
slug: musicbrainz-picard-audio-tagging-tool
description: |
  MusicBrainz Picard 是一款跨平台的音频标记应用程序，支持多种音频格式（如 MP3、FLAC、OGG 等），使用 AcoustID 音频指纹来识别音乐，允许高效的 CD 查找及标签处理。该工具开源，并基于社区维护的 MusicBrainz 数据库。
tags: 
  - opensource
  - tool
  - music
pubDatetime: 2025-05-26T14:54:51+08:00
ogImage: 
---

[原文链接](https://github.com/metabrainz/picard)

---

# MusicBrainz Picard

[](#musicbrainz-picard)

[![Github Actions Status](https://github.com/metabrainz/picard/workflows/Run%20tests/badge.svg)](https://github.com/metabrainz/picard/workflows/Run%20tests/badge.svg) [![Codacy Grade](https://camo.githubusercontent.com/2af133bb20b00b1429e0be6d08ba29dceb3cb23a1c9d561ec88012013c35b12a/68747470733a2f2f696d672e736869656c64732e696f2f636f646163792f67726164652f34646361626630613133656434623237623361333831636539626139366563632f6d61737465722e7376673f7374796c653d666c61742d737175617265266c6162656c3d436f64616379)](https://app.codacy.com/gh/metabrainz/picard)

[MusicBrainz Picard](https://picard.musicbrainz.org) is a cross-platform (Linux, macOS, Windows) audio tagging application. It is the official [MusicBrainz](https://musicbrainz.org) tagger.[MusicBrainz Picard](https://picard.musicbrainz.org) 是一款跨平台（Linux、macOS、Windows）的音频标记应用程序。它是 [MusicBrainz](https://musicbrainz.org) 官方的标记器。

Picard supports the majority of audio file formats, is capable of using audio fingerprints ([AcoustIDs](https://musicbrainz.org/doc/AcoustID)), performing CD lookups and [disc ID](https://musicbrainz.org/doc/Disc_ID) submissions, and it has excellent Unicode support. Additionally, there are several plugins available that extend Picard's features.Picard 支持大多数音频文件格式，能够使用音频指纹 ( [AcoustID](https://musicbrainz.org/doc/AcoustID) ) 进行 CD 查找和[光盘 ID](https://musicbrainz.org/doc/Disc_ID) 提交，并且对 Unicode 的支持非常出色。此外，还有多个插件可用于扩展 Picard 的功能。

When tagging files, Picard uses an album-oriented approach. This approach allows it to utilize the MusicBrainz data as effectively as possible and correctly tag your music. For more information, [see the illustrated quick start guide to tagging](https://picard.musicbrainz.org/quick-start/) and the [documentation](https://picard-docs.musicbrainz.org/).Picard 在标记文件时采用面向专辑的方法。这种方法使其能够尽可能高效地利用 MusicBrainz 数据，并正确地标记您的音乐。有关更多信息，[ 请参阅图文并茂的标记快速入门指南](https://picard.musicbrainz.org/quick-start/)和[文档 ](https://picard-docs.musicbrainz.org/)。

## Features  特征

[](#features)

* **Multiple formats:** Picard supports all popular music formats, including MP3, FLAC, OGG, M4A, WMA, WAV, and more.**多种格式：** Picard 支持所有流行的音乐格式，包括 MP3、FLAC、OGG、M4A、WMA、WAV 等。
* **AcoustID:** Picard uses [AcoustID](https://musicbrainz.org/doc/AcoustID) audio fingerprints, allowing files to be identified by the actual music, even if they have no metadata.**AcoustID：** Picard 使用 [AcoustID](https://musicbrainz.org/doc/AcoustID) 音频指纹，允许通过实际的 音乐，即使它们没有元数据。
* **Comprehensive database:** Picard uses the open and community-maintained [MusicBrainz database](https://musicbrainz.org) to provide accurate information about millions of music releases.**综合数据库：** Picard 使用开放且由社区维护的 [MusicBrainz 数据库](https://musicbrainz.org) 提供有关数百万首音乐发行的准确信息。
* **CD lookups:** Picard can lookup entire music CDs with a click.**CD 查找：** Picard 只需单击即可查找整个音乐 CD。
* **Plugin support:** If you need a particular feature, you can choose from a selection of [available plugins](https://picard.musicbrainz.org/plugins/) or [write your own](https://picard-docs.musicbrainz.org/en/extending/plugins.html).**插件支持：** 如果您需要特定功能，您可以从[可用的插件](https://picard.musicbrainz.org/plugins/)中进行选择，或者 [写你自己的 ](https://picard-docs.musicbrainz.org/en/extending/plugins.html)。
* **Scripting:** A flexible and powerful, yet easy to learn, scripting language allows you to exactly specify how your music files will be named and how the tags will look like.**脚本：** 一种灵活、强大且易于学习的脚本语言，允许您精确指定音乐文件的命名方式以及标签的外观。
* **Cover Art:** Picard can find and download the correct cover art for your albums.**封面艺术：** Picard 可以找到并下载适合您专辑的正确封面艺术。
* **Open Source:** Picard is licensed under the [GNU General Public License 2.0](https://github.com/metabrainz/picard/blob/master/COPYING.txt) or later, and is hosted on GitHub where it is actively developed.**开源：** Picard 已获得以下许可 [GNU 通用公共许可证 2.0](https://github.com/metabrainz/picard/blob/master/COPYING.txt) 或更高版本，并托管在 GitHub 上，并积极 发达。

## Installation  安装

[](#installation)

Binary downloads are available on the [Picard download page](https://picard.musicbrainz.org/downloads/).二进制下载可在 [Picard 下载页面](https://picard.musicbrainz.org/downloads/)获取。

[INSTALL.md has instructions on building this codebase.INSTALL.md 包含有关构建此代码库的说明。](https://github.com/metabrainz/picard/blob/master/INSTALL.md)

## Support and issue reporting支持和问题报告

[](#support-and-issue-reporting)

Please report all bugs and feature requests in the [MusicBrainz issue tracker](https://tickets.metabrainz.org/browse/PICARD). If you need support in using Picard please read the [documentation](https://picard-docs.musicbrainz.org/) first and have a look at the [MusicBrainz community forums](https://community.metabrainz.org/c/picard).请在 [MusicBrainz 问题跟踪器](https://tickets.metabrainz.org/browse/PICARD)中报告所有错误和功能请求。如果您在使用 Picard 时需要支持，请先阅读[文档 ](https://picard-docs.musicbrainz.org/)，然后访问 [MusicBrainz 社区论坛 ](https://community.metabrainz.org/c/picard)。

## Trivia  琐事

[](#trivia)

Picard is named after [Captain Jean-Luc Picard](https://en.wikipedia.org/wiki/Jean-Luc_Picard) from the TV series [Star Trek: The Next Generation](https://en.wikipedia.org/wiki/Star_Trek:_The_Next_Generation).皮卡德 (Picard) 的名字取自电视剧 [《星际迷航：下一代》](https://en.wikipedia.org/wiki/Star_Trek:_The_Next_Generation) 中的[让-吕克·皮卡德 (Jean-Luc Picard) 舰长 ](https://en.wikipedia.org/wiki/Jean-Luc_Picard)。


