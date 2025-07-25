---
title: "Quarkdown: 一款具有超能力的Markdown工具，用于创作演示文稿、文章和书籍"
slug: quarkdown-markdown-superpowers
description: |
  Quarkdown是一种现代的Markdown排版系统，旨在实现多功能性，可以无缝地将项目编译成可打印的书籍或交互式演示文稿。通过强大的Turing完备扩展，Quarkdown将您的想法自动转换为纸质文档，提供丰富的功能和实时预览，满足创作需求。
tags: 
  - AI
  - tool
  - writing
  - opensource
pubDatetime: 2025-05-22T10:28:44+08:00
ogImage: https://repository-images.githubusercontent.com/750550657/039ae946-fcb4-49f9-9190-1859ac4aafc2
---

[原文链接](https://github.com/iamgio/quarkdown)

---

![Quarkdown banner](https://github.com/user-attachments/assets/68dfb3bf-9466-44f3-b220-7067322c4887)\
[![Wiki](https://camo.githubusercontent.com/470ce16ecf86058c422345998d9b2d65f4de03584914396066d84bc5047485cd/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f77696b692d726561642d6461726b6379616e)](https://github.com/iamgio/quarkdown/wiki)[![Docs](https://camo.githubusercontent.com/7fec441e57782735d92d43331abace82579194eae17c6e28bf8a31e3ec6b58ed/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f63732d726561642d626c7565)](https://quarkdown.com/docs)[![Release](https://camo.githubusercontent.com/64e01d18f92821dd6e068b07dbd724b665efdaabff088dcc1363bf94dc4eb986/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f69616d67696f2f717561726b646f776e3f636f6c6f723d6d656469756d736561677265656e)](https://github.com/iamgio/quarkdown/releases/latest)[![FMT: Ktlint](https://camo.githubusercontent.com/2980cb9544c2566c9c3d03a30c47d27e4a4be2a7ba3e2dbfebc33edfb2bf6c60/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f666d742d6b746c696e742d3766353266663f6c6f676f3d6b6f746c696e266c6f676f436f6c6f723d663566356635)](https://pinterest.github.io/ktlint)[![CodeFactor](https://camo.githubusercontent.com/09de5f11e22d217441b1784e5c3108ff65db268fee1afb144cf714a67c4774fd/68747470733a2f2f7777772e636f6465666163746f722e696f2f7265706f7369746f72792f6769746875622f69616d67696f2f717561726b646f776e2f62616467652f6d61696e)](https://www.codefactor.io/repository/github/iamgio/quarkdown)\
\
**Download**\
**[Stable](https://github.com/iamgio/quarkdown/releases/latest)**    |   \
[Latest](https://github.com/iamgio/quarkdown/releases/tag/latest)

***

# Table of contents

[](#table-of-contents)

1. [About](#about)

2. [Demo](#as-simple-as-you-expect)

3. [Targets](#targets)

4. [Comparison](#comparison)

5. [Installation](#installation)

6. [Getting started](#getting-started)

   * [Creating a project](#creating-a-project)
   * [Compiling](#compiling)

7. [Mock document](#mock-document)

8. [Contributing](#contributing)

9. [Sponsors](#sponsors)

10. [Concept](#concept)

 

# About

[](#about)

Quarkdown is a modern Markdown-based typetting system, designed around the key concept of **versatility**, by seamlessly compiling a project into a print-ready book or an interactive presentation. All through an incredibly powerful Turing-complete extension of Markdown, ensuring your ideas flow automatically into paper.

 

[![Paper demo](https://raw.githubusercontent.com/iamgio/quarkdown/project-files/images/paged-demo.png)](https://raw.githubusercontent.com/iamgio/quarkdown/project-files/images/paged-demo.png)

*Original credits: [Attention Is All You Need](https://arxiv.org/abs/1706.03762v7)*

\


Born as an extension of CommonMark and GFM, the Quarkdown Flavor brings **functions** to Markdown, along with many other syntax extensions.

\


> This is a function call:
>
> ```
> .somefunction {arg1} {arg2}
>     Body argument
> ```

\


**Possibilities are unlimited** thanks to an ever-expanding [standard library](https://github.com/iamgio/quarkdown/blob/main/quarkdown-stdlib/src/main/kotlin/com/quarkdown/stdlib), which offers layout builders, I/O, math, conditional statements and loops.

**Not enough?** You can still define your own functions and variables — all within Markdown. You can even create awesome libraries for everyone to use.

\


> ```
> .function {greet}
>     to from:
>     **Hello, .to** from .from!
>
> .greet {world} from:{iamgio}
> ```
>
> Result: **Hello, world** from iamgio!

\


This out-of-the-box scripting support opens doors to complex and dynamic content that would be otherwise impossible to achieve with vanilla Markdown.

Combined with live preview and ⚡ fast compilation speed, Quarkdown simply gets the work done.

 

[![Live preview](https://raw.githubusercontent.com/iamgio/quarkdown/project-files/video/livepreview.gif)](https://raw.githubusercontent.com/iamgio/quarkdown/project-files/video/livepreview.gif)[![Live preview](https://raw.githubusercontent.com/iamgio/quarkdown/project-files/video/livepreview.gif) ](https://raw.githubusercontent.com/iamgio/quarkdown/project-files/video/livepreview.gif)     [](https://raw.githubusercontent.com/iamgio/quarkdown/project-files/video/livepreview.gif)

 

Check the [wiki](https://github.com/iamgio/quarkdown/wiki) to learn more about the language and its features.

 

***

## Check out the demo presentation [here](https://iamgio.eu/quarkdown/demo)

[](#check-out-the-demo-presentation-here)

Built with Quarkdown itself — [**source code**](https://github.com/iamgio/quarkdown/blob/main/demo/demo.qmd)\
\
*(Desktop view is suggested)*

***

 

## As simple as you expect...

[](#as-simple-as-you-expect)

[![Paper code demo](https://raw.githubusercontent.com/iamgio/quarkdown/project-files/images/code-paper.png)](https://raw.githubusercontent.com/iamgio/quarkdown/project-files/images/code-paper.png)

*Inspired by: [X-ray flashes from a nearby supermassive black hole accelerate mysteriously](https://news.mit.edu/2025/x-ray-flashes-nearby-supermassive-black-hole-accelerate-mysteriously-0113)*

 

## ...as complex as you need.

[](#as-complex-as-you-need)

[![Chart code demo](https://raw.githubusercontent.com/iamgio/quarkdown/project-files/images/code-chart.png)](https://raw.githubusercontent.com/iamgio/quarkdown/project-files/images/code-chart.png)

# Targets

[](#targets)

* **HTML**

  * ✅ Plain output (default)
  * ✅ Slides via [reveal.js](https://revealjs.com)
  * ✅ Paged (books, articles) via [paged.js](https://pagedjs.org)\
    *Paged documents require a webserver to render in the browser. See the [`-p`](#options) option below.*

* **PDF**

  * ✅ All document types and features supported by HTML are also supported when exporting to PDF.
  * Check the wiki's [PDF export](https://github.com/iamgio/quarkdown/wiki/pdf-export) page to learn more.

The desired document type can be set by calling the [`.doctype` function](https://github.com/iamgio/quarkdown/wiki/document-metadata) within the source itself:

* `.doctype {slides}`
* `.doctype {paged}`

# Comparison

[](#comparison)

|                       | Quarkdown | Markdown |      LaTeX      |     AsciiDoc    |     MDX     |
| --------------------- | :-------: | :------: | :-------------: | :-------------: | :---------: |
| Concise and readable  |     ✅     |     ✅    |        ❌        |        ✅        |      ✅      |
| Full document control |     ✅     |     ❌    |        ✅        |        ❌        |      ❌      |
| Scripting             |     ✅     |     ❌    |     Partial     |        ❌        |      ✅      |
| Book/article export   |     ✅     |     ❌    |        ✅        |        ✅        | Third-party |
| Presentation export   |     ✅     |     ❌    |        ✅        |        ✅        | Third-party |
| Targets               | HTML, PDF |   HTML   | PDF, PostScript | HTML, PDF, ePub |     HTML    |

| LaTeX                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Quarkdown                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ```
\tableofcontents

\section{Section}

\subsection{Subsection}

\begin{enumerate}
    \item \textbf{First} item
    \item \textbf{Second} item
\end{itemize}

\begin{center}
    This text is \textit{centered}.
\end{center}

\begin{figure}[!h]
    \centering
    \begin{subfigure}[b]
        \includegraphics[width=0.3\linewidth]
    \end{subfigure}
    \begin{subfigure}[b]
        \includegraphics[width=0.3\linewidth]
    \end{subfigure}
    \begin{subfigure}[b]
        \includegraphics[width=0.3\linewidth]
    \end{subfigure}
\end{figure}
``` | ```
.tableofcontents

# Section

## Subsection

1. **First** item
2. **Second** item

.center
    This text is _centered_.

.row alignment:{spacebetween}

``` |

 

# Getting started

[](#getting-started)

## Installation

[](#installation)

Download `quarkdown.zip` from the [releases](https://github.com/iamgio/quarkdown/releases) page or build it with `gradlew distZip`, and unzip it.

* The `bin` directory contains the executable scripts. Optionally, adding it to your `PATH` allows you to access Quarkdown more easily.
* The `lib/qmd` directory contains `.qmd` libraries that can be imported into a project.

Java 17 or higher is required.

## Creating a project

[](#creating-a-project)

Running **`quarkdown create [directory]`** will launch the prompt-based project wizard, making it quicker than ever to set up a new Quarkdown project, with all [metadata](https://github.com/iamgio/quarkdown/wiki/document-metadata) and initial content already present.

For more information about the project creator, check out its [wiki page](https://github.com/iamgio/quarkdown/wiki/cli%3A-project-creator).

Alternatively, you may manually create a `.qmd` source file and start from there.

## Compiling

[](#compiling)

Running **`quarkdown c file.qmd`** will compile the given file and save the output to file.

> If the project is composed by multiple source files, the target file must be the root one, i.e. the one that includes the other files.
>
> * [How to include other files?](https://github.com/iamgio/quarkdown/wiki/including-other-quarkdown-files)

If you would like to familiarize yourself with Quarkdown instead, `quarkdown repl` lets you play with an interactive REPL mode.

#### Options

[](#options)

* **`-p`** or **`--preview`**: enables automatic content reloading after compiling.\
  If a [webserver](https://github.com/iamgio/quarkdown/wiki/cli%3A-webserver) is not running yet, it is started and the document is opened in the default browser.\
  This is required in order to render paged documents in the browser.

* **`-w`** or **`--watch`**: recompiles the source everytime a file from the source directory is changed.

Tip

Combine `-p -w` to achieve ***live preview***!

* **`--pdf`**: produces a PDF file. Learn more in the wiki's [*PDF export*](https://github.com/iamgio/quarkdown/wiki/pdf-export) page.

* `-o <dir>` or `--output <dir>`: sets the directory of the output files. Defaults to `./output`.

* `-l <dir>` or `--libs <dir>`: sets the directory where external libraries can be loaded from. Defaults to `<install dir>/lib/qmd`. [(?)](https://github.com/iamgio/quarkdown/wiki/importing-external-libraries)

* `-r <renderer>` or `--render <renderer>`: sets the target renderer. Defaults to `html`. Accepted values:

  * `html`
  * `html-pdf` (equivalent to `-r html --pdf`)

* `--server-port <port>`: optional customization of the local webserver's port. Defaults to `8089`.

* `--pretty`: produces pretty output code. This is useful for debugging or to read the output code more easily, but it should be disabled in production as the results might be visually affected.

* `--clean`: deletes the content of the output directory before producing new files. Destructive operation.

* `--strict`: forces the program to exit if an error occurs. When not in strict mode, errors are shown as boxes in the document.

* `--no-media-storage`: turns the media storage system off. [(?)](https://github.com/iamgio/quarkdown/wiki/media-storage)

* `-Dloglevel=<level>` (JVM property): sets the log level. If set to `warning` or higher, the output content is not printed out.

 

***

 

## Mock document

[](#mock-document)

 

[![Mock document demo](https://raw.githubusercontent.com/iamgio/quarkdown/project-files/images/mock-demo.png)](https://raw.githubusercontent.com/iamgio/quarkdown/project-files/images/mock-demo.png)

***Mock***, written in Quarkdown, is a comprehensive collection of visual elements offered by the language, making it ideal for exploring and understanding its key features — all while playing and experimenting hands-on with a concrete outcome in the form of pages or slides.

* The document's source files are available in the [`mock`](https://github.com/iamgio/quarkdown/blob/main/mock) directory, and can be compiled via `quarkdown c mock/main.qmd -p`.
* The PDF artifacts generated for all possible theme combinations are available and can be viewed in the [`generated`](https://github.com/iamgio/quarkdown/tree/generated/pdf/mock) branch.

## Contributing

[](#contributing)

Contributions are welcome! Please check [CONTRIBUTING.md](https://github.com/iamgio/quarkdown/blob/main/CONTRIBUTING.md) to know how contribute via issues or pull requests.

## Sponsors

[](#sponsors)

A special thanks to all the sponsors who [supported this project](https://github.com/sponsors/iamgio)!

[![LunaBluee](https://avatars.githubusercontent.com/u/145209701?v=4)](https://github.com/https://github.com/LunaBluee)

## Concept

[](#concept)

The logo resembles the original [Markdown icon](https://github.com/dcurtis/markdown-mark), with focus on Quarkdown's completeness, richness of features and customization options, emphasized by the revolving arrow all around the sphere.

![Quarkdown icon](https://raw.githubusercontent.com/iamgio/quarkdown/project-files/images/ticon-dark.svg)

What could be mistaken for a planet is actually a **quark** or, more specifically, a **down quark**, an elementary particle that is a major constituent of matter: they give life to every complex structure we know of, while also being one of the lightest objects in existence.

This is, indeed, the concept **Quarkdown** is built upon.


