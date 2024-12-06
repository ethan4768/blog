---
title: 为何 DatoCMS 从 Next.js 迁移至 Astro 以提升性能和简化架构
slug: 为什么我们从-next-js-迁移到-astro
description: 在本文中，DatoCMS 分享了他们从 Next.js 迁移到 Astro 的经历，探讨了迁移的原因、获得的好处，以及供内容驱动站点参考的实用建议。从简化架构、实时更新到精确缓存，Astro 的优势逐一呈现。
tags: 
  - ai
  - tool
  - dev
  - startup
pubDatetime: 2024-12-06T15:25:47+08:00
ogImage: https://www.datocms-assets.com/205/1733237052-cover-astro.png?auto=format&fit=max&w=1200
---

[原文链接](https://www.datocms.com/blog/why-we-switched-to-astro)

---

If everything went according to plan, no one should have noticed anything. But for a few days now, this site has been completely new.如果一切都按计划进行的话，应该不会有人注意到什么。但几天来，这个网站已经焕然一新了。

**We took our old Next 13 site and completely rewrote it in Astro! 🧑‍🚀🚀我们采用了旧的 Next 13 网站并用 Astro 完全重写了它！ 🧑‍🚀🚀**

Not only that: we also moved from the classic Vercel hosting to a completely server-side rendering approach on a VPS, which allows our team an editing experience with immediate feedback, combined with a blazing-fast CDN for the website visitors.不仅如此：我们还从经典的 Vercel 托管转向 VPS 上的完全服务器端渲染方法，这使我们的团队能够获得即时反馈的编辑体验，并为网站访问者提供超快的 CDN。

Astro was a bet. We didn't know it well enough to be sure everything would go as expected. But **the result was a complete success from every perspective**, and the development experience was extremely educational and — not something to be taken for granted — *fun*.Astro 是一个赌注。我们对此了解不够，无法确保一切都会按预期进行。但从**各个角度来看，结果都是完全成功的**，而且开发体验非常有教育意义，并且充满*乐趣*（不是理所当然的事情）。

The final architecture offers performance and consumption typical of a static site, coupled with instant and granular page-level invalidation thanks to our [Cache Tags](https://www.datocms.com/blog/introducing-datocms-cache-tags). The dream of every website.最终的架构提供了静态站点典型的性能和消耗，再加上我们的[缓存标签](https://www.datocms.com/blog/introducing-datocms-cache-tags)的即时和细粒度的页面级失效。每个网站的梦想。

This is part one of a series of articles in which we'll try to summarize our journey, sharing many cool little Astro details we discovered (or totally came up with) in the process. We hope they can be useful to those, who like us, manage a content-driven site and would like to consider an alternative to the classic Next/Nuxt/Svelte + Vercel/Netlify stack.这是一系列文章中的一部分，我们将在其中总结我们的旅程，分享我们在此过程中发现（或完全想出）的许多很酷的 Astro 小细节。我们希望它们对那些像我们一样管理内容驱动网站并希望考虑经典 Next/Nuxt/Svelte + Vercel/Netlify 堆栈的替代方案的人有用。

Now let’s be clear – by no means are we suggesting we’re *against&#x20;*&#x4E;ext.js. Heck, we’re incredibly proud of the official [Next.js conference starter](http://next.js/) which was originally built with DatoCMS in 2020! However, considering our content and sitemap, several factors came into play to make this decision.现在让我们明确一点——我们绝不是在暗示我们*反对*Next.js。哎呀，我们对官方[Next.js 会议启动器](http://next.js/)感到非常自豪，它最初是在 2020 年使用 DatoCMS 构建的！然而，考虑到我们的内容和站点地图，做出这个决定时需要考虑几个因素。

## Why did you do it?你为什么这么做？[]()[](#why-did-you-do-it)

There are many reasons why we needed to make BIG changes to our website.我们需要对网站进行重大更改的原因有很多。

##### TypeScript  打字稿[]()[](#typescript)

Our Next site was a project born in 2019: five years in the magical frontend world is a geological era (unfortunately). At the time, there were no reliable typed GraphQL schema generators. The result was that the old site was written in pure JS, without TypeScript. Over time, as pages increased, we felt less and less comfortable making big modifications with the confidence of not breaking anything.我们的 Next 站点是一个诞生于 2019 年的项目：在神奇的前端世界里，五年是一个地质时代（不幸的是）。当时，还没有可靠的类型化 GraphQL 模式生成器。结果是旧站点是用纯 JS 编写的，没有 TypeScript。随着时间的推移，随着页面的增加，我们越来越不愿意在不破坏任何东西的情况下进行重大修改。

Hence the first objective: **regain confidence by switching to a complete TypeScript codebase**, where every GraphQL query would be fully typed. But since that meant rewriting a good chunk of our code anyways, why not consider alternatives to Next.js?因此第一个目标是：**通过切换到完整的 TypeScript 代码库来重新获得信心**，其中每个 GraphQL 查询都将被完全键入。但既然这意味着无论如何都要重写我们的大部分代码，为什么不考虑 Next.js 的替代品呢？

##### Eating our own dog food吃我们自己的狗粮[]()[](#eating-our-own-dog-food)

Our product, DatoCMS, has changed A LOT since 2019. Yet our Next site wasn't leveraging some of the coolest features we've released in recent times, like [GraphQL "Strict Mode"](https://www.datocms.com/blog/introducing-strict-mode-for-graphql-cda-get-the-best-typescript-dx) — which pairs wonderfully with TypeScript — but especially [Cache Tags](https://www.datocms.com/blog/introducing-datocms-cache-tags), which can offer top-notch performance through **completely static and cached content**, while still letting visitors access the latest version of any page, seconds after changes have been published.我们的产品 DatoCMS 自 2019 年以来发生了很大变化。然而，我们的 Next 网站并没有利用我们最近发布的一些最酷的功能，例如[GraphQL“严格模式”](https://www.datocms.com/blog/introducing-strict-mode-for-graphql-cda-get-the-best-typescript-dx) ——它与 TypeScript 完美搭配——但尤其是[缓存标签](https://www.datocms.com/blog/introducing-datocms-cache-tags)，它可以通过**完全静态和缓存的内容**提供一流的性能，同时仍然允许访问者在更改发布后几秒钟内访问任何页面的最新版本。

We wanted a site that represented **the state of the art of what DatoCMS can offer**.我们想要一个能够代表**DatoCMS 所能提供的最先进内容的**网站。

##### A simpler mental model  更简单的心智模型[]()[](#a-simpler-mental-model)

In 2019, Next.js introduced [`getStaticProps()`](https://nextjs.org/blog/next-9-3#next-gen-static-site-generation-ssg-support) along with [Draft Mode ](https://nextjs.org/blog/next-9-3#preview-mode)— a revolutionary hybrid static/dynamic approach that was a breath of fresh air compared to our former Gatsby setup. The developer experience was delightful and straightforward.2019 年，Next.js 引入了[`getStaticProps()`](https://nextjs.org/blog/next-9-3#next-gen-static-site-generation-ssg-support)和[Draft Mode——](https://nextjs.org/blog/next-9-3#preview-mode)一种革命性的静态/动态混合方法，与我们之前的 Gatsby 设置相比，令人耳目一新。开发人员的体验是令人愉快且简单的。

Fast forward to today, and the React ecosystem has transformed dramatically. Setting up React is now so complex that React itself [recommends using it exclusively through a framework](https://react.dev/learn/start-a-new-react-project). Next.js and React have become almost indistinguishable, to the point where, at the time of its public launch, Next.js 15 was using... an unreleased React release candidate?快进到今天，React 生态系统已经发生了巨大的变化。现在设置 React 非常复杂，以至于 React 本身[建议通过框架专门使用它](https://react.dev/learn/start-a-new-react-project)。 Next.js 和 React 几乎无法区分，以至于在公开发布时，Next.js 15 使用的是……未发布的 React 候选版本？

Starting with Next.js 14, the introduction of the app router, Server Components, and Incremental Regeneration (ISR) have **exponentially increased complexity**. Our team frequently encountered bewildering results and errors, with Next.js documentation offering little clarity about the underlying mechanics. We're not alone in this frustration — many developers are questioning the framework's direction (i.e. [Why I Won't Use Next.js](https://www.epicweb.dev/why-i-wont-use-nextjs)).从 Next.js 14 开始，应用程序路由器、服务器组件和增量再生 (ISR) 的引入使**复杂性呈指数级增加**。我们的团队经常遇到令人困惑的结果和错误，Next.js 文档几乎没有提供有关底层机制的清晰信息。我们并不是唯一遇到这种挫败感的人——许多开发人员都在质疑框架的方向（即[为什么我不会使用 Next.js](https://www.epicweb.dev/why-i-wont-use-nextjs) ）。

While Next.js 15 addresses some issues, and is an incredibly powerful framework, it feels like React/Next is moving in a direction that isn't ours. **For a content-driven site with static pages that look the same to every visitor, these increasingly sophisticated solutions feel like overkill&#x20;**&#x61;nd force us into unnecessary complexity.虽然 Next.js 15 解决了一些问题，并且是一个非常强大的框架，但感觉 React/Next 正在朝着不属于我们的方向发展。**对于一个内容驱动的网站，静态页面对每个访问者来说都是一样的，这些日益复杂的解决方案感觉有点矫枉过正**，迫使我们陷入不必要的复杂性。

Hence the last objectives:因此最后的目标是：

* **return to a simple mental model** that doesn't require a frontend degree to navigate without making massive errors.**返回到一个简单的思维模型**，不需要前端学位就可以在不犯大错误的情况下进行导航。

* **design a simple, standards-based architecture** that offers maximum control and remains cost-effective.**设计一个简单的、基于标准的架构**，提供最大限度的控制并保持成本效益。

## Why Astro?  为什么是阿斯特罗？[]()[](#why-astro)

With these premises, choosing Astro as the reference framework was quite an obvious consequence.有了这些前提，选择 Astro 作为参考框架是一个非常明显的结果。

To use DatoCMS Cache Tags, the only requirement at the "engine" level of the website is to offer a server-side rendering mode capable of freely manipulating the headers of each page's response, and [Astro checks the box](https://docs.astro.build/en/reference/api-reference/). This is certainly not a strict requirement: Next, Nuxt, SvelteKit... are all frameworks that offer server-side rendering.要使用DatoCMS缓存标签，网站“引擎”级别的唯一要求是提供能够自由操作每个页面响应的标头的服务器端渲染模式， [Astro选中了该框](https://docs.astro.build/en/reference/api-reference/)。这当然不是一个严格的要求：Next、Nuxt、SvelteKit...都是提供服务器端渲染的框架。

The critical distinction lies in their core architectures. Next, Nuxt, and SvelteKit are built with complex, runtime browser rendering engines — a massive overhead for content-driven websites with minimal interactive elements. This approach introduces unnecessary mental overhead for developers, forcing them to constantly juggle the cognitive load of writing code that must execute flawlessly in both server and browser environments. It also increases the overall computational complexity and page size for the final visitor.关键区别在于它们的核心架构。接下来，Nuxt 和 SvelteKit 是使用复杂的运行时浏览器渲染引擎构建的，这对于具有最少交互元素的内容驱动网站来说是巨大的开销。这种方法给开发人员带来了不必要的心理负担，迫使他们不断地应对编写必须在服务器和浏览器环境中完美执行的代码的认知负担。它还增加了最终访问者的整体计算复杂性和页面大小。

Astro takes a bold and clear position: it is firmly focused on server-side and static generation. Unlike its competitors, **Astro categorically refuses browser-side rendering**. It doesn't just minimize client-side rendering — it eliminates it entirely. And this goes exactly towards our goal: a simple mental model.Astro 采取了大胆而明确的立场：它坚定地专注于服务器端和静态生成。与竞争对手不同， **Astro 断然拒绝浏览器端渲染**。它不仅最大限度地减少了客户端渲染，还完全消除了它。这正是我们的目标：一个简单的心理模型。

> Wait, why not just use PHP then? 👀等等，为什么不直接使用 PHP 呢？ 👀

Because web development isn't black and white. No site can be completely absent of JavaScript — *certainly not ours!* And when you need to break free from pure server-side rendering and add interactive elements, Astro provides a seamless solution that PHP simply cannot match.因为网络开发并不是黑白分明的。没有一个网站可以完全没有 JavaScript——*当然不是我们的网站！*&#x5F53;您需要摆脱纯粹的服务器端渲染并添加交互元素时，Astro 提供了 PHP 根本无法比拟的无缝解决方案。

Having Vite as its engine, Astro allows you to effortlessly insert JavaScript code, handling all the bundling for you. Moreover: if for particular areas of the page you need strong browser-side interactivity, Astro allows you to insert entire [interactive "islands"](https://docs.astro.build/en/concepts/islands/) of React/Vue/Svelte, limiting hydration only to those specific parts.Astro 以 Vite 作为引擎，可以让您轻松插入 JavaScript 代码，为您处理所有捆绑工作。此外：如果对于页面的特定区域，您需要强大的浏览器端交互性，Astro 允许您插入 React/Vue/Svelte 的整个[交互式“岛”](https://docs.astro.build/en/concepts/islands/) ，仅将水合作用限制在这些特定部分。

That's exactly what we, and most content-driven websites, need: the performance and simplicity of server-side rendering for the vast majority of the pages, combined with targeted, rich interactivity where necessary.这正是我们和大多数内容驱动的网站所需要的：绝大多数页面的服务器端渲染的性能和简单性，以及必要时有针对性的丰富交互性。

*(Also, as you may recall, one of our goals was to incorporate a form of safety net through typed languages. PHP/Ruby/Python are not inherently typed, plus lack advanced tools like TypeScript for automatically managing the typing of GraphQL queries. So yeah, PHP will need to take a backseat for now.&#x20;*&#xD83E;�‍♂&#xFE0F;*)**（此外，您可能还记得，我们的目标之一是通过类型化语言纳入一种形式的安全网。PHP/Ruby/Python 本质上不是类型化的，而且缺乏像 TypeScript 这样的高级工具来自动管理 GraphQL 查询的类型化。所以是的，PHP 现在需要退居次要位置*🤷‍♂️ *）*

## The new stack  新堆栈[]()[](#the-new-stack)

[![](https://www.datocms-assets.com/205/1732877403-schema.svg)](https://www.datocms-assets.com/205/1732877403-schema.svg?auto=format\&fit=max\&w=2000)

Wow, that's a lot of arrows! (14 to be precise)哇，有很多箭头！ （准确地说是14个）

Let's analyze it point by point what we came out with:让我们逐点分析一下我们得出的结论：

* The new site is written in Astro and uses the [Node adapter](https://docs.astro.build/en/guides/integrations-guide/node/), meaning the final output of a build is a **Node.js server** that needs to run on a physical server. Astro generates new server-side responses for each incoming request.新站点是用 Astro 编写的，并使用[Node 适配器](https://docs.astro.build/en/guides/integrations-guide/node/)，这意味着构建的最终输出是需要在物理服务器上运行的**Node.js 服务器**。 Astro 为每个传入请求生成新的服务器端响应。

* The server in question is a VPS on [Hetzner](https://www.hetzner.com/). The app deployment is managed by [Kamal](https://kamal-deploy.org/), and can occur manually from the command line or via GitHub Actions. With Hetzner's outrageous prices, you can acquire all the necessary hardware for the task, and more, for just €15/month.有问题的服务器是[Hetzner](https://www.hetzner.com/)上的 VPS。应用程序部署由[Kamal](https://kamal-deploy.org/)管理，可以从命令行或通过 GitHub Actions 手动进行。借助 Hetzner 的惊人价格，您只需每月 15 欧元即可获得完成任务所需的所有硬件以及更多硬件。

* The domain `www-draft.datocms.com` points directly to the Astro server.域名`www-draft.datocms.com`直接指向 Astro 服务器。

* The domain `www.datocms.com`, on the other hand, points to Fastly, a CDN that supports [surrogate keys](https://docs.fastly.com/en/guides/working-with-surrogate-keys). Fastly uses `www-draft.datocms.com` as the origin.另一方面，域名`www.datocms.com`指向 Fastly，这是一个支持[代理键](https://docs.fastly.com/en/guides/working-with-surrogate-keys)的 CDN。 Fastly 使用`www-draft.datocms.com`作为来源。

* Astro pages, depending on whether the request host is either `www-draft` or `www`, will execute GraphQL requests to DatoCMS with the [`X-Include-Drafts` header](https://www.datocms.com/docs/content-delivery-api/api-endpoints#preview-mode-to-retrieve-draft-content) either active or not. This allows our team to access draft content while regular visitors do not.Astro 页面，根据请求主机是`www-draft`还是`www` ，将执行对 DatoCMS 的 GraphQL 请求，其中[`X-Include-Drafts`标头](https://www.datocms.com/docs/content-delivery-api/api-endpoints#preview-mode-to-retrieve-draft-content)要么处于活动状态，要么处于非活动状态。这使得我们的团队能够访问草稿内容，而普通访问者则无法访问。

* Astro also leverages [DatoCMS Cache Tags](https://www.datocms.com/blog/introducing-datocms-cache-tags) to cache pages on Fastly indefinitely. In practical terms, Astro reads the `X-Cache-Tags` header for each GraphQL request made to DatoCMS, and applies those tags identically in its own response via the `Surrogate-Key` header.Astro 还利用[DatoCMS 缓存标签](https://www.datocms.com/blog/introducing-datocms-cache-tags)无限期地缓存 Fastly 上的页面。实际上，Astro 会读取向 DatoCMS 发出的每个 GraphQL 请求的`X-Cache-Tags`标头，并通过`Surrogate-Key`标头将这些标签相同地应用到其自己的响应中。

There's only one missing piece: cache invalidation. DatoCMS, through webhooks, sends cache invalidation tags to the Astro server with every content change on the CMS. Astro then uses those tags to [purge the Fastly cache](https://docs.fastly.com/en/guides/purging-with-surrogate-keys) via an API call:只有一个缺失的部分：缓存失效。 DatoCMS 通过 Webhook，在 CMS 上的每次内容更改时将缓存失效标签发送到 Astro 服务器。然后，Astro 使用这些标签通过 API 调用来[清除 Fastly 缓存](https://docs.fastly.com/en/guides/purging-with-surrogate-keys)：

[![](https://www.datocms-assets.com/205/1732877411-schema2.svg)](https://www.datocms-assets.com/205/1732877411-schema2.svg?auto=format\&fit=max\&w=2000)

Cache invalidation via DatoCMS Webhooks通过 DatoCMS Webhooks 使缓存失效

## How did it go?  进展如何？[]()[](#how-did-it-go)

Honestly, **we cannot be happier** about the final result:老实说，**我们对最终结果感到非常高兴**：

* Astro's support for TypeScript is excellent, and in general, it has allowed us to do everything we needed, even when we had to go outside "the norm".Astro 对 TypeScript 的支持非常出色，总的来说，它使我们能够做我们需要的一切，即使我们不得不超出“规范”。

* The mental model of the architecture is extremely simple: **everything's server-side generated. Period.** No re-hydration, no huge client-side JavaScript bundles.该架构的心智模型非常简单：**一切都是服务器端生成的。时期。**&#x65E0;需重新水化，无需庞大的客户端 JavaScript 包。

* Our team can work on the content and see the results in real-time as they save their drafts through [Web Previews](https://www.datocms.com/marketplace/plugins/i/datocms-plugin-web-previews) and [Real-time Updates](https://www.datocms.com/docs/astro/real-time-updates).我们的团队可以处理内容并在通过[网络预览](https://www.datocms.com/marketplace/plugins/i/datocms-plugin-web-previews)和[实时更新](https://www.datocms.com/docs/astro/real-time-updates)保存草稿时实时查看结果。

* End visitors always get cached content from CDN (thanks to [`stale-while-revalidate`](https://httpwg.org/specs/rfc5861.html#rfc.section.3)), so the **response is immediate**.最终访问者总是从 CDN 获取缓存内容（感谢[`stale-while-revalidate`](https://httpwg.org/specs/rfc5861.html#rfc.section.3) ），因此**响应是立即的**。

* Thanks to cache tags, **cache purging is laser-precise**, ensuring that only the pages that truly require updates are invalidated...由于缓存标签，**缓存清除非常精确**，确保只有真正需要更新的页面才会失效......

* ...yet, developers do not need to take any action to manage all the traditional complexity of caching. Once again, the mental model is straightforward, to the extent that **you can forget about it**....然而，开发人员不需要采取任何操作来管理缓存的所有传统复杂性。再一次，心智模型很简单，以至于**你可以忘记它**。

* Thanks to Fastly, **cache purging happens in less than 150ms**: if we accidentally publish incorrect content, we can correct it instantly, without having to wait minutes for a build to complete.借助 Fastly，**缓存清除的时间不到 150 毫秒**：如果我们不小心发布了不正确的内容，我们可以立即纠正它，而无需等待几分钟才能完成构建。

* Complete builds and cache purging only occur when a new version of the repo is pushed. In our case, the **total build time is approximately 3 minutes**. We can probably improve this if we commit ourselves... the important feature, however, is that this time is **independent of the number of pages** on the site.仅当推送新版本的存储库时才会发生完整的构建和缓存清除。在我们的例子中，**总构建时间约为 3 分钟**。如果我们自己承诺的话，我们也许可以改进这一点……但是，重要的特点是，这个时间**与网站上的页面数量无关**。

* Last, but not least: **hosting costs are ridiculously low**.最后但并非最不重要的一点是：**托管成本低得离谱**。

## How bad was the actual migration?实际的迁移有多糟糕？[]()[](#how-bad-was-the-actual-migration)

Our site is about a hundred different sections: from the beginning of the first tests to the full release, approximately **two and a half months** have passed. Not bad, considering it was never a full-time commitment, and that it has only been [Marco](https://www.marcomezzavilla.com/) and me working on it.我们的网站大约有一百个不同的部分：从第一次测试开始到完整发布，大约已经过去了**两个半月**。还不错，考虑到这从来都不是一个全职的承诺，而且只有[Marco](https://www.marcomezzavilla.com/)和我在努力。

Astro's [JSX-like syntax](https://docs.astro.build/en/basics/astro-syntax/) made it pretty easy to transition all the components. Only the more complex components have remained in React as [Astro Islands](https://docs.astro.build/en/concepts/islands/), while small interactivity (`useState`, `useEffect`, etc.) has been **converted into Web Components** fairly easily.Astro[类似 JSX 的语法](https://docs.astro.build/en/basics/astro-syntax/)使得转换所有组件变得非常容易。 React 中仅保留了较复杂的组件，如[Astro 群岛](https://docs.astro.build/en/concepts/islands/)，而小型交互性（ `useState` 、 `useEffect`等）已相当容易地**转换为 Web 组件**。

## "I want the juicy details!"“我想要有趣的细节！”[]()[](#i-want-the-juicy-details)

Good, because we can't wait to talk to you about it! 😜 After this first introduction to the overall architecture of the new site, the upcoming articles will explore in detail many practical topics related to Astro in conjunction with DatoCMS, and how we achieved clear, clean, and highly maintainable code.很好，因为我们迫不及待地想和您谈谈这件事！ 😜 在首次介绍新网站的整体架构之后，接下来的文章将详细探讨与 Astro 结合 DatoCMS 相关的许多实用主题，以及我们如何实现清晰、干净且高度可维护的代码。

These are just a few of the topics we want to discuss:这些只是我们想要讨论的一些主题：

* Typed GraphQL schema; 类型化 GraphQL 模式；

* GraphQL Fragment Colocation;GraphQL 片段托管；

* URL Building / SEO Management / Sitemaps;URL 建设/SEO 管理/站点地图；

* Error management; 错误管理；

* Astro Actions; 天文行动；

* Replacing React with Web Components;用 Web 组件替换 React；

* View Transitions; 视图转换；

* SVGs; SVG；

Whether you're considering a similar migration or just curious about modern web development best practices, we hope our journey inspires and informs yours. See you in the next episode! 👋无论您是考虑进行类似的迁移，还是只是对现代 Web 开发最佳实践感到好奇，我们都希望我们的旅程能够给您带来启发和启发。下一集见！ 👋


