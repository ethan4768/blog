---
title: Readest：一款功能丰富的开源电子书阅读器
slug: readest-open-source-ebook-reader
description: Readest 是一款现代化的开源电子书阅读器，适合热爱阅读的用户。它提供强大的工具、直观的界面及无缝的跨平台访问，支持多种电子书格式并具备注释、文本翻译及可自定义布局等高级功能。
tags: 
  - opensource
  - tool
  - reading
  - ai
pubDatetime: 2024-12-13T21:52:21+08:00
ogImage: https://opengraph.githubassets.com/d1b1c253e3238665960a0d7c6b20b9c0960b828305ba0c9984262b949280bb61/chrox/readest
---

[原文链接](https://github.com/chrox/readest)

---

[![Readest Logo](https://github.com/chrox/readest/raw/main/apps/readest-app/src-tauri/icons/icon.png?raw=true)](https://readest.com?utm_source=github\&utm_medium=referral\&utm_campaign=readme)

# Readest

[](#readest)

\


[Readest](https://readest.com?utm_source=github\&utm_medium=referral\&utm_campaign=readme) is an open-source ebook reader designed for immersive and deep reading experiences. Built as a modern rewrite of [Foliate](https://github.com/johnfactotum/foliate), it leverages [Next.js 15](https://github.com/vercel/next.js) and [Tauri v2](https://github.com/tauri-apps/tauri) to offer a seamless cross-platform experience on macOS, Windows, Linux and Web, with support for mobile platforms coming soon.

[![Website](https://camo.githubusercontent.com/1ede12665b796ec732674edf238594f1352b99d7e6765df24844d55e26e48f4d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f776562736974652d726561646573742e636f6d2d6f72616e6765)](https://readest.com?utm_source=github\&utm_medium=referral\&utm_campaign=readme) [![Web App](https://camo.githubusercontent.com/2f44940b49937296e8f202e8f1dd85671c9680025ebe7956500752728f9ae267/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f726561642532306f6e6c696e652d7765622e726561646573742e636f6d2d6f72616e6765)](https://web.readest.com) [![OS](https://camo.githubusercontent.com/cc69384e152826a7835ab939a68f8ed1b86a818aea7912a7b652770d2cd86597/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f532d6d61634f5325324325323057696e646f77732532432532304c696e75782532432532305765622d677265656e)](https://readest.com?utm_source=github\&utm_medium=referral\&utm_campaign=readme) [![](https://camo.githubusercontent.com/a6ac245ab351ef26872fbb08996fc385b62130723842e7d347ff93ac1619cb06/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f313331343232363132303838363937363534343f636f6c6f723d353836354632266c6162656c3d646973636f7264266c6162656c436f6c6f723d626c61636b266c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465267374796c653d666c61742d737175617265)](https://discord.gg/gntyVNk3BJ)\
[![AGPL Licence](https://camo.githubusercontent.com/4d7ee0b56d068b8e028ccab058c090a8230b7f2978efb498f72f693de130c3f6/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6368726f782f726561646573743f636f6c6f723d7465616c)](https://github.com/chrox/readest/blob/main/LICENSE) [![Latest release](https://camo.githubusercontent.com/8bbf1c7321bbec98ac94611c8333abcea08de8402bda703d86c356835b828175/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f72656c656173652f6368726f782f726561646573743f636f6c6f723d677265656e)](https://github.com/chrox/readest/releases) [![Last commit](https://camo.githubusercontent.com/a5638ac0207331348ce553e0b21ed37c804bb741c5e52768bc7c9b3da395a044/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6173742d636f6d6d69742f6368726f782f726561646573743f636f6c6f723d677265656e)](https://github.com/chrox/readest/commits/main) [![Commits](https://camo.githubusercontent.com/cf19825d4d8290b36831b39d22a767b8b6c53b70198810f7e843cf3c35a39007/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6d6d69742d61637469766974792f6d2f6368726f782f72656164657374)](https://github.com/chrox/readest/pulse)

[Features](#features) • [Planned Features](#planned-features) • [Screenshots](#screenshots) • [Downloads](#downloads) • [Getting Started](#getting-started) • [Contributors](#contributors) • [License](#license)

[![Readest Banner](/chrox/readest/raw/main/data/screenshots/landing_preview.png)](https://readest.com)

## Features

[](#features)

✅ Implemented

| **Feature**                                             | **Description**                                                                  | **Status** |
| ------------------------------------------------------- | -------------------------------------------------------------------------------- | ---------- |
| **Multi-Format Support**                                | Support EPUB, MOBI, KF8 (AZW3), FB2, CBZ, PDF (experimental)                     | ✅          |
| **Scroll/Page View Modes**                              | Switch between scrolling or paginated reading modes.                             | ✅          |
| **Full-Text Search**                                    | Search across the entire book to find relevant sections.                         | ✅          |
| **Annotations and Highlighting**                        | Add highlights, bookmarks, and notes to enhance your reading experience.         | ✅          |
| **Excerpt Text for Note-Taking**                        | Easily excerpt text from books for detailed notes and analysis.                  | ✅          |
| **Dictionary/Wikipedia Lookup**                         | Instantly look up words and terms when reading.                                  | ✅          |
| **Translate with DeepL**                                | Translate selected text instantly using DeepL for accurate translations.         | ✅          |
| **[Parallel Read](https://readest.com/#parallel-read)** | Read two books or documents simultaneously in a split-screen view.               | ✅          |
| **Customize Font and Layout**                           | Adjust font, layout, theme mode, and theme colors for a personalized experience. | ✅          |
| **File Association and Open With**                      | Quickly open files in Readest in your file browser with one-click.               | ✅          |

## Planned Features

[](#planned-features)

🛠 Building

🔄 Planned

| **Feature**                      | **Description**                                                                                                   | **Priority** |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------ |
| **Support iOS and Android**      | Expand the APP to work on iOS and Android devices.                                                                | 🛠           |
| **Sync Across Platforms**        | Synchronize reading progress, notes, and bookmarks across all supported platforms.                                | 🛠           |
| **Sync with Koreader**           | Synchronize reading progress, notes, and bookmarks with [Koreader](https://github.com/koreader/koreader) devices. | 🔄           |
| **Keyboard Navigation**          | Implement vimium-style keybindings for book navigation.                                                           | 🔄           |
| **Library Management**           | Organize, sort, and manage your entire ebook library.                                                             | 🔄           |
| **Support OPDS/Calibre**         | Integrate OPDS/Calibre to access online libraries and catalogs.                                                   | 🔄           |
| **Text-to-Speech (TTS) Support** | Enable text-to-speech functionality for a more accessible reading experience.                                     | 🔄           |
| **Audiobook Support**            | Extend functionality to play and manage audiobooks.                                                               | 🔄           |
| **Handwriting Annotations**      | Add support for handwriting annotations using a pen on compatible devices.                                        | 🔄           |
| **Advanced Reading Stats**       | Track reading time, pages read, and more for detailed insights.                                                   | 🔄           |
| **In-Library Full-Text Search**  | Search across your entire ebook library to find topics and quotes.                                                | 🔄           |
| **AI-Powered Summarization**     | Generate summaries of books or chapters using AI for quick insights.                                              | 🔄           |

Stay tuned for continuous improvements and updates! Contributions and suggestions are always welcome—let's build the ultimate reading experience together. 😊

## Screenshots

[](#screenshots)

[![Annotations](/chrox/readest/raw/main/data/screenshots/annotations.png)](https://github.com/chrox/readest/blob/main/data/screenshots/annotations.png)

[![DeepL](/chrox/readest/raw/main/data/screenshots/deepl.png)](https://github.com/chrox/readest/blob/main/data/screenshots/deepl.png)

[![Footnote](/chrox/readest/raw/main/data/screenshots/footnote_popover.png)](https://github.com/chrox/readest/blob/main/data/screenshots/footnote_popover.png)

[![Wikipedia](/chrox/readest/raw/main/data/screenshots/wikipedia_vertical.png)](https://github.com/chrox/readest/blob/main/data/screenshots/wikipedia_vertical.png)

[![Dark Mode](/chrox/readest/raw/main/data/screenshots/dark_mode.png)](https://github.com/chrox/readest/blob/main/data/screenshots/dark_mode.png)

***

## Downloads

[](#downloads)

The Readest app is available for download! 🥳 🚀

* macOS : Search for "Readest" on the [macOS App Store](https://apps.apple.com/app/apple-store/id6738622779?pt=127463130\&ct=github\&mt=8).
* Windows / Linux: Visit [https://readest.com](https://readest.com?utm_source=github\&utm_medium=referral\&utm_campaign=readme) or the [Releases on GitHub](https://github.com/chrox/readest/releases).
* Web: Visit <https://web.readest.com>.
* iOS / Android: coming soon 👀

## Requirements

[](#requirements)

* **Node.js** and **pnpm** for Next.js development
* **Rust** and **Cargo** for Tauri development

For the best experience to build Readest for yourself, use a recent version of Node.js and Rust. Refer to the [Tauri documentation](https://v2.tauri.app/start/prerequisites/) for details on setting up the development environment prerequisites on different platforms.

```
nvm install v22
nvm use v22
npm install -g pnpm
rustup update
```

## Getting Started

[](#getting-started)

To get started with Readest, follow these steps to clone and build the project.

### 1. Clone the Repository

[](#1-clone-the-repository)

```
git clone https://github.com/chrox/readest.git
cd readest
git submodule update --init --recursive
```

### 2. Install Dependencies

[](#2-install-dependencies)

```
# might need to rerun this when code is updated
pnpm install
# copy pdfjs-dist to Next.js public directory
pnpm --filter @readest/readest-app setup-pdfjs
```

### 3. Verify Dependencies Installation

[](#3-verify-dependencies-installation)

To confirm that all dependencies are correctly installed, run the following command:

```
pnpm tauri info
```

This command will display information about the installed Tauri dependencies and configuration on your platform. Note that the output may vary depending on the operating system and environment setup. Please review the output specific to your platform for any potential issues.

For Windows targets, “Build Tools for Visual Studio 2022” (or a higher edition of Visual Studio) and the “Desktop development with C++” workflow must be installed. For Windows ARM64 targets, the “VS 2022 C++ ARM64 build tools” and "C++ Clang Compiler for Windows" components must be installed. And make sure `clang` can be found in the path by adding `C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\Llvm\x64\bin` for example in the environment variable `Path`.

### 4. Build for Development

[](#4-build-for-development)

```
pnpm tauri dev
```

### 5. Build for Production

[](#5-build-for-production)

```
pnpm tauri build
```

## Contributors

[](#contributors)

Readest is open-source, and contributions are welcome! Feel free to open issues, suggest features, or submit pull requests. Please **review our [contributing guidelines](https://github.com/chrox/readest/blob/main/CONTRIBUTING.md) before you start**. We also welcome you to join our [Discord](https://discord.gg/gntyVNk3BJ) community for either support or contributing guidance.

[![A table of avatars from the project's contributors](https://camo.githubusercontent.com/166192853d2f49dd106b68fd9f3fe5d30bd899d477cf23242d5159267e350297/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d6368726f782f72656164657374)](https://github.com/chrox/readest/graphs/contributors)

## License

[](#license)

Readest is free software: you can redistribute it and/or modify it under the terms of the [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.html) as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. See the [LICENSE](https://github.com/chrox/readest/blob/main/LICENSE) file for details.

The following JavaScript libraries are bundled in this software:

* [foliate-js](https://github.com/johnfactotum/foliate-js), which is MIT licensed.
* [zip.js](https://github.com/gildas-lormeau/zip.js), which is licensed under the BSD-3-Clause license.
* [fflate](https://github.com/101arrowz/fflate), which is MIT licensed.
* [PDF.js](https://github.com/mozilla/pdf.js), which is licensed under Apache License 2.0.

***

Happy reading with Readest!


