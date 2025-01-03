---
title: "为什么我们将 ComfyDeploy 从 Next.js 迁移到 React"
slug: migrate-from-nextjs-to-react
description: |
  我们将 ComfyDeploy 仪表板从 Next.js 迁移到 React，让构建时间从 3 分钟缩短至 18 秒，热重载时间低于 200 毫秒。通过去除 Next.js 带来的不必要复杂性，我们让开发更加高效和愉悦。
tags: 
  - AI
  - dev
  - react
  - startup
pubDatetime: 2025-01-03T20:08:28+08:00
ogImage: 
---

[原文链接](https://www.comfydeploy.com/blog/you-dont-need-nextjs)

---

We migrated the ComfyDeploy dashboard from Next.js to just React我们将 ComfyDeploy 仪表板从 Next.js 迁移到 React

> You don't need Next.js  你不需要 Next.js

We migrated the ComfyDeploy dashboard from Next.js to just React我们将 ComfyDeploy 仪表板从 Next.js 迁移到 React

## TL;DR  长话短说

* Build time went from **3 mins** to **18 secs**构建时间从**3 分钟**缩短至**18 秒**
* Hot reload under **200ms****200ms**以下热重载
* Everybody on the team is happier (like, way happier)团队中的每个人都更快乐（就像，更快乐）

My tweet about this blew up, so I thought it'd be helpful to break down exactly why we made this move.我关于此事的推文引起了热议，所以我认为详细解释我们采取这一举措的具体原因会有所帮助。

[![Server with GPUs](https://cd-misc.s3.us-east-2.amazonaws.com/docs/CleanShot+2024-12-31+at+14.19.29%402x.png)](https://x.com/BennyKokMusic/status/1873733195767971892)

## How we got here  我们是如何到达这里的

I started ComfyDeploy as an open source project ([GitHub](https://github.com/BennyKok/comfyui-deploy)) - a full stack app with Next.js doing all the heavy lifting for both frontend and backend. We had Drizzle + Server Actions making everything type-safe and neat.我开始将 ComfyDeploy 作为一个开源项目 ( [GitHub](https://github.com/BennyKok/comfyui-deploy) ) - 一个完整的堆栈应用程序，其中 Next.js 负责前端和后端的所有繁重工作。我们使用 Drizzle + Server Actions 使一切都类型安全且整洁。

It was all good until things started hitting the fan:一切都很好，直到事情开始引起关注：

* We received an unexpected $2,000 bill from Vercel due to high API usage from a single user由于单个用户的 API 使用率较高，我们意外收到了 Vercel 发出的 2,000 美元账单
* Testing APIs became a nightmare, because we had a lof of server actions mixed with api routes.测试 API 变成了一场噩梦，因为我们有大量服务器操作与 API 路由混合在一起。
* Build times got so slow it felt like watching paint dry.构建时间变得如此之慢，感觉就像看着油漆变干一样。
* Local dev was brutal - every tiny change triggered a full SSR reload本地开发是残酷的 - 每一个微小的变化都会触发完整的 SSR 重新加载

Next.js is a powerful full-stack framework, but its all-in-one approach can lead to development complexity as your application grows. Our decision to migrate was driven by two key factors: First, as an API platform, we needed to scale beyond Vercel's function limitations - a dedicated auto-scaling server made more sense than Next.js's API layers. Second, since our dashboard was primarily React-based and didn't require Next.js's server-side features, the framework's optimizations were adding unnecessary overhead. Moving to a pure React setup was the logical choice for our use case.Next.js 是一个强大的全栈框架，但随着应用程序的增长，其一体化方法可能会导致开发复杂性。我们做出迁移的决定是由两个关键因素驱动的：首先，作为一个 API 平台，我们需要超越 Vercel 的功能限制 - 专用的自动扩展服务器比 Next.js 的 API 层更有意义。其次，由于我们的仪表板主要基于 React，并且不需要 Next.js 的服务器端功能，因此框架的优化增加了不必要的开销。对于我们的用例来说，转向纯 React 设置是合理的选择。

## The build up  建立起来

As we kept growing, we kept adding more libraries. The build just kept getting slower and slower. At one point, after adding Sentry, it hit 7 minutes. Seven. Minutes. Fixing a typo literally give you a coffee break.随着我们的不断发展，我们不断添加更多的库。构建变得越来越慢。有一次，加入Sentry后，时间达到了7分钟。七。分钟。纠正一个拼写错误实际上可以让你喝杯咖啡休息一下。

The local dev situation wasn't any better. We're running this monorepo with Turborepo, not to mention it became such a pain to manage. Starting up dev servers felt like booting up an old Windows 95 PC, on my M3 Max Macbook Pro.当地的开发情况也好不到哪儿去。我们正在使用 Turborepo 运行这个 monorepo，更不用说管理它变得如此痛苦。启动开发服务器感觉就像在我的 M3 Max Macbook Pro 上启动一台旧的 Windows 95 PC。

Then Next.js 15 RC dropped. I thought, "Hey, Turbopack might save us!" Spent a week upgrading, only to run into compatibility issues. Another week later, we're back on 14, wondering why we're spending more time wrestling with Next.js than actually building our product.然后 Next.js 15 RC 就被放弃了。我想，“嘿，Turbopack 可能会拯救我们！”花了一周的时间升级，却遇到了兼容性问题。又一周后，我们又回到了 14，想知道为什么我们花更多的时间来研究 Next.js，而不是实际构建我们的产品。

## The turning point  转折点

One morning, I'm sitting there watching Next.js take 10 seconds just to start up. That was it. I'd had enough.一天早上，我坐在那里看着 Next.js 启动需要 10 秒。就是这样。我已经受够了。

> "Hey team, we're going back to React. Give me a week."“嘿，团队，我们要回到 React。给我一周时间。”

We went all in with TanStack Router + Rspack. Moved our entire shadcn folder, our components, everything. And you know what? Within days, it felt like we'd broken free from chains we didn't even know we had:我们全力以赴使用 TanStack Router + Rspack。移动了我们的整个 shadcn 文件夹，我们的组件，一切。你知道吗？几天之内，我们感觉就像摆脱了我们甚至不知道自己拥有的枷锁：

* Instant dev server - less than **2 secs**.即时开发服务器 - 不到**2 秒**。
* Vercel build under **18 secs**.Vercel 构建时间不到**18 秒**。
* Web dev actually **fun** again!Web 开发真的又**有趣了**！

The migration forced us to clean house too - ditching old features we didn't need, dropping unused dependencies, and completely rethinking our API setup. Sometimes you need to tear things down to build them back better.这次迁移也迫使我们进行清理——抛弃我们不需要的旧功能，删除未使用的依赖项，并完全重新考虑我们的 API 设置。有时你需要拆除一些东西才能更好地重建它们。

## The Numbers  数字

## Next js 15 with turbo modeNext js 15 采用 Turbo 模式

Here's our local dev experience with next js 15 with turbo mode这是我们使用 Turbo 模式的 next js 15 的本地开发经验

| Metric  公制              | Time  时间         |
| ----------------------- | ---------------- |
| First page build  第一页构建 | 10.4 secs  10.4秒 |

## React with Tanstack Router + Rspack使用 Tanstack Router + Rspack 进行反应

| Metric  公制                | Time  时间          |
| ------------------------- | ----------------- |
| Route compute  路由计算       | \~200ms  〜200毫秒   |
| Initial dev bundle  初始开发包 | 1.67 secs  1.67 秒 |

## The Trade-offs  权衡

Let's be real - every technical decision comes with trade-offs. Here's what we gave up and gained:让我们面对现实吧——每个技术决策都需要权衡。这是我们放弃和获得的：

## What We Lost  我们失去了什么

1. **Co-location of Frontend and Backend前端和后端共置**

Now we have separate frontend and backend codebases but end up having better separation of concerns, clearer boundaries现在我们有独立的前端和后端代码库，但最终有更好的关注点分离、更清晰的边界

2. **Next.js Caching Features  Next.js 缓存功能**

We lost built-in caching mechanisms but actually most of our data needed real-time updates. We ended up implementing specific caching where actually needed我们失去了内置的缓存机制，但实际上我们的大部分数据都需要实时更新。我们最终在实际需要的地方实现了特定的缓存

1. **Pre-rendering and Initial Load预渲染和初始加载**

No more automatic static generation. Required more thoughtful code splitting to save page load speed. But actually improved UX. No more "ghost clicks" where users see buttons they can't interact with because JS hasn't loaded. More predictable loading states不再有自动静态生成。需要更周到的代码分割以节省页面加载速度。但实际上改善了用户体验。不再有“幽灵点击”，用户会看到由于 JS 尚未加载而无法与之交互的按钮。更可预测的加载状态

4. **Server Components and Actions服务器组件和操作**

Lost the "magic" of server components. Server Actions made quick data fetching too easy (maybe too easy?) Forced us to design better, more intentional APIs Better for our real-time needs - polling updates were actually harder with [blocking server actions](https://github.com/vercel/next.js/discussions/50743).失去了服务器组件的“魔力”。服务器操作使快速数据获取变得太容易了（也许太容易了？）迫使我们设计更好、更有意的 API 更好地满足我们的实时需求 - 由于[阻塞服务器操作，](https://github.com/vercel/next.js/discussions/50743)轮询更新实际上更困难。

## The Reality Check  现实检验

Here's the thing: these "losses" forced us to make better architectural decisions. Instead of relying on framework magic, we had to:事情是这样的：这些“损失”迫使我们做出更好的架构决策。我们不能依赖框架魔法，而是必须：

* Design our API contracts more thoughtfully更周到地设计我们的 API 合约
* Implement caching where it actually mattered在真正重要的地方实施缓存
* Think about data flow and state management more deliberately更仔细地考虑数据流和状态管理

Sometimes constraints are exactly what you need to build something better.有时，约束正是你构建更好的东西所需要的。

## Conclusion  结论

If you want to compare the two version [ComfyDeploy React](https://app.comfydeploy.com/) vs [ComfyDeploy Next.js](https://www.comfydeploy.com/workflows).如果您想比较[ComfyDeploy React](https://app.comfydeploy.com/)与[ComfyDeploy Next.js 的](https://www.comfydeploy.com/workflows)两个版本。

Next.js is great for what it's meant to do - landing pages, SEO stuff, that kind of thing. It makes simple concepts look fancy (Server Actions - is just REST API calls).Next.js 非常适合它的用途 - 登陆页面、SEO 等。它使简单的概念看起来很奇特（服务器操作 - 只是 REST API 调用）。

But for most products? It's like using a sledgehammer to hang a picture frame. The jump from Next.js 14 to 15 really drove this home - dependencies breaking left and right, and even with Turbo mode, dev server is still slow enough to make you want to bang your head against the wall.但对于大多数产品呢？这就像用大锤来挂相框一样。从 Next.js 14 到 15 的跳跃确实推动了这一点 - 依赖关系左右断裂，即使使用 Turbo 模式，开发服务器仍然慢得足以让你想用头撞墙。

We still keep Next.js around for our landing page and SEO stuff, but the dashboard? Pure React with TanStack Router + Rspack. Our API? A simple Python FastAPI server chilling on Google Cloud Run, scaling whenever it needs to.我们仍然保留 Next.js 用于我们的登陆页面和 SEO 内容，但是仪表板呢？纯 React 与 TanStack Router + Rspack。我们的 API？一个简单的 Python FastAPI 服务器在 Google Cloud Run 上运行，可在需要时进行扩展。

Sometimes less really is more. And in our case, less Next.js meant more shipping, more speed, and more happy developers.有时，少确实是多。在我们的例子中，更少的 Next.js 意味着更多的运输、更快的速度和更快乐的开发人员。

And I want to be clear - Vercel itself is an amazing company that's built incredible products. We still use and love their platform for various projects. Next.js just turned out to be more than what we needed for our specific use case at this stage of our product.我想明确一点 - Vercel 本身就是一家了不起的公司，打造了令人难以置信的产品。我们仍然使用并喜欢他们的平台来进行各种项目。事实证明，Next.js 超出了我们产品现阶段特定用例所需的功能。

## Lastly!  最后！

We are looking for people obsessed with shipping dev tools, from pushing the pixels on the frontend to optimizing diffusion models in the backend. DM me on [twitter](https://x.com/BennyKokMusic) if you're down.我们正在寻找痴迷于开发工具的人，从推动前端的像素到优化后端的扩散模型。如果您心情不好，请在[Twitter](https://x.com/BennyKokMusic)上给我发私信。


