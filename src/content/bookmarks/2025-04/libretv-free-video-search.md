---
title: "LibreTV: 一键部署的免费在线视频搜索与观看平台"
slug: libretv-free-video-search
description: |
  LibreTV是一个轻量级的免费在线视频搜索与观看平台，支持多种视频源搜索与播放。无须注册，立即使用，提供响应式设计并支持多设备访问。项目采用纯前端技术构建，方便用户一键部署。
tags: 
  - video
  - opensource
  - API
  - dev
pubDatetime: 2025-04-09T14:48:57+08:00
ogImage: https://opengraph.githubassets.com/10136fc6e1b87866b90b476749a47a372f8b7adf1e1dca187b679e73e143389a/bestZwei/LibreTV
---

[原文链接](https://github.com/bestZwei/LibreTV?tab=readme-ov-file)

---

# LibreTV - 免费在线视频搜索与观看平台

[](#libretv---免费在线视频搜索与观看平台)

## 📺 项目简介

[](#-项目简介)

LibreTV是一个轻量级、免费的在线视频搜索与观看平台，提供来自多个视频源的内容搜索与播放服务。无需注册，即开即用，支持多种设备访问。项目采用纯前端技术构建，可轻松部署在各类静态网站托管服务上。

本项目基于 <https://github.com/bestK/tv>

演示站：<https://libretv.is-an.org/>

[![image-20250406231222216](https://camo.githubusercontent.com/89e0e271f49156c3681e56320dbfddc6a526d4910a7010adb414a343aa910774/68747470733a2f2f74657374696e6763662e6a7364656c6976722e6e65742f67682f626573745a7765692f696d6773406d61737465722f706963676f2f696d6167652d32303235303430363233313232323231362e706e67)](https://camo.githubusercontent.com/89e0e271f49156c3681e56320dbfddc6a526d4910a7010adb414a343aa910774/68747470733a2f2f74657374696e6763662e6a7364656c6976722e6e65742f67682f626573745a7765692f696d6773406d61737465722f706963676f2f696d6167652d32303235303430363233313232323231362e706e67)

**感谢 [NodeSupport](https://www.nodeseek.com/post-305185-1) 友情赞助**

## ✨ 主要特性

[](#-主要特性)

* 🔍 多源视频搜索功能，覆盖电影、电视剧等内容
* 📱 响应式设计，完美支持电脑、平板和手机
* 🌐 聚合多个视频源，自动提取播放链接
* 🔄 支持自定义API接口，灵活扩展
* 💾 本地存储搜索历史，提升使用体验
* 🚀 纯静态部署，无需后端服务器
* 🛡️ 内置广告过滤功能，提供更干净的观影体验
* 🎬 自定义视频播放器，支持HLS流媒体格式

## 📹 视频源支持说明

[](#-视频源支持说明)

LibreTV 默认支持以下几种视频源接口：

* 黑木耳影视 (heimuer)
* 非凡影视 (ffzy)
* 天涯资源 (tyyszy)
* …

### CMS采集站源兼容性

[](#cms采集站源兼容性)

本项目支持标准的苹果CMS V10 API格式。自定义API需遵循以下格式：

* 搜索接口: `https://example.com/api.php/provide/vod/?ac=videolist&wd=关键词`
* 详情接口: `https://example.com/api.php/provide/vod/?ac=detail&ids=视频ID`

**重要提示**: 像 `https://360zy.com/api.php/provide/vod` 这样的CMS源需要按照以下格式添加：

1. 在设置面板中选择"自定义接口"
2. 接口地址只填写到域名部分: `https://360zy.com`（不要包含`/api.php/provide/vod`部分）
3. 项目会自动补全正确的路径格式

如果CMS接口非标准格式，可能需要修改项目中的`config.js`文件中的`API_CONFIG.search.path`和`API_CONFIG.detail.path`配置。

## 🛠️ 技术栈

[](#️-技术栈)

* HTML5 + CSS3 + JavaScript (ES6+)
* Tailwind CSS (通过CDN引入)
* HLS.js 用于HLS流处理和广告过滤
* DPlayer 视频播放器核心
* 前端API请求拦截技术
* localStorage本地存储

## 🚀 一键部署

[](#-一键部署)

[![Deploy with Vercel](https://camo.githubusercontent.com/20bea215d35a4e28f2c92ea5b657d006b087687486858a40de2922a4636301ab/68747470733a2f2f76657263656c2e636f6d2f627574746f6e)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FbestZwei%2FLibreTV)

[![Deploy to Cloudflare Pages](https://camo.githubusercontent.com/baf9767e356aab4af1d4a95e9380d4c76cfa233cf11f97872104a728401ec730/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4465706c6f79253230746f2d436c6f7564666c61726525323050616765732d626c75653f7374796c653d666f722d7468652d6261646765266c6f676f3d636c6f7564666c617265)](https://dash.cloudflare.com/)

## 🚀 部署指南

[](#-部署指南)

### Cloudflare Pages部署

[](#cloudflare-pages部署)

1. Fork或克隆本仓库到你的GitHub账户

2. 登录Cloudflare Dashboard，进入Pages服务

3. 点击"创建项目"，连接GitHub仓库

4. 使用以下设置：

   * 构建命令：留空（无需构建）
   * 输出目录：留空（默认为根目录）
   * 部署命令：留空

5. 点击"保存并部署"

### Vercel/Netlify部署

[](#vercelnetlify部署)

类似Cloudflare Pages，只需连接仓库并部署即可，无需特殊配置。

### 本地测试

[](#本地测试)

如果你想在本地测试，可以使用任何静态文件服务器：

```
# 使用Python
python -m http.server 8080

# 或使用Node.js的http-server
npx http-server -p 8080
```

### Docker 部署

[](#docker-部署)

```
docker pull bestzwei/libretv:latest
docker run -d --name libretv -p 8899:80 bestzwei/libretv:latest
```

访问 <http://localhost:8899> 查看效果。

### Docker Compose 部署

[](#docker-compose-部署)

你也可以通过 Docker Compose 部署本项目。新建一个名为 `docker-compose.yaml` 的文件，内容如下：

```
version: '3'
services:
  libretv:
    image: bestzwei/libretv:latest
    container_name: libretv
    ports:
      - "8899:80"
    restart: unless-stopped
```

## 🔧 自定义配置

[](#-自定义配置)

项目主要配置在`js/config.js`文件中，你可以修改以下内容：

* `PROXY_URL`: 修改为你自己的代理服务地址
* `API_SITES`: 添加或修改视频源API接口
* `SITE_CONFIG`: 更改站点名称、描述等基本信息
* `PLAYER_CONFIG`: 调整播放器参数，如自动播放、广告过滤等

注意：若使用docker部署，可进入容器，在`/usr/share/nginx/html/js`内修改相关配置

## 🌟 项目结构

[](#-项目结构)

```
LibreTV/
├── css/
│   └── styles.css       // 自定义样式
├── js/
│   ├── app.js           // 主应用逻辑
│   ├── api.js           // API请求处理
│   ├── config.js        // 全局配置
│   └── ui.js            // UI交互处理
├── player.html          // 自定义视频播放器
├── index.html           // 主页面
├── robots.txt           // 搜索引擎爬虫配置
└── sitemap.xml          // 站点地图
```

## Star History

[](#star-history)

[![Star History Chart](https://camo.githubusercontent.com/c02a0d1348cc9991da10fd9b30c682744f2aa8f0c5ae36a5da87d496fdd1aca0/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d626573745a7765692f4c69627265545626747970653d44617465)](https://www.star-history.com/#bestZwei/LibreTV\&Date)

## ⚠️ 免责声明

[](#️-免责声明)

LibreTV 仅作为视频搜索工具，不存储、上传或分发任何视频内容。所有视频均来自第三方API接口提供的搜索结果。如有侵权内容，请联系相应的内容提供方。

## 🔄 更新日志

[](#-更新日志)

* 1.0.0 (2025-04-06): 初始版本发布
* 1.0.1 (2025-04-07): 添加广告过滤功能，优化播放器性能
* 1.0.2 (2025-04-08): 分离了播放页面，优化视频源API兼容性


