---
title: "WXPush：一个极简且免费的微信消息推送API服务"
slug: wxpush-wechat-message-push-service
description: |
  WXPush是一个基于Cloudflare Workers构建的免费微信消息推送服务，提供简单的API接口。用户可通过HTTP请求轻松推送消息，集成简单，安全性高，无需服务器管理，享受Cloudflare的慷慨免费套餐。
tags: 
  - API
  - dev
  - Cloudflare
pubDatetime: 2025-12-08T11:08:48+08:00
ogImage: https://opengraph.githubassets.com/f2db060d29c75a3b3892a460d744ff3ce4dacaf0741418f0753c749e4df64467/frankiejun/wxpush
---

[原文链接](https://github.com/frankiejun/wxpush)

---

# WXPush - 微信消息推送服务 (Cloudflare Workers)

[](#wxpush---微信消息推送服务-cloudflare-workers)

这是一个基于 [Cloudflare Workers](https://workers.cloudflare.com/) 搭建的、轻量级的微信公众号模板消息推送服务。它提供了一个简单的 API 接口，让您可以轻松地通过 HTTP 请求将消息推送到指定的微信用户。

## ✨ 特性

[](#-特性)

* **快速部署**: 只需几分钟即可将服务部署到 Cloudflare 的全球网络上。
* **无需服务器**: 构建于 Serverless 架构之上，无需管理自己的服务器。
* **高度可定制**: 支持通过 URL 参数临时覆盖默认的微信配置。
* **安全**: 敏感信息通过 Cloudflare 的 Secrets 进行加密存储，不暴露在代码中。
* **成本低廉**: 享受 Cloudflare Workers 慷慨的免费套餐（每日 10 万次请求）。

## 🎬 视频教学

[](#-视频教学)

我们制作了一个详细的视频教程，手把手教您如何完成所有部署步骤。如果您偏爱视频指导，请点击下方链接观看：

[![点击观看视频教程](https://camo.githubusercontent.com/038fd2a80261d3359f0fbad56a4ff754ad966e3c0fe6db0a0fe18b923b934744/68747470733a2f2f6c6f6f6b2e706963732e636c6f75646e732e63682f696d672fe69e81e7ae80e5beaee4bfa1e6b688e681afe68ea8e98081e69c8de58aa12de5b081e99da22e6a7067)](https://youtu.be/sE1Kcol_XRs?si=G-UbUGlMhyysv-US)

*点击上方图片或链接，即可跳转到 YouTube 观看视频教程。*

## 🚀 部署指南

[](#-部署指南)

我们提供两种简单的部署方式，您可以根据自己的需求选择其中一种。

### 方法一：直接粘贴代码到 Cloudflare (最简单)

[](#方法一直接粘贴代码到-cloudflare-最简单)

这种方法无需任何本地开发环境，只需复制粘贴即可完成部署。

1. **登录 Cloudflare 仪表板**

   * 打开浏览器，访问 <https://dash.cloudflare.com/> 并登录。

2. **创建 Worker 服务**

   * 在左侧菜单中，选择 **Workers 和 Pages**。
   * 点击 **创建应用程序**，然后选择 **创建 Worker**。
   * 为您的 Worker 指定一个全局唯一的名称 (例如 `my-wxpush-service`)，然后点击 **部署**。

3. **粘贴代码**

   * 部署完成后，点击 **编辑代码** 进入在线代码编辑器。
   * 删除编辑器中所有的默认代码。
   * 将项目 `src/index.js` 文件中的全部内容复制并粘贴到编辑器中。

4. **保存并部署**

   * 点击编辑器右上角的 **保存并部署** 按钮。

5. **配置环境变量 (重要)**

   * 返回 Worker 的主管理页面，进入 **设置** > **变量**。

   * 在 **环境变量** 部分，点击 **添加变量**，依次添加以下配置。这些是服务运行所必需的敏感信息。

     * `API_TOKEN`: 用于接口调用的访问令牌，请设置一个足够复杂的随机字符串。
     * `WX_APPID`: 您的微信公众号 AppID。
     * `WX_SECRET`: 您的微信公众号 AppSecret。
     * `WX_USERID`: 默认接收消息用户的 OpenID，多个用户请用 `|` 符号分隔 (例如 `openid1|openid2`)。
     * `WX_TEMPLATE_ID`: 您要使用的微信模板消息 ID。
     * `WX_BASE_URL`: (可选) 点击模板消息后跳转的基础 URL。

   * **注意**：添加变量时，请确保勾选 **加密** 选项，以保护您的凭证安全。

### 方法二：通过关联 GitHub 仓库自动部署

[](#方法二通过关联-github-仓库自动部署)

如果您希望通过 Git 进行版本控制和持续集成，推荐使用此方法。

1. **Fork 或克隆项目**

   * 首先，将本项目 Fork 到您自己的 GitHub 账户，或者克隆后推送到您自己的新仓库。

2. **连接到 GitHub**

   * 登录 Cloudflare 仪表板，进入 **Workers 和 Pages**。
   * 点击 **创建应用程序**，切换到 **Pages** 选项卡，然后点击 **连接到 Git**。

3. **选择仓库**

   * 选择您刚刚创建的 GitHub 仓库。

4. **配置构建和部署**

   * **项目名称**：为您项目指定一个名称。
   * **生产分支**：选择您希望部署的分支 (通常是 `main` 或 `master`)。
   * **框架预设**：选择 `None`。
   * **构建设置**：将所有构建相关的字段 (如构建命令、输出目录) 留空。
   * **根目录**：保持默认的 `/` 即可。

5. **添加环境变量**

   * 在配置页面的 **环境变量** 部分，添加与 **方法一** 中相同的 `API_TOKEN`, `WX_APPID`, `WX_SECRET` 等变量。
   * 同样，请务必为每个变量勾选 **加密** 选项。

6. **保存并部署**

   * 点击 **保存并部署**。Cloudflare 会自动从您的仓库拉取代码并完成部署。
   * 此后，每当您向指定的生产分支推送新的代码提交时，Cloudflare 都会自动为您重新部署。

部署成功后，您的服务访问地址会显示在 Worker 或 Pages 的主页面上。

## ⚙️ API 使用方法

[](#️-api-使用方法)

服务部署成功后，您可以通过构造 URL 发起 `GET` 请求来推送消息。

### 请求地址

[](#请求地址)

```
https://<您的Worker地址>/wxsend
```

### 请求参数

[](#请求参数)

| 参数名           | 类型     | 是否必填 | 描述                       |
| ------------- | ------ | ---- | ------------------------ |
| `token`       | String | 是    | 您在 `API_TOKEN` 中设置的访问令牌。 |
| `title`       | String | 是    | 消息的标题。                   |
| `content`     | String | 是    | 消息的具体内容。                 |
| `appid`       | String | 否    | 临时覆盖默认的微信 AppID。         |
| `secret`      | String | 否    | 临时覆盖默认的微信 AppSecret。     |
| `userid`      | String | 否    | 临时覆盖默认的接收用户 OpenID。      |
| `template_id` | String | 否    | 临时覆盖默认的模板消息 ID。          |
| `base_url`    | String | 否    | 临时覆盖默认的跳转 URL。           |

### 使用示例

[](#使用示例)

**基础推送**

向默认配置的所有用户推送一条消息：

```
https://<您的Worker地址>/wxsend?title=服务器通知&content=服务已于北京时间%2022:00%20重启&token=your_secret_token
```

**临时覆盖用户**

向一个临时指定的用户推送消息：

```
https://<您的Worker地址>/wxsend?title=私人提醒&content=记得带钥匙&token=your_secret_token&userid=temporary_openid_here
```

### Webhook / POST 请求

[](#webhook--post-请求)

除了 `GET` 请求，服务也支持 `POST` 方法，更适合用于自动化的 Webhook 集成。

**请求地址**

```
https://<您的Worker地址>/wxsend
```

**请求方法**

```
POST
```

**请求头 (Headers)**

```
{
  "Authorization": "你的token",
  "Content-Type": "application/json"
}
```

**请求体 (Body)**

请求体需要是一个 JSON 对象，包含与 `GET` 请求相同的参数。

```
{
  "title": "Webhook 通知",
  "content": "这是一个通过 POST 请求发送的 Webhook 消息。"
}
```

**使用示例 (cURL)**

```
curl -X POST \
  https://<您的Worker地址>/wxsend \
  -H 'Authorization': '你的token' \
  -H 'Content-Type': 'application/json' \
  -d '{
    "title": "来自 cURL 的消息",
    "content": "自动化任务已完成。"
  }'
```

### 成功响应

[](#成功响应)

如果消息成功发送给至少一个用户，服务会返回 `HTTP 200` 状态码和类似 `Successfully sent messages to 1 user(s). First response: ok` 的文本。

### 失败响应

[](#失败响应)

如果发生错误（如 token 错误、缺少参数、微信接口调用失败等），服务会返回相应的 `HTTP 4xx` 或 `5xx` 状态码和错误信息。

## 🤝 贡献

[](#-贡献)

欢迎任何形式的贡献！如果您有好的想法或发现了 Bug，请随时提交 Pull Request 或创建 Issue。

## 📜 许可证

[](#-许可证)

本项目采用 [MIT License](https://github.com/frankiejun/wxpush/blob/main/LICENSE) 开源许可证。


