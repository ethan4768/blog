---
title: "AstroWind: 免费的Astro 5与Tailwind CSS模板"
slug: astrowind-free-template-astro-tailwind
description: |
  AstroWind是一个使用Astro 5.0和Tailwind CSS打造的免费开源模板，提供快速创建响应式和SEO友好网站的解决方案。包括暗黑模式、MDX支持、图像优化以及内置分析工具，是web开发者的理想选择。
tags: 
  - design
  - opensource
  - Astro
  - Tailwind
pubDatetime: 2025-03-29T07:26:32+08:00
ogImage: https://repository-images.githubusercontent.com/506862351/0e254e61-50e4-4ce2-888f-41ccad55d3d4
---

[原文链接](https://github.com/onwidget/astrowind)

---

# 🚀 AstroWind

[](#-astrowind)

[![AstroWind Lighthouse Score](https://raw.githubusercontent.com/onwidget/.github/main/resources/astrowind/lighthouse-score.png)](https://raw.githubusercontent.com/onwidget/.github/main/resources/astrowind/lighthouse-score.png)

🌟 *Most *starred* & *forked* Astro theme in 2022, 2023 & 2024*. 🌟

**AstroWind** is a free and open-source template to make your website using **[Astro 5.0](https://astro.build/) + [Tailwind CSS](https://tailwindcss.com/)**. Ready to start a new project and designed taking into account web best practices.

* ✅ **Production-ready** scores in **PageSpeed Insights** reports.
* ✅ Integration with **Tailwind CSS** supporting **Dark mode** and ***RTL***.
* ✅ **Fast and SEO friendly blog** with automatic **RSS feed**, **MDX** support, **Categories & Tags**, **Social Share**, ...
* ✅ **Image Optimization** (using new **Astro Assets** and **Unpic** for Universal image CDN).
* ✅ Generation of **project sitemap** based on your routes.
* ✅ **Open Graph tags** for social media sharing.
* ✅ **Analytics** built-in Google Analytics, and Splitbee integration.

\


[![AstroWind Theme Screenshot](https://raw.githubusercontent.com/onwidget/.github/main/resources/astrowind/screenshot-astrowind-1.0.png)](https://raw.githubusercontent.com/onwidget/.github/main/resources/astrowind/screenshot-astrowind-1.0.png)

[![onWidget](https://camo.githubusercontent.com/408b1438a6ac07fb1d015bf45f721345e632a7a5b6a4d59ae80e5adc63f1429a/68747470733a2f2f637573746f6d2d69636f6e2d6261646765732e64656d6f6c61622e636f6d2f62616467652f6d61646525323062792532302d6f6e5769646765742d3535366266323f7374796c653d666c61742d737175617265266c6f676f3d6f6e776964676574266c6f676f436f6c6f723d7768697465266c6162656c436f6c6f723d313031383237)](https://onwidget.com) [![License](https://camo.githubusercontent.com/9709c3cb8685ce12598789a5b7a29747e9d4bb949093fdd23cde3078f3846b7c/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6f6e7769646765742f617374726f77696e643f7374796c653d666c61742d73717561726526636f6c6f723d646464646464266c6162656c436f6c6f723d303030303030)](https://github.com/onwidget/astrowind/blob/main/LICENSE.md) [![Maintained](https://camo.githubusercontent.com/2d6a4cde3d9242cb9fca9ea180bf632bd8c13be8ba533a3b3337d769cdc84172/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d61696e7461696e65642533462d7965732d627269676874677265656e2e7376673f7374796c653d666c61742d737175617265)](https://github.com/onwidget) [![Contributions Welcome](https://camo.githubusercontent.com/0ddc5ef9663d99d289f17507ffc90ef73e33b7a01f91fb475197dc57c4e95508/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f6e747269627574696f6e732d77656c636f6d652d627269676874677265656e2e7376673f7374796c653d666c61742d737175617265)](https://github.com/onwidget/astrowind#contributing) [![Known Vulnerabilities](https://camo.githubusercontent.com/f9e7f166394ad76f1467dc9a4f18040ba4612d5d9bcde2a1e6e67c475b07e15c/68747470733a2f2f736e796b2e696f2f746573742f6769746875622f6f6e7769646765742f617374726f77696e642f62616467652e7376673f7374796c653d666c61742d737175617265)](https://snyk.io/test/github/onwidget/astrowind) [![Stars](https://camo.githubusercontent.com/db7b469a2bb56c27e24af49cedd3caa114f842da6c3fd0a6de021aca1f4f8ebb/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6f6e7769646765742f617374726f77696e642e7376673f7374796c653d736f6369616c266c6162656c3d7374617273266d61784167653d383634303026636f6c6f723d666636396234)](https://github.com/onwidget/astrowind) [![Forks](https://camo.githubusercontent.com/d43799830c1e623b321ac3fc81bfd2f7909cc68e8d11b45ac17471445b74fd06/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f6f6e7769646765742f617374726f77696e642e7376673f7374796c653d736f6369616c266c6162656c3d666f726b73266d61784167653d383634303026636f6c6f723d666636396234)](https://github.com/onwidget/astrowind)

\


Table of Contents

* [Demo](#demo)

* [Upcoming: AstroWind 2.0 – We Need Your Vision!](#-upcoming-astrowind-20--we-need-your-vision)

* [Getting started](#getting-started)

  * [Project structure](#project-structure)
  * [Commands](#commands)
  * [Configuration](#configuration)
  * [Deploy](#deploy)

* [Frequently Asked Questions](#frequently-asked-questions)

* [Related Projects](#related-projects)

* [Contributing](#contributing)

* [Acknowledgements](#acknowledgements)

* [License](#license)

\


## Demo

[](#demo)

📌 <https://astrowind.vercel.app/>

\


## 🔔 Upcoming: AstroWind 2.0 – We Need Your Vision!

[](#-upcoming-astrowind-20--we-need-your-vision)

We're embarking on an exciting journey with **AstroWind 2.0**, and we want you to be a part of it! We're currently taking the first steps in developing this new version and your insights are invaluable. Join the discussion and share your feedback, ideas, and suggestions to help shape the future of **AstroWind**. Let's make **AstroWind 2.0** even better, together!

[Share Your Feedback in Our Discussion!](https://github.com/onwidget/astrowind/discussions/392)

\


## Getting started

[](#getting-started)

**AstroWind** tries to give you quick access to creating a website using [Astro 5.0](https://astro.build/) + [Tailwind CSS](https://tailwindcss.com/). It's a free theme which focuses on simplicity, good practices and high performance.

Very little vanilla javascript is used only to provide basic functionality so that each developer decides which framework (React, Vue, Svelte, Solid JS...) to use and how to approach their goals.

In this version the template supports all the options in the `output` configuration, `static`, `hybrid` and `server`, but the blog only works with `prerender = true`. We are working on the next version and aim to make it fully compatible with SSR.

### Project structure

[](#project-structure)

Inside **AstroWind** template, you'll see the following folders and files:

```
/
├── public/
│   ├── _headers
│   └── robots.txt
├── src/
│   ├── assets/
│   │   ├── favicons/
│   │   ├── images/
│   │   └── styles/
│   │       └── tailwind.css
│   ├── components/
│   │   ├── blog/
│   │   ├── common/
│   │   ├── ui/
│   │   ├── widgets/
│   │   │   ├── Header.astro
│   │   │   └── ...
│   │   ├── CustomStyles.astro
│   │   ├── Favicons.astro
│   │   └── Logo.astro
│   ├── content/
│   │   ├── post/
│   │   │   ├── post-slug-1.md
│   │   │   ├── post-slug-2.mdx
│   │   │   └── ...
│   │   └-- config.ts
│   ├── layouts/
│   │   ├── Layout.astro
│   │   ├── MarkdownLayout.astro
│   │   └── PageLayout.astro
│   ├── pages/
│   │   ├── [...blog]/
│   │   │   ├── [category]/
│   │   │   ├── [tag]/
│   │   │   ├── [...page].astro
│   │   │   └── index.astro
│   │   ├── index.astro
│   │   ├── 404.astro
│   │   ├-- rss.xml.ts
│   │   └── ...
│   ├── utils/
│   ├── config.yaml
│   └── navigation.js
├── package.json
├── astro.config.ts
└── ...
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.

Any static assets, like images, can be placed in the `public/` directory if they do not require any transformation or in the `assets/` directory if they are imported directly.

[![Edit AstroWind on CodeSandbox](https://camo.githubusercontent.com/ecd139ba9847d0c77607c86339eb8ee6939ca85143a92ae16ebf20f58325e1b6/68747470733a2f2f636f646573616e64626f782e696f2f7374617469632f696d672f706c61792d636f646573616e64626f782e737667)](https://githubbox.com/onwidget/astrowind/tree/main) [![Open in Gitpod](https://camo.githubusercontent.com/c382d7567ed2a922b5195a3c2a7db8f4329cc4c990bdf319e286592048db9569/68747470733a2f2f73766773686172652e636f6d2f692f7864692e737667)](https://gitpod.io/?on=gitpod#https://github.com/onwidget/astrowind) [![Open in StackBlitz](https://camo.githubusercontent.com/e9392ad1a0cb081a5be23067cfb953616abc12f4e260f581a302e020c41d41c0/68747470733a2f2f646576656c6f7065722e737461636b626c69747a2e636f6d2f696d672f6f70656e5f696e5f737461636b626c69747a2e737667)](https://stackblitz.com/github/onwidget/astrowind)

> 🧑‍🚀 **Seasoned astronaut?** Delete this file `README.md`. Update `src/config.yaml` and contents. Have fun!

\


### Commands

[](#commands)

All commands are run from the root of the project, from a terminal:

| Command             | Action                                             |
| :------------------ | :------------------------------------------------- |
| `npm install`       | Installs dependencies                              |
| `npm run dev`       | Starts local dev server at `localhost:4321`        |
| `npm run build`     | Build your production site to `./dist/`            |
| `npm run preview`   | Preview your build locally, before deploying       |
| `npm run check`     | Check your project for errors                      |
| `npm run fix`       | Run Eslint and format codes with Prettier          |
| `npm run astro ...` | Run CLI commands like `astro add`, `astro preview` |

\


### Configuration

[](#configuration)

Basic configuration file: `./src/config.yaml`

```
site:
  name: 'Example'
  site: 'https://example.com'
  base: '/' # Change this if you need to deploy to Github Pages, for example
  trailingSlash: false # Generate permalinks with or without "/" at the end

  googleSiteVerificationId: false # Or some value,

# Default SEO metadata
metadata:
  title:
    default: 'Example'
    template: '%s — Example'
  description: 'This is the default meta description of Example website'
  robots:
    index: true
    follow: true
  openGraph:
    site_name: 'Example'
    images:
      - url: '~/assets/images/default.png'
        width: 1200
        height: 628
    type: website
  twitter:
    handle: '@twitter_user'
    site: '@twitter_user'
    cardType: summary_large_image

i18n:
  language: en
  textDirection: ltr

apps:
  blog:
    isEnabled: true # If the blog will be enabled
    postsPerPage: 6 # Number of posts per page

    post:
      isEnabled: true
      permalink: '/blog/%slug%' # Variables: %slug%, %year%, %month%, %day%, %hour%, %minute%, %second%, %category%
      robots:
        index: true

    list:
      isEnabled: true
      pathname: 'blog' # Blog main path, you can change this to "articles" (/articles)
      robots:
        index: true

    category:
      isEnabled: true
      pathname: 'category' # Category main path /category/some-category, you can change this to "group" (/group/some-category)
      robots:
        index: true

    tag:
      isEnabled: true
      pathname: 'tag' # Tag main path /tag/some-tag, you can change this to "topics" (/topics/some-category)
      robots:
        index: false

    isRelatedPostsEnabled: true # If a widget with related posts is to be displayed below each post
    relatedPostsCount: 4 # Number of related posts to display

analytics:
  vendors:
    googleAnalytics:
      id: null # or "G-XXXXXXXXXX"

ui:
  theme: 'system' # Values: "system" | "light" | "dark" | "light:only" | "dark:only"
```

\


#### Customize Design

[](#customize-design)

To customize Font families, Colors or more Elements refer to the following files:

* `src/components/CustomStyles.astro`
* `src/assets/styles/tailwind.css`

### Deploy

[](#deploy)

#### Deploy to production (manual)

[](#deploy-to-production-manual)

You can create an optimized production build with:

```
npm run build
```

Now, your website is ready to be deployed. All generated files are located at `dist` folder, which you can deploy the folder to any hosting service you prefer.

#### Deploy to Netlify

[](#deploy-to-netlify)

Clone this repository on your own GitHub account and deploy it to Netlify:

[![Netlify Deploy button](https://camo.githubusercontent.com/8ef0cc1d083b2d67eb72500031401d9b52c3ecb9fb4c4405f46afd0d0aba02d6/68747470733a2f2f7777772e6e65746c6966792e636f6d2f696d672f6465706c6f792f627574746f6e2e737667)](https://app.netlify.com/start/deploy?repository=https://github.com/onwidget/astrowind)

#### Deploy to Vercel

[](#deploy-to-vercel)

Clone this repository on your own GitHub account and deploy to Vercel:

[![Deploy with Vercel](https://camo.githubusercontent.com/20bea215d35a4e28f2c92ea5b657d006b087687486858a40de2922a4636301ab/68747470733a2f2f76657263656c2e636f6d2f627574746f6e)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fonwidget%2Fastrowind)

\


## Frequently Asked Questions

[](#frequently-asked-questions)

* Why?
*
*

\


## Related projects

[](#related-projects)

* [TailNext](https://tailnext.vercel.app/) - Free template using Next.js 14 and Tailwind CSS with the new App Router.
* [Qwind](https://qwind.pages.dev/) - Free template to make your website using Qwik + Tailwind CSS.

## Contributing

[](#contributing)

If you have any ideas, suggestions or find any bugs, feel free to open a discussion, an issue or create a pull request. That would be very useful for all of us and we would be happy to listen and take action.

## Acknowledgements

[](#acknowledgements)

Initially created by [onWidget](https://onwidget.com) and maintained by a community of [contributors](https://github.com/onwidget/astrowind/graphs/contributors).

## License

[](#license)

**AstroWind** is licensed under the MIT license — see the [LICENSE](https://github.com/onwidget/astrowind/blob/main/LICENSE.md) file for details.


---
title: "AstroWind: 免费的Astro 5与Tailwind CSS模板"
slug: astrowind-free-template-astro-tailwind
description: |
  AstroWind是一个使用Astro 5.0和Tailwind CSS打造的免费开源模板，提供快速创建响应式和SEO友好网站的解决方案。包括暗黑模式、MDX支持、图像优化以及内置分析工具，是web开发者的理想选择。
tags: 
  - design
  - opensource
  - Astro
  - Tailwind
pubDatetime: 2025-03-29T07:26:29+08:00
ogImage: https://repository-images.githubusercontent.com/506862351/0e254e61-50e4-4ce2-888f-41ccad55d3d4
---

[原文链接](https://github.com/onwidget/astrowind)

---

# 🚀 AstroWind

[](#-astrowind)

[![AstroWind Lighthouse Score](https://raw.githubusercontent.com/onwidget/.github/main/resources/astrowind/lighthouse-score.png)](https://raw.githubusercontent.com/onwidget/.github/main/resources/astrowind/lighthouse-score.png)

🌟 *Most *starred* & *forked* Astro theme in 2022, 2023 & 2024*. 🌟

**AstroWind** is a free and open-source template to make your website using **[Astro 5.0](https://astro.build/) + [Tailwind CSS](https://tailwindcss.com/)**. Ready to start a new project and designed taking into account web best practices.

* ✅ **Production-ready** scores in **PageSpeed Insights** reports.
* ✅ Integration with **Tailwind CSS** supporting **Dark mode** and ***RTL***.
* ✅ **Fast and SEO friendly blog** with automatic **RSS feed**, **MDX** support, **Categories & Tags**, **Social Share**, ...
* ✅ **Image Optimization** (using new **Astro Assets** and **Unpic** for Universal image CDN).
* ✅ Generation of **project sitemap** based on your routes.
* ✅ **Open Graph tags** for social media sharing.
* ✅ **Analytics** built-in Google Analytics, and Splitbee integration.

\


[![AstroWind Theme Screenshot](https://raw.githubusercontent.com/onwidget/.github/main/resources/astrowind/screenshot-astrowind-1.0.png)](https://raw.githubusercontent.com/onwidget/.github/main/resources/astrowind/screenshot-astrowind-1.0.png)

[![onWidget](https://camo.githubusercontent.com/408b1438a6ac07fb1d015bf45f721345e632a7a5b6a4d59ae80e5adc63f1429a/68747470733a2f2f637573746f6d2d69636f6e2d6261646765732e64656d6f6c61622e636f6d2f62616467652f6d61646525323062792532302d6f6e5769646765742d3535366266323f7374796c653d666c61742d737175617265266c6f676f3d6f6e776964676574266c6f676f436f6c6f723d7768697465266c6162656c436f6c6f723d313031383237)](https://onwidget.com) [![License](https://camo.githubusercontent.com/9709c3cb8685ce12598789a5b7a29747e9d4bb949093fdd23cde3078f3846b7c/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6f6e7769646765742f617374726f77696e643f7374796c653d666c61742d73717561726526636f6c6f723d646464646464266c6162656c436f6c6f723d303030303030)](https://github.com/onwidget/astrowind/blob/main/LICENSE.md) [![Maintained](https://camo.githubusercontent.com/2d6a4cde3d9242cb9fca9ea180bf632bd8c13be8ba533a3b3337d769cdc84172/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d61696e7461696e65642533462d7965732d627269676874677265656e2e7376673f7374796c653d666c61742d737175617265)](https://github.com/onwidget) [![Contributions Welcome](https://camo.githubusercontent.com/0ddc5ef9663d99d289f17507ffc90ef73e33b7a01f91fb475197dc57c4e95508/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f6e747269627574696f6e732d77656c636f6d652d627269676874677265656e2e7376673f7374796c653d666c61742d737175617265)](https://github.com/onwidget/astrowind#contributing) [![Known Vulnerabilities](https://camo.githubusercontent.com/f9e7f166394ad76f1467dc9a4f18040ba4612d5d9bcde2a1e6e67c475b07e15c/68747470733a2f2f736e796b2e696f2f746573742f6769746875622f6f6e7769646765742f617374726f77696e642f62616467652e7376673f7374796c653d666c61742d737175617265)](https://snyk.io/test/github/onwidget/astrowind) [![Stars](https://camo.githubusercontent.com/db7b469a2bb56c27e24af49cedd3caa114f842da6c3fd0a6de021aca1f4f8ebb/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6f6e7769646765742f617374726f77696e642e7376673f7374796c653d736f6369616c266c6162656c3d7374617273266d61784167653d383634303026636f6c6f723d666636396234)](https://github.com/onwidget/astrowind) [![Forks](https://camo.githubusercontent.com/d43799830c1e623b321ac3fc81bfd2f7909cc68e8d11b45ac17471445b74fd06/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f6f6e7769646765742f617374726f77696e642e7376673f7374796c653d736f6369616c266c6162656c3d666f726b73266d61784167653d383634303026636f6c6f723d666636396234)](https://github.com/onwidget/astrowind)

\


Table of Contents

* [Demo](#demo)

* [Upcoming: AstroWind 2.0 – We Need Your Vision!](#-upcoming-astrowind-20--we-need-your-vision)

* [Getting started](#getting-started)

  * [Project structure](#project-structure)
  * [Commands](#commands)
  * [Configuration](#configuration)
  * [Deploy](#deploy)

* [Frequently Asked Questions](#frequently-asked-questions)

* [Related Projects](#related-projects)

* [Contributing](#contributing)

* [Acknowledgements](#acknowledgements)

* [License](#license)

\


## Demo

[](#demo)

📌 <https://astrowind.vercel.app/>

\


## 🔔 Upcoming: AstroWind 2.0 – We Need Your Vision!

[](#-upcoming-astrowind-20--we-need-your-vision)

We're embarking on an exciting journey with **AstroWind 2.0**, and we want you to be a part of it! We're currently taking the first steps in developing this new version and your insights are invaluable. Join the discussion and share your feedback, ideas, and suggestions to help shape the future of **AstroWind**. Let's make **AstroWind 2.0** even better, together!

[Share Your Feedback in Our Discussion!](https://github.com/onwidget/astrowind/discussions/392)

\


## Getting started

[](#getting-started)

**AstroWind** tries to give you quick access to creating a website using [Astro 5.0](https://astro.build/) + [Tailwind CSS](https://tailwindcss.com/). It's a free theme which focuses on simplicity, good practices and high performance.

Very little vanilla javascript is used only to provide basic functionality so that each developer decides which framework (React, Vue, Svelte, Solid JS...) to use and how to approach their goals.

In this version the template supports all the options in the `output` configuration, `static`, `hybrid` and `server`, but the blog only works with `prerender = true`. We are working on the next version and aim to make it fully compatible with SSR.

### Project structure

[](#project-structure)

Inside **AstroWind** template, you'll see the following folders and files:

```
/
├── public/
│   ├── _headers
│   └── robots.txt
├── src/
│   ├── assets/
│   │   ├── favicons/
│   │   ├── images/
│   │   └── styles/
│   │       └── tailwind.css
│   ├── components/
│   │   ├── blog/
│   │   ├── common/
│   │   ├── ui/
│   │   ├── widgets/
│   │   │   ├── Header.astro
│   │   │   └── ...
│   │   ├── CustomStyles.astro
│   │   ├── Favicons.astro
│   │   └── Logo.astro
│   ├── content/
│   │   ├── post/
│   │   │   ├── post-slug-1.md
│   │   │   ├── post-slug-2.mdx
│   │   │   └── ...
│   │   └-- config.ts
│   ├── layouts/
│   │   ├── Layout.astro
│   │   ├── MarkdownLayout.astro
│   │   └── PageLayout.astro
│   ├── pages/
│   │   ├── [...blog]/
│   │   │   ├── [category]/
│   │   │   ├── [tag]/
│   │   │   ├── [...page].astro
│   │   │   └── index.astro
│   │   ├── index.astro
│   │   ├── 404.astro
│   │   ├-- rss.xml.ts
│   │   └── ...
│   ├── utils/
│   ├── config.yaml
│   └── navigation.js
├── package.json
├── astro.config.ts
└── ...
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.

Any static assets, like images, can be placed in the `public/` directory if they do not require any transformation or in the `assets/` directory if they are imported directly.

[![Edit AstroWind on CodeSandbox](https://camo.githubusercontent.com/ecd139ba9847d0c77607c86339eb8ee6939ca85143a92ae16ebf20f58325e1b6/68747470733a2f2f636f646573616e64626f782e696f2f7374617469632f696d672f706c61792d636f646573616e64626f782e737667)](https://githubbox.com/onwidget/astrowind/tree/main) [![Open in Gitpod](https://camo.githubusercontent.com/c382d7567ed2a922b5195a3c2a7db8f4329cc4c990bdf319e286592048db9569/68747470733a2f2f73766773686172652e636f6d2f692f7864692e737667)](https://gitpod.io/?on=gitpod#https://github.com/onwidget/astrowind) [![Open in StackBlitz](https://camo.githubusercontent.com/e9392ad1a0cb081a5be23067cfb953616abc12f4e260f581a302e020c41d41c0/68747470733a2f2f646576656c6f7065722e737461636b626c69747a2e636f6d2f696d672f6f70656e5f696e5f737461636b626c69747a2e737667)](https://stackblitz.com/github/onwidget/astrowind)

> 🧑‍🚀 **Seasoned astronaut?** Delete this file `README.md`. Update `src/config.yaml` and contents. Have fun!

\


### Commands

[](#commands)

All commands are run from the root of the project, from a terminal:

| Command             | Action                                             |
| :------------------ | :------------------------------------------------- |
| `npm install`       | Installs dependencies                              |
| `npm run dev`       | Starts local dev server at `localhost:4321`        |
| `npm run build`     | Build your production site to `./dist/`            |
| `npm run preview`   | Preview your build locally, before deploying       |
| `npm run check`     | Check your project for errors                      |
| `npm run fix`       | Run Eslint and format codes with Prettier          |
| `npm run astro ...` | Run CLI commands like `astro add`, `astro preview` |

\


### Configuration

[](#configuration)

Basic configuration file: `./src/config.yaml`

```
site:
  name: 'Example'
  site: 'https://example.com'
  base: '/' # Change this if you need to deploy to Github Pages, for example
  trailingSlash: false # Generate permalinks with or without "/" at the end

  googleSiteVerificationId: false # Or some value,

# Default SEO metadata
metadata:
  title:
    default: 'Example'
    template: '%s — Example'
  description: 'This is the default meta description of Example website'
  robots:
    index: true
    follow: true
  openGraph:
    site_name: 'Example'
    images:
      - url: '~/assets/images/default.png'
        width: 1200
        height: 628
    type: website
  twitter:
    handle: '@twitter_user'
    site: '@twitter_user'
    cardType: summary_large_image

i18n:
  language: en
  textDirection: ltr

apps:
  blog:
    isEnabled: true # If the blog will be enabled
    postsPerPage: 6 # Number of posts per page

    post:
      isEnabled: true
      permalink: '/blog/%slug%' # Variables: %slug%, %year%, %month%, %day%, %hour%, %minute%, %second%, %category%
      robots:
        index: true

    list:
      isEnabled: true
      pathname: 'blog' # Blog main path, you can change this to "articles" (/articles)
      robots:
        index: true

    category:
      isEnabled: true
      pathname: 'category' # Category main path /category/some-category, you can change this to "group" (/group/some-category)
      robots:
        index: true

    tag:
      isEnabled: true
      pathname: 'tag' # Tag main path /tag/some-tag, you can change this to "topics" (/topics/some-category)
      robots:
        index: false

    isRelatedPostsEnabled: true # If a widget with related posts is to be displayed below each post
    relatedPostsCount: 4 # Number of related posts to display

analytics:
  vendors:
    googleAnalytics:
      id: null # or "G-XXXXXXXXXX"

ui:
  theme: 'system' # Values: "system" | "light" | "dark" | "light:only" | "dark:only"
```

\


#### Customize Design

[](#customize-design)

To customize Font families, Colors or more Elements refer to the following files:

* `src/components/CustomStyles.astro`
* `src/assets/styles/tailwind.css`

### Deploy

[](#deploy)

#### Deploy to production (manual)

[](#deploy-to-production-manual)

You can create an optimized production build with:

```
npm run build
```

Now, your website is ready to be deployed. All generated files are located at `dist` folder, which you can deploy the folder to any hosting service you prefer.

#### Deploy to Netlify

[](#deploy-to-netlify)

Clone this repository on your own GitHub account and deploy it to Netlify:

[![Netlify Deploy button](https://camo.githubusercontent.com/8ef0cc1d083b2d67eb72500031401d9b52c3ecb9fb4c4405f46afd0d0aba02d6/68747470733a2f2f7777772e6e65746c6966792e636f6d2f696d672f6465706c6f792f627574746f6e2e737667)](https://app.netlify.com/start/deploy?repository=https://github.com/onwidget/astrowind)

#### Deploy to Vercel

[](#deploy-to-vercel)

Clone this repository on your own GitHub account and deploy to Vercel:

[![Deploy with Vercel](https://camo.githubusercontent.com/20bea215d35a4e28f2c92ea5b657d006b087687486858a40de2922a4636301ab/68747470733a2f2f76657263656c2e636f6d2f627574746f6e)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fonwidget%2Fastrowind)

\


## Frequently Asked Questions

[](#frequently-asked-questions)

* Why?
*
*

\


## Related projects

[](#related-projects)

* [TailNext](https://tailnext.vercel.app/) - Free template using Next.js 14 and Tailwind CSS with the new App Router.
* [Qwind](https://qwind.pages.dev/) - Free template to make your website using Qwik + Tailwind CSS.

## Contributing

[](#contributing)

If you have any ideas, suggestions or find any bugs, feel free to open a discussion, an issue or create a pull request. That would be very useful for all of us and we would be happy to listen and take action.

## Acknowledgements

[](#acknowledgements)

Initially created by [onWidget](https://onwidget.com) and maintained by a community of [contributors](https://github.com/onwidget/astrowind/graphs/contributors).

## License

[](#license)

**AstroWind** is licensed under the MIT license — see the [LICENSE](https://github.com/onwidget/astrowind/blob/main/LICENSE.md) file for details.


