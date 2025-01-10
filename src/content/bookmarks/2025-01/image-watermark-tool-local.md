---
title: "Image Watermark Tool: 在本地为图片添加水印的开源工具"
slug: image-watermark-tool-local
description: |
  Image Watermark Tool 是一个开源项目，允许用户在本地设备上轻松为图片（如身份证、驾照、护照等）添加水印。所有操作都在本地完成，无需网络连接，确保您的敏感信息安全。
tags: 
  - opensource
  - tool
  - dev
  - image
pubDatetime: 2025-01-10T10:53:38+08:00
ogImage: 
---

[原文链接](https://github.com/unilei/image-watermark-tool?tab=readme-ov-file)

---

# Image Watermark Tool

[](#image-watermark-tool)

Image Watermark Tool 是一个开源项目，用户可以在本地设备上给自己的图片（如身份证、驾照、护照等）添加水印，无需任何网络连接，并具有轻松的一键网站部署功能。 👉 [Image Watermark Tool](https://watermark.aicompasspro.com)

[English](https://github.com/unilei/image-watermark-tool/blob/master/README.EN.md) | 简体中文

## 快速开始

[](#快速开始)

### 在 Vercel 上部署

[](#在-vercel-上部署)

[![Deploy with Vercel](https://camo.githubusercontent.com/20bea215d35a4e28f2c92ea5b657d006b087687486858a40de2922a4636301ab/68747470733a2f2f76657263656c2e636f6d2f627574746f6e)](https://vercel.com/new/clone?repository-url=https://github.com/unilei/image-watermark-tool.git\&project-name=image-watermark-tool\&repository-name=image-watermark-tool)

### 在 Vercel 上手动部署 操作方法

[](#在-vercel-上手动部署-操作方法)

```
1. fork 本项目
2. 在 [Vercel] 官网点击 [New Project]
3. 点击 [Import Git Repository] 并选择你 fork 的此项目并点击 [import]
4. 然后直接点 [Deploy] 接着等部署完成即可
```

### 1. 克隆项目

[](#1-克隆项目)

```
git clone https://github.com/unilei/image-watermark-tool.git
```

### 2. 安装依赖

[](#2-安装依赖)

```
# npm
npm install

# pnpm
pnpm install

# yarn
yarn install
```

### 3. 运行到浏览器

[](#3-运行到浏览器)

```
# npm
npm run dev

# pnpm
pnpm run dev

# yarn
yarn dev
```

### 4. 在浏览器打开 <http://localhost:3001>

[](#4-在浏览器打开-httplocalhost3001)

[![success\_deploy.jpg](https://camo.githubusercontent.com/9b33c957a5178ed1b14d1c21e956b743f5595dae2154249e3a46e2b5167cd24a/68747470733a2f2f7777772e6169636f6d7061737370726f2e636f6d2f6170692f696d67686f7374696e672f66696c652f6664646331336337386131306437663834316163312e706e67)](https://camo.githubusercontent.com/9b33c957a5178ed1b14d1c21e956b743f5595dae2154249e3a46e2b5167cd24a/68747470733a2f2f7777772e6169636f6d7061737370726f2e636f6d2f6170692f696d67686f7374696e672f66696c652f6664646331336337386131306437663834316163312e706e67)

#### 如何部署到自己服务器？ NUXT.JS 打包部署文档

[](#如何部署到自己服务器-nuxtjs-打包部署文档)

[部署文档](https://nuxt.com/docs/getting-started/deployment)

### 如何通过 Docker 部署

[](#如何通过-docker-部署)

### 1. 方式一

[](#1-方式一)

```
docker pull ghcr.io/chung1912/image-watermark-tool:master
```

```
docker run -it --name image-watermark-tool \
-p 3000:3000 \
--restart always \
ghcr.io/chung1912/image-watermark-tool:master
```

### 2. 方式二

[](#2-方式二)

```
docker pull ghcr.io/chung1912/image-watermark-tool-nginx:master
```

```
docker run -it --name image-watermark-tool-nginx \
-p 8080:80 \
-p 8443:443 \
-v /path/to/private.pem:/etc/nginx/private.pem  \
-v /path/to/private.key:/etc/nginx/private.key \
--restart always \
ghcr.io/chung1912/image-watermark-tool-nginx:master
```


