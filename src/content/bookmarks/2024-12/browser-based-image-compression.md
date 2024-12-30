---
title: "Squish: 高效浏览器端批量图像压缩工具"
slug: browser-based-image-compression
description: |
  Squish是一款现代化的浏览器端图像压缩工具，利用WebAssembly实现高性能图像优化。支持多种图像格式（如AVIF、JPEG、PNG等），并提供直观的界面，帮助用户批量压缩图像而不牺牲质量。
tags: 
  - tool
  - image
  - compression
pubDatetime: 2024-12-30T10:09:42+08:00
ogImage: https://repository-images.githubusercontent.com/903631539/4ccbb78c-4501-4749-ad9c-81a81f2e5f71
---

[原文链接](https://github.com/addyosmani/squish)

---

# Squish 🎨

[](#squish-)

[![License: MIT](https://camo.githubusercontent.com/cce5a2a14b0faab422e0bfcdc074afb46089831a0bf5930a7d8af3f31b98f847/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d626c75652e737667)](https://opensource.org/licenses/MIT)

A modern, browser-based image compression tool that leverages WebAssembly for high-performance image optimization. Squish supports multiple formats and provides an intuitive interface for compressing your images without compromising quality.

[![](https://camo.githubusercontent.com/d312d61ae43f0055931bc332fa7ee62ef71b7fa52c744f6430c1dc2c7da5f1e8/68747470733a2f2f7371756973682e616464792e69652f6d6574612e6a7067)](https://camo.githubusercontent.com/d312d61ae43f0055931bc332fa7ee62ef71b7fa52c744f6430c1dc2c7da5f1e8/68747470733a2f2f7371756973682e616464792e69652f6d6574612e6a7067)

## ✨ Features

[](#-features)

* 🖼️ Support for multiple image formats:

  * AVIF (AV1 Image Format)
  * JPEG (using MozJPEG)
  * JPEG XL
  * PNG (using OxiPNG)
  * WebP

* 🚀 Key capabilities:

  * Browser-based compression (no server uploads needed)
  * Batch processing support
  * Format conversion
  * Quality adjustment per format
  * Real-time preview
  * Size reduction statistics
  * Drag and drop interface
  * Smart queue for compressing large number of files

## 🛠️ Technology

[](#️-technology)

Squish is built with modern web technologies:

* React + TypeScript for the UI
* Vite for blazing fast development
* WebAssembly for native-speed image processing
* Tailwind CSS for styling
* jSquash for image codec implementations

## 🚀 Getting Started

[](#-getting-started)

### Prerequisites

[](#prerequisites)

* Node.js 18 or later
* npm 7 or later

### Installation

[](#installation)

1. Clone the repository:

```
git clone https://github.com/addyosmani/squish.git
cd squish
```

2. Install dependencies:

```
npm install
```

3. Start the development server:

```
npm run dev
```

4. Build for production:

```
npm run build
```

## 💡 Usage

[](#-usage)

1. **Drop or Select Images**: Drag and drop images onto the upload area or click to select files
2. **Choose Output Format**: Select your desired output format (AVIF, JPEG, JPEG XL, PNG, or WebP)
3. **Adjust Quality**: Use the quality slider to balance between file size and image quality
4. **Download**: Download individual images or use the "Download All" button for batch downloads

## 🔧 Default Quality Settings

[](#-default-quality-settings)

* AVIF: 50%
* JPEG: 75%
* JPEG XL: 75%
* PNG: Lossless
* WebP: 75%

## 🤝 Contributing

[](#-contributing)

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

[](#-license)

This project is licensed under the MIT License - see the [LICENSE](https://github.com/addyosmani/squish/blob/main/LICENSE) file for details.

## 🙏 Acknowledgments

[](#-acknowledgments)

* [jSquash](https://github.com/jamsinclair/jSquash) for the WebAssembly image codecs
* [MozJPEG](https://github.com/mozilla/mozjpeg) for JPEG compression
* [libavif](https://github.com/AOMediaCodec/libavif) for AVIF support
* [libjxl](https://github.com/libjxl/libjxl) for JPEG XL support
* [Oxipng](https://github.com/shssoichiro/oxipng) for PNG optimization


