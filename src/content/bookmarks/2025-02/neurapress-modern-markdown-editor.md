---
title: "NeuraPress: 一个现代化的 Markdown 编辑器，提升微信公众号排版体验"
slug: neurapress-modern-markdown-editor
description: |
  NeuraPress 是一个专注于微信公众号排版的现代化 Markdown 编辑器，支持移动设备，让你利用碎片时间轻松编辑文章。它提供实时预览、一键复制、模板系统等功能，基于 Next.js 构建，性能卓越。
tags: 
  - tool
  - markdown
pubDatetime: 2025-02-21T13:34:38+08:00
ogImage: https://opengraph.githubassets.com/c45cf7cb921c025c129dcec0efa3b1b5e80bc6edb0579d3c070a5f8338583f88/tianyaxiang/neurapress
---

[原文链接](https://github.com/tianyaxiang/neurapress)

---

# NeuraPress

[](#neurapress)

NeuraPress 是一个现代化的 Markdown 编辑器，专注于提供优质的微信公众号排版体验。响应式设计，支持移动设备。搭配 DeepSeek和微信公众号助手使用，碎片时间也能用手机发有排版的文章了。

## 特性

[](#特性)

* 🎨 实时预览 - 所见即所得的编辑体验
* 📱 移动端支持 - 支持手机上直接编辑，搭配 DeepSeek和微信公众号助手使用
* 🎯 微信风格 - 完美适配微信公众号样式
* 🔧 样式定制 - 灵活的样式配置选项
* 📋 一键复制 - 支持复制带格式的预览内容
* 🎭 模板系统 - 内置多种排版模板，一键切换
* 🚀 快速高效 - 基于 Next.js 构建，性能优异

## 快速开始

[](#快速开始)

### 环境要求

[](#环境要求)

* Node.js 18+
* pnpm 8+

### 安装

[](#安装)

```
# 克隆项目
git clone https://github.com/tianyaxiang/neurapress.git

# 进入项目目录
cd neurapress

# 安装依赖
pnpm install

# 启动开发服务器
pnpm dev
```

### 构建

[](#构建)

```
# 构建生产版本
pnpm build

# 启动生产服务器
pnpm start
```

## 使用指南

[](#使用指南)

1. **编辑内容**

   * 左侧为 Markdown 编辑区
   * 支持标准 Markdown 语法
   * 支持 GFM (GitHub Flavored Markdown)

2. **预览内容**

   * 右侧为实时预览区
   * 展示最终在微信中的显示效果
   * 可以切换预览窗口的显示/隐藏

3. **样式设置**

   * 使用样式选择器选择预设模板
   * 通过样式配置对话框自定义样式
   * 支持自定义字体、颜色、间距等属性

4. **复制内容**

   * 点击"复制源码"获取 HTML 源码
   * 点击"复制预览"获取带格式的预览内容
   * 直接粘贴到微信公众号编辑器中使用

## 技术栈

[](#技术栈)

* Next.js 14
* React
* TypeScript
* Tailwind CSS
* ByteMD
* Marked
* shadcn/ui

## 🌐 Community

[](#-community)

[Email](mailto:tianyaxiang@qq.com) | [Twitter](https://x.com/tianyaxiang)

## 贡献指南

[](#贡献指南)

欢迎提交 Issue 和 Pull Request。在提交 PR 之前，请确保：

1. 代码通过 ESLint 检查
2. 新功能包含适当的测试
3. 更新相关文档

## 许可证

[](#许可证)

[MIT License](https://github.com/tianyaxiang/neurapress/blob/main/LICENSE)


