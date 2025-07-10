---
title: "OpenCut：开源的CapCut替代品，隐私、安全、易用"
slug: opencut-open-source-capcut-alternative
description: |
  OpenCut是一个免费的开源视频编辑器，适用于网络、桌面和移动平台。用户的视频保留在本地，提供丰富功能，无水印或订阅，并具有易用性。OpenCut是CapCut的理想替代品，支持时间轴编辑、多轨道和实时预览，是一个注重隐私的理想工具。
tags: 
  - opensource
  - tool
pubDatetime: 2025-07-10T17:21:53+08:00
ogImage: https://opengraph.githubassets.com/45fe542561c783b3f0f8e9dd3a9158e4e0759430f459eb026155f79cd11e0847/OpenCut-app/OpenCut
---

[原文链接](https://github.com/OpenCut-app/OpenCut)

---

|                                                                                                                                                      |                                                                                                                                                                                  |
| :--------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [![OpenCut Logo](/OpenCut-app/OpenCut/raw/main/apps/web/public/logo.png)](https://github.com/OpenCut-app/OpenCut/blob/main/apps/web/public/logo.png) | # OpenCut (prev AppCut)[](#opencut-prev-appcut)### A free, open-source video editor for web, desktop, and mobile.[](#a-free-open-source-video-editor-for-web-desktop-and-mobile) |

## Why?

[](#why)

* **Privacy**: Your videos stay on your device
* **Free features**: Every basic feature of CapCut is paywalled now
* **Simple**: People want editors that are easy to use - CapCut proved that

## Features

[](#features)

* Timeline-based editing
* Multi-track support
* Real-time preview
* No watermarks or subscriptions
* Analytics provided by [Databuddy](https://www.databuddy.cc?utm_source=opencut), 100% Anonymized & Non-invasive.

## Project Structure

[](#project-structure)

* `apps/web/` – Main Next.js web application
* `src/components/` – UI and editor components
* `src/hooks/` – Custom React hooks
* `src/lib/` – Utility and API logic
* `src/stores/` – State management (Zustand, etc.)
* `src/types/` – TypeScript types

## Getting Started

[](#getting-started)

### Prerequisites

[](#prerequisites)

Before you begin, ensure you have the following installed on your system:

* [Bun](https://bun.sh/docs/installation)
* [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
* [Node.js](https://nodejs.org/en/) (for `npm` alternative)

### Setup

[](#setup)

1. **Clone the repository**

   ```
   git clone https://github.com/OpenCut-app/OpenCut.git
   cd OpenCut
   ```

2. **Start backend services** From the project root, start the PostgreSQL and Redis services:

   ```
   docker-compose up -d
   ```

3. **Set up environment variables** Navigate into the web app's directory and create a `.env` file from the example:

   ```
   cd apps/web


   # Unix/Linux/Mac
   cp .env.example .env.local

   # Windows Command Prompt
   copy .env.example .env.local

   # Windows PowerShell
   Copy-Item .env.example .env.local
   ```

   *The default values in the `.env` file should work for local development.*

4. **Install dependencies** Install the project dependencies using `bun` (recommended) or `npm`.

   ```
   # With bun
   bun install

   # Or with npm
   npm install
   ```

5. **Run database migrations** Apply the database schema to your local database:

   ```
   # With bun
   bun run db:push:local

   # Or with npm
   npm run db:push:local
   ```

6. **Start the development server**

   ```
   # With bun
   bun run dev

   # Or with npm
   npm run dev
   ```

The application will be available at <http://localhost:3000>.

## Contributing

[](#contributing)

**Note**: We're currently moving at an extremely fast pace with rapid development and breaking changes. While we appreciate the interest, it's recommended to wait until the project stabilizes before contributing to avoid conflicts and wasted effort.

## Visit [CONTRIBUTING.md](https://github.com/OpenCut-app/OpenCut/blob/main/.github/CONTRIBUTING.md)

[](#visit-contributingmd)

We welcome contributions! Please see our [Contributing Guide](https://github.com/OpenCut-app/OpenCut/blob/main/.github/CONTRIBUTING.md) for detailed setup instructions and development guidelines.

**Quick start for contributors:**

* Fork the repo and clone locally
* Follow the setup instructions in CONTRIBUTING.md
* Create a feature branch and submit a PR

## Sponsors

[](#sponsors)

Thanks to [Vercel](https://vercel.com?utm_source=github-opencut\&utm_campaign=oss) for their support of open-source software.

[![Deploy with Vercel](https://camo.githubusercontent.com/20bea215d35a4e28f2c92ea5b657d006b087687486858a40de2922a4636301ab/68747470733a2f2f76657263656c2e636f6d2f627574746f6e)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FOpenCut-app%2FOpenCut\&project-name=opencut\&repository-name=opencut)

## License

[](#license)

[MIT LICENSE](https://github.com/OpenCut-app/OpenCut/blob/main/LICENSE)


