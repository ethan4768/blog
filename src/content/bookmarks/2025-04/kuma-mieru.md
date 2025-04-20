---
title: "Kuma Mieru：基于 Next.js 15 的 Uptime Kuma 监控仪表盘"
slug: kuma-mieru
description: |
  Kuma Mieru 是一款基于 Next.js 15、TypeScript 和 Recharts 构建的第三方 Uptime Kuma 监控仪表盘。它提供实时监控、交互式图表和多主题支持，极大地提升了 Uptime Kuma 的可视化效果。
tags: 
  - AI
  - dev
  - tool
  - dashboard
  - typescript
pubDatetime: 2025-04-20T17:14:15+08:00
ogImage: https://opengraph.githubassets.com/2c751bc646bd12acd839c52c85a6862cb54df6c6eea10c137e4e97c211d0041c/Alice39s/kuma-mieru
---

[原文链接](https://github.com/Alice39s/kuma-mieru)

---

# Kuma Mieru 🚥

[](#kuma-mieru-traffic_light)

Kuma Mieru 是一款基于 Next.js 15、TypeScript 和 Recharts 构建的第三方 Uptime Kuma 监控仪表盘。

本项目使用 Recharts 解决了 Uptime Kuma 内建公开状态页面不够直观、没有延迟图表等痛点。

中文版 | [English Version](https://github.com/Alice39s/kuma-mieru/blob/main/README.en.md)

Warning

新版 (v1.1.4+) 重构了时间处理逻辑，请注意修改 *Uptime Kuma* 后台设置的 `Display Timezone` (显示时区) 为 `UTC+0` 时区。

[![Release](https://camo.githubusercontent.com/1823cd555d4e4f7662b032d44911ad1fb224c5021264d4ebba39bc28bd8b7820/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f416c6963653339732f6b756d612d6d696572753f7374796c653d666c61742d73717561726526636f6c6f723d626c7565266c6162656c3d52656c65617365)](https://github.com/Alice39s/kuma-mieru/releases/latest) [![License](https://camo.githubusercontent.com/360c720358a82a543b3127b2b6ab65b9d138bd4265ab2736746d1adc4fc493a4/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f416c6963653339732f6b756d612d6d696572753f7374796c653d666c61742d73717561726526636f6c6f723d626c7565)](https://github.com/Alice39s/kuma-mieru/blob/main/LICENSE) [![Release](https://camo.githubusercontent.com/7d4c5590e40ae4106c1cc0b35e798369b416f593107060f7c752e5915c965fe2/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f416c6963653339732f6b756d612d6d696572752f72656c656173652e796d6c3f6272616e63683d6d61696e267374796c653d666c61742d737175617265266c6f676f3d676974687562266c6162656c3d52656c65617365)](https://github.com/Alice39s/kuma-mieru/actions/workflows/release.yml) [![Docker](https://camo.githubusercontent.com/c0cba08e69ee48b71e715153ef85545620280eb983c5a2a78135b81672953e2b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f416c6963653339732f6b756d612d6d696572752f646f636b65722d6275696c642e796d6c3f6272616e63683d6d61696e267374796c653d666c61742d737175617265266c6f676f3d646f636b6572266c6162656c3d446f636b6572)](https://github.com/Alice39s/kuma-mieru/actions/workflows/docker-build.yml)

[![TypeScript](https://camo.githubusercontent.com/6dbef1ca6166bfbfe91c0eebdcf1eae67f3b80dee8bcad760902e0dfc3ac9d06/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f547970655363726970742d3030374143433f7374796c653d666c61742d737175617265266c6f676f3d74797065736372697074266c6f676f436f6c6f723d7768697465)](https://www.typescriptlang.org/) [![React](https://camo.githubusercontent.com/338096f570b39e527d6a64c5d60156039ae5614c5f6278e5927c3f9833d5e367/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f52656163742d7631392d3338374341303f7374796c653d666c61742d737175617265266c6f676f3d7265616374266c6f676f436f6c6f723d7768697465)](https://reactjs.org/) [![Next.js](https://camo.githubusercontent.com/83fbf09ee4ae64ea3c898254f1690c579e99ebaab733de03983c6685a6ac1621/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4e6578742e6a732d31352d626c61636b3f7374796c653d666c61742d737175617265266c6f676f3d6e6578742e6a73266c6f676f436f6c6f723d7768697465)](https://nextjs.org/)

[![Bun](https://camo.githubusercontent.com/6dc1a30ba898550ea4b0fccc109a5ab356a6f4cc15b9e380125e7db5a3c77071/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f42756e2d5061636b6167652532304d616e616765722d3134313531413f7374796c653d666c61742d737175617265266c6f676f3d62756e266c6f676f436f6c6f723d7768697465)](https://bun.sh/) [![Recharts](https://camo.githubusercontent.com/dbfe91d0ebd29173145b5408f8e90393e7267f854bf8f25862a3e0d5fde7afab/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f52656368617274732d4368617274696e672532304c6962726172792d3838383464383f7374796c653d666c61742d737175617265266c6f676f3d7265636861727473266c6f676f436f6c6f723d7768697465)](https://recharts.org/en-US/) [![Tailwind CSS](https://camo.githubusercontent.com/e8eaa22e4aae86582d2a33662ff3763a1619e5f4935008a7a7160d9b436c7703/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5461696c77696e642532304353532d76332d3445423946413f7374796c653d666c61742d737175617265266c6f676f3d7461696c77696e642d637373266c6f676f436f6c6f723d7768697465)](https://v3.tailwindcss.com/)

[![Stars](https://camo.githubusercontent.com/60422a719b135af49ea186712825fe5402e54daa3f0cad62b31e4dc4e77a9f64/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f416c6963653339732f6b756d612d6d696572753f7374796c653d666c61742d737175617265266c6f676f3d67697468756226636f6c6f723d79656c6c6f77266c6162656c3d5374617273)](https://github.com/Alice39s/kuma-mieru/stargazers) [![Forks](https://camo.githubusercontent.com/b6b9d8bee4f9cefe9f25ad8a5e96eb4b64d75ff32830495f392b395c5cc6deb4/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f416c6963653339732f6b756d612d6d696572753f7374796c653d666c61742d737175617265266c6f676f3d67697468756226636f6c6f723d79656c6c6f77266c6162656c3d466f726b73)](https://github.com/Alice39s/kuma-mieru/network/members)

## 目录

[](#目录)

* [目录](#%E7%9B%AE%E5%BD%95)

* [功能亮点 ✨](#%E5%8A%9F%E8%83%BD%E4%BA%AE%E7%82%B9-sparkles)

* [测试截图 📷](#%E6%B5%8B%E8%AF%95%E6%88%AA%E5%9B%BE-camera)

* [快速部署 ⭐](#%E5%BF%AB%E9%80%9F%E9%83%A8%E7%BD%B2-star)

  * [使用 Vercel 部署 (推荐)](#%E4%BD%BF%E7%94%A8-vercel-%E9%83%A8%E7%BD%B2-%E6%8E%A8%E8%8D%90)

    * [1. Fork 仓库](#1-fork-%E4%BB%93%E5%BA%93)
    * [2. 导入到 Vercel](#2-%E5%AF%BC%E5%85%A5%E5%88%B0-vercel)
    * [3. 配置环境变量](#3-%E9%85%8D%E7%BD%AE%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F)
    * [4. 更新仓库](#4-%E6%9B%B4%E6%96%B0%E4%BB%93%E5%BA%93)

  * [本地部署](#%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2)

* [Docker 部署 🐳 (Beta)](#docker-%E9%83%A8%E7%BD%B2-whale-beta)

  * [使用 Docker Compose（推荐）](#%E4%BD%BF%E7%94%A8-docker-compose-%E6%8E%A8%E8%8D%90)

  * [Docker Run 部署](#docker-run-%E9%83%A8%E7%BD%B2)

    * [1. 获取容器镜像](#1-%E8%8E%B7%E5%8F%96%E5%AE%B9%E5%99%A8%E9%95%9C%E5%83%8F)
    * [2. 修改环境变量](#2-%E4%BF%AE%E6%94%B9%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F)
    * [3. 启动容器服务](#3-%E5%90%AF%E5%8A%A8%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1)

* [环境变量配置](#%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E9%85%8D%E7%BD%AE)

* [与 Uptime Kuma 集成 🔗](#%E4%B8%8E-uptime-kuma-%E9%9B%86%E6%88%90-link)

* [FAQ ❓](#faq-question)

  * [为什么我在 Kuma Mieru 中看到的时间与 Uptime Kuma 中有偏移？](#%E4%B8%BA%E4%BB%80%E4%B9%88%E6%88%91%E5%9C%A8-kuma-mieru-%E4%B8%AD%E7%9C%8B%E5%88%B0%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E-uptime-kuma-%E4%B8%AD%E6%9C%89%E5%81%8F%E7%A7%BB)
  * [请问兼容 Uptime Robot / Better Stack / 其他监控数据源吗？](#%E8%AF%B7%E9%97%AE%E5%85%BC%E5%AE%B9-uptime-robot-better-stack-%E5%85%B6%E4%BB%96%E7%9B%91%E6%8E%A7%E6%95%B0%E6%8D%AE%E6%BA%90%E5%90%97)

* [贡献指南 🤝](#%E8%B4%A1%E7%8C%AE%E6%8C%87%E5%8D%97-handshake)

* [Star History 🌟](#star-history-star2)

* [开源许可 🔒](#%E5%BC%80%E6%BA%90%E8%AE%B8%E5%8F%AF-lock)

## 功能亮点 ✨

[](#功能亮点-sparkles)

* **实时监控，自动刷新** 🔃：状态显示**实时更新**，无需手动刷新，随时掌握最新动态。
* **美观响应式界面** 🎨：采用 **HeroUI 组件** 构建，界面更加现代，**完美适配**各种设备屏幕。
* **交互式图表** 📈：利用 **Recharts** 图表库实现数据可视化，可以 **交互式** 地查看各节点的延迟、状态等数据。
* **多主题支持** 💡：提供 **暗色** / **亮色** / **系统** 多种主题，满足不同偏好。
* **维护公告**：支持 Uptime Kuma 的 **事件公告** 和 **状态更新** 特性，实时同步更高效。

## 测试截图 📷

[](#测试截图-camera)

| Dark Mode                                                                                                                                       | Light Mode                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [![Dark Mode](/Alice39s/kuma-mieru/raw/main/docs/v1.2.1-dark-zh.png)](https://github.com/Alice39s/kuma-mieru/blob/main/docs/v1.2.1-dark-zh.png) | [![Light Mode](/Alice39s/kuma-mieru/raw/main/docs/v1.2.1-light-zh.png)](https://github.com/Alice39s/kuma-mieru/blob/main/docs/v1.2.1-light-zh.png) |

## 快速部署 ⭐

[](#快速部署-star)

### 使用 Vercel 部署 (推荐)

[](#使用-vercel-部署-推荐)

#### 1. Fork 仓库

[](#1-fork-仓库)

Fork 本仓库到您的 GitHub 用户下，如图所示：

1. 在这里 [Fork](https://github.com/Alice39s/kuma-mieru/fork) 本仓库
2. 点击 `Create fork` 按钮

Note

请确保您 Fork 的仓库是公开的，否则后续可能无法快速同步本仓库的更新。

请放心，您所有的配置均使用环境变量配置，Fork 的代码库 **不会泄漏** 您的任何配置信息。

#### 2. 导入到 Vercel

[](#2-导入到-vercel)

进入 <https://vercel.com/new> ，选择 Import 刚才 Fork 的仓库，如图所示：

[![导入仓库](/Alice39s/kuma-mieru/raw/main/docs/vercel-import.png)](https://github.com/Alice39s/kuma-mieru/blob/main/docs/vercel-import.png)

#### 3. 配置环境变量

[](#3-配置环境变量)

Note

请确保您已经配置了 `UPTIME_KUMA_BASE_URL` 和 `PAGE_ID` 两个环境变量，否则无法正常显示监控数据。

关于 `UPTIME_KUMA_BASE_URL` 和 `PAGE_ID` 等配置，请参考 [环境变量配置](#%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E9%85%8D%E7%BD%AE) 一节。

1. 点击 `Environment Variables` 添加 `UPTIME_KUMA_BASE_URL` 和 `PAGE_ID` 两个环境变量，如图所示：

[![部署到 Vercel](/Alice39s/kuma-mieru/raw/main/docs/vercel-deploy.png)](https://github.com/Alice39s/kuma-mieru/blob/main/docs/vercel-deploy.png)

2. 点击 `Deploy` 按钮即可一键部署到 Vercel

#### 4. 更新仓库

[](#4-更新仓库)

1. 进入你 Fork 的 GitHub 仓库，点击 `Sync fork` 按钮
2. 点击 `Update branch` 按钮，即可自动同步本仓库的最新代码

### 本地部署

[](#本地部署)

只需简单几步，即可快速启动 Kuma Mieru：

1. **克隆仓库**

   ```
   git clone https://github.com/Alice39s/kuma-mieru.git
   cd kuma-mieru
   ```

2. **安装依赖**

   Kuma Mieru 使用 [Bun](https://bun.sh/) 作为包管理器，您需要先安装 Bun：

   ```
   # Linux/macOS
   curl -fsSL https://bun.sh/install | bash
   # Windows
   powershell -c "irm bun.sh/install.ps1 | iex"
   ```

   然后再安装依赖包：

   ```
   bun install
   ```

3. **配置环境变量** 复制 `.env.example` 文件为 `.env`：

   ```
   cp .env.example .env
   ```

   `.env` 文件中 **必填** 的环境变量，可参考 [环境变量配置](#%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E9%85%8D%E7%BD%AE) 章节。

4. **启动开发服务器**

   ```
   bun run dev
   ```

5. **访问仪表盘** 打开浏览器，访问 <http://localhost:3883> 即可查看您的 Kuma Mieru 监控仪表盘。

6. **部署上线**

   ```
   bun run build
   bun run start
   ```

## Docker 部署 🐳 (Beta)

[](#docker-部署-whale-beta)

### 使用 Docker Compose（推荐）

[](#使用-docker-compose推荐)

1. **克隆仓库**

   ```
   git clone https://github.com/Alice39s/kuma-mieru.git
   cd kuma-mieru
   ```

2. **配置环境变量** 复制 `.env.example` 文件并创建 `.env` 文件：

   ```
   cp .env.example .env
   ```

   参考 [环境变量配置](#%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E9%85%8D%E7%BD%AE) 章节，配置必要的环境变量。

3. **启动服务**

   ```
   docker compose up -d
   ```

   > \[!NOTE] 如果需要更新镜像，可以添加 `--build` 参数：

   ```
   docker compose up -d --build
   ```

   服务将在 `http://0.0.0.0:3883` 上运行。

4. **查看日志**

   ```
   docker compose logs -f
   ```

### Docker Run 部署

[](#docker-run-部署)

#### 1. 获取容器镜像

[](#1-获取容器镜像)

**从源码构建镜像**

```
docker build -t kuma-mieru .
```

#### 2. 修改环境变量

[](#2-修改环境变量)

复制 `.env.example` 文件并创建 `.env` 文件：

```
cp .env.example .env
```

请参考 [环境变量配置](#%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E9%85%8D%E7%BD%AE) 章节，修改 `.env` 文件中的 `UPTIME_KUMA_BASE_URL` 和 `PAGE_ID` 变量。

#### 3. 启动容器服务

[](#3-启动容器服务)

**使用源码构建镜像**

```
docker run -d \
  --name kuma-mieru \
  -p 3883:3000 \
  -e UPTIME_KUMA_BASE_URL="..." \
  -e PAGE_ID="..." \
  kuma-mieru
```

## 环境变量配置

[](#环境变量配置)

首先，假设您的 Uptime Kuma 的状态页面 URL 为 `https://example.kuma-mieru.invalid/status/test1`

那么您需要配置的环境变量如下：

| 变量名                         | 必填  | 说明                       | 示例/默认值                                             |
| --------------------------- | --- | ------------------------ | -------------------------------------------------- |
| UPTIME\_KUMA\_BASE\_URL     | Yes | Uptime Kuma 实例的基础 URL    | <https://example.kuma-mieru.invalid>               |
| PAGE\_ID                    | Yes | Uptime Kuma 实例的状态页面 ID   | test1                                              |
| FEATURE\_EDIT\_THIS\_PAGE   | No  | 是否展示 "Edit This Page" 按钮 | false                                              |
| FEATURE\_SHOW\_STAR\_BUTTON | No  | 是否展示 "Star on Github" 按钮 | true                                               |
| FEATURE\_TITLE              | No  | 自定义页面标题                  | Kuma Mieru                                         |
| FEATURE\_DESCRIPTION        | No  | 自定义页面描述                  | A beautiful and modern uptime monitoring dashboard |
| FEATURE\_ICON               | No  | 自定义页面图标URL               | /icon.svg                                          |

## 与 Uptime Kuma 集成 🔗

[](#与-uptime-kuma-集成-link)

Note

经测试，本项目兼容 Uptime Kuma 的最新稳定版本 (v1.23.0+)

如您使用的版本较低，请参考 [Uptime Kuma 官方文档](https://github.com/louislam/uptime-kuma/wiki/%F0%9F%86%99-How-to-Update) 尝试升级到最新稳定版 (v1.23.0+)，注意备份好数据。

Kuma Mieru 与备受好评的开源监控工具 [Uptime Kuma](https://github.com/louislam/uptime-kuma) 无缝集成，您只需要：

1. 安装并配置 Uptime Kuma
2. 在 Uptime Kuma 设置中修改 `Display Timezone` (显示时区) 为任意 `UTC+0` 时区
3. 在 Uptime Kuma 中创建 "状态页面"
4. 在 `.env` 文件中配置环境变量

## FAQ ❓

[](#faq-question)

### 为什么我在 Kuma Mieru 中看到的时间与 Uptime Kuma 中有偏移？

[](#为什么我在-kuma-mieru-中看到的时间与-uptime-kuma-中有偏移)

由于 Uptime Kuma 后端传递到前端的时间 **没有携带时区信息**，为了方便开发，Kuma Mieru 会 **自动将时间转换为 UTC+0 时区** 并显示。

如果您发现时区偏移，请前往 Uptime Kuma 设置中修改 `Display Timezone` (显示时区) 为任意 `UTC+0` 时区。

### 请问兼容 Uptime Robot / Better Stack / 其他监控数据源吗？

[](#请问兼容-uptime-robot--better-stack--其他监控数据源吗)

Kuma Mieru 设计之初就是为了解决 Uptime Kuma 的不足，所以 v1 暂时不考虑支持其他监控数据源。

不过 v2 版本可能会考虑支持 Uptime Robot / Better Stack 等其他监控工具的 API 接口。

## 贡献指南 🤝

[](#贡献指南-handshake)

非常欢迎您为 Kuma Mieru 项目作出贡献！

如果您有任何想法或建议，请参阅 [CONTRIBUTING.md](https://github.com/Alice39s/kuma-mieru/blob/main/CONTRIBUTING.md) 了解详细的贡献方式。

## Star History 🌟

[](#star-history-star2)

[![Star History Chart](https://camo.githubusercontent.com/a8947c398f264a931c20c9827dfcbb4e8511aa514b67881a76746d9da264c25e/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d416c6963653339732f6b756d612d6d6965727526747970653d54696d656c696e65)](https://github.com/Alice39s/kuma-mieru/stargazers)

## 开源许可 🔒

[](#开源许可-lock)

本项目采用 [MPL-2.0](https://github.com/Alice39s/kuma-mieru/blob/main/LICENSE) (Mozilla Public License Version 2.0) 开源许可证。


