---
title: "Nextflux: 一个基于Web的现代RSS阅读器，专为Miniflux设计"
slug: nextflux-web-based-rss-reader
description: |
  Nextflux是一个现代的RSS阅读器客户端，使用React + Vite构建，支持移动设备与PWA。具备快速反应的用户界面、自动后台同步、主题切换和丰富的阅读体验，适合连接Miniflux服务器的用户。
tags: 
  - webdev
  - react
  - PWA
  - RSS
  - opensource
pubDatetime: 2025-01-19T22:32:29+08:00
ogImage: https://repository-images.githubusercontent.com/901896523/0b5e855d-7b82-4bc4-adfd-c73ea99ccad5
---

[原文链接](https://github.com/electh/nextflux)

---

# Nextflux

[](#nextflux)

A modern RSS reader client for Miniflux built with React + Vite.

[![preview](/electh/nextflux/raw/main/images/preview.png)](https://github.com/electh/nextflux/blob/main/images/preview.png)

## ✨ Features

[](#-features)

* 🚀 Fast and responsive UI built with NextUI

* 🌐 Connect to your Miniflux server

* 🔄 Automatic background sync with configurable intervals

* 📱 Mobile-friendly with PWA support

* 🌙 Light/Dark mode with multiple theme options

* 🌍 i18n support (English & Chinese)

* 👀 Mark as read on scroll

* 🎯 Rich reading experience

  * Custom font settings
  * Image gallery with touch gestures support
  * Podcast support
  * Video player support

* ⌨️ Keyboard shortcuts

* 📊 Feed management

  * OPML import
  * Category organization
  * Feed hiding

## 📸 Screenshot Galleries

[](#-screenshot-galleries)

|                                                                                                                      |                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Podcast                                                                                                              | YouTube                                                                                                                    |
| [![](/electh/nextflux/raw/main/images/podcast.png)](https://github.com/electh/nextflux/blob/main/images/podcast.png) | [![](/electh/nextflux/raw/main/images/youtube.png)](https://github.com/electh/nextflux/blob/main/images/youtube.png)       |
| Code Highlight                                                                                                       | Image Gallery                                                                                                              |
| [![](/electh/nextflux/raw/main/images/code.png)](https://github.com/electh/nextflux/blob/main/images/code.png)       | [![](/electh/nextflux/raw/main/images/images.png)](https://github.com/electh/nextflux/blob/main/images/images.png)         |
| Feed Management                                                                                                      | Settings                                                                                                                   |
| [![](/electh/nextflux/raw/main/images/feed.png)](https://github.com/electh/nextflux/blob/main/images/feed.png)       | [![](/electh/nextflux/raw/main/images/settings.png)](https://github.com/electh/nextflux/blob/main/images/settings.png)     |
| Stone theme                                                                                                          | Responsive                                                                                                                 |
| [![](/electh/nextflux/raw/main/images/stone.png)](https://github.com/electh/nextflux/blob/main/images/stone.png)     | [![](/electh/nextflux/raw/main/images/responsive.png)](https://github.com/electh/nextflux/blob/main/images/responsive.png) |
| Search                                                                                                               | Dark Mode                                                                                                                  |
| [![](/electh/nextflux/raw/main/images/search.png)](https://github.com/electh/nextflux/blob/main/images/search.png)   | [![](/electh/nextflux/raw/main/images/dark.png)](https://github.com/electh/nextflux/blob/main/images/dark.png)             |
| Mobile                                                                                                               | Windows                                                                                                                    |
| [![](/electh/nextflux/raw/main/images/mobile.png)](https://github.com/electh/nextflux/blob/main/images/mobile.png)   | [![](/electh/nextflux/raw/main/images/windows.png)](https://github.com/electh/nextflux/blob/main/images/windows.png)       |

## 🛠️ Tech Stack

[](#️-tech-stack)

* React 18
* Vite
* TailwindCSS
* NextUI
* i18next
* IndexedDB
* Nanostores
* DayJS

## 🚀 Deployment

[](#-deployment)

### Docker Deployment

[](#docker-deployment)

Run with Docker using the following command:

```
docker run -d --name nextflux -p 80:80 --restart unless-stopped electh/nextflux:latest
```

### Cloudflare Pages Deployment

[](#cloudflare-pages-deployment)

1. Fork this repository to your GitHub account
2. Create a new project in Cloudflare Pages
3. Select your forked repository
4. Select Framework preset: `React(Vite)`
5. Set build command: `npm run build`
6. Set build output directory: `dist`
7. Deploy and access through the Cloudflare-assigned domain

## 📝 Configuration

[](#-configuration)

The app requires a Miniflux server to function. You'll need to provide:

* Server URL
* Username
* Password

## 🌍 Browser Support

[](#-browser-support)

* Chrome (recommended)
* Firefox
* Safari
* Edge

## 📱 Mobile Support

[](#-mobile-support)

The app is fully responsive and works well on mobile devices. It can also be installed as a PWA for a native app-like experience.

## 🤝 Contributing

[](#-contributing)

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

[](#-license)

This project is licensed under the MIT License - see the LICENSE file for details.


