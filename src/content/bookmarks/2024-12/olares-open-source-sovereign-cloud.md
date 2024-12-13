---
title: Olares：开源自托管的主权云替代方案
slug: olares-open-source-sovereign-cloud
description: Olares是一个开放源代码的自托管主权云解决方案，旨在为用户提供数据所有权和隐私保护。它允许本地AI部署、数据管理及个性化应用，真正掌控您的计算资源。适合希望摆脱公共云的用户。
tags: 
  - opensource
  - selfhosted
  - cloud
  - dev
  - ai
pubDatetime: 2024-12-13T10:04:16+08:00
ogImage: https://opengraph.githubassets.com/f7f0a7d2919ccd295be6e5d8cd2dc7cb2a5cfc9f1a8cffefc3628f4b2aa5a114/beclab/Olares
---

[原文链接](https://github.com/beclab/Olares)

---

# Olares - Your Sovereign Cloud, an Open-Source Self-Hosted Alternative to Public Clouds

[](#olares---your-sovereign-cloud-an-open-source-self-hosted-alternative-to-public-clouds-)

[![Mission](https://camo.githubusercontent.com/c32c4bc942a4181e960a2ee0ad5c948a085997973e76b08d36e70fa9f848ac71/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d697373696f6e2d4c657425323070656f706c652532306f776e253230746865697225323064617461253230616761696e2d707572706c65)](#)\
[![Last Commit](https://camo.githubusercontent.com/ca99b5c9e5a29d811261ccee8e82f22d930375a9dde3ec84691f18238cb17724/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6173742d636f6d6d69742f6265636c61622f6f6c61726573)](https://github.com/beclab/olares/commits/main) [![Build Status](https://github.com/beclab/olares/actions/workflows/release-daily.yaml/badge.svg)](https://github.com/beclab/olares/actions/workflows/release-daily.yaml/badge.svg) [![GitHub release (latest by date)](https://camo.githubusercontent.com/1b161d5fd38b1343350f5decd3108a79e059c527428b8f97ffc397cce5ae2e18/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f6265636c61622f6f6c61726573)](https://github.com/beclab/olares/releases) [![GitHub Repo stars](https://camo.githubusercontent.com/681b4311b739cfc2a34dd5f8ad65ae0297638a766debd577bd6d3d0fa6ebb206/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6265636c61622f6f6c617265733f7374796c653d736f6369616c)](https://github.com/beclab/olares/stargazers) [![Discord](https://camo.githubusercontent.com/a49f1de892e0c1ec199f346c486b0e07b730b30609037f71c9600b65db2c8309/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446973636f72642d3732383944413f6c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465)](https://discord.com/invite/BzfqrgQPDK) [![License](https://camo.githubusercontent.com/72161c3ee048917d7e2edd8ea66ed8bdc7222b0e53f54bcfc84165d95ba94376/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4f6c617265732d6461726b626c7565)](https://github.com/beclab/olares/blob/main/LICENSE.md)

[![Readme in English](https://camo.githubusercontent.com/9460179be0e4faf1adbfbb0a2cab2c0305ea8d34a1950d49c932d5b081d2e5f4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f456e676c6973682d464646464646)](https://github.com/beclab/Olares/blob/main/README.md) [![Readme in Chinese](https://camo.githubusercontent.com/7df2e86518566c312f383c7a0253b055596ae5152559e8807b3bc6d146502a86/68747470733a2f2f696d672e736869656c64732e696f2f62616467652fe7ae80e4bd93e4b8ade696872d464646464646)](https://github.com/beclab/Olares/blob/main/README_CN.md)

Olares.mp4

[](https://private-user-images.githubusercontent.com/110797546/384893928-5ea2fe30-7bd2-49ed-be26-e12f1d5d8cb1.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzQwNTMzMTIsIm5iZiI6MTczNDA1MzAxMiwicGF0aCI6Ii8xMTA3OTc1NDYvMzg0ODkzOTI4LTVlYTJmZTMwLTdiZDItNDllZC1iZTI2LWUxMmYxZDVkOGNiMS5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMjEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTIxM1QwMTIzMzJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lN2FhYmI3MzlhNjliNjc1MTgwOTAyN2UyNWE0OWZmYzQ4MjU0NWE3MDMwZTJiZWYxM2JiMzJmNzk5ZTMyYjk2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.CBMn-TysM-LsVDDEW_hm9PvkwdzuFvEHvqMulzYvT7k)

*Build your local AI assistants, sync data across places, self-host your workspace, stream your own media, and more—all in your sovereign cloud made possible by Olares.*

[Website](https://olares.xyz) · [Documentation](https://docs.olares.xyz) · [Download LarePass](https://olares.xyz/larepass) · [Olares Apps](https://github.com/beclab/apps) · [Olares Space](https://space.olares.xyz)

Important

We just finished our rebranding from Terminus to Olares recently. For more information, refer to our [rebranding blog](https://olares.medium.com/terminus-is-now-olares-2c3bf782f9d1).

## Table of Contents

[](#table-of-contents-)

* [Introduction](#introduction)
* [Motivation and design](#motivation-and-design)
* [Tech stacks](#tech-stacks)
* [Features](#features)
* [Feature comparison](#feature-comparison)
* [Getting started](#getting-started)
* [Project navigation](#project-navigation)
* [Contributing to Olares](#contributing-to-olares)
* [Community & contact](#community--contact)
* [Staying ahead](#staying-ahead)
* [Special thanks](#special-thanks)

## Introduction

[](#introduction)

Olares is the sovereign cloud that puts you in control. It's an open-source, self-hosted alternative to public clouds like AWS, built to reclaim your data ownership and privacy. By combining the power of Kubernetes with a streamlined interface, Olares enables you to take full control of your data and computing resources. Whether you're managing a homelab, hosting applications, or safeguarding your privacy, Olares delivers the flexibility and capabilities of public clouds, without compromising privacy or security.

Typical use cases of Olares include:

🤖 **Local AI**: Host and run world-class open-source AI models locally, including large language models, image generation, and speech recognition. Create custom AI assistants that integrate seamlessly with your personal data and applications, all while ensuring enhanced privacy and control.

💻**Personal data repository**: Securely store, sync, and manage your photos, documents, and important files in a unified storage and access anywhere.

🛠️ **Self-hosted workspace**: Create a free, powerful workspace for your team or family with open source self-hosted alternatives.

🎥 **Private media server**: Host your own streaming services with your personal media collections.

🏡 **Smart Home Hub**: Create a central control point for your IoT devices and home automation.

🤝 **User-owned decentralized social media**: Easily install decentralized social media apps such as Mastodon, Ghost, and WordPress on Olares, allowing you to build a personal brand without the risk of being banned or paying platform commissions.

📚 **Learning platform**: Explore self-hosting, container orchestration, and cloud technologies hands-on.

## Motivation and design

[](#motivation-and-design)

We believe the current state of the internet, where user data is centralized and exploited by monopolistic corporations, is deeply flawed. Our goal is to empower individuals with true data ownership and control.

Olares provides a next-generation decentralized Internet framework consisting of the following three integral components:

* **Snowinning Protocol**: A decentralized identity and reputation system that integrates decentralized identifiers (DIDs), verifiable credentials (VCs), and reputation data.
* **Olares OS**: An one-stop self-hosted operating system running on edge devices, allowing users to host their own data and applications.
* **LarePass**: A comprehensive client software that securely bridges users to their Olares systems. It offers remote access, identity and device management, data storage, and productivity tools, providing a seamless interface for all Olares interactions.

## Tech stacks

[](#tech-stacks)

Public clouds have IaaS, PaaS, and SaaS layers. Olares provides open-source alternatives to these layers.

[![Tech Stacks](https://camo.githubusercontent.com/2db4884bb753990d05b4e337bddb2d75ff073f8768dbd5f113985891373b0198/68747470733a2f2f66696c652e62747463646e2e636f6d2f6769746875622f7465726d696e75732f76322f746563682d737461636b2d6f6c617265732e6a706567)](https://camo.githubusercontent.com/2db4884bb753990d05b4e337bddb2d75ff073f8768dbd5f113985891373b0198/68747470733a2f2f66696c652e62747463646e2e636f6d2f6769746875622f7465726d696e75732f76322f746563682d737461636b2d6f6c617265732e6a706567)

## Features

[](#features)

Olares offers a wide array of features designed to enhance security, ease of use, and development flexibility:

* **Enterprise-grade security**: Simplified network configuration using Tailscale, Headscale, Cloudflare Tunnel, and FRP.
* **Secure and permissionless application ecosystem**: Sandboxing ensures application isolation and security.
* **Unified file system and database**: Automated scaling, backups, and high availability.
* **Single sign-on**: Log in once to access all applications within Olares with a shared authentication service.
* **AI capabilities**: Comprehensive solution for GPU management, local AI model hosting, and private knowledge bases while maintaining data privacy.
* **Built-in applications**: Includes file manager, sync drive, vault, reader, app market, settings, and dashboard.
* **Seamless anywhere access**: Access your devices from anywhere using dedicated clients for mobile, desktop, and browsers.
* **Development tools**: Comprehensive development tools for effortless application development and porting.

## Feature comparison

[](#feature-comparison)

To help you understand how Olares stands out in the landscape, we've created a comparison table that highlights its features alongside those of other leading solutions in the market.

**Legend:**

* 🚀: **Auto**, indicates that the system completes the task automatically.
* ✅: **Yes**, indicates that users without a developer background can complete the setup through the product's UI prompts.
* 🛠️: **Manual Configuration**, indicates that even users with an engineering background need to refer to tutorials to complete the setup.
* ❌: **No**, indicates that the feature is not supported.

|                           | Olares                                                                                                         | Synology                                 | TrueNAS                                  | CasaOS                  | Unraid                                   |
| ------------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ---------------------------------------- | ----------------------- | ---------------------------------------- |
| Source Code License       | Olares License                                                                                                 | Closed                                   | GPL 3.0                                  | Apache 2.0              | Closed                                   |
| Built On                  | Kubernetes                                                                                                     | Linux                                    | Kubernetes                               | Docker                  | Docker                                   |
| Multi-Node                | ✅                                                                                                              | ❌                                        | ✅                                        | ❌                       | ❌                                        |
| Build-in Apps             | ✅ (Rich desktop apps)                                                                                          | ✅ (Rich desktop apps)                    | ❌ (CLI)                                  | ✅ (Simple desktop apps) | ✅ (Dashboard)                            |
| Free Domain Name          | ✅                                                                                                              | ✅                                        | ❌                                        | ❌                       | ❌                                        |
| Auto SSL Certificate      | 🚀                                                                                                             | ✅                                        | 🛠️                                      | 🛠️                     | 🛠️                                      |
| Reverse Proxy             | 🚀                                                                                                             | ✅                                        | 🛠️                                      | 🛠️                     | 🛠️                                      |
| VPN Management            | 🚀                                                                                                             | 🛠️                                      | 🛠️                                      | 🛠️                     | 🛠️                                      |
| Graded App Entrance       | 🚀                                                                                                             | 🛠️                                      | 🛠️                                      | 🛠️                     | 🛠️                                      |
| Multi-User Management     | ✅ User management 🚀 Resource isolation                                                                        | ✅ User management 🛠️ Resource isolation | ✅ User management 🛠️ Resource isolation | ❌                       | ✅ User management 🛠️ Resource isolation |
| Single Login for All Apps | 🚀                                                                                                             | ❌                                        | ❌                                        | ❌                       | ❌                                        |
| Cross-Node Storage        | 🚀 (Juicefs+ MinIO)                                                                                            | ❌                                        | ❌                                        | ❌                       | ❌                                        |
| Database Solution         | 🚀 (Built-in cloud-native solution)                                                                            | 🛠️                                      | 🛠️                                      | 🛠️                     | 🛠️                                      |
| Disaster Recovery         | 🚀 (MinIO's [**Erasure Coding**](https://min.io/docs/minio/linux/operations/concepts/erasure-coding.html)**)** | ✅ RAID                                   | ✅ RAID                                   | ✅ RAID                  | ✅ Unraid Storage                         |
| Backup                    | ✅ App Data ✅ User Data                                                                                         | ✅ User Data                              | ✅ User Data                              | ✅ User Data             | ✅ User Data                              |
| App Sandboxing            | ✅                                                                                                              | ❌                                        | ❌ (K8S's namespace)                      | ❌                       | ❌                                        |
| App Ecosystem             | ✅ (Official + third-party)                                                                                     | ✅ (Majorly official apps)                | ✅ (Official + third-party submissions)   | ✅ Majorly official apps | ✅ (Community app market)                 |
| Developer Friendly        | ✅ IDE ✅ CLI ✅ SDK ✅ Doc                                                                                        | ✅ CLI ✅ SDK ✅ Doc                        | ✅ CLI ✅ Doc                              | ✅ CLI ✅ Doc             | ✅ Doc                                    |
| Local LLM Hosting         | 🚀                                                                                                             | 🛠️                                      | 🛠️                                      | 🛠️                     | 🛠️                                      |
| Local LLM app development | 🚀                                                                                                             | 🛠️                                      | 🛠️                                      | 🛠️                     | 🛠️                                      |
| Client Platforms          | ✅ Android ✅ iOS ✅ Windows ✅ Mac ✅ Chrome Plugin                                                                | ✅ Android ✅ iOS                          | ❌                                        | ❌                       | ❌                                        |
| Client Functionality      | ✅ (All-in-one client app)                                                                                      | ✅ (14 separate client apps)              | ❌                                        | ❌                       | ❌                                        |

## Getting started

[](#getting-started)

### System compatibility

[](#system-compatibility)

Olares is available for Linux, Raspberry Pi, Mac, and Windows. It has been tested and verified on the following systems:

| Platform            | Operating system                | Notes                                                 |
| ------------------- | ------------------------------- | ----------------------------------------------------- |
| Linux               | Ubuntu 24.04 Debian 12.8        |                                                       |
| Raspberry Pi        | RaspbianOS                      | Verified on Raspberry Pi 4 Model B and Raspberry Pi 5 |
| Windows             | Windows 11 23H2 Windows 10 22H2 |                                                       |
| Mac (Apple silicon) | macOS Ventura 13.3.1            |                                                       |
| Proxmox VE (PVE)    | Proxmox Virtual Environment 8.0 |                                                       |

> **Note**
>
> If you successfully install Olares on an operating system that is not listed in the compatibility table, please let us know! You can [open an issue](https://github.com/beclab/Olares/issues/new) or submit a pull request on our GitHub repository.

### Set up Olares

[](#set-up-olares)

To get started with Olares on your own device, follow the [Getting Started Guide](https://docs.olares.xyz/manual/get-started/) for step-by-step instructions.

## Project navigation

[](#project-navigation)

Olares consists of numerous code repositories publicly available on GitHub. The current repository is responsible for the final compilation, packaging, installation, and upgrade of the operating system, while specific changes mostly take place in their corresponding repositories.

The following table lists the project directories under Olares and their corresponding repositories. Find the one that interests you:

**Framework components**

| Directory                                                                                       | Repository                                | Description                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [frameworks/app-service](https://github.com/beclab/olares/tree/main/frameworks/app-service)     | <https://github.com/beclab/app-service>   | A system framework component that provides lifecycle management and various security controls for all apps in the system.                                                                     |
| [frameworks/backup-server](https://github.com/beclab/olares/tree/main/frameworks/backup-server) | <https://github.com/beclab/backup-server> | A system framework component that provides scheduled full or incremental cluster backup services.                                                                                             |
| [frameworks/bfl](https://github.com/beclab/olares/tree/main/frameworks/bfl)                     | <https://github.com/beclab/bfl>           | Backend For Launcher (BFL), a system framework component serving as the user access point and aggregating and proxying interfaces of various backend services.                                |
| [frameworks/GPU](https://github.com/beclab/olares/tree/main/frameworks/GPU)                     | <https://github.com/grgalex/nvshare>      | GPU sharing mechanism that allows multiple processes (or containers running on Kubernetes) to securely run on the same physical GPU concurrently, each having the whole GPU memory available. |
| [frameworks/l4-bfl-proxy](https://github.com/beclab/olares/tree/main/frameworks/l4-bfl-proxy)   | <https://github.com/beclab/l4-bfl-proxy>  | Layer 4 network proxy for BFL. By prereading SNI, it provides a dynamic route to pass through into the user's Ingress.                                                                        |
| [frameworks/osnode-init](https://github.com/beclab/olares/tree/main/frameworks/osnode-init)     | <https://github.com/beclab/osnode-init>   | A system framework component that initializes node data when a new node joins the cluster.                                                                                                    |
| [frameworks/system-server](https://github.com/beclab/olares/tree/main/frameworks/system-server) | <https://github.com/beclab/system-server> | As a part of system runtime frameworks, it provides a mechanism for security calls between apps.                                                                                              |
| [frameworks/tapr](https://github.com/beclab/olares/tree/main/frameworks/tapr)                   | <https://github.com/beclab/tapr>          | Olares Application Runtime components.                                                                                                                                                        |

**System-Level Applications and Services**

| Directory                                                                           | Repository                                   | Description                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [apps/analytic](https://github.com/beclab/olares/tree/main/apps/analytic)           | <https://github.com/beclab/analytic>         | Developed based on [Umami](https://github.com/umami-software/umami), Analytic is a simple, fast, privacy-focused alternative to Google Analytics.                                                                                                    |
| [apps/market](https://github.com/beclab/olares/tree/main/apps/market)               | <https://github.com/beclab/market>           | This repository deploys the front-end part of the application market in Olares.                                                                                                                                                                      |
| [apps/market-server](https://github.com/beclab/olares/tree/main/apps/market-server) | <https://github.com/beclab/market>           | This repository deploys the back-end part of the application market in Olares.                                                                                                                                                                       |
| [apps/argo](https://github.com/beclab/olares/tree/main/apps/argo)                   | <https://github.com/argoproj/argo-workflows> | A workflow engine for orchestrating container execution of local recommendation algorithms.                                                                                                                                                          |
| [apps/desktop](https://github.com/beclab/olares/tree/main/apps/desktop)             | <https://github.com/beclab/desktop>          | The built-in desktop application of the system.                                                                                                                                                                                                      |
| [apps/devbox](https://github.com/beclab/olares/tree/main/apps/devbox)               | <https://github.com/beclab/devbox>           | An IDE for developers to port and develop Olares applications.                                                                                                                                                                                       |
| [apps/vault](https://github.com/beclab/olares/tree/main/apps/vault)                 | <https://github.com/beclab/termipass>        | A free alternative to 1Password and Bitwarden for teams and enterprises of any size Developed based on [Padloc](https://github.com/padloc/padloc). It serves as the client that helps you manage DID, Olares ID, and Olares devices.                 |
| [apps/files](https://github.com/beclab/olares/tree/main/apps/files)                 | <https://github.com/beclab/files>            | A built-in file manager modified from [Filebrowser](https://github.com/filebrowser/filebrowser), providing management of files on Drive, Sync, and various Olares physical nodes.                                                                    |
| [apps/notifications](https://github.com/beclab/olares/tree/main/apps/notifications) | <https://github.com/beclab/notifications>    | The notifications system of Olares                                                                                                                                                                                                                   |
| [apps/profile](https://github.com/beclab/olares/tree/main/apps/profile)             | <https://github.com/beclab/profile>          | Linktree alternative in Olares                                                                                                                                                                                                                       |
| [apps/rsshub](https://github.com/beclab/olares/tree/main/apps/rsshub)               | <https://github.com/beclab/rsshub>           | A RSS subscription manager based on [RssHub](https://github.com/DIYgod/RSSHub).                                                                                                                                                                      |
| [apps/settings](https://github.com/beclab/olares/tree/main/apps/settings)           | <https://github.com/beclab/settings>         | Built-in system settings.                                                                                                                                                                                                                            |
| [apps/system-apps](https://github.com/beclab/olares/tree/main/apps/system-apps)     | <https://github.com/beclab/system-apps>      | Built based on the *kubesphere/console* project, system-service provides a self-hosted cloud platform that helps users understand and control the system's runtime status and resource usage through a visual Dashboard and feature-rich ControlHub. |
| [apps/wizard](https://github.com/beclab/olares/tree/main/apps/wizard)               | <https://github.com/beclab/wizard>           | A wizard application to walk users through the system activation process.                                                                                                                                                                            |

**Third-party Components and Services**

| Directory                                                                                                           | Repository                                           | Description                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [third-party/authelia](https://github.com/beclab/olares/tree/main/third-party/authelia)                             | <https://github.com/beclab/authelia>                 | An open-source authentication and authorization server providing two-factor authentication and single sign-on (SSO) for your applications via a web portal. |
| [third-party/headscale](https://github.com/beclab/olares/tree/main/third-party/headscale)                           | <https://github.com/beclab/headscale>                | An open source, self-hosted implementation of the Tailscale control server in Olares to manage Tailscale in LarePass across different devices.              |
| [third-party/infisical](https://github.com/beclab/olares/tree/main/third-party/infisical)                           | <https://github.com/beclab/infisical>                | An open-source secret management platform that syncs secrets across your teams/infrastructure and prevents secret leaks.                                    |
| [third-party/juicefs](https://github.com/beclab/olares/tree/main/third-party/juicefs)                               | <https://github.com/beclab/juicefs-ext>              | A distributed POSIX file system built on top of Redis and S3, allowing apps on different nodes to access the same data via POSIX interface.                 |
| [third-party/ks-console](https://github.com/beclab/olares/tree/main/third-party/ks-console)                         | <https://github.com/kubesphere/console>              | Kubesphere console that allows for cluster management via a Web GUI.                                                                                        |
| [third-party/ks-installer](https://github.com/beclab/olares/tree/main/third-party/ks-installer)                     | <https://github.com/beclab/ks-installer-ext>         | Kubesphere installer component that automatically creates Kubesphere clusters based on cluster resource definitions.                                        |
| [third-party/kube-state-metrics](https://github.com/beclab/olares/tree/main/third-party/kube-state-metrics)         | <https://github.com/beclab/kube-state-metrics>       | kube-state-metrics (KSM) is a simple service that listens to the Kubernetes API server and generates metrics about the state of the objects.                |
| [third-party/notification-manager](https://github.com/beclab/olares/tree/main/third-party/notification-manager)     | <https://github.com/beclab/notification-manager-ext> | Kubesphere's notification management component for unified management of multiple notification channels and custom aggregation of notification content.     |
| [third-party/predixy](https://github.com/beclab/olares/tree/main/third-party/predixy)                               | <https://github.com/beclab/predixy>                  | Redis cluster proxy service that automatically identifies available nodes and adds namespace isolation.                                                     |
| [third-party/redis-cluster-operator](https://github.com/beclab/olares/tree/main/third-party/redis-cluster-operator) | <https://github.com/beclab/redis-cluster-operator>   | A cloud-native tool for creating and managing Redis clusters based on Kubernetes.                                                                           |
| [third-party/seafile-server](https://github.com/beclab/olares/tree/main/third-party/seafile-server)                 | <https://github.com/beclab/seafile-server>           | The backend service of Seafile (Sync Drive) for handling data storage.                                                                                      |
| [third-party/seahub](https://github.com/beclab/olares/tree/main/third-party/seahub)                                 | <https://github.com/beclab/seahub>                   | The front-end and middleware service of Seafile (Sync Drive) for handling file sharing, data synchronization, etc.                                          |
| [third-party/tailscale](https://github.com/beclab/olares/tree/main/third-party/tailscale)                           | <https://github.com/tailscale/tailscale>             | Tailscale has been integrated in LarePass of all platforms.                                                                                                 |

**Additional libraries and components**

| Directory                                                                     | Repository                         | Description                                                                        |
| ----------------------------------------------------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------- |
| [build/installer](https://github.com/beclab/olares/tree/main/build/installer) |                                    | The template for generating the installer build.                                   |
| [build/manifest](https://github.com/beclab/olares/tree/main/build/manifest)   |                                    | Installation build image list template.                                            |
| [libs/fs-lib](https://github.com/beclab/olares/tree/main/libs)                | <https://github.com/beclab/fs-lib> | The SDK library for the iNotify-compatible interface implemented based on JuiceFS. |
| [scripts](https://github.com/beclab/olares/tree/main/scripts)                 |                                    | Assisting scripts for generating the installer build.                              |

## Contributing to Olares

[](#contributing-to-olares)

We are welcoming contributions in any form:

* If you want to develop your own applications on Olares, refer to:\
  <https://docs.olares.xyz/developer/develop/>

* If you want to help improve Olares, refer to:\
  <https://docs.olares.xyz/developer/contribute/olares.html>

## Community & contact

[](#community--contact)

* [**GitHub Discussion**](https://github.com/beclab/olares/discussions). Best for sharing feedback and asking questions.
* [**GitHub Issues**](https://github.com/beclab/olares/issues). Best for filing bugs you encounter using Olares and submitting feature proposals.
* [**Discord**](https://discord.com/invite/BzfqrgQPDK). Best for sharing anything Olares.

## Staying ahead

[](#staying-ahead)

Star the Olares project to receive instant notifications about new releases and updates.

[![star us](https://camo.githubusercontent.com/e1f31e2699d4d29490aecd31c7ac2e638633915eebe5170fcbdb1411fa483b9d/68747470733a2f2f66696c652e62747463646e2e636f6d2f6769746875622f7465726d696e75732f7465726d696e75732e6769742e76322e676966)](https://camo.githubusercontent.com/e1f31e2699d4d29490aecd31c7ac2e638633915eebe5170fcbdb1411fa483b9d/68747470733a2f2f66696c652e62747463646e2e636f6d2f6769746875622f7465726d696e75732f7465726d696e75732e6769742e76322e676966)[![star us](https://camo.githubusercontent.com/e1f31e2699d4d29490aecd31c7ac2e638633915eebe5170fcbdb1411fa483b9d/68747470733a2f2f66696c652e62747463646e2e636f6d2f6769746875622f7465726d696e75732f7465726d696e75732e6769742e76322e676966) ](https://camo.githubusercontent.com/e1f31e2699d4d29490aecd31c7ac2e638633915eebe5170fcbdb1411fa483b9d/68747470733a2f2f66696c652e62747463646e2e636f6d2f6769746875622f7465726d696e75732f7465726d696e75732e6769742e76322e676966)     [](https://camo.githubusercontent.com/e1f31e2699d4d29490aecd31c7ac2e638633915eebe5170fcbdb1411fa483b9d/68747470733a2f2f66696c652e62747463646e2e636f6d2f6769746875622f7465726d696e75732f7465726d696e75732e6769742e76322e676966)

## Special thanks

[](#special-thanks)

The Olares project has incorporated numerous third-party open source projects, including: [Kubernetes](https://kubernetes.io/), [Kubesphere](https://github.com/kubesphere/kubesphere), [Padloc](https://padloc.app/), [K3S](https://k3s.io/), [JuiceFS](https://github.com/juicedata/juicefs), [MinIO](https://github.com/minio/minio), [Envoy](https://github.com/envoyproxy/envoy), [Authelia](https://github.com/authelia/authelia), [Infisical](https://github.com/Infisical/infisical), [Dify](https://github.com/langgenius/dify), [Seafile](https://github.com/haiwen/seafile),[HeadScale](https://headscale.net/), [tailscale](https://tailscale.com/), [Redis Operator](https://github.com/spotahome/redis-operator), [Nitro](https://nitro.jan.ai/), [RssHub](http://rsshub.app/), [predixy](https://github.com/joyieldInc/predixy), [nvshare](https://github.com/grgalex/nvshare), [LangChain](https://www.langchain.com/), [Quasar](https://quasar.dev/), [TrustWallet](https://trustwallet.com/), [Restic](https://restic.net/), [ZincSearch](https://zincsearch-docs.zinc.dev/), [filebrowser](https://filebrowser.org/), [lego](https://go-acme.github.io/lego/), [Velero](https://velero.io/), [s3rver](https://github.com/jamhall/s3rver), [Citusdata](https://www.citusdata.com/).


