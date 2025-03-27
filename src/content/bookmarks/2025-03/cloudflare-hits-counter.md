---
title: "基于Cloudflare Workers的通用访问计数器xykt/Hits"
slug: cloudflare-hits-counter
description: |
  xykt/Hits是一个完全免费的服务器无关轻量级访问计数器系统，基于Cloudflare Workers和D1 SQL数据库。支持JSON与GitHub风格SVG图像，部署速度快，适合多个网站使用，确保安全与可靠性。
tags: 
  - API
  - Cloudflare
  - tool
  - opensource
pubDatetime: 2025-03-27T10:57:06+08:00
ogImage: https://opengraph.githubassets.com/91ce03452bb5975495bf0f607fff375f0ef83d6dd06ff7ee58245c511902f4a5/xykt/Hits
---

[原文链接](https://github.com/xykt/Hits)

---

# Hits! - General purpose hits counter based on Cloudflare Workers （[中文说明](https://github.com/xykt/Hits/blob/main/README_CN.md)）

[](#hits---general-purpose-hits-counter-based-on-cloudflare-workers-中文说明)

[![](https://camo.githubusercontent.com/42cfaf32b70043b0d67e2374fd7215683aff66744da43536865bde135879e5c5/68747470733a2f2f686974732e78796b742e64652f686974735f6769746875622e7376673f616374696f6e3d68697426636f756e745f62673d253233464641353532267469746c655f62673d253233314438383334267469746c653d56697369747326656467655f666c61743d66616c73652674733d247b6e6577204461746528292e67657454696d6528297d)](https://camo.githubusercontent.com/42cfaf32b70043b0d67e2374fd7215683aff66744da43536865bde135879e5c5/68747470733a2f2f686974732e78796b742e64652f686974735f6769746875622e7376673f616374696f6e3d68697426636f756e745f62673d253233464641353532267469746c655f62673d253233314438383334267469746c653d56697369747326656467655f666c61743d66616c73652674733d247b6e6577204461746528292e67657454696d6528297d) [![license](https://camo.githubusercontent.com/2817475dd3f38d12681f79bb4a2dd943b31e4339512a019b8f7d720e04ec38c7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4147504c25323076332d626c75652e737667)](https://github.com/xykt/Hits/blob/main/LICENSE)

Hits! A completely free, serverless, lightweight access counter system based on **Cloudflare Workers** and **D1 SQL Database**, supporting JSON and GitHub-style SVG images, with quick deployment in just one minute

## ✨ Features

[](#-features)

* 🚀 **Quick Deployment** - Deploy in just one minute
* ☁️ **Cloud Hosting** - No server maintenance required
* 💰 **Completely Free** - Utilizes Cloudflare's free plan
* 📊 **Multi-Site Support** - Supports multiple counters via different keywords
* 🔒 **Secure and Reliable** - Powered by Cloudflare's global network
* 🎨 **Colorful Display** - Supports customizable color SVG and JSON output

## 🛠 Quick Deployment Guide

[](#-quick-deployment-guide)

### 1. Create D1 Database

[](#1-create-d1-database)

Go to the Cloudflare Dashboard, navigate to **Storage & Databases** > **D1 SQL Database** > **Create**, name it *hits*, and run the following SQL to create the table in Console

```
CREATE TABLE counters ( name TEXT PRIMARY KEY, count INTEGER DEFAULT 0 );
```

### 2. Create Workers

[](#2-create-workers)

Navigate to **Workers & Pages** > **Create application** > **Create Worker**, name it *hits*. Copy the [hit.js](https://github.com/xykt/Hits/blob/main/hits.js) code into the Worker editor. Modify line 7 to change the domain to your counter's domain, and set the keywords in line 8. Each counter corresponds to a keyword. For subsequent counters, simply add new keywords for them.

### 3. Configure Bindings

[](#3-configure-bindings)

In the Worker **Settings** > **Bindings** > **Add** > **D1 Database**, enter the variable name as *HITS*, and select the *hits* database. In **Domains & Routes** - **Add** - **Custom domain**, add your newly configured counter domain.

### 4. How to Use

[](#4-how-to-use)

* SVG Image

```
https://your.domain/keyword.svg?action=view&count_bg=%233DC8C0&title_bg=%23555555&title=Visits&edge_flat=false
```

| Parameter  | Values         | Description                    | 说明        |
| ---------- | -------------- | ------------------------------ | --------- |
| action     | view / hit     | View only or hit & view        | 仅展示/点击并展示 |
| count\_bg  | %23{colorcode} | Background color of count area | 数字部分背景颜色  |
| title\_bg  | %23{colorcode} | Background color of title area | 标题部分背景颜色  |
| title      | TitleToShow    | Text to display                | 展示标题      |
| edge\_flat | true / false   | Sharp or rounded corners       | 尖角/圆角     |

| [Styles](https://github.com/xykt/Hits/blob/main/res/style.md) | Black                                                                                                                                                   | Gray                                                                                                                                                    | Blue                                                                                                                                                    | Green                                                                                                                                                   | Purple                                                                                                                                                  | Red                                                                                                                                                     |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Red**                                                       | [![1](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/11.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/11.svg)  | [![2](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/12.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/12.svg)  | [![3](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/13.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/13.svg)  | [![4](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/14.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/14.svg)  | [![5](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/15.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/15.svg)  | [![6](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/16.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/16.svg)  |
| **Orange**                                                    | [![7](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/21.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/21.svg)  | [![8](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/22.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/22.svg)  | [![9](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/23.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/23.svg)  | [![10](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/24.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/24.svg) | [![11](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/25.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/25.svg) | [![12](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/26.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/26.svg) |
| **Yellow**                                                    | [![13](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/31.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/31.svg) | [![14](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/32.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/32.svg) | [![15](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/33.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/33.svg) | [![16](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/34.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/34.svg) | [![17](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/35.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/35.svg) | [![18](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/36.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/36.svg) |
| **Green**                                                     | [![19](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/41.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/41.svg) | [![20](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/42.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/42.svg) | [![21](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/43.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/43.svg) | [![22](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/44.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/44.svg) | [![23](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/45.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/45.svg) | [![24](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/46.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/46.svg) |
| **Blue**                                                      | [![25](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/51.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/51.svg) | [![26](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/52.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/52.svg) | [![27](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/53.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/53.svg) | [![28](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/54.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/54.svg) | [![29](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/55.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/55.svg) | [![30](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/56.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/56.svg) |
| **Purple**                                                    | [![31](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/61.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/61.svg) | [![32](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/62.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/62.svg) | [![33](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/63.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/63.svg) | [![34](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/64.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/64.svg) | [![35](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/65.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/65.svg) | [![36](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/66.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/66.svg) |
| **Gray**                                                      | [![37](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/71.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/71.svg) | [![38](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/72.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/72.svg) | [![39](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/73.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/73.svg) | [![40](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/74.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/74.svg) | [![41](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/75.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/75.svg) | [![42](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/76.svg)](https://raw.githubusercontent.com/xykt/Hits/refs/heads/main/res/76.svg) |

* JSON Result

| Request                                   | Description | 说明    |
| ----------------------------------------- | ----------- | ----- |
| `https://your.domain/keyword?action=view` | View only   | 仅展示   |
| `https://your.domain/keyword?action=hit`  | Hit & View  | 点击并展示 |

JSON Response

```
{
  "counter": "keyword",
  "action": "hit",
  "total": 1024,
  "daily": 64,
  "date": "2025-03-25",
  "timestamp": "2025-03-25T09:50:53.096Z"
}
```

### Acknowledgements

[](#acknowledgements)

* Thanks to [酒神@Nodeseek](https://www.nodeseek.com/space/9#/general) for technical support and valuable feedback.

Welcome to submit Pull Request or Issue!


