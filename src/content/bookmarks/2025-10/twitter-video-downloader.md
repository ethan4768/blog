---
title: "强大的Twitter视频下载器和营销工具：ezshine/twitterxdownload"
slug: twitter-video-downloader
description: |
  ezshine/twitterxdownload是一个强大的Twitter视频下载器和营销工具，支持多种媒体提取和一键翻译与再发布功能。适合内容创作者和市场营销人员，同时也为开发人员提供学习Next.js、MongoDB等技术的最佳项目。
tags: 
  - tool
  - opensource
  - makemoney
pubDatetime: 2025-10-14T13:57:52+08:00
ogImage: https://opengraph.githubassets.com/51525b49397d055d3e1c8a0e929c1947283ed7c1c8a60c4e3277358bf3153bba/ezshine/twitterxdownload
---

[原文链接](https://github.com/ezshine/twitterxdownload)

---

[![TwitterXDownload](https://camo.githubusercontent.com/f4ac4fb5881d71120ab09ddf836f19ea2c303b1ccd205bcbdc9d62aaaac93627/68747470733a2f2f7477697474657278646f776e6c6f61642e636f6d2f696d616765732f6c6f676f2e706e67)](https://camo.githubusercontent.com/f4ac4fb5881d71120ab09ddf836f19ea2c303b1ccd205bcbdc9d62aaaac93627/68747470733a2f2f7477697474657278646f776e6c6f61642e636f6d2f696d616765732f6c6f676f2e706e67)

# TwitterXDownload

[](#twitterxdownload)

TwitterXDownload is a powerful Twitter video downloader (not only video). And it's also a marketing tool that helps you republish the content efficiently. You can translate threads with one click.

So, its perfect for content creators, marketers.

BTW: also a best project for Developers to learn Next.js, HeroUI, TailwindCSS, MongoDB, etc.

## ✨ Key Features

[](#-key-features)

* 🎥 **Advanced Media Extraction**: Extract videos and other media from tweets, with support for batch extraction from thread tweets.

* 🔍 **Smart Search**: Search tweets by creator, date, and media type (images/videos)

* 🌐 **Translation & Republishing**: One-click translation and republishing of tweets - an essential tool for Twitter thread marketing

* 🌍 **Multi-language Support**: Available in 12 languages for global accessibility

* 📦 **Self Hosted**:

  * 💰 **AdSense Ready**: optimized for AdSense approval
  * 📈 **SEO Optimized**: optimized for SEO

## 🚀 Self Hosted Guide

[](#-self-hosted-guide)

### Prerequisites

[](#prerequisites)

* Node.js 20+
* Git
* A server with Coolify installed

> Get a supercheap and stable server from RackNerd (<https://my.racknerd.com/aff.php?aff=10399>)

### Local Development Setup

[](#local-development-setup)

`Star` and `Fork` this repository to your own GitHub account.

1. Clone the repository:

```
git clone https://github.com/your-github-username/twitterxdownload.git
cd twitterxdownload
```

2. Install dependencies:

```
npm install
```

3. Create a `.env.local` file and configure environment variables:

```
cp .env.example .env.local
```

```
# MONGODB URI is required
MONGODB_URI=your-mongodb-uri
```

4. Start the development server:

```
npm run dev
```

### Production Deployment with Coolify

[](#production-deployment-with-coolify)

`You can skip this step if you use another deployment service like Vercel, Dokploy, etc.`

#### 1. Setting up Coolify Server

[](#1-setting-up-coolify-server)

1. Install Coolify on your server:

```
curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash
```

2. Access Coolify dashboard through your server IP:

```
http://YOUR_SERVER_IP:8000
```

#### 2. Database Setup in Coolify

[](#2-database-setup-in-coolify)

`You can skip this step if you use another MongoDB service`

1. Navigate to `Projects` in Coolify side menu

2. Click `New Resource` and select `MongoDB`

3. Configure MongoDB settings:

   * Make it publicly available \[✔]
   * Copy the Mongo URL (public)

4. Paste the Mongo URL to your `.env.local` file

#### 3. Environment Variables in Coolify

[](#3-environment-variables-in-coolify)

1. Navigate to `Projects` in Coolify side menu
2. Click `New Resource` and select `Public` or `Private` Repository
3. Select your repository (keep the default settings)
4. Click `Environment Variables` and set the variables same as `.env.local` file

#### 4. Deploying Your Site

[](#4-deploying-your-site)

1. Click `Deploy` button in Project's page

## 💡 Making Money with AdSense

[](#-making-money-with-adsense)

it's perfect designed for SEO, so you can make money with AdSense easily.

1. Deploy your instance following the guide above
2. Apply for Google AdSense
3. Set up your custom domain and fill the `NEXT_PUBLIC_GOOGLE_ADSENSE_ID` in `.env.local` file
4. Monitor and optimize your earnings through the AdSense dashboard

## 🌟 Support

[](#-support)

If you find this project helpful, please consider giving it a star ⭐️

For support, please contact me at Twitter: [@ezshine](https://x.com/intent/follow?screen_name=ezshine)

## 📄 License

[](#-license)

This project is licensed under the GPL-3.0 License - see the [LICENSE](https://github.com/ezshine/twitterxdownload/blob/main/LICENSE) file for details.


