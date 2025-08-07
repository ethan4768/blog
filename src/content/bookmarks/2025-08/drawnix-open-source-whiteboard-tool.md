---
title: "Drawnix：一体化开源白板工具，支持思维导图和流程图"
slug: drawnix-open-source-whiteboard-tool
description: |
  Drawnix 是一个开源的白板工具，集成思维导图、流程图和自由画功能，支持自动保存和多种导出格式。基于插件架构，允许用户自由扩展功能，适用于多个 UI 框架。
tags: 
  - opensource
  - dev
  - tool
  - AI
pubDatetime: 2025-08-07T13:31:38+08:00
ogImage: https://opengraph.githubassets.com/b0017d868d43d1c1e409fac2b3bba6991291ca0b24742e722ba7cf79fcbadf5f/plait-board/drawnix
---

[原文链接](https://github.com/plait-board/drawnix)

---

![Drawnix logo and name](https://github.com/plait-board/drawnix/raw/develop/apps/web/public/logo/logo_drawnix_h.svg?raw=true)

## 开源白板工具（SaaS），一体化白板，包含思维导图、流程图、自由画等

[](#----开源白板工具saas一体化白板包含思维导图流程图自由画等----)

[![Product showcase](https://github.com/plait-board/drawnix/raw/develop/apps/web/public/product_showcase/case-2.png)](https://github.com/plait-board/drawnix/blob/develop/apps/web/public/product_showcase/case-2.png)

All in one 白板，思维导图、流程图、自由画等

[![Featured｜HelloGitHub](https://camo.githubusercontent.com/c690b166d339060c56d2dce5101f9b77f440773c76ef40cefce1de32fb11f194/68747470733a2f2f6162726f61642e68656c6c6f6769746875622e636f6d2f76312f776964676574732f7265636f6d6d656e642e7376673f7269643d346463656138303766616237343638613936326331353362303761653465346526636c61696d5f7569643d7a6d465359356b3845755a72693433267468656d653d6e65757472616c)](https://hellogithub.com/repository/plait-board/drawnix)

[*English README*](https://github.com/plait-board/drawnix/blob/develop/README_en.md)

## 特性

[](#特性)

* 💯 免费 + 开源
* ⚒️ 思维导图、流程图
* 🖌 画笔
* 😀 插入图片
* 🚀 基于插件机制
* 🖼️ 📃 导出为 PNG, JSON(`.drawnix`)
* 💾 自动保存（浏览器缓存）
* ⚡ 编辑特性：撤销、重做、复制、粘贴等
* 🌌 无限画布：缩放、滚动
* 🎨 主题模式
* 📱 移动设备适配
* 📈 支持 mermaid 语法转流程图
* ✨ 支持 markdown 文本转思维导图（新支持 🔥🔥🔥）

## 关于名称

[](#关于名称)

***Drawnix*** ，源于绘画( ***Draw*** )与凤凰( ***Phoenix*** )的灵感交织。

凤凰象征着生生不息的创造力，而 *Draw* 代表着人类最原始的表达方式。在这里，每一次创作都是一次艺术的涅槃，每一笔绘画都是灵感的重生。

创意如同凤凰，浴火方能重生，而 ***Drawnix*** 要做技术与创意之火的守护者。

*Draw Beyond, Rise Above.*

## 与 Plait 画图框架

[](#与-plait-画图框架)

*Drawnix* 的定位是一个开箱即用、开源、免费的工具产品，它的底层是 *Plait* 框架，*Plait* 是我司开源的一款画图框架，代表着公司在知识库产品上的重要技术沉淀。

Drawnix 是插件架构，与前面说到开源工具比技术架构更复杂一些，但是插件架构也有优势，比如能够支持多种 UI 框架（*Angular、React*），能够集成不同富文本框架（当前仅支持 *Slate* 框架），在开发上可以很好的实现业务的分层，开发各种细粒度的可复用插件，可以扩展更多的画板的应用场景。

## 仓储结构

[](#仓储结构)

```
drawnix/
├── apps/
│   ├── web                   # drawnix.com
│   │    └── index.html       # HTML
├── dist/                     # 构建产物
├── packages/
│   └── drawnix/              # 白板应用
│   └── react-board/          # 白板 React 视图层
│   └── react-text/           # 文本渲染模块
├── package.json
├── ...
└── README.md
└── README_en.md
```

## 应用

[](#应用)

[*https://drawnix.com*](https://drawnix.com) 是 *drawnix* 的最小化应用。

近期会高频迭代 drawnix.com，直到发布 *Dawn（破晓）* 版本。

## 开发

[](#开发)

```
npm install

npm run start
```

## Docker

[](#docker)

```
docker pull pubuzhixing/drawnix:latest
```

## 依赖

[](#依赖)

* [plait](https://github.com/worktile/plait) - 画图框架
* [slate](https://github.com/ianstormtaylor/slate) - 富文本编辑器框架
* [floating-ui](https://github.com/floating-ui/floating-ui) - 一个超级好用的创建弹出层基础库

## 贡献

[](#贡献)

欢迎任何形式的贡献：

* 提 Bug

* 贡献代码

## 支持

[](#支持)

*欢迎大家 star ⭐️⭐️⭐️ 支持。*

## License

[](#license)

[MIT License](https://github.com/plait-board/drawnix/blob/master/LICENSE)


