---
title: "AI趋势发现与内容发布系统: 自动化微信公众号管理"
slug: ai-trend-publish
description: |
  AI趋势发现与内容发布系统支持多源数据采集、智能总结和自动发布到微信公众号。使用DeepseekAI进行内容分析和智能生成，可有效提高内容管理效率，提升公众号运营效果。
tags: 
  - AI
  - dev
  - blog
  - tool
pubDatetime: 2025-02-27T16:05:25+08:00
ogImage: https://opengraph.githubassets.com/c6dd446176d048b88ca8155db1f4afe6def541029174a01df0fd74d36a49df9b/OpenAISpace/ai-trend-publish
---

[原文链接](https://github.com/OpenAISpace/ai-trend-publish)

---

# TrendPublish

[](#trendpublish)

一个基于 AI 的趋势发现和内容发布系统，支持多源数据采集、智能总结和自动发布到微信公众号。

> 🌰 示例公众号：**深巷懒猫**

> 即刻关注，体验 AI 智能创作的内容～

## 🌟 主要功能

[](#-主要功能)

* 🤖 多源数据采集

  * Twitter/X 内容抓取
  * 网站内容抓取 (基于 FireCrawl)
  * 支持自定义数据源配置

* 🧠 AI 智能处理

  * 使用 DeepseekAI 进行内容总结
  * 关键信息提取
  * 智能标题生成

* 📢 自动发布

  * 微信公众号文章发布
  * 自定义文章模板
  * 定时发布任务

* 📱 通知系统

  * Bark 通知集成
  * 任务执行状态通知
  * 错误告警

## 🛠 技术栈

[](#-技术栈)

* **运行环境**: Node.js + TypeScript

* **框架**: Express.js

* **AI 服务**: DeepseekAI

* **数据源**:

  * Twitter/X API
  * FireCrawl

* **定时任务**: node-cron

* **模板引擎**: EJS

* **开发工具**:

  * nodemon (热重载)
  * TypeScript
  * Jest (测试)

## 📦 项目结构

[](#-项目结构)

```
src/
├── controllers/     # 控制器层，处理请求
├── data-sources/    # 数据源配置
├── publishers/      # 发布器实现
├── scrapers/        # 数据采集实现
├── services/        # 业务逻辑层
├── summarizer/      # AI 总结实现
├── templates/       # 文章模板
└── utils/          # 工具函数
```

## 🚀 快速开始

[](#-快速开始)

### 环境要求

[](#环境要求)

* Node.js (v14+)
* npm 或 yarn
* TypeScript
* Docker (可选，用于容器化部署)

### 安装

[](#安装)

1. 克隆项目

```
git clone [repository-url]
cd trendpublish
```

2. 安装依赖

```
npm install
```

3. 配置环境变量

```
cp .env.example .env
# 编辑 .env 文件配置必要的环境变量
```

4. 启动项目

```
# 开发模式
npm run start

# 构建
npm run build
```

## 📦 部署指南

[](#-部署指南)

### 方式一：直接部署

[](#方式一直接部署)

1. 在服务器上安装 Node.js (v20+) 和 PM2

```
# 安装 PM2
npm install -g pm2
```

2. 构建项目

```
npm run build
```

3. 使用 PM2 启动服务

```
pm2 start dist/index.js --name trend-finder
```

### 方式二：Docker 部署

[](#方式二docker-部署)

1. 构建 Docker 镜像

```
docker build -t trend-finder .
```

2. 运行容器

```
docker run -d -p 3000:3000 --name trend-finder trend-finder
```

### 方式三：使用 Docker Compose

[](#方式三使用-docker-compose)

1. 启动服务

```
docker-compose up -d
```

2. 查看日志

```
docker-compose logs -f
```

3. 停止服务

```
docker-compose down
```

### CI/CD 自动部署

[](#cicd-自动部署)

项目已配置 GitHub Actions 自动部署流程：

1. 推送代码到 main 分支会自动触发部署

2. 也可以在 GitHub Actions 页面手动触发部署

3. 确保在 GitHub Secrets 中配置以下环境变量：

   * `SERVER_HOST`: 服务器地址
   * `SERVER_USER`: 服务器用户名
   * `SSH_PRIVATE_KEY`: SSH 私钥
   * 其他必要的环境变量（参考 .env.example）

## ⚙️ 环境变量配置

[](#️-环境变量配置)

在 `.env` 文件中配置以下必要的环境变量：

```
# DeepseekAI API 配置
DEEPSEEK_API_KEY=your_api_key

# FireCrawl 配置
FIRECRAWL_API_KEY=your_api_key

# Twitter API 配置
TWITTER_API_KEY=your_api_key

# 微信公众号配置
WEIXIN_APP_ID=your_app_id
WEIXIN_APP_SECRET=your_app_secret

# Bark 通知配置
BARK_KEY=your_key
```

## 📝 使用说明

[](#-使用说明)

### 添加新数据源

[](#添加新数据源)

在 `src/data-sources/getCronSources.ts` 中配置数据源：

```
export const sourceConfigs = {
  AI: {
    firecrawl: [{ identifier: "https://example.com" }],
    twitter: [{ identifier: "https://twitter.com/username" }],
  },
};
```

### 自定义文章模板

[](#自定义文章模板)

在 `src/templates` 目录下创建新的模板文件，参考现有的模板实现。

### 定时任务配置

[](#定时任务配置)

修改 `src/controllers/cron.ts` 中的定时任务配置：

```
cron.schedule("0 18 * * *", async () => {
  // 每天 18:00 执行
  await workflow.process();
});
```

## 🤝 贡献指南

[](#-贡献指南)

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 提交 Pull Request

## 📄 许可证

[](#-许可证)

本项目采用 MIT 许可证 - 详见 [LICENSE](https://github.com/OpenAISpace/ai-trend-publish/blob/main/LICENSE) 文件


