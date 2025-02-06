---
title: "HiPixel: 一款基于 AI 的 macOS 原生图像超分辨率应用程序"
slug: hipixel-ai-image-super-resolution
description: |
  HiPixel 是一款原生 macOS 应用程序，利用 Upscayl 的强大 AI 模型实现图像超分辨率处理。它采用 SwiftUI 构建，具备现代化的用户界面以及快速的处理性能，支持多种图像格式，旨在提升您的图像处理效率。
tags: 
  - AI
  - macos
  - tool
  - image
  - performance
pubDatetime: 2025-02-06T10:27:16+08:00
ogImage: https://opengraph.githubassets.com/2ede5f3f56ed0443bed5dfa372b273b1d37ce893752911330bee9c76034e00c8/okooo5km/HiPixel
---

[原文链接](https://github.com/okooo5km/HiPixel?tab=readme-ov-file#%E4%B8%AD%E6%96%87)

---

# HiPixel

[](#hipixel)

[![HiPixel Logo](/okooo5km/HiPixel/raw/main/HiPixel/Assets.xcassets/AppIcon.appiconset/icon_256x256.png)](https://github.com/okooo5km/HiPixel/blob/main/HiPixel/Assets.xcassets/AppIcon.appiconset/icon_256x256.png)

# HiPixel

[](#hipixel-1)

[![License: AGPL v3](https://camo.githubusercontent.com/2817475dd3f38d12681f79bb4a2dd943b31e4339512a019b8f7d720e04ec38c7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4147504c25323076332d626c75652e737667) ](https://github.com/yourusername/hipixel/blob/main/LICENSE)[![Swift 5.9](https://camo.githubusercontent.com/9cda32d1eda591fb105f12f932f2e497cfa6ecae6c25d277b677b4a8e84c98f5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53776966742d352e392d6f72616e67652e737667) ](https://developer.apple.com/swift)[![Platform: macOS](https://camo.githubusercontent.com/19f38939c074797b5b7d987327b7761b4e9f455645d442259bdd84058e6837cb/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506c6174666f726d2d6d61634f532d6c69676874677265792e737667)](https://developer.apple.com/macos)

[English](#english) | [中文](#中文)

***

## AI-Powered Image Super-Resolution for macOS

[](#ai-powered-image-super-resolution-for-macos)

HiPixel is a native macOS application for AI-powered image super-resolution, built with SwiftUI and leveraging Upscayl's powerful AI models.

[![HiPixel Screenshot](/okooo5km/HiPixel/raw/main/screenshot.jpeg)](https://github.com/okooo5km/HiPixel/blob/main/screenshot.jpeg)

### ✨ Features

[](#-features)

* 🖥️ Native macOS application with SwiftUI interface
* 🎨 High-quality image upscaling using AI models
* 🚀 Fast processing with GPU acceleration
* 🖼️ Supports various image formats
* 💻 Modern, intuitive user interface

### 💡 Why HiPixel?

[](#-why-hipixel)

While [Upscayl](https://github.com/upscayl/upscayl) already offers an excellent macOS application, HiPixel was developed with specific goals in mind:

1. **Native macOS Experience**

   * Built as a native SwiftUI application while utilizing Upscayl's powerful binary tools and AI models
   * Provides a seamless, platform-native experience that feels right at home on macOS

2. **Enhanced Workflow Efficiency**

   * Streamlined interaction with drag-and-drop processing - images are processed automatically upon dropping
   * Batch processing support for handling multiple images simultaneously
   * URL Scheme support for third-party integration, enabling automation and workflow extensions
   * Simplified interface focusing on the most commonly used features, making the upscaling process more straightforward

HiPixel aims to complement Upscayl by offering an alternative approach focused on workflow efficiency and native macOS integration, while building upon Upscayl's excellent AI upscaling foundation.

### 🔗 URL Scheme Support

[](#-url-scheme-support)

HiPixel supports URL Scheme for processing images via external applications or scripts. The URL format is:

```
hipixel://?path=/path/to/image1&path=/path/to/image2
```

Example usage in Terminal:

```
# Process a single image
open "hipixel://?path=/Users/username/Pictures/image.jpg"

# Process multiple images
open "hipixel://?path=/Users/username/Pictures/image1.jpg&path=/Users/username/Pictures/image2.jpg"
```

Example usage in AppleScript:

```
tell application "Finder"
    set selectedFiles to selection as alias list
    set urlString to "hipixel://"
    repeat with theFile in selectedFiles
        set urlString to urlString & "?path=" & POSIX path of theFile
    end repeat
    open location urlString
end tell
```

### 🚀 Installation

[](#-installation)

1. Download the latest release from GitHub
2. Move HiPixel.app to your Applications folder
3. Launch HiPixel

### 🛠️ Building from Source

[](#️-building-from-source)

1. Clone the repository

```
git clone https://github.com/okooo5km/hipixel
cd hipixel
```

2. Open HiPixel.xcodeproj in Xcode
3. Build and run the project

### 📝 License

[](#-license)

HiPixel is licensed under the GNU Affero General Public License v3.0 (AGPLv3). This means:

* ✅ You can use, modify, and distribute this software

* ✅ If you modify the software, you must:

  * Make your modifications available under the same license
  * Provide access to the complete source code
  * Preserve all copyright notices and attributions

This software uses Upscayl's binaries and AI models, which are also licensed under AGPLv3.

### ☕️ Support the Project

[](#️-support-the-project)

If you find HiPixel helpful, please consider supporting its development:

* ⭐️ Star the project on GitHub
* 🐛 Report bugs or suggest features
* 💝 Support via:

[![](https://camo.githubusercontent.com/5eb4118bbb9509b96a6b2491d72931785c33d6ecb7eb804c0a856a86006f00d1/68747470733a2f2f696d672e6275796d6561636f666665652e636f6d2f627574746f6e2d6170692f3f746578743d427579206d65206120636f6666656526656d6f6a693d26736c75673d6f6b6f6f6f356b6d26627574746f6e5f636f6c6f75723d46464444303026666f6e745f636f6c6f75723d30303030303026666f6e745f66616d696c793d436f6f6b6965266f75746c696e655f636f6c6f75723d30303030303026636f666665655f636f6c6f75723d666666666666)](https://buymeacoffee.com/okooo5km)

More ways to support

* 🛍️ **[One-time Support via LemonSqueezy](https://okooo5km.lemonsqueezy.com/buy/4f1e3249-2683-4000-acd4-6b05ae117b40?discount=0)**

* **WeChat Pay**

  [![WeChat Pay QR Code](https://camo.githubusercontent.com/6ef89b1a56929cb5c61b8a94cb61ad41bb584071477ea8fd55f175bbd53d3ee7/68747470733a2f2f73746f726167652e356b6d2e686f73742f7765636861747061792e706e67)](https://camo.githubusercontent.com/6ef89b1a56929cb5c61b8a94cb61ad41bb584071477ea8fd55f175bbd53d3ee7/68747470733a2f2f73746f726167652e356b6d2e686f73742f7765636861747061792e706e67)

* **Alipay**

  [![Alipay QR Code](https://camo.githubusercontent.com/8ddc1c87509332b9d11265d2ea466f629451402b7f2ad7b2ff350e0b2123f4ed/68747470733a2f2f73746f726167652e356b6d2e686f73742f616c697061792e706e67)](https://camo.githubusercontent.com/8ddc1c87509332b9d11265d2ea466f629451402b7f2ad7b2ff350e0b2123f4ed/68747470733a2f2f73746f726167652e356b6d2e686f73742f616c697061792e706e67)

Your support helps maintain and improve HiPixel!

### 🙏 Attribution

[](#-attribution)

HiPixel uses the following components from [Upscayl](https://github.com/upscayl/upscayl):

* upscayl-bin - The binary tool for AI upscaling (AGPLv3)
* AI Models - The AI models for image super-resolution (AGPLv3)

HiPixel also uses:

* [Sparkle](https://github.com/sparkle-project/Sparkle) - A software update framework for macOS applications (MIT License)
* [NotchNotification](https://github.com/Lakr233/NotchNotification) - A custom notch-style notification banner for macOS (MIT License)
* [GeneralNotification](https://github.com/okooo5km/GeneralNotification) - A custom notification banner for macOS (MIT License)

***

## macOS 原生的 AI 图像超分辨率工具

[](#macos-原生的-ai-图像超分辨率工具)

HiPixel 是一款原生 macOS 应用程序，用于 AI 图像超分辨率处理，使用 SwiftUI 构建，并采用 Upscayl 的强大 AI 模型。

[![HiPixel 截图](/okooo5km/HiPixel/raw/main/screenshot.jpeg)](https://github.com/okooo5km/HiPixel/blob/main/screenshot.jpeg)

### ✨ 功能特点

[](#-功能特点)

* 🖥️ 原生 macOS 应用程序，使用 SwiftUI 界面
* 🎨 使用 AI 模型进行高质量图像放大
* 🚀 GPU 加速，处理速度快
* 🖼️ 支持多种图像格式
* 💻 现代化直观的用户界面

### 💡 为什么选择 HiPixel？

[](#-为什么选择-hipixel)

虽然 [Upscayl](https://github.com/upscayl/upscayl) 已经提供了一个优秀的 macOS 应用程序，但是 HiPixel 是为了特定的目标而开发的：

1. **原生 macOS 体验**

   * 以原生 SwiftUI 应用程序的形式构建，同时利用 Upscayl 的强大二进制工具和 AI 模型
   * 提供一种无缝的、平台原生的体验，感觉就像在 macOS 上一样

2. **提高工作流效率**

   * 简化交互，支持拖放处理 - 图像在放下时会自动处理
   * 支持批量处理，能够同时处理多张图像
   * 支持 URL Scheme，能够与第三方应用程序集成，实现自动化和工作流扩展
   * 简化界面，专注于最常用的功能，使得图像放大过程更加直接

HiPixel 旨在通过提供一种专注于工作流效率和原生 macOS 集成的替代方法来补充 Upscayl，同时建立在 Upscayl 优秀的 AI 图像放大基础之上。

### 🔗 URL Scheme 使用说明

[](#-url-scheme-使用说明)

HiPixel 支持 URL Scheme，用于通过外部应用程序或脚本处理图像。URL 格式如下：

```
hipixel://?path=/path/to/image1&path=/path/to/image2
```

在终端中的示例用法：

```
# 处理单张图像
open "hipixel://?path=/Users/username/Pictures/image.jpg"

# 处理多张图像
open "hipixel://?path=/Users/username/Pictures/image1.jpg&path=/Users/username/Pictures/image2.jpg"
```

在 AppleScript 中的示例用法：

```
tell application "Finder"
    set selectedFiles to selection as alias list
    set urlString to "hipixel://"
    repeat with theFile in selectedFiles
        set urlString to urlString & "?path=" & POSIX path of theFile
    end repeat
    open location urlString
end tell
```

### 🚀 安装方法

[](#-安装方法)

1. 从 GitHub 下载最新版本
2. 将 HiPixel.app 移动到应用程序文件夹
3. 启动 HiPixel

### 🛠️ 从源代码构建

[](#️-从源代码构建)

1. 克隆仓库

```
git clone https://github.com/okooo5km/hipixel
cd hipixel
```

2. 在 Xcode 中打开 HiPixel.xcodeproj
3. 构建并运行项目

### 📝 许可证

[](#-许可证)

HiPixel 采用 GNU Affero 通用公共许可证第3版 (AGPLv3) 授权。这意味着：

* ✅ 您可以使用、修改和分发此软件

* ✅ 如果您修改了软件，您必须：

  * 在相同的许可证下提供您的修改
  * 提供完整源代码的访问
  * 保留所有版权声明和归属

本软件使用 Upscayl 的二进制文件和 AI 模型，这些也都采用 AGPLv3 许可。

### ☕️ 支持项目

[](#️-支持项目)

如果您觉得 HiPixel 对您有帮助，可以通过以下方式支持项目的开发：

* ⭐️ 在 GitHub 上给项目点星
* 🐛 报告问题或提出建议
* 💝 赞助支持：

[![](https://camo.githubusercontent.com/5eb4118bbb9509b96a6b2491d72931785c33d6ecb7eb804c0a856a86006f00d1/68747470733a2f2f696d672e6275796d6561636f666665652e636f6d2f627574746f6e2d6170692f3f746578743d427579206d65206120636f6666656526656d6f6a693d26736c75673d6f6b6f6f6f356b6d26627574746f6e5f636f6c6f75723d46464444303026666f6e745f636f6c6f75723d30303030303026666f6e745f66616d696c793d436f6f6b6965266f75746c696e655f636f6c6f75723d30303030303026636f666665655f636f6c6f75723d666666666666)](https://buymeacoffee.com/okooo5km)

更多支持方式

* 🛍️ **[通过 LemonSqueezy 一次性支持](https://okooo5km.lemonsqueezy.com/buy/4f1e3249-2683-4000-acd4-6b05ae117b40?discount=0)**

* **微信支付**

  [![微信支付二维码](https://camo.githubusercontent.com/6ef89b1a56929cb5c61b8a94cb61ad41bb584071477ea8fd55f175bbd53d3ee7/68747470733a2f2f73746f726167652e356b6d2e686f73742f7765636861747061792e706e67)](https://camo.githubusercontent.com/6ef89b1a56929cb5c61b8a94cb61ad41bb584071477ea8fd55f175bbd53d3ee7/68747470733a2f2f73746f726167652e356b6d2e686f73742f7765636861747061792e706e67)

* **支付宝**

  [![支付宝二维码](https://camo.githubusercontent.com/8ddc1c87509332b9d11265d2ea466f629451402b7f2ad7b2ff350e0b2123f4ed/68747470733a2f2f73746f726167652e356b6d2e686f73742f616c697061792e706e67)](https://camo.githubusercontent.com/8ddc1c87509332b9d11265d2ea466f629451402b7f2ad7b2ff350e0b2123f4ed/68747470733a2f2f73746f726167652e356b6d2e686f73742f616c697061792e706e67)

您的支持将帮助我们持续改进 HiPixel！

### 🙏 致谢

[](#-致谢)

HiPixel 使用了以下来自 [Upscayl](https://github.com/upscayl/upscayl) 的组件：

* upscayl-bin - AI 放大的二进制工具 (AGPLv3)
* AI Models - 图像超分辨率 AI 模型 (AGPLv3)

HiPixel 还使用了：

* [Sparkle](https://github.com/sparkle-project/Sparkle) - macOS 应用程序的软件更新框架 (MIT 许可证)
* [NotchNotification](https://github.com/Lakr233/NotchNotification) - 适用于 macOS 的刘海屏样式通知横幅 (MIT 许可证)
* [GeneralNotification](https://github.com/okooo5km/GeneralNotification) - 适用于 macOS 的自定义通知横幅 (MIT 许可证)


