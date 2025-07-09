---
title: "Crawlee：一个用于 Node.js 的网络爬虫和浏览器自动化库，支持 AI 和 LLM 数据提取"
slug: crawlee-web-scraping-library
description: |
  Crawlee 是一个为 Node.js 提供的网络爬虫和浏览器自动化库，支持 JavaScript 和 TypeScript。它能够高效提取数据供 AI、LLM 和 RAG 使用，同时支持 HTML、PDF、JPG、PNG 等多种文件类型下载，兼容多种爬虫工具，是构建可靠爬虫的理想选择。
tags: 
  - AI
  - dev
  - tool
  - python
  - opensource
pubDatetime: 2025-07-09T11:43:59+08:00
ogImage: https://repository-images.githubusercontent.com/66670819/8242c30a-d9dc-4580-ae44-f7ea1bfd9b41
---

[原文链接](https://github.com/apify/crawlee)

---

[![Crawlee](https://raw.githubusercontent.com/apify/crawlee/master/website/static/img/crawlee-light.svg?sanitize=true)](https://crawlee.dev)\
A web scraping and browser automation library
=============================================

[](#----------------------------------------------------a-web-scraping-and-browser-automation-library)

[![apify%2Fcrawlee | Trendshift](https://camo.githubusercontent.com/f45162d19225bebf4c2eaf6e3f7dcfe4253278bbbc1b615e635d64d851fe792b/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7265706f7369746f726965732f35313739)](https://trendshift.io/repositories/5179)

[![NPM latest version](https://camo.githubusercontent.com/0254a8a134a98b27e3c3a22da5bfb90fae31709d0cd76d0370b06426dcaeb116/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f40637261776c65652f636f72652e737667)](https://www.npmjs.com/package/@crawlee/core) [![Downloads](https://camo.githubusercontent.com/a9a876e2cefe6ad81ded3d089f0a0506366658d75c28fe98e944327943b39521/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f646d2f40637261776c65652f636f72652e737667)](https://www.npmjs.com/package/@crawlee/core) [![Chat on discord](https://camo.githubusercontent.com/afa7e1b87d07c3e1531206ff182c487373079a12f504d7a95b371871ca09d3b0/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f3830313136333731373931353537343332333f6c6162656c3d646973636f7264)](https://discord.gg/jyEM2PRvMU) [![Build Status](https://github.com/apify/crawlee/actions/workflows/test-ci.yml/badge.svg?branch=master)](https://github.com/apify/crawlee/actions/workflows/test-ci.yml)

Crawlee covers your crawling and scraping end-to-end and **helps you build reliable scrapers. Fast.**

Your crawlers will appear human-like and fly under the radar of modern bot protections even with the default configuration. Crawlee gives you the tools to crawl the web for links, scrape data, and store it to disk or cloud while staying configurable to suit your project's needs.

Crawlee is available as the [`crawlee`](https://www.npmjs.com/package/crawlee) NPM package.

> 👉 **View full documentation, guides and examples on the [Crawlee project website](https://crawlee.dev)** 👈

> Crawlee for Python is open for early adopters. 🐍 [👉 Checkout the source code 👈](https://github.com/apify/crawlee-python).

## Installation

[](#installation)

We recommend visiting the [Introduction tutorial](https://crawlee.dev/js/docs/introduction) in Crawlee documentation for more information.

> Crawlee requires **Node.js 16 or higher**.

### With Crawlee CLI

[](#with-crawlee-cli)

The fastest way to try Crawlee out is to use the **Crawlee CLI** and choose the **Getting started example**. The CLI will install all the necessary dependencies and add boilerplate code for you to play with.

```
npx crawlee create my-crawler
```

```
cd my-crawler
npm start
```

### Manual installation

[](#manual-installation)

If you prefer adding Crawlee **into your own project**, try the example below. Because it uses `PlaywrightCrawler` we also need to install [Playwright](https://playwright.dev). It's not bundled with Crawlee to reduce install size.

```
npm install crawlee playwright
```

```
import { PlaywrightCrawler, Dataset } from 'crawlee';

// PlaywrightCrawler crawls the web using a headless
// browser controlled by the Playwright library.
const crawler = new PlaywrightCrawler({
    // Use the requestHandler to process each of the crawled pages.
    async requestHandler({ request, page, enqueueLinks, log }) {
        const title = await page.title();
        log.info(`Title of ${request.loadedUrl} is '${title}'`);

        // Save results as JSON to ./storage/datasets/default
        await Dataset.pushData({ title, url: request.loadedUrl });

        // Extract links from the current page
        // and add them to the crawling queue.
        await enqueueLinks();
    },
    // Uncomment this option to see the browser window.
    // headless: false,
});

// Add first URL to the queue and start the crawl.
await crawler.run(['https://crawlee.dev']);
```

By default, Crawlee stores data to `./storage` in the current working directory. You can override this directory via Crawlee configuration. For details, see [Configuration guide](https://crawlee.dev/js/docs/guides/configuration), [Request storage](https://crawlee.dev/js/docs/guides/request-storage) and [Result storage](https://crawlee.dev/js/docs/guides/result-storage).

### Installing pre-release versions

[](#installing-pre-release-versions)

We provide automated beta builds for every merged code change in Crawlee. You can find them in the npm [list of releases](https://www.npmjs.com/package/crawlee?activeTab=versions). If you want to test new features or bug fixes before we release them, feel free to install a beta build like this:

```
npm install crawlee@3.12.3-beta.13
```

If you also use the [Apify SDK](https://github.com/apify/apify-sdk-js), you need to specify dependency overrides in your `package.json` file so that you don't end up with multiple versions of Crawlee installed:

```
{
    "overrides": {
       "apify": {
           "@crawlee/core": "3.12.3-beta.13",
           "@crawlee/types": "3.12.3-beta.13",
           "@crawlee/utils": "3.12.3-beta.13"
       }
    }
}
```

## 🛠 Features

[](#-features)

* Single interface for **HTTP and headless browser** crawling
* Persistent **queue** for URLs to crawl (breadth & depth first)
* Pluggable **storage** of both tabular data and files
* Automatic **scaling** with available system resources
* Integrated **proxy rotation** and session management
* Lifecycles customizable with **hooks**
* **CLI** to bootstrap your projects
* Configurable **routing**, **error handling** and **retries**
* **Dockerfiles** ready to deploy
* Written in **TypeScript** with generics

### 👾 HTTP crawling

[](#-http-crawling)

* Zero config **HTTP2 support**, even for proxies
* Automatic generation of **browser-like headers**
* Replication of browser **TLS fingerprints**
* Integrated fast **HTML parsers**. Cheerio and JSDOM
* Yes, you can scrape **JSON APIs** as well

### 💻 Real browser crawling

[](#-real-browser-crawling)

* JavaScript **rendering** and **screenshots**
* **Headless** and **headful** support
* Zero-config generation of **human-like fingerprints**
* Automatic **browser management**
* Use **Playwright** and **Puppeteer** with the same interface
* **Chrome**, **Firefox**, **Webkit** and many others

## Usage on the Apify platform

[](#usage-on-the-apify-platform)

Crawlee is open-source and runs anywhere, but since it's developed by [Apify](https://apify.com), it's easy to set up on the Apify platform and run in the cloud. Visit the [Apify SDK website](https://sdk.apify.com) to learn more about deploying Crawlee to the Apify platform.

## Support

[](#support)

If you find any bug or issue with Crawlee, please [submit an issue on GitHub](https://github.com/apify/crawlee/issues). For questions, you can ask on [Stack Overflow](https://stackoverflow.com/questions/tagged/apify), in GitHub Discussions or you can join our [Discord server](https://discord.com/invite/jyEM2PRvMU).

## Contributing

[](#contributing)

Your code contributions are welcome, and you'll be praised to eternity! If you have any ideas for improvements, either submit an issue or create a pull request. For contribution guidelines and the code of conduct, see [CONTRIBUTING.md](https://github.com/apify/crawlee/blob/master/CONTRIBUTING.md).

## License

[](#license)

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](https://github.com/apify/crawlee/blob/master/LICENSE.md) file for details.


