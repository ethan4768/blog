---
title: "Polaris: 一款自托管的音乐流媒体应用，随时随地享受音乐"
slug: self-hosted-music-streaming-with-polaris
description: |
  Polaris是一款自托管的音乐流媒体服务器，允许用户在任何计算机或移动设备上享受自己的音乐库。作为开源软件，Polaris具备卓越性能，支持大容量（超过100,000首曲目）的音乐收藏，同时提供易于安装和维护的用户界面。
tags: 
  - music
  - opensource
  - streaming
  - tool
pubDatetime: 2025-02-07T09:57:19+08:00
ogImage: https://repository-images.githubusercontent.com/65657180/384fcc71-44f4-4099-9131-c2c0ffad7b0c
---

[原文链接](https://github.com/agersant/polaris?tab=readme-ov-file)

---

# [![](/agersant/polaris/raw/master/res/readme/logo.png?raw=true)](https://github.com/agersant/polaris/blob/master/res/readme/logo.png?raw=true)

[](#)

[![Actions Status](https://github.com/agersant/polaris/workflows/Build/badge.svg)](https://github.com/agersant/polaris/actions) [![codecov](https://camo.githubusercontent.com/cdd11ec51558efa52bb113a8895d8d55ec1f4583937091812cec0d63958dbb35/68747470733a2f2f636f6465636f762e696f2f6769746875622f6167657273616e742f706f6c617269732f67726170682f62616467652e7376673f746f6b656e3d455171436d4245663254)](https://codecov.io/github/agersant/polaris) [![License: MIT](https://camo.githubusercontent.com/cce5a2a14b0faab422e0bfcdc074afb46089831a0bf5930a7d8af3f31b98f847/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d626c75652e737667)](https://github.com/agersant/polaris/blob/master/LICENSE-MIT)

[![Polaris Web UI](/agersant/polaris/raw/master/res/readme/web_ui.png?raw=true "Polaris Web UI")](https://github.com/agersant/polaris/blob/master/res/readme/web_ui.png?raw=true)

# About

[](#about)

Polaris is a self-hosted music streaming server, to enjoy your music collection from any computer or mobile device. It is free and open-source software, without any kind of premium version.

The goals of this project are:

* 🔥 Exceptional performance and responsiveness
* 📚️ First-class support for large music collections (100,000+ songs)
* 📦️ Ease of installation, deployment and maintenance
* ✨ Beautiful user interface

# Try It Out!

[](#try-it-out)

Check out the demo over at <https://demo.polaris.stream>, featuring a selection of Creative Commons Music. The credentials to access this server are:

Username: `demo_user`\
Password: `demo_password`

# Features

[](#features)

* 🖥️ Runs on Windows, Linux, BSD, or through Docker

* 🔊 Support for `flac`, `mp3`, `mp4`, `mpc`, `ogg`, `opus`, `ape`, `wav` and `aiff` files

* 🌈 Dark mode variants and customizable color palette

* 💿️ Browse your music by album, artist or genre

* 📂 Browse your music as a file tree

* 🌊 Song audio-waveform visualization

* 🏷️ Support for multi-value fields in song metadata (eg. multiple artists per song)

* 🔍️ Powerful search functionality with per-field queries

* ⚙️ Plain-text configuration also editable with built-in UI

* 👥 Setup multiple users, each with their own playlists

* 📱 Listen to your music on the go:

  * Polaris Android ([Google Play Store](https://play.google.com/store/apps/details?id=agersant.polaris) · [F-Droid](https://f-droid.org/packages/agersant.polaris/) · [Repository](https://github.com/agersant/polaris-android))
  * Polarios ([App Store](https://apps.apple.com/app/polarios/id1662366309) · [Repository](https://gitlab.com/elise/Polarios)) \[third-party]

# Installation

[](#installation)

[Installation documentation](https://github.com/agersant/polaris/blob/master/docs/SETUP.md)

[Streaming from remote devices](https://github.com/agersant/polaris/blob/master/docs/DDNS.md)

[![Packaging status](https://camo.githubusercontent.com/fb56fac35b9f30702fdcaae6d26dd02387e5750295a2a1fe7b52ed86a0855a19/68747470733a2f2f7265706f6c6f67792e6f72672f62616467652f766572746963616c2d616c6c7265706f732f706f6c617269732d73747265616d696e672e7376673f636f6c756d6e733d33)](https://repology.org/project/polaris-streaming/versions)

# Documentation

[](#documentation)

* 📒 [Changelog](https://github.com/agersant/polaris/blob/master/CHANGELOG.md)
* 🔧 [Configuration](https://github.com/agersant/polaris/blob/master/docs/CONFIGURATION.md)
* 👷 [Contribute to Polaris](https://github.com/agersant/polaris/blob/master/docs/CONTRIBUTING.md)
* 🛟 [Maintenance Runbooks](https://github.com/agersant/polaris/blob/master/docs/MAINTENANCE.md)

The Polaris server API is documented via [OpenAPI](https://demo.polaris.stream/api-docs/). Every installation of Polaris distributes this interactive documentation. To access it, open <http://localhost:5050/api-docs/> in your browser on the machine running Polaris.

# Credits & License Information

[](#credits--license-information)

Music featured in the demo installation:

* [Chris Zabriskie - Abandon Babylon](https://chriszabriskie.bandcamp.com/album/abandon-babylon) [(License)](https://creativecommons.org/licenses/by/3.0/)
* [Chris Zabriskie - Angie's Sunday Service](https://chriszabriskie.bandcamp.com/album/angies-sunday-service) [(License)](https://creativecommons.org/licenses/by/3.0/)
* [glaciære - pool water blue](https://steviasphere.bandcamp.com/album/pool-water-blue) [(License)](https://creativecommons.org/licenses/by/3.0/)
* [glaciære - light ripples](https://steviasphere.bandcamp.com/album/light-ripples) [(License)](https://creativecommons.org/licenses/by/3.0/)
* [Koresma South](https://koresma.bandcamp.com/album/south) [(License)](https://creativecommons.org/licenses/by-nc-sa/3.0/)
* [Pete Murphy - Essence EP](https://petemurphy.bandcamp.com/album/falling-down-the-fred-astaires-solo-jazz-piano) [(License)](https://creativecommons.org/licenses/by-nc-sa/3.0/)
* [Rameses B - Essence EP](https://ramesesb.bandcamp.com/album/essence-ep) [(License)](https://creativecommons.org/licenses/by-nc-nd/3.0/)


