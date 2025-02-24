---
title: "MoePush: 基于 NextJS 和 Cloudflare 的可爱消息推送服务"
slug: moepush-nextjs-cloudflare
description: |
  MoePush 是一个开源的消息推送服务，基于 NextJS 和 Cloudflare 技术栈，支持钉钉、企业微信、Telegram 等多种渠道，提供简易的接口和精美的 UI 设计，完全免费使用！
tags: 
  - AI
  - cloudflare
  - dev
  - tool
  - push
pubDatetime: 2025-02-24T10:22:32+08:00
ogImage: https://opengraph.githubassets.com/6e36cae73f33a1c619374e289800e1d0a5643c76331b30e8b843bb518b18158f/beilunyang/moepush
---

[原文链接](https://github.com/beilunyang/moepush)

---

[![MoePush Logo](/beilunyang/moepush/raw/main/public/logo.png)](https://github.com/beilunyang/moepush/blob/main/public/logo.png)

# MoePush

[](#moepush)

一个基于 NextJS + Cloudflare 技术栈构建的可爱消息推送服务, 支持多种消息推送渠道✨

## 在线演示

[](#在线演示)

<https://moepush.app>

[![home](https://camo.githubusercontent.com/09272aac928381a828ebe12491123b96f16beff2c7235f24789dab9ed06fe24d/68747470733a2f2f7069632e6f74616b752e72656e2f32303235303232312f4151414435623878473976567746562d2e6a7067)](https://camo.githubusercontent.com/09272aac928381a828ebe12491123b96f16beff2c7235f24789dab9ed06fe24d/68747470733a2f2f7069632e6f74616b752e72656e2f32303235303232312f4151414435623878473976567746562d2e6a7067)

[![login](https://camo.githubusercontent.com/e478d90baa7429d1b3d5df061bdb4722c51b58d3ee59c62b924d7df140c12f3a/68747470733a2f2f7069632e6f74616b752e72656e2f32303235303232312f4151414436373878473976567746562d2e6a7067)](https://camo.githubusercontent.com/e478d90baa7429d1b3d5df061bdb4722c51b58d3ee59c62b924d7df140c12f3a/68747470733a2f2f7069632e6f74616b752e72656e2f32303235303232312f4151414436373878473976567746562d2e6a7067)

[![dashboard](https://camo.githubusercontent.com/54e74313b90a3c71c020e58f3a0e1cc2f065c79443dec390b5f337eaad47a208/68747470733a2f2f7069632e6f74616b752e72656e2f32303235303232312f4151414437623878473976567746562d2e6a7067)](https://camo.githubusercontent.com/54e74313b90a3c71c020e58f3a0e1cc2f065c79443dec390b5f337eaad47a208/68747470733a2f2f7069632e6f74616b752e72656e2f32303235303232312f4151414437623878473976567746562d2e6a7067)

## 特性

[](#特性)

* 📡**多渠道支持** ：支持钉钉、企业微信、Telegram 等多种消息推送渠道。
* 🛠️**简单易用** ：提供简单的接口调用，支持多种消息模板，快速集成。
* 💖**开源免费** ：基础功能完全免费使用，代码开源，欢迎贡献。
* 🎨**精美 UI** ：使用 shadcn/ui 组件库，提供精美 UI 设计。

## 已支持渠道

[](#已支持渠道)

* 钉钉机器人
* 企业微信应用
* 企业微信机器人
* Telegram 机器人

## 技术栈

[](#技术栈)

* **框架**: [Next.js](https://nextjs.org/) (App Router)
* **平台**: [Cloudflare Pages](https://pages.cloudflare.com/)
* **数据库**: [Cloudflare D1](https://developers.cloudflare.com/d1/) (SQLite)
* **认证**: [NextAuth](https://authjs.dev/getting-started/installation?framework=Next.js) 配合 GitHub 登录
* **样式**: [Tailwind CSS](https://tailwindcss.com/)
* **UI 组件**: 基于 [Radix UI](https://www.radix-ui.com/) 的自定义组件
* **类型安全**: [TypeScript](https://www.typescriptlang.org/)
* **ORM**: [Drizzle ORM](https://orm.drizzle.team/)

## 本地运行

[](#本地运行)

1. 克隆项目并安装依赖：

```
git clone https://github.com/beilunyang/moepush.git
cd moepush
pnpm install
```

2. 复制环境变量文件：

```
cp .env.example .env
```

环境变量文件 `.env` 中需要配置以下变量：

* `AUTH_SECRET`：加密 Session 的密钥
* `AUTH_GITHUB_ID`：GitHub OAuth App ID
* `AUTH_GITHUB_SECRET`：GitHub OAuth App Secret

3. 运行开发服务器：

```
pnpm run dev
```

访问 <http://localhost:3000> 查看应用。

## 部署

[](#部署)

### GitHub Actions 自动部署

[](#github-actions-自动部署)

项目已配置 GitHub Actions 用于自动部署, 可以通过两种方式进行触发：

* 推送新的 tag（格式：`v*`）会触发自动部署。例如：`git tag v1.0.0 && git push origin v1.0.0`
* 手动触发工作流。前往 [Actions](https://github.com/beilunyang/moepush/actions) 页面，点击 `Deploy` 工作流，点击 `Run workflow` 按钮即可。

### 部署前需要在 GitHub 仓库设置中添加以下 Secrets：

[](#部署前需要在-github-仓库设置中添加以下-secrets)

* `CLOUDFLARE_API_TOKEN`：Cloudflare API Token
* `CLOUDFLARE_ACCOUNT_ID`：Cloudflare Account ID
* `D1_DATABASE_NAME`：D1 数据库名称
* `AUTH_SECRET`：加密 Session 的密钥
* `AUTH_GITHUB_ID`：GitHub OAuth App ID
* `AUTH_GITHUB_SECRET`：GitHub OAuth App Secret
* `PROJECT_NAME`：项目名称 (可选，默认：moepush)

## 贡献

[](#贡献)

欢迎提交 Pull Request 或者 Issue来帮助改进这个项目

## 交流群

[](#交流群)

[![](https://camo.githubusercontent.com/e4a8eeec545c99b532edf41672d3bfc58e398ec39c28538f8505898be625f6f3/68747470733a2f2f7069632e6f74616b752e72656e2f32303235303232312f4151414438623878473976567746562d2e6a7067)](https://camo.githubusercontent.com/e4a8eeec545c99b532edf41672d3bfc58e398ec39c28538f8505898be625f6f3/68747470733a2f2f7069632e6f74616b752e72656e2f32303235303232312f4151414438623878473976567746562d2e6a7067)

\
如二维码失效，请添加我的个人微信（hansenones），并备注 "MoePush" 加入微信交流群\


## 支持

[](#支持)

如果你喜欢这个项目，欢迎给它一个 Star ⭐️ 或者进行赞助\
\
[![](https://camo.githubusercontent.com/29d2edf4609d47ff06d823482b5992cdca6c6a9f0b7b1ab540d6ddfb2f69f4b9/68747470733a2f2f7069632e6f74616b752e72656e2f32303234303231322f415141445072677847776f4957465a2d2e6a7067)](https://camo.githubusercontent.com/29d2edf4609d47ff06d823482b5992cdca6c6a9f0b7b1ab540d6ddfb2f69f4b9/68747470733a2f2f7069632e6f74616b752e72656e2f32303234303231322f415141445072677847776f4957465a2d2e6a7067)\
\
[![Buy Me A Coffee](https://camo.githubusercontent.com/10550f5b06d56d3478f5638a645e2df94cbd70fe828104d4ae55dd24d29486bc/68747470733a2f2f63646e2e6275796d6561636f666665652e636f6d2f627574746f6e732f76322f64656661756c742d626c75652e706e67)](https://www.buymeacoffee.com/beilunyang)

## 许可证

[](#许可证)

[MIT](https://github.com/beilunyang/moepush/blob/main/LICENSE)


