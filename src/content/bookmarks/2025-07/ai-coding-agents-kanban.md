---
title: "Vibe Kanban: 管理你的AI编码代理的高效看板工具"
slug: ai-coding-agents-kanban
description: |
  Vibe Kanban是一款专为管理AI编码代理而设计的工具，让你能更高效地组织和协调多个编码代理的工作。通过其直观的界面，你可以轻松切换编码代理、并行或顺序执行任务、快速审查工作进度，以及集中管理代理配置。
tags: 
  - AI
  - tool
  - dev
  - opensource
  - vibe
pubDatetime: 2025-07-14T13:51:43+08:00
ogImage: 
---

[原文链接](https://github.com/BloopAI/vibe-kanban?tab=readme-ov-file)

---

[![Vibe Kanban Logo](/BloopAI/vibe-kanban/raw/main/frontend/public/vibe-kanban-logo.svg)](https://vibekanban.com)

Get 10X more out of Claude Code, Gemini CLI, Codex, Amp and other coding agents...

[![npm](https://camo.githubusercontent.com/ee2119b4a59e07e06d70b809512a66ca4081ee2777f5c9f70dbc9a5b09f45bdd/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f766962652d6b616e62616e3f7374796c653d666c61742d737175617265)](https://www.npmjs.com/package/vibe-kanban) [![Build status](https://camo.githubusercontent.com/cd85e5fe9c492eccc0ae2d5d90ce18cc504984c8a895b643d144e52628ec93a4/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f626c6f6f702f766962652d6b616e62616e2f7075626c6973682e796d6c3f7374796c653d666c61742d737175617265266272616e63683d646576)](https://github.com/bloop/vibe-kanban/actions/workflows/publish.yml)

[![](/BloopAI/vibe-kanban/raw/main/frontend/public/vibe-kanban-screenshot-overview.png)](https://github.com/BloopAI/vibe-kanban/blob/main/frontend/public/vibe-kanban-screenshot-overview.png)

## Overview

[](#overview)

AI coding agents are increasingly writing the world's code and human engineers now spend the majority of their time planning, reviewing, and orchestrating tasks. Vibe Kanban streamlines this process, enabling you to:

* Easily switch between different coding agents
* Orchestrate the execution of multiple coding agents in parallel or in sequence
* Quickly review work and start dev servers
* Track the status of tasks that your coding agents are working on
* Centralise configuration of coding agent MCP configs

You can watch a video overview [here](https://youtu.be/TFT3KnZOOAk).

## Installation

[](#installation)

Make sure you have authenticated with your favourite coding agent. A full list of supported coding agents can be found in the [docs](https://vibekanban.com/). Then in your terminal run:

```
npx vibe-kanban
```

## Documentation

[](#documentation)

Please head to the [website](https://vibekanban.com) for the latest documentation and user guides.

## Support

[](#support)

Please open an issue on this repo if you find any bugs or have any feature requests.

## Contributing

[](#contributing)

We would prefer that ideas and changes are raised with the core team via GitHub issues, where we can discuss implementation details and alignment with the existing roadmap. Please do not open PRs without first discussing your proposal with the team.

## Development

[](#development)

### Prerequisites

[](#prerequisites)

* [Rust](https://rustup.rs/) (latest stable)
* [Node.js](https://nodejs.org/) (>=18)
* [pnpm](https://pnpm.io/) (>=8)

```
pnpm i
```

### Running the dev server

[](#running-the-dev-server)

```
pnpm run dev
```

This will start the frontend and backend with live reloading. A blank DB will be copied from the `dev_assets_seed` folder.

### Build from source

[](#build-from-source)

1. Run `build-npm-package.sh`
2. In the `npx-cli` folder run `npm pack`
3. You can run your build with `npx [GENERATED FILE].tgz`


