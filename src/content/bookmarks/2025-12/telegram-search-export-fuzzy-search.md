---
title: "Telegram Search: 高效导出和模糊搜索你的 Telegram 聊天记录"
slug: telegram-search-export-fuzzy-search
description: |
  Telegram Search 是一款强大的工具，支持导出和模糊搜索 Telegram 聊天记录。它采用先进的AI语义搜索技术，能够准确识别和查找多语言聊天信息，提升消息检索的准确性和效率。立即体验便捷的聊天记录管理！
tags: 
  - tool
pubDatetime: 2025-12-16T11:55:45+08:00
ogImage: https://repository-images.githubusercontent.com/929338255/79f38ce0-f48c-437d-9fd9-2f7c80b58bf7
---

[原文链接](https://github.com/groupultra/telegram-search?tab=readme-ov-file)

---

[![preview](/groupultra/telegram-search/raw/main/docs/assets/preview.png)](https://github.com/groupultra/telegram-search/blob/main/docs/assets/preview.png)

***

[![groupultra%2Ftelegram-search | Trendshift](https://camo.githubusercontent.com/d37e6d8992dc90957f9ad93d0c86885cf2411b7d2b160304ebfcbab0c3a05c68/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7265706f7369746f726965732f3133383638)](https://trendshift.io/repositories/13868)

\[[立即体验](https://search.lingogram.app)] \[[English](https://github.com/groupultra/telegram-search/blob/main/docs/README_EN.md)] \[[日本語](https://github.com/groupultra/telegram-search/blob/main/docs/README_JA.md)]

[![Discord](https://camo.githubusercontent.com/b08b149a8bb87b30a464be2ae7ea7800c534b37f87d1af40e28b95ebc14af1f9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f64796e616d69632f6a736f6e3f75726c3d6874747073253341253246253246646973636f72642e636f6d253246617069253246696e76697465732532464e7a59736d4a53674354253346776974685f636f756e7473253344747275652671756572793d2532342e617070726f78696d6174655f6d656d6265725f636f756e74267375666669783d2532306d656d62657273266c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465266c6162656c3d25323026636f6c6f723d373338394438266c6162656c436f6c6f723d364137454332) ](https://discord.gg/NzYsmJSgCT)[![Telegram](https://camo.githubusercontent.com/827b3222c9f7e8979684bbe4f4e14054123524e2e048621c0fa3febcee5e51c6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f54656c656772616d2d2532333541413945363f6c6f676f3d74656c656772616d266c6162656c436f6c6f723d464646464646) ](https://t.me/+Gs3SH2qAPeFhYmU9)[![DeepWiki](https://camo.githubusercontent.com/0f5ae213ac378635adeb5d7f13cef055ad2f7d9a47b36de7b1c67dbe09f609ca/68747470733a2f2f6465657077696b692e636f6d2f62616467652e737667)](https://deepwiki.com/groupultra/telegram-search)\
[![GitHub Package Version](https://camo.githubusercontent.com/e6234b76780394eec867b321d63617782040e963451a02cb11c3c1f1c58594e5/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7061636b6167652d6a736f6e2f762f67726f7570756c7472612f74656c656772616d2d7365617263683f7374796c653d666c617426636f6c6f72413d30383066313226636f6c6f72423d316661363639) ](https://github.com/groupultra/telegram-search/releases)[![Release Docker / OCI](https://github.com/groupultra/telegram-search/actions/workflows/release-docker.yaml/badge.svg) ](https://github.com/groupultra/telegram-search/actions/workflows/release-docker.yaml)[![CI](https://github.com/groupultra/telegram-search/actions/workflows/ci.yaml/badge.svg)](https://github.com/groupultra/telegram-search/actions/workflows/ci.yaml)

Tip

您是否曾因 Telegram 无法搜索中文聊天记录而苦恼？

或者想查找一条重要消息，却因消息过多而难以定位？

现在，使用 Telegram Search，您可以轻松查找和导出自己的 Telegram 消息。强大的语义搜索支持所有语言，完美应对无分词句子的检索场景。

同时支持向量搜索，实现句子级别的模糊匹配，让查找更智能、更准确。

## 💖 赞助者

[](#-赞助者)

[![Sponsors](https://github.com/luoling8192/luoling8192/raw/master/sponsorkit/sponsors.svg)](https://github.com/luoling8192/luoling8192/raw/master/sponsorkit/sponsors.svg)

## ✅ 功能特性

[](#-功能特性)

### 📦 导出与备份

[](#-导出与备份)

* [x] 支持多种数据库导出聊天记录：PGlite、PostgreSQL
* [x] 媒体资源可自动导出至 MinIO 对象存储
* [x] 消息导出时自动完成向量嵌入和分词处理
* [x] 实时同步，自动拉取最新对话内容

### 🔍 聊天记录搜索

[](#-聊天记录搜索)

* [x] 智能分词精准检索，支持多语言
* [x] 支持模糊匹配与向量语义搜索，查找更高效
* [x] RAG 智能问答：直接与 AI 对话，基于历史上下文实时解答

## 🛣️ 未来规划

[](#️-未来规划)

### 🧠 AI 赋能

[](#-ai-赋能)

* [ ] 自动生成会话总结
* [ ] 超级大脑：基于历史消息自动抽取人物与事件知识图谱

### 🔗 媒体与链接功能

[](#-媒体与链接功能)

* [ ] 智能整理“已保存消息”收藏夹，更高效管理重要内容
* [ ] 链接与图片深度索引：实现网页智能摘要、图片 OCR 文字识别与智能描述，赋能搜索与内容整理

### 🌐 多平台扩展

[](#-多平台扩展)

* [ ] 增加 Telegram Bot 支持，满足更多消息管理需求
* [ ] 支持扩展至 Discord 及其他社交/通讯平台，实现跨平台统一检索与备份

## 🌐 立即使用

[](#-立即使用)

我们提供了一个在线体验版，无需自行部署，即可体验 Telegram Search 的全部功能。

访问以下网址开始使用：<https://search.lingogram.app>

Warning

本项目未发行任何虚拟货币，请警惕相关诈骗风险。

本软件仅供您导出和检索个人聊天记录使用，切勿将其用于任何违法用途。

## 🚀 快速开始

[](#-快速开始)

默认使用 PGlite 作为消息数据库，如果需要使用更高性能的 PostgreSQL 数据库以及提供的 MinIO 作为媒体存储引擎，请参考下文自定义环境变量或者使用 `docker compose up -d` 启动全部服务。

镜像提供 latest 和 nightly 版本，请自行选择。

```
docker run -d --name telegram-search \
  -p 3333:3333 \
  -v telegram-search-data:/app/data \
  ghcr.io/groupultra/telegram-search:latest
```

然后打开 **<http://localhost:3333>** 即可使用 🎉

### 自定义环境变量

[](#自定义环境变量)

Important

AI Embedding & LLM 设置现在在应用内**按账户**配置（设置 → API）。

| 环境变量                          | 说明                                                                     | 示例值                                                   |
| ----------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------- |
| `TELEGRAM_API_ID`             | 从 [my.telegram.org](https://my.telegram.org/apps) 获取的 Telegram 应用 ID   |                                                       |
| `TELEGRAM_API_HASH`           | 从 [my.telegram.org](https://my.telegram.org/apps) 获取的 Telegram 应用 Hash |                                                       |
| `DATABASE_TYPE`               | 数据库类型，可选 `postgres` 或 `pglite`                                         | `pglite`                                              |
| `DATABASE_URL`                | PostgreSQL 连接字符串（仅在 `DATABASE_TYPE=postgres` 时填写）                      | `postgresql://postgres:123456@pgvector:5432/postgres` |
| `PROXY_URL`                   | 代理地址（支持如 `socks5://user:pass@host:port` 等格式）                           | `socks5://user:pass@host:port`                        |
| `PORT`                        | 后端服务 HTTP/WebSocket 监听端口                                               | `3333`                                                |
| `HOST`                        | 后端服务监听地址                                                               | `0.0.0.0`                                             |
| `BACKEND_URL`                 | Nginx 作为反向代理时用于 `/api` 和 `/ws` 的上游后端地址                                 | `http://127.0.0.1:3333`                               |
| `MINIO_ENDPOINT`              | MinIO 服务地址（主机名或 IP）                                                    | `minio`                                               |
| `MINIO_PORT`                  | MinIO 服务端口                                                             | `9000`                                                |
| `MINIO_USE_SSL`               | MinIO 是否启用 SSL（`true` 或 `false`）                                       | `false`                                               |
| `MINIO_ACCESS_KEY`            | MinIO 访问密钥                                                             | `minioadmin`                                          |
| `MINIO_SECRET_KEY`            | MinIO 访问密钥对应的密钥                                                        | `minioadmin`                                          |
| `MINIO_BUCKET`                | MinIO 存储桶名称                                                            | `telegram-media`                                      |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OpenTelemetry OTLP 日志采集端点                                              | `http://loki:3100/otlp/v1/logs`                       |

**使用 PostgreSQL 的示例：**

```
docker run -d --name telegram-search \
  -p 3333:3333 \
  -v telegram-search-data:/app/data \
  -e DATABASE_TYPE=postgres \
  -e DATABASE_URL=postgresql://<host>:5432/postgres \
  ghcr.io/groupultra/telegram-search:latest
```

**代理格式：**

* SOCKS5: `socks5://user:pass@host:port`
* SOCKS4: `socks4://user:pass@host:port`
* HTTP: `http://user:pass@host:port`
* MTProxy: `mtproxy://secret@host:port`

### 使用 Docker Compose 启动

[](#使用-docker-compose-启动)

1. 克隆仓库。

2. 运行 docker compose 启动包括数据库、MinIO 在内的全部服务：

```
docker compose up -d
```

3. 访问 `http://localhost:3333` 打开搜索界面。

## 💻 开发指南

[](#-开发指南)

### 纯浏览器模式

[](#纯浏览器模式)

```
git clone https://github.com/groupultra/telegram-search.git
cd telegram-search
pnpm install
cp .env.example .env
pnpm run dev
```

### 服务器模式

[](#服务器模式)

```
git clone https://github.com/groupultra/telegram-search.git
cd telegram-search
pnpm install

cp .env.example .env

docker compose up -d pgvector minio

pnpm run server:dev
pnpm run web:dev
```

📖 **更多开发细节和架构细节：** [CONTRIBUTING.md](https://github.com/groupultra/telegram-search/blob/main/CONTRIBUTING.md)

## 🚀 Activity

[](#-activity)

[![Alt](https://camo.githubusercontent.com/406b807837e4a3684afe094bcc67000fd70e56b4c0ff8caf87de34ffd05ef9f8/68747470733a2f2f7265706f62656174732e6178696f6d2e636f2f6170692f656d6265642f363964356566396635653732636437393031623332666637316235663335396263376361343265612e737667 "Repobeats analytics image")](https://camo.githubusercontent.com/406b807837e4a3684afe094bcc67000fd70e56b4c0ff8caf87de34ffd05ef9f8/68747470733a2f2f7265706f62656174732e6178696f6d2e636f2f6170692f656d6265642f363964356566396635653732636437393031623332666637316235663335396263376361343265612e737667)

[![Star History Chart](https://camo.githubusercontent.com/0f87de399727f41d6f4c6898188228bc91a69f41bee61790c76aeee8b3ef9932/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d67726f7570756c7472612f74656c656772616d2d73656172636826747970653d44617465)](https://star-history.com/#groupultra/telegram-search\&Date)


