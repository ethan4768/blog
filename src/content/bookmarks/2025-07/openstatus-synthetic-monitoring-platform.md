---
title: "OpenStatus: 开源的合成监控平台，让您的网站和API时刻保持在线"
slug: openstatus-synthetic-monitoring-platform
description: |
  OpenStatus是一个开源的合成监控平台，可以全球监测您的网站和API，并在它们出现故障或速度缓慢时通知您。利用OpenStatus，您可以轻松获得实时状态更新，确保您的在线服务持续可用。
tags: 
  - openstatus
  - opensource
  - dev
  - tool
pubDatetime: 2025-07-18T19:49:04+08:00
ogImage: https://repository-images.githubusercontent.com/655783613/6d94e471-95fb-4f99-9343-dd6b120fe0c2
---

[原文链接](https://github.com/openstatusHQ/openstatus?tab=readme-ov-file)

---

### OpenStatus

[](#openstatus)

[![](https://camo.githubusercontent.com/38ed91e0e35d6c3ed20b39749f54d4c891c2aa02ddaeee4d141db1d98e90ceb8/68747470733a2f2f7374617475732e6f70656e7374617475732e6465762f6261646765)](https://status.openstatus.dev)

The Open-Source synthetic monitoring platform.\
[**Learn more »**](https://www.openstatus.dev)\
\
[Discord](https://www.openstatus.dev/discord) · [Website](https://www.openstatus.dev) · [Issues](https://github.com/openstatushq/openstatus/issues)

## About OpenStatus 🏓

[](#about-openstatus-)

OpenStatus is open-source synthetic monitoring platform.

* **Synthetic monitoring**: Monitor your website and APIs globally and receive notifications when they are down or slow.

## Recognitions 🏆

[](#recognitions-)

[![openstatusHQ%2Fopenstatus | Trendshift](https://camo.githubusercontent.com/1456f5d15191099af651d619158145ae8d28c7d5b70c7794f914d19e2f7ff792/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7265706f7369746f726965732f31373830)](https://trendshift.io/repositories/1780)

[![Featured on Hacker News](https://camo.githubusercontent.com/92769b4b6728055aa28dc8bc0faa1ba255a481ee1eef69ea000f7a46a2663d82/68747470733a2f2f6861636b657262616467652e6e6f772e73682f6170693f69643d3337373430383730)](https://news.ycombinator.com/item?id=37740870)

## Contact us 💌

[](#contact-us-)

If you are interested in our enterprise plan or need special features, please email us at <ping@openstatus.dev> or book a call\
\
[![Book us with Cal.com](https://camo.githubusercontent.com/298517cca77af25bc85b9663f5f3981400cbfff904619bffae30dae85f45d5a5/68747470733a2f2f63616c2e636f6d2f626f6f6b2d776974682d63616c2d6461726b2e737667)](https://cal.com/team/openstatus/30min)

## Contributing 🤝

[](#contributing-)

If you want to help us building the best status page and alerting system, you can check our [contributing guidelines](https://github.com/openstatusHQ/openstatus/blob/main/CONTRIBUTING.MD)

### Top Contributors

[](#top-contributors)

[![](https://camo.githubusercontent.com/b0eec28446b585df008c5595fddaa7886db6fe80e1c921a6edecc5367fd21ba8/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d6f70656e73746174757368712f6f70656e737461747573)](https://github.com/openstatushq/openstatus/graphs/contributors)

Made with [Contrib.rocks](https://contrib.rocks)

### Stats

[](#stats)

[![Alt](https://camo.githubusercontent.com/b0170e19f96f2e55d8d6239e6fcc8802e839baea5b21f18f6cebe94ec737cdca/68747470733a2f2f7265706f62656174732e6178696f6d2e636f2f6170692f656d6265642f313830656565313539633031323866363833613330663135663531616333356264626439666134342e737667 "Repobeats analytics image")](https://camo.githubusercontent.com/b0170e19f96f2e55d8d6239e6fcc8802e839baea5b21f18f6cebe94ec737cdca/68747470733a2f2f7265706f62656174732e6178696f6d2e636f2f6170692f656d6265642f313830656565313539633031323866363833613330663135663531616333356264626439666134342e737667)

## Tech stack 🥞

[](#tech-stack-)

* [Next.js](https://nextjs.org/)
* [Tailwind CSS](https://tailwindcss.com/)
* [shadcn/ui](https://ui.shadcn.com/)
* [tinybird](https://tinybird.co/?ref=openstatus.dev)
* [turso](https://turso.tech/)
* [drizzle](https://orm.drizzle.team/)
* [Resend](https://resend.com/)

[![Built with Depot](https://camo.githubusercontent.com/b8eaf4c5ce553c0dda2e82335dff6000e84a2e66d937e0283b6aa3c1ed3788ed/68747470733a2f2f6465706f742e6465762f6261646765732f6275696c742d776974682d6465706f742e737667)](https://depot.dev/?utm_source=Opource=OpenStatus)

## Getting Started 🚀

[](#getting-started-)

### With Devbox

[](#with-devbox)

You can use [Devbox](https://www.jetify.com/devbox/) and get started with the following commands:

1. Install Devbox

   ```
   curl -fsSL https://get.jetify.com/devbox | bash
   ```

2. Install project dependencies, build and start services

   ```
   devbox services up
   ```

Alternatively, follow the instructions below.

### Requirements

[](#requirements)

* [Node.js](https://nodejs.org/en/) >= 20.0.0
* [pnpm](https://pnpm.io/) >= 8.6.2
* [Bun](https://bun.sh/)
* [Turso CLI](https://docs.turso.tech/quickstart)

### Setup

[](#setup)

1. Clone the repository

```
git clone https://github.com/openstatushq/openstatus.git
```

2. Install dependencies

```
pnpm install
```

3. Initialize the development environment

Launch the database in one terminal:

```
turso dev --db-file openstatus-dev.db
```

In another terminal, run the following command:

```
pnpm dx
```

4. Launch the web app

```
pnpm dev:web
```

5. See the results:

* open <http://localhost:3000> for the web app

### Videos

[](#videos)

Videos to better understand the OpenStatus codebase:

* [The code behind OpenStatus and how it uses Turbopack](https://youtube.com/watch?v=PYfSJATE8v8).
* [Drop Betterstack and go open source](https://www.youtube.com/watch?v=PKag0USy3eQ)


