---
title: "ZTM（零信任网格）：基于HTTP/2隧道的开源去中心化网络软件"
slug: flomesh-ztm-zero-trust-mesh
description: |
  ZTM（零信任网格）是一款隐私优先的开源去中心化网络软件，基于HTTP/2隧道构建。它支持在各种IP网络上运行，提供跨网关和防火墙的安全连接功能，是构建去中心化应用程序的理想基础。
tags: 
  - opensource
  - security
  - dev
  - tool
  - performance
pubDatetime: 2025-01-07T10:08:24+08:00
ogImage: https://opengraph.githubassets.com/9bbf80b2bd9d610c23fa3a43691e3ef09ed086db22b7703c02390c2756e1565f/flomesh-io/ztm
---

[原文链接](https://github.com/flomesh-io/ztm)

---

[![](https://camo.githubusercontent.com/eae5b9541a9ddfb3c9be0ddbf03eba4402ebcf490c5b89ef14c0fb4ef7d966bc/68747470733a2f2f666c6f6d6573682e696f2f696d672f7a746d2e706e67)](https://camo.githubusercontent.com/eae5b9541a9ddfb3c9be0ddbf03eba4402ebcf490c5b89ef14c0fb4ef7d966bc/68747470733a2f2f666c6f6d6573682e696f2f696d672f7a746d2e706e67)

[![](https://camo.githubusercontent.com/1613b1dd9fee136c8f50b232263a648dae5dfdacf0017e94d01c83d3a2f5093c/68747470733a2f2f666c6f6d6573682e696f2f696d672f66617669636f6e2e69636f)](https://github.com/flomesh-io/pipy) [![](https://camo.githubusercontent.com/86811529844c9325ae8364521d48d1217e738fe2e373dbaaa81034c1bbc81b28/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506970794a532d303061646566)](https://camo.githubusercontent.com/86811529844c9325ae8364521d48d1217e738fe2e373dbaaa81034c1bbc81b28/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506970794a532d303061646566) [![](https://camo.githubusercontent.com/41cc7c1087048882afc35e27a854890501e993290f88015a8d0e4e92f07687b8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f432b2b2d677265656e)](https://camo.githubusercontent.com/41cc7c1087048882afc35e27a854890501e993290f88015a8d0e4e92f07687b8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f432b2b2d677265656e) [![](https://camo.githubusercontent.com/5ba42d149efc47c9d25431e93300afeab52b2209b8c5bb9010070203daf62a96/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f54617572692d3234433844423f6c6f676f3d7461757269266c6f676f436f6c6f723d464643313331)](https://camo.githubusercontent.com/5ba42d149efc47c9d25431e93300afeab52b2209b8c5bb9010070203daf62a96/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f54617572692d3234433844423f6c6f676f3d7461757269266c6f676f436f6c6f723d464643313331) [![](https://camo.githubusercontent.com/a7c253f047eeb60e097abf452c4165fae34f3a5d1ab31d0322aab12ca4f8a557/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f527573742d6335376335343f6c6f676f3d72757374266c6f676f436f6c6f723d453334463236)](https://camo.githubusercontent.com/a7c253f047eeb60e097abf452c4165fae34f3a5d1ab31d0322aab12ca4f8a557/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f527573742d6335376335343f6c6f676f3d72757374266c6f676f436f6c6f723d453334463236) [![](https://camo.githubusercontent.com/72dba13c1b4ff6d747f152d788c247e161955493261a91391b5853bcbd83011a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f56697465352d3335343935453f6c6f676f3d76697465266c6f676f436f6c6f723d343144314646)](https://camo.githubusercontent.com/72dba13c1b4ff6d747f152d788c247e161955493261a91391b5853bcbd83011a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f56697465352d3335343935453f6c6f676f3d76697465266c6f676f436f6c6f723d343144314646) [![star](https://camo.githubusercontent.com/43cfb03ac3b860cf885a0901efb17e42fbab86e645cebbc9b31342890f5e871e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f666c6f6d6573682d696f2f7a746d)](https://gitee.com/link?target=https://github.com/flomesh-io/ztm/stargazers)

[![](https://camo.githubusercontent.com/48846ba685f9fb08cd402d602ab050c94758c293b9803560d563c64d333acb57/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5765622d677265656e)](https://camo.githubusercontent.com/48846ba685f9fb08cd402d602ab050c94758c293b9803560d563c64d333acb57/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5765622d677265656e) [![](https://camo.githubusercontent.com/ec8036ebe3a90154de45d45b976e85cc52e77684ef1539a78d97c3a56e006ae8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d61634f532d67726179)](https://camo.githubusercontent.com/ec8036ebe3a90154de45d45b976e85cc52e77684ef1539a78d97c3a56e006ae8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d61634f532d67726179) [![](https://camo.githubusercontent.com/a7f50ef10e433b5e7eec19fd007489cf7d0deaf0015d933728e22d2cf1147299/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f57696e646f77732d626c7565)](https://camo.githubusercontent.com/a7f50ef10e433b5e7eec19fd007489cf7d0deaf0015d933728e22d2cf1147299/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f57696e646f77732d626c7565) [![](https://camo.githubusercontent.com/2b7c34e28036546fd944e199cd15f25165dc9c9c41a78254cd781ba2e1bed6b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c696e75782d6f72616e6765)](https://camo.githubusercontent.com/2b7c34e28036546fd944e199cd15f25165dc9c9c41a78254cd781ba2e1bed6b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c696e75782d6f72616e6765) [![](https://camo.githubusercontent.com/7b8456fc2797e73a9b9e8dd33614e76ff624cfb0428d46d3f81d0f2e1bcdd58c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f694f532d416e64726f69642d626c7565)](https://camo.githubusercontent.com/7b8456fc2797e73a9b9e8dd33614e76ff624cfb0428d46d3f81d0f2e1bcdd58c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f694f532d416e64726f69642d626c7565)

# ZTM (Zero Trust Mesh)  ZTM（零信任网格）

[](#ztm-zero-trust-mesh)

ZTM is an open source network infrastructure software for running a ***decentralized*** network. It is built upon ***HTTP/2 tunnels*** and can run on ***any sort of IP networks*** such as LANs, containerized networks and the Internet, etc.ZTM 是一款用于运&#x884C;***去中心化***&#x7F51;络的开源网络基础设施软件。它基&#x4E8E;***HTTP/2 隧道***&#x6784;建，可以&#x5728;***任何类型的 IP 网络***&#x4E0A;运行，例如 LAN、容器化网络和互联网等。

## Why ZTM?  为什么选择ZTM？

[](#why-ztm)

ZTM lays the foundation for building ***decentralized applications*** by providing a set of core capabilities including:ZTM 通过提供一系列核心功能，为构&#x5EFA;***去中心化应用程序***&#x5960;定了基础，包括：

* Network connectivity across Internet gateways and firewalls跨 Internet 网关和防火墙的网络连接
* TLS-encrypted communication channelsTLS 加密的通信通道
* Certificate-based authentication and access control基于证书的身份验证和访问控制
* Decentralized application publishing and deployment去中心化的应用程序发布和部署
* Decentralized file discovery and data sharing分散式文件发现和数据共享

ZTM can be used in various settings ranging from a ***2-node personal network connecting one's home and workplace*** to a ***10,000-node enterprise network connecting offices and branches across the globe***. Examples of applications that can leverage ZTM are:ZTM 可用于各种设置，&#x4ECE;***连接家庭和工作场所的 2 节点个人网络***&#x5230;***连接全球办公室和分支机构的 10,000 节点企业网络***。可以利用 ZTM 的应用程序示例包括：

* Remote access your home computer from anywhere in the world从世界任何地方远程访问您的家庭计算机
* Share documents, pictures and videos within a group of people without the need of a big-tech social networking platform无需大型科技社交网络平台即可在一群人中共享文档、图片和视频
* Private and secure P2P data transfer without the fear of eavesdropping私密且安全的 P2P 数据传输，无需担心窃听

## Features  特征

[](#features)

ZTM is written in **PipyJS**, a JavaScript dialect designed for [**Pipy**](https://github.com/flomesh-io/pipy) (<https://github.com/flomesh-io/pipy>). **Pipy** is an open source programmable proxy software. Thanks to **Pipy**, ZTM has many unique features on top of the capabilities it offers:ZTM 是用**PipyJS**编写的，PipyJS 是一种专为[**Pipy**](https://github.com/flomesh-io/pipy)设计的 JavaScript 方言 ( <https://github.com/flomesh-io/pipy> )。 **Pipy**是一款开源可编程代理软件。得益于**Pipy** ，ZTM 除了提供的功能之外还具有许多独特的功能：

* **Fast**. HTTP/2 multiplexing is fast. And **Pipy** is fast. Like, C++ fast.**快速地**。 HTTP/2 多路复用速度很快。而且**Pipy**速度很快。就像，C++ 速度很快。

* **Secure**. All traffic is encrypted by TLS and has identities via certificates. By using **PipyJS**, security policy can be easily customized to meet the requirements in your organization.**安全的**。所有流量均通过 TLS 加密，并通过证书进行身份识别。通过使用**PipyJS** ，可以轻松自定义安全策略以满足您组织的要求。

* **Highly customizable and programmable**, since **Pipy** in itself is a general-purpose network scripting engine.**高度可定制和可编程**，因为**Pipy**本身就是一个通用网络脚本引擎。

* **Portable**. Choose your CPU architecture: x86, ARM, MIPS, RISC-V, LoongArch... Choose your operating system: Linux, Windows, macOS, FreeBSD, Android... ZTM runs anywhere.**便携的**。选择您的 CPU 架构：x86、ARM、MIPS、RISC-V、LoongArch...选择您的操作系统：Linux、Windows、macOS、FreeBSD、Android...ZTM 在任何地方运行。

## Documentation  文档

[](#documentation)

* [Architecture & Concepts  架构与概念](https://github.com/flomesh-io/ztm/blob/main/docs/Architecture-Concepts.md)
* [CLI  命令行界面](https://github.com/flomesh-io/ztm/blob/main/docs/CLI.md)
* [ZT-App  中通应用](https://github.com/flomesh-io/ztm/blob/main/docs/ZT-App.md)
* [Agent API  代理接口](https://github.com/flomesh-io/ztm/blob/main/docs/Agent-API.md)
* [Build  建造](https://github.com/flomesh-io/ztm/blob/main/docs/Build.md)

## Quick Start  快速入门

[](#quick-start)

### Download  下载

[](#download)

The easiest way to get started is download the latest binary release of ZTM from our [release page](https://github.com/flomesh-io/ztm/releases). If you prefer to have your own build from the source, you can follow the instructions in [Build](https://github.com/flomesh-io/ztm/blob/main/docs/Build.md).最简单的开始方法是从我们的[发布页面](https://github.com/flomesh-io/ztm/releases)下载最新的 ZTM 二进制版本。如果您希望从源代码构建自己的版本，则可以按照[构建](https://github.com/flomesh-io/ztm/blob/main/docs/Build.md)中的说明进行操作。

> The official build releases of ZTM come in two forms of packaging: the CLI tool as a SEA (Single Executable Application), and the desktop application that wraps up the CLI tool and provides a GUI for desktop environments.ZTM 的官方构建版本有两种打包形式：作为 SEA（单一可执行应用程序）的 CLI 工具，以及包装 CLI 工具并为桌面环境提供 GUI 的桌面应用程序。
>
> In this guide, we'll be only utilizing the CLI for setting up a simple mesh. For more guides, including the usage of the desktop app, please check out our [Wiki](https://github.com/flomesh-io/ztm/wiki).在本指南中，我们将仅利用 CLI 来设置简单的网格。如需更多指南，包括桌面应用程序的使用，请查看我们的[Wiki](https://github.com/flomesh-io/ztm/wiki) 。

### Setup  设置

[](#setup)

A common setup consists of 3 nodes: 1 node running the *Hub*, the other 2 nodes running two *Agents* who wish to communicate with each other.常见的设置由 3 个节点组成：1 个节点运行*Hub* ，另外 2 个节点运行两个希望相互通信的*代理*。

```
                            Data Center
          +-------------------------------------------+
          |                     Hub                   |
          |        (state in ~/.ztm/ztm-hub.db)       |
          +-------------------------------------------+
        HTTPS | Port 8888                 HTTPS | Port 8888
              |                                 |
  ------------|---------------------------------|--------------
              |             Firewall            |
  ------------|---------------------------------|--------------
              |                                 |
              |             Internet            |
              |                                 |
  ----------------------------  |  ----------------------------
          Firewall              |            Firewall
  ----------------------------  |  ----------------------------
              |                 |               |
              |                 |               |
  +--------------------------+  |  +--------------------------+
  |      Agent @ Home        |  |  |    Agent @ Workplace     |
  | (state in ~/.ztm/ztm.db) |  |  | (state in ~/.ztm/ztm.db) |
  +--------------------------+  |  +--------------------------+
                                |
```

> We'll only cover the setup of a Hub on Linux, since that's where they are usually run - a cloud-hosted Linux virtual machine.我们只会介绍 Linux 上 Hub 的设置，因为它们通常运行在云托管的 Linux 虚拟机上。

#### Setup a Hub  设置集线器

[](#setup-a-hub)

Suppose you have a Linux box in the cloud, with a public IP address `1.2.3.4` and a public TCP port `8888`. Start a Hub service by typing:假设您在云端有一个 Linux 盒子，具有公共 IP 地址`1.2.3.4`和公共 TCP 端口`8888` 。通过键入以下内容启动 Hub 服务：

```
ztm start hub --listen 0.0.0.0:8888 --names 1.2.3.4:8888 --permit root.json
```

> You might need `sudo` when executing the above command because it needs to install a service to `systemd`.执行上述命令时可能需要`sudo` ，因为它需要向`systemd`安装服务。

Now the Hub should be up an running. Plus, a file named `root.json` should have been generated for us to allow *endpoints* to join our mesh.现在集线器应该可以运行了。另外，应该为我们生成一个名为`root.json`的文件，以允许*端点*加入我们的网格。

#### Setup Endpoints  设置端点

[](#setup-endpoints)

Once the Hub gets up and running in the cloud, we can go on and add as many *endpoints* as we like to the mesh by using the generated permit file `root.json`.一旦 Hub 在云中启动并运行，我们就可以使用生成的许可文件`root.json`继续向网格添加任意数量*的端点*。

> An *endpoint* is just a computer running in various network environments with access to the Internet.*端点*只是运行在各种网络环境中并可以访问 Internet 的计算机。

First, start an Agent on an endpoint computer that is going to join our mesh:首先，在要加入我们的网格的端点计算机上启动代理：

```
ztm start agent
```

> On Windows, starting as a system service isn't supported yet. You'll have to do `ztm run agent` instead.在 Windows 上，尚不支持作为系统服务启动。您必须改为执行`ztm run agent` 。

And then, join the mesh by saying:然后，通过说以下内容加入网格：

```
ztm join MESH_NAME --as EP_NAME --permit root.json
```

Where `MESH_NAME` can be any name of your choice for identifying a mesh locally if you have many. `EP_NAME` is the name of your current endpoint seen by other endpoints in the same mesh. `root.json` is the permit file generated in our first step where a Hub is set up.其中`MESH_NAME`可以是您选择的任何名称，用于在本地标识网格（如果您有多个网格）。 `EP_NAME`是同一网格中其他端点看到的当前端点的名称。 `root.json`是在设置集线器的第一步中生成的许可文件。

If everything works out, you can now check out the status of the mesh by typing:如果一切顺利，您现在可以通过键入以下内容来检查网格的状态：

```
ztm get mesh
```

Or look up for endpoints that already joined the mesh:或者查找已经加入网格的端点：

```
ztm get ep
```

For detailed usage of the command-line tool, type:有关命令行工具的详细使用方法，请键入：

```
ztm help
```

If you prefer GUI, you can open your browser and point it to `http://localhost:7777` right after command `ztm start agent`. You can join a mesh, find other endpoints, using apps and everything. Almost all functionalities ZTM provides are available from both the CLI and the GUI.如果您更喜欢 GUI，您可以在命令`ztm start agent`之后打开浏览器并将其指向`http://localhost:7777` 。您可以使用应用程序等加入网格、查找其他端点。 ZTM 提供的几乎所有功能都可以通过 CLI 和 GUI 获得。

Repeat the above procedure for every endpoint in your mesh. Then, you will be able to manage your mesh via terminal or browser from any endpoint in the mesh.

#### Using Your Mesh

[](#using-your-mesh)

Only connecting a bunch of endpoints as a mesh isn't very useful. What makes your mesh useful is the *apps* running in it. The official ZTM releases come with a number of builtin apps including:

* Tunnel - Establish secure TCP/UDP tunnels between endpoints
* Proxy - A SOCKS/HTTP forward proxy that takes in traffic from one endpoint and forward out via another endpoint
* Script - Execute *PipyJS* scripts remotely on an endpoint
* Terminal - Remote access to the shell on an endpoint

Third-party apps can also be installed. Also, new apps can be developed rather easily thanks to the *PipyJS* scripting capability of [**Pipy**](https://github.com/flomesh-io/pipy).

To get a list of all installed apps, type:

```
ztm get app
```

You can use an app from either the browser GUI or the command-line tool. On a terminal, one can access an app's CLI in a way like:

```
ztm APP_NAME ...
```

To find out detailed information about using an app via CLI, type:

```
ztm APP_NAME help
```

#### CLI Commands Summary

[](#cli-commands-summary)

Here's a recap of what CLI commands you need to do on each computer node.

```
                       Cloud-hosted VM
  +---------------------------------------------------------+
  | ztm start hub --names x.x.x.x:8888 --permit root.json   | ---+
  +---------------------------------------------------------+    |
              |          x.x.x.x:8888          |                 |
  ------------|--------------------------------|-------------    |
              |            Firewall            |                 |
  ------------|--------------------------------|-------------    |
              |                                |                 |
              |            Internet            |                 | root.json
              |                                |                 |
  --------------------------   |   --------------------------    |
           Firewall            |            Firewall             |
  --------------------------   |   --------------------------    |
              |                |               |                 |
              |                |               |                 |
  +------------------------+   |   +------------------------+    |
  | ztm start agent        |   |   | ztm start agent        |    |
  | ztm join my-mesh \     |   |   | ztm join my-mesh \     | <--+
  |   --as home \          |   |   |   --as workplace \     |
  |   --permit root.json   |   |   |   --permit root.json   |
  +------------------------+   |   +------------------------+
           PC @ Home           |         PC @ Workplace
```

For more information on the CLI, please refer to:

```
ztm help
```

## Quick Links:

[](#quick-links)

* [How-to: Using ZTM for Secure Remote Desktop Protocol (RDP) Access](https://github.com/flomesh-io/ztm/wiki/2.-HOWTO-:-using-ztm-for-secure-RDP-access)
* [QuickStart : ZTM Tunnel](https://github.com/flomesh-io/ztm/blob/main/docs/ZT-App.md#zt-tunnel) | [Tunnel Demo](https://github.com/flomesh-io/ztm/wiki/2.-HOWTO-:-using-ztm-for-secure-RDP-access#4-configuring-ztm-tunnel-for-rdp-connection)
* [QuickStart : ZTM Proxy](https://github.com/flomesh-io/ztm/blob/main/docs/ZT-App.md#zt-proxy)
* [QuickStart : ZTM Terminal](https://github.com/flomesh-io/ztm/blob/main/docs/ZT-App.md#zt-terminal)
* [QuickStart : ZTM Script](https://github.com/flomesh-io/ztm/blob/main/docs/ZT-App.md#zt-script)
* [QuickStart : ZTM Cloud](https://github.com/flomesh-io/ztm/blob/main/docs/ZT-App.md#zt-cloud) | [Cloud Demo](https://github.com/flomesh-io/ztm/wiki/4.-HOWTO-:-File-Sharing-between-ZTM-End-Points#sharing-files-on-macos)


