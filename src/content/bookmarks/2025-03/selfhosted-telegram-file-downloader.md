---
title: "自托管Telegram文件下载器：稳定、持续且无人值守的下载方式"
slug: selfhosted-telegram-file-downloader
description: |
  jarvis2f的自托管Telegram文件下载器，支持从Telegram频道和群组下载文件。具有多Telegram账户支持、暂停和恢复下载、自动转移文件等功能，适用于桌面和移动端，提供流畅的用户体验。
tags: 
  - AI
  - dev
  - tool
  - telegram
  - download
pubDatetime: 2025-03-13T17:23:16+08:00
ogImage: https://opengraph.githubassets.com/641db824a40a97375e1676ed6f4f22a90066eecdc93d16e7e309406781f52c70/jarvis2f/telegram-files
---

[原文链接](https://github.com/jarvis2f/telegram-files)

---

[![](/jarvis2f/telegram-files/raw/main/web/public/favicon.svg)](https://github.com/jarvis2f/telegram-files/blob/main/web/public/favicon.svg)

# Telegram Files

[](#telegram-files)

*`A self-hosted Telegram file downloader for continuous, stable, and unattended downloads.`*

[![license](https://camo.githubusercontent.com/daffe68873fa14a73033b049d992ad8ef51734281aad2e043df62e0e20ae9bb4/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6a617276697332662f74656c656772616d2d66696c65733f7374796c653d64656661756c74266c6f676f3d6f70656e736f75726365696e6974696174697665266c6f676f436f6c6f723d776869746526636f6c6f723d303038306666)](https://camo.githubusercontent.com/daffe68873fa14a73033b049d992ad8ef51734281aad2e043df62e0e20ae9bb4/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6a617276697332662f74656c656772616d2d66696c65733f7374796c653d64656661756c74266c6f676f3d6f70656e736f75726365696e6974696174697665266c6f676f436f6c6f723d776869746526636f6c6f723d303038306666) [![last-commit](https://camo.githubusercontent.com/15d8a296c92ea67af1260e6c1150e29774747bf61ac73137c80283dbae019965/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6173742d636f6d6d69742f6a617276697332662f74656c656772616d2d66696c65733f7374796c653d64656661756c74266c6f676f3d676974266c6f676f436f6c6f723d776869746526636f6c6f723d303038306666)](https://camo.githubusercontent.com/15d8a296c92ea67af1260e6c1150e29774747bf61ac73137c80283dbae019965/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6173742d636f6d6d69742f6a617276697332662f74656c656772616d2d66696c65733f7374796c653d64656661756c74266c6f676f3d676974266c6f676f436f6c6f723d776869746526636f6c6f723d303038306666) [![release](https://camo.githubusercontent.com/1c9893ec7db162f669490df9a7c3b19ddde4b7829c24c175a214b7d52fa1e7d8/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f6a617276697332662f74656c656772616d2d66696c65733f7374796c653d64656661756c74266c6f676f3d676974266c6f676f436f6c6f723d776869746526636f6c6f723d303038306666)](https://camo.githubusercontent.com/1c9893ec7db162f669490df9a7c3b19ddde4b7829c24c175a214b7d52fa1e7d8/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f6a617276697332662f74656c656772616d2d66696c65733f7374796c653d64656661756c74266c6f676f3d676974266c6f676f436f6c6f723d776869746526636f6c6f723d303038306666) [![](https://camo.githubusercontent.com/54606588210bb0038722af6da38e3bfc508ca6f2044bb4a0adeafa97f5739b2c/68747470733a2f2f636f6465636f762e696f2f67682f6a617276697332662f74656c656772616d2d66696c65732f67726170682f62616467652e7376673f746f6b656e3d5934594e325738415256)](https://codecov.io/gh/jarvis2f/telegram-files)

\


## 🔗 Table of Contents

[](#-table-of-contents)

* [📍 Overview](#-overview)

* [🧩 Screenshots](#-screenshots)

* [🚀 Getting Started](#-getting-started)

* [⌨️ Development](#%EF%B8%8F-development)

  * [☑️ Prerequisites](#-prerequisites)
  * [⚙️ Installation](#-installation)

* [📌 Project Roadmap](#-project-roadmap)

* [🔰 Contributing](#-contributing)

* [🎗 License](#-license)

* [🆗 FAQs](#-faqs)

***

## 📍 Overview

[](#-overview)

* Support for downloading files from telegram channels and groups.
* Support multiple telegram accounts for downloading files.
* Support suspending and resuming downloads, and auto transfer files to other destinations.
* Preview of downloaded videos and pictures.
* Responsive design supports mobile access, PWAs, and offline access.

***

## 🧩 Screenshots

[](#-screenshots)

[![](/jarvis2f/telegram-files/raw/main/misc/preview-files-pc.gif)](https://github.com/jarvis2f/telegram-files/blob/main/misc/preview-files-pc.gif) [![preview-files-pc.gif](https://github.com/jarvis2f/telegram-files/raw/main/misc/preview-files-pc.gif) ](https://github.com/jarvis2f/telegram-files/blob/main/misc/preview-files-pc.gif)     [ ](https://github.com/jarvis2f/telegram-files/blob/main/misc/preview-files-pc.gif)[![](/jarvis2f/telegram-files/raw/main/misc/preview-files-mobile.gif)](https://github.com/jarvis2f/telegram-files/blob/main/misc/preview-files-mobile.gif)[![preview-files-mobile.gif](https://github.com/jarvis2f/telegram-files/raw/main/misc/preview-files-mobile.gif) ](https://github.com/jarvis2f/telegram-files/blob/main/misc/preview-files-mobile.gif)     [](https://github.com/jarvis2f/telegram-files/blob/main/misc/preview-files-mobile.gif)

More Screenshots

[![](/jarvis2f/telegram-files/raw/main/misc/screenshot-3.png)](https://github.com/jarvis2f/telegram-files/blob/main/misc/screenshot-3.png) [![](/jarvis2f/telegram-files/raw/main/misc/screenshot-4.png)](https://github.com/jarvis2f/telegram-files/blob/main/misc/screenshot-4.png)

[![](/jarvis2f/telegram-files/raw/main/misc/screenshot.png)](https://github.com/jarvis2f/telegram-files/blob/main/misc/screenshot.png) [![](/jarvis2f/telegram-files/raw/main/misc/screenshot-2.png)](https://github.com/jarvis2f/telegram-files/blob/main/misc/screenshot-2.png)

## 🚀 Getting Started

[](#-getting-started)

Before getting started with telegram-files, you should apply a telegram api id and hash. You can apply for it on the [Telegram API](https://my.telegram.org/apps) page.

**Using `docker`**   [![](https://camo.githubusercontent.com/58473405fa60cfb13b6557eba57da7500545e5e519e9f8d097955edf157234b9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f636b65722d3243413545302e7376673f7374796c653d7b62616467655f7374796c657d266c6f676f3d646f636b6572266c6f676f436f6c6f723d7768697465)](https://www.docker.com/)

```
docker run -d \
  --name telegram-files \
  --restart always \
  -e APP_ENV=${APP_ENV:-prod} \
  -e APP_ROOT=${APP_ROOT:-/app/data} \
  -e TELEGRAM_API_ID=${TELEGRAM_API_ID} \
  -e TELEGRAM_API_HASH=${TELEGRAM_API_HASH} \
  -p 6543:80 \
  -v ./data:/app/data \
  ghcr.io/jarvis2f/telegram-files:latest
```

**Using `docker-compose`**

Copy [docker-compose.yaml](https://github.com/jarvis2f/telegram-files/blob/main/docker-compose.yaml) and [.env.example](https://github.com/jarvis2f/telegram-files/blob/main/.env.example) to your project directory and run the following command:

```
docker-compose up -d
```

**Install on unRaid**

On unRaid, install from the Community Repositories by searching for `telegram-files`.

> **Important Note:** You should NOT expose the service to the public internet. Because the service is not secure.

***

## ⌨️ Development

[](#️-development)

### ☑️ Prerequisites

[](#️-prerequisites)

Before getting started with telegram-files, ensure your runtime environment meets the following requirements:

* **Programming Language:** JDK21,TypeScript
* **Package Manager:** Gradle,Npm
* **Container Runtime:** Docker

### ⚙️ Installation

[](#️-installation)

Install telegram-files using one of the following methods:

**Build from source:**

1. Clone the telegram-files repository:

```
git clone https://github.com/jarvis2f/telegram-files
```

2. Navigate to the project directory:

```
cd telegram-files
```

3. Install the project dependencies:

**Using `npm`**   [![](https://camo.githubusercontent.com/a4266152579248887b8275ad10755bf278eb2a326742930933521697e7933e40/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6e706d2d4342333833372e7376673f7374796c653d7b62616467655f7374796c657d266c6f676f3d6e706d266c6f676f436f6c6f723d7768697465)](https://www.npmjs.com/)

```
cd web
npm install
```

**Using `gradle`**   [![](https://camo.githubusercontent.com/129fe673be4d66224279e0b45674a37162e9747d7df1af87884e636fd20b2727/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f477261646c652d3032333033412e7376673f7374796c653d7b62616467655f7374796c657d266c6f676f3d677261646c65266c6f676f436f6c6f723d7768697465)](https://gradle.org/)

```
cd api
gradle build
```

**Using `docker`**   [![](https://camo.githubusercontent.com/58473405fa60cfb13b6557eba57da7500545e5e519e9f8d097955edf157234b9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f636b65722d3243413545302e7376673f7374796c653d7b62616467655f7374796c657d266c6f676f3d646f636b6572266c6f676f436f6c6f723d7768697465)](https://www.docker.com/)

```
docker build -t jarvis2f/telegram-files .
```

## 📌 Project Roadmap

[](#-project-roadmap)

* ✅ **`Task 1`**: Automatically download files based on set rules.
* ✅ **`Task 2`**: Download statistics and reports.
* ✅ **`Task 3`**: Improve Telegram’s login functionality.
* ✅ **`Task 4`**: Support auto transfer files to other destinations.
* ✅ **`Task 5`**: File table is optimized using virtual lists.
* ✅ **`Task 6`**: Preload file information to support responsible searches.

***

## 🔰 Contributing

[](#-contributing)

* **💬 [Join the Discussions](https://github.com/jarvis2f/telegram-files/discussions)**: Share your insights, provide feedback, or ask questions.
* **🐛 [Report Issues](https://github.com/jarvis2f/telegram-files/issues)**: Submit bugs found or log feature requests for the `telegram-files` project.
* **💡 [Submit Pull Requests](https://github.com/jarvis2f/telegram-files/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

Contributing Guidelines

1. **Fork the Repository**: Start by forking the project repository to your github account.

2. **Clone Locally**: Clone the forked repository to your local machine using a git client.

   ```
   git clone https://github.com/jarvis2f/telegram-files
   ```

3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.

   ```
   git checkout -b new-feature-x
   ```

4. **Make Your Changes**: Develop and test your changes locally.

5. **Commit Your Changes**: Commit with a clear message describing your updates.

   ```
   git commit -m 'Implemented new feature x.'
   ```

6. **Push to github**: Push the changes to your forked repository.

   ```
   git push origin new-feature-x
   ```

7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!

***

## 🎗 License

[](#-license)

This project is protected under the MIT License. For more details, refer to the [LICENSE](https://github.com/jarvis2f/telegram-files/blob/main/LICENSE) file.

***

## 🆗 FAQs

[](#-faqs)

~~**Q.** Can't start the api server, error：`java.lang.UnsatisfiedLinkError: no tdjni in java.library.path`~~

~~**A.** Maybe download tdlib failed, you can see the [entrypoint.sh](https://github.com/jarvis2f/telegram-files/blob/main/entrypoint.sh) file, then download tdlib manually.~~

**Q.** Web's spoiler is static, how to solve it?

**A.** 1. Because `CSS Houdini Paint API` is not supported by all browsers. 2. It is only supported on https.

Use in http environment, you can use the following method to solve it

Open the `chrome://flags` page, search for `Insecure origins treated as secure`, and add the address of the web page to the list.

**Q.** How to use the telegram-files maintenance tool?

**A.** You can use the following command to run the maintenance tool(**before running the command, you should stop telegram-files container**):

Command

```
docker run --rm \
  --entrypoint /bin/bash \
  -v $(pwd)/data:/app/data \
  -e APP_ROOT=${APP_ROOT:-/app/data} \
  -e TELEGRAM_API_ID=${TELEGRAM_API_ID} \
  -e TELEGRAM_API_HASH=${TELEGRAM_API_HASH} \
  ghcr.io/jarvis2f/telegram-files:latest tfm ${Maintenance Command}
```

**Maintenance Command:**

* `album-caption`: Fixed issue with missing caption for album messages before `0.1.15`.


