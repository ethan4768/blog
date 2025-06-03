---
title: "开源事件追踪工具Operational：监控技术产品的事件并获得通知"
slug: operational-event-tracker
description: |
  Operational是一个开源事件追踪工具，支持监控技术产品中的关键事件。轻松发送事件并通过手机或网络应用接收推送通知。支持自托管选项，助力企业实时掌握重要动态，提升运营效率。
tags: 
  - opensource
  - dev
  - tool
  - startup
pubDatetime: 2025-06-03T10:32:14+08:00
ogImage: https://repository-images.githubusercontent.com/701982306/c2a06f3d-c6b5-4420-9df9-8b1d251738c8
---

[原文链接](https://github.com/operational-co/operational.co)

---

[![Operational Event tracker](/operational-co/operational.co/raw/master/media/operational-banner.jpg)](https://operational.co)

[Website](https://operational.co) | [Docs](https://operational.co/api) | [Self-hosting](https://operational.co/selfhosted/introduction) | [Pitch](https://operational.co/pitch) | [Vision](https://operational.co/other/vision)

[Operational.co](https://operational.co) is a open-source Event tracking tool. Monitor signups, webhooks, cronjobs and more.

Operational is a Open source alternative to Logsnag, another Event tracking tool in the same category.

[![Operational Event tracker](/operational-co/operational.co/raw/master/media/operational-screenshot.png?v=1)](https://github.com/operational-co/operational.co/blob/master/media/operational-screenshot.png?v=1)

### Why use Operational?

[](#why-use-operational)

* Get push notifications for critical events straight to your phone, or on the webapp
* Monitor critical events
* Trigger webhooks via action buttons
* Understand complex events via contexts(events-in-events)
* Usable on mobile as a progressive web app(can receive push notifications on mobile too)
* Built for tech businesses

## How to use Operational?

[](#how-to-use-operational)

There are two ways to use Operational:

* Join the waitlist on [Discord](https://discord.gg/QmfGeMGM)
* Self-host [Operational](https://operational.co/selfhosted)

### Highlights

[](#highlights)

* Heaps of self-hosting options, from Render.com to docker images, with video guides. We want you to self-host!
* Very few 3rd party dependencies. No need to install clickhouse in the open source version.
* Feature packed. Send json, formatted json, bundle up logs in contexts, add action buttons, and more.
* Easy to grok and tear apart - no useless dependencies, nor unnecessarily complex code.

## Community

[](#community)

We have a active [Discord](https://discord.gg/QmfGeMGM) community. We highly recommend jumping on our Discord server for updates, feedback and help.

## Contributing to Operational

[](#contributing-to-operational)

[How to contribute?](https://operational.co/other/contributing)

## Technology

[](#technology)

Operational has a dead-simple tech stack:

* Nodejs >=18
* Mysql 8.x
* Prismajs
* Clickhouse(optional)
* Expressjs 5.x
* Vue 3
* Vite

Operational itself is a monorepo of 3 repos:

* /app the SPA for operational.co

* /backend the expressjs app powering the backend

* /website astrojs marketing website

* /packages folder has public npm packages which are shared across all repos.


