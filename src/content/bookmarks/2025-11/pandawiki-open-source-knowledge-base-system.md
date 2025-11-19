---
title: "PandaWiki: 基于AI大模型的开源知识库搭建系统"
slug: pandawiki-open-source-knowledge-base-system
description: |
  PandaWiki 是一款 AI 大模型驱动的开源知识库搭建系统，能够帮助你快速构建智能化的产品文档、技术文档、FAQ、博客系统，并提供 AI 创作、AI 问答、AI 搜索等多种功能。
tags: 
  - AI
  - opensource
  - dev
pubDatetime: 2025-11-19T14:29:15+08:00
ogImage: https://opengraph.githubassets.com/94744c86d78f069f27058373b12161d6dcd38d893d648eac78dfc6a2c4d3e912/chaitin/PandaWiki
---

[原文链接](https://github.com/chaitin/PandaWiki)

---

[![](/chaitin/PandaWiki/raw/main/images/banner.png)](https://github.com/chaitin/PandaWiki/blob/main/images/banner.png)

[📖 官方网站](https://ly.safepoint.cloud/Br48PoX)   |   [🙋‍♂️ 微信交流群](https://github.com/chaitin/PandaWiki/blob/main/images/wechat.png)

## 👋 项目介绍

[](#-项目介绍)

PandaWiki 是一款 AI 大模型驱动的**开源知识库搭建系统**，帮助你快速构建智能化的 **产品文档、技术文档、FAQ、博客系统**，借助大模型的力量为你提供 **AI 创作、AI 问答、AI 搜索** 等能力。

[![](/chaitin/PandaWiki/raw/main/images/setup.png)](https://github.com/chaitin/PandaWiki/blob/main/images/setup.png)

## ⚡️ 界面展示

[](#️-界面展示)

| PandaWiki 控制台                                                                                                                      | Wiki 网站前台                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| [![](/chaitin/PandaWiki/raw/main/images/screenshot-1.png)](https://github.com/chaitin/PandaWiki/blob/main/images/screenshot-1.png) | [![](/chaitin/PandaWiki/raw/main/images/screenshot-2.png)](https://github.com/chaitin/PandaWiki/blob/main/images/screenshot-2.png) |
| [![](/chaitin/PandaWiki/raw/main/images/screenshot-3.png)](https://github.com/chaitin/PandaWiki/blob/main/images/screenshot-3.png) | [![](/chaitin/PandaWiki/raw/main/images/screenshot-4.png)](https://github.com/chaitin/PandaWiki/blob/main/images/screenshot-4.png) |

## 🔥 功能与特色

[](#-功能与特色)

* AI 驱动智能化：AI 辅助创作、AI 辅助问答、AI 辅助搜索。
* 强大的富文本编辑能力：兼容 Markdown 和 HTML，支持导出为 word、pdf、markdown 等多种格式。
* 轻松与第三方应用进行集成：支持做成网页挂件挂在其他网站上，支持做成钉钉、飞书、企业微信等聊天机器人。
* 通过第三方来源导入内容：根据网页 URL 导入、通过网站 Sitemap 导入、通过 RSS 订阅、通过离线文件导入等。

## 🚀 上手指南

[](#-上手指南)

### 安装 PandaWiki

[](#安装-pandawiki)

你需要一台支持 Docker 20.x 以上版本的 Linux 系统来安装 PandaWiki。

使用 root 权限登录你的服务器，然后执行以下命令。

```
bash -c "$(curl -fsSLk https://release.baizhi.cloud/panda-wiki/manager.sh)"
```

根据命令提示的选项进行安装，命令执行过程将会持续几分钟，请耐心等待。

> 关于安装与部署的更多细节请参考 [安装 PandaWiki](https://pandawiki.docs.baizhi.cloud/node/01971602-bb4e-7c90-99df-6d3c38cfd6d5)。

### 登录 PandaWiki

[](#登录-pandawiki)

在上一步中，安装命令执行结束后，你的终端会输出以下内容。

```
SUCCESS  控制台信息:
SUCCESS    访问地址(内网): http://*.*.*.*:2443
SUCCESS    访问地址(外网): http://*.*.*.*:2443
SUCCESS    用户名: admin
SUCCESS    密码: **********************
```

使用浏览器打开上述内容中的 “访问地址”，你将看到 PandaWiki 的控制台登录入口，使用上述内容中的 “用户名” 和 “密码” 登录即可。

### 配置 AI 模型

[](#配置-ai-模型)

> PandaWiki 是由 AI 大模型驱动的 Wiki 系统，在未配置大模型的情况下 AI 创作、AI 问答、AI 搜索 等功能无法正常使用。

首次登录时会提示需要先配置 AI 模型，根据下方图片配置 “Chat 模型”。

[![](/chaitin/PandaWiki/raw/main/images/modelconfig.png)](https://github.com/chaitin/PandaWiki/blob/main/images/modelconfig.png)

> 推荐使用 [百智云模型广场](https://baizhi.cloud/) 快速接入 AI 模型，注册即可获赠 5 元的模型使用额度。 关于大模型的更多配置细节请参考 [接入 AI 模型](https://pandawiki.docs.baizhi.cloud/node/01971616-811c-70e1-82d9-706a202b8498)。

### 创建知识库

[](#创建知识库)

一切配置就绪后，你需要先创建一个 “知识库”。

“知识库” 是一组文档的集合，PandaWiki 将会根据知识库中的文档，为不同的知识库分别创建 “Wiki 网站”。

[![](/chaitin/PandaWiki/raw/main/images/createkb.png)](https://github.com/chaitin/PandaWiki/blob/main/images/createkb.png)

> 关于知识库的更多配置细节请参考 [知识库设置](https://pandawiki.docs.baizhi.cloud/node/01971b5e-5bea-76d2-9f89-a95f98347bb0)。

### 💪 开始使用

[](#-开始使用)

如果你顺利完成了以上步骤，那么恭喜你，属于你的 PandaWiki 搭建成功，你可以：

* 访问 **控制台** 来管理你的知识库内容
* 访问 **Wiki 网站** 让你的用户使用知识库

## 社区交流

[](#社区交流)

欢迎加入我们的微信群进行交流。

[![](/chaitin/PandaWiki/raw/main/images/wechat.png)](https://github.com/chaitin/PandaWiki/blob/main/images/wechat.png)

## 🙋‍♂️ 贡献

[](#‍️-贡献)

欢迎提交 [Pull Request](https://github.com/chaitin/PandaWiki/pulls) 或创建 [Issue](https://github.com/chaitin/PandaWiki/issues) 来帮助改进项目。

## 📝 许可证

[](#-许可证)

本项目采用 GNU Affero General Public License v3.0 (AGPL-3.0) 许可证。这意味着：

* 你可以自由使用、修改和分发本软件
* 你必须以相同的许可证开源你的修改
* 如果你通过网络提供服务，也必须开源你的代码
* 商业使用需要遵守相同的开源要求

## Star History

[](#star-history)

[![Star History Chart](https://camo.githubusercontent.com/c9ef283b18e5e715d1b39cb0e0fc17c1fbbb973bbc93f90036a65c6b44bb5e6e/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d6368616974696e2f50616e646157696b6926747970653d44617465)](https://www.star-history.com/#chaitin/PandaWiki\&Date)


