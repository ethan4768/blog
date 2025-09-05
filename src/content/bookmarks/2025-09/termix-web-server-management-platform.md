---
title: "Termix：一个基于Web的开源服务器管理平台，提供SSH终端、隧道和文件编辑功能"
slug: termix-web-server-management-platform
description: |
  Termix是一个开源的自托管服务器管理平台，提供SSH终端访问、SSH隧道管理和远程文件编辑等功能。它旨在通过直观的界面简化服务器和基础设施的管理，同时支持英语和中文。
tags: 
  - opensource
  - dev
  - tool
  - selfhosted
pubDatetime: 2025-09-05T20:03:43+08:00
ogImage: 
---

[原文链接](https://github.com/LukeGus/Termix)

---

# Repo Stats

[](#repo-stats)

[![English](https://camo.githubusercontent.com/61925fcfa4af65108396cac3e1d615fbbf8145aa358f984461b6b15e835dbe6e/68747470733a2f2f666c616763646e2e636f6d2f75732e737667)](https://camo.githubusercontent.com/61925fcfa4af65108396cac3e1d615fbbf8145aa358f984461b6b15e835dbe6e/68747470733a2f2f666c616763646e2e636f6d2f75732e737667) English | [![中文](https://camo.githubusercontent.com/87ca87290863249cecd64fef8c39ea5a00ec859546dff87d1051fe2542137763/68747470733a2f2f666c616763646e2e636f6d2f636e2e737667) 中文](https://github.com/LukeGus/Termix/blob/main/README-CN.md)

[![GitHub Repo stars](https://camo.githubusercontent.com/9dc532529add7bfdfd559aaf8d1d1c2cd6e389935c1b39033d900d6fdc04a648/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f4c756b654775732f5465726d69783f7374796c653d666c6174266c6162656c3d5374617273)](https://camo.githubusercontent.com/9dc532529add7bfdfd559aaf8d1d1c2cd6e389935c1b39033d900d6fdc04a648/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f4c756b654775732f5465726d69783f7374796c653d666c6174266c6162656c3d5374617273) [![GitHub forks](https://camo.githubusercontent.com/32c40fdb3ac187167e1285d6c075c0d798d8c28ff989804928811fda600ce071/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f4c756b654775732f5465726d69783f7374796c653d666c6174266c6162656c3d466f726b73)](https://camo.githubusercontent.com/32c40fdb3ac187167e1285d6c075c0d798d8c28ff989804928811fda600ce071/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f4c756b654775732f5465726d69783f7374796c653d666c6174266c6162656c3d466f726b73) [![GitHub Release](https://camo.githubusercontent.com/96208c095278e238b2a64a79cef3af99d264e3f0e92d9a00b58890e1359ac9c7/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f4c756b654775732f5465726d69783f7374796c653d666c6174266c6162656c3d52656c65617365)](https://camo.githubusercontent.com/96208c095278e238b2a64a79cef3af99d264e3f0e92d9a00b58890e1359ac9c7/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f4c756b654775732f5465726d69783f7374796c653d666c6174266c6162656c3d52656c65617365) [![Discord](https://camo.githubusercontent.com/873245ad1a0f14f52b189de1c67fb5ccd223cec7efb1809e37e5640f38349130/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f31333437333734323638323533343730373230)](https://discord.gg/jVQGdvHDrf)

#### Top Technologies

[](#top-technologies)

[![React Badge](https://camo.githubusercontent.com/8cf84fb43a29de7f71b2054a35cd4169c9011a41cb9582cea5e2ae06959618a7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d52656163742d3631444246423f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d626c61636b266c6f676f3d7265616374266c6f676f436f6c6f723d363144424642)](#) [![TypeScript Badge](https://camo.githubusercontent.com/0336ba33910a717b2d51c5910c8f439cc4a7b564f579cc1872538dc9776d0365/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d547970655363726970742d3331373843363f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d626c61636b266c6f676f3d74797065736372697074266c6f676f436f6c6f723d333137384336)](#) [![Node.js Badge](https://camo.githubusercontent.com/752a4ab7eaeea73ffec55c816da62d00b4eee365a74acccd8c9f136421e02e17/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d4e6f64652e6a732d3343383733413f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d626c61636b266c6f676f3d6e6f64652e6a73266c6f676f436f6c6f723d334338373341)](#) [![Vite Badge](https://camo.githubusercontent.com/6b7d22db8776630bca414cd1353ee27cabbbac77d51973d1d92c5f6bcb3fa383/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d566974652d3634364346463f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d626c61636b266c6f676f3d76697465266c6f676f436f6c6f723d363436434646)](#) [![Tailwind CSS Badge](https://camo.githubusercontent.com/db5230ef49308547efe98a223db013a5560f6add9bb4ce80dea38a9499a53b9b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d5461696c77696e644353532d3338423241433f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d626c61636b266c6f676f3d7461696c77696e64637373266c6f676f436f6c6f723d333842324143)](#) [![Docker Badge](https://camo.githubusercontent.com/e5281ef7b6b093fc16a167c6a966fafd4b3d5294771679fd8dc08a3d097c49ef/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d446f636b65722d3234393645443f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d626c61636b266c6f676f3d646f636b6572266c6f676f436f6c6f723d323439364544)](#) [![SQLite Badge](https://camo.githubusercontent.com/c66af748b001da0da464477ad93fbe8f77f4e415b69625fc59bf1fd2b3f8337b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d53514c6974652d3030334235373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d626c61636b266c6f676f3d73716c697465266c6f676f436f6c6f723d303033423537)](#) [![Radix UI Badge](https://camo.githubusercontent.com/cbbd07c11cb365472ad6c50ebbf28d806b606b816039752fb79e43503167491e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d526164697825323055492d3136313631383f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d626c61636b266c6f676f3d72616469787569266c6f676f436f6c6f723d313631363138)](#)

\


[![Termix Banner](/LukeGus/Termix/raw/main/repo-images/HeaderImage.png)](https://github.com/LukeGus/Termix)

If you would like, you can support the project here!\
[![GitHub Sponsor](https://camo.githubusercontent.com/34289a327fcac115d9637b3ccf13d9708c5ae68fe58d054412f5dc9cd143774d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53706f6e736f722d4c756b654775732d3138313731373f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465)](https://github.com/sponsors/LukeGus)

# Overview

[](#overview)

[![Termix Banner](/LukeGus/Termix/raw/main/public/icon.svg)](https://github.com/LukeGus/Termix)

Termix is an open-source, forever-free, self-hosted all-in-one server management platform. It provides a web-based solution for managing your servers and infrastructure through a single, intuitive interface. Termix offers SSH terminal access, SSH tunneling capabilities, and remote file editing, with many more tools to come.

# Features

[](#features)

* **SSH Terminal Access** - Full-featured terminal with split-screen support (up to 4 panels) and tab system
* **SSH Tunnel Management** - Create and manage SSH tunnels with automatic reconnection and health monitoring
* **Remote File Editor** - Edit files directly on remote servers with syntax highlighting, file management features (uploading, removing, renaming, deleting files)
* **SSH Host Manager** - Save, organize, and manage your SSH connections with tags and folders
* **Server Stats** - View CPU, memory, and HDD usage on any SSH server
* **User Authentication** - Secure user management with admin controls and OIDC and 2FA (TOTP) support
* **Modern UI** - Clean interface built with React, Tailwind CSS, and Shadcn
* **Languages** - Built-in support for English and Chinese

# Planned Features

[](#planned-features)

* **Improved Admin Control** - Give more fine-grained control over user and admin permissions, share hosts, etc
* **Theming** - Modify theming for all tools
* **Improved Terminal Support** - Add more terminal protocols such as VNC and RDP (anyone who has experience in integrating RDP into a web-application similar to Apache Guacamole, please contact me by creating an issue)
* **Mobile Support** - Support a mobile app or version of the Termix website to manage servers from your phone

# Installation

[](#installation)

Visit the Termix [Docs](https://docs.termix.site/install) for more information on how to install Termix. Otherwise, view a sample docker-compose file here:

```
services:
  termix:
    image: ghcr.io/lukegus/termix:latest
    container_name: termix
    restart: unless-stopped
    ports:
      - "8080:8080"
    volumes:
      - termix-data:/app/data
    environment:
      PORT: "8080"

volumes:
  termix-data:
    driver: local 
```

# Support

[](#support)

If you need help with Termix, you can join the [Discord](https://discord.gg/jVQGdvHDrf) server and visit the support channel. You can also open an issue or open a pull request on the [GitHub](https://github.com/LukeGus/Termix/issues) repo.

# Show-off

[](#show-off)

[![Termix Demo 1](</LukeGus/Termix/raw/main/repo-images/Image 1.png>)](https://github.com/LukeGus/Termix/blob/main/repo-images/Image%201.png) [![Termix Demo 2](</LukeGus/Termix/raw/main/repo-images/Image 2.png>)](https://github.com/LukeGus/Termix/blob/main/repo-images/Image%202.png)

[![Termix Demo 3](</LukeGus/Termix/raw/main/repo-images/Image 3.png>)](https://github.com/LukeGus/Termix/blob/main/repo-images/Image%203.png) [![Termix Demo 4](</LukeGus/Termix/raw/main/repo-images/Image 4.png>)](https://github.com/LukeGus/Termix/blob/main/repo-images/Image%204.png) [![Termix Demo 5](</LukeGus/Termix/raw/main/repo-images/Image 5.png>)](https://github.com/LukeGus/Termix/blob/main/repo-images/Image%205.png)

Termix.Show\.Off.Video.mov

[](https://github.com/user-attachments/assets/f9caa061-10dc-4173-ae7d-c6d42f05cf56)

# License

[](#license)

Distributed under the Apache License Version 2.0. See LICENSE for more information.


