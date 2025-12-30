---
title: "一款超精致的 React 图片预览组件 – react-photo-view"
slug: 一款超精致的-react-图片预览组件-react-photo-view
description: |
  react-photo-view: A beautiful photo preview component
tags: 
  - React
pubDatetime: 2025-12-30T14:18:25+08:00
ogImage: 
---

[原文链接](https://react-photo-view.vercel.app/)

---

一款超精致的 React 图片预览组件

#### 触摸手势

#### 反馈动画

#### 图像自适应

#### 自定义元素

#### 键盘导航

#### 基于 TypeScript

#### 轻量体积

#### 更多...

`react-photo-view` 拥有无与伦比的预览交互体验：从打开图像开始，每一帧的动画、细节和交互都经过了精心设计与反复调试，媲美原生图片预览的效果。

![](https://react-photo-view.vercel.app/_next/static/media/1.c788857d.jpg)![](https://react-photo-view.vercel.app/_next/static/media/2.b43f1ead.jpg)![](https://react-photo-view.vercel.app/_next/static/media/3.70695fb9.jpg)![](https://react-photo-view.vercel.app/_next/static/media/4.57ff8e86.jpg)![](https://react-photo-view.vercel.app/_next/static/media/5.7ace37c7.jpg)![](https://react-photo-view.vercel.app/_next/static/media/6.0271162c.jpg)

## 概览[](#概览)

```
import { PhotoProvider, PhotoView } from 'react-photo-view';
import 'react-photo-view/dist/react-photo-view.css';
 
export default function App() {
  return (
    <PhotoProvider>
      <PhotoView src="/1.jpg">
        <img src="/1-thumbnail.jpg" alt="" />
      </PhotoView>
    </PhotoProvider>
  );
}
```

该示例中，`react-photo-view` 提供了两个组件： `PhotoProvider` 和 `PhotoView`。以 `PhotoProvider`为界限，里面所有的 `PhotoView` 图片会按照运行顺序提取为一组图片预览画廊。当某个 `<img />` 被点击，则会定位到指定的图片并打开预览。

## 特性[](#特性)

它拥有非常完善的细节与特性：

* 支持触摸手势，**拖动/平移/物理效果滑动，双指指定位置放大/缩小**
* 全方面动画衔接，**打开/关闭/回弹/触边**，顺其自然的交互效果
* 图像自适应，以一个合适的最初呈现大小，并根据调整自适应
* 支持自定义如 `<video />` 或任意 `HTML` 元素的预览
* 键盘导航，完美适配桌面端
* 支持自定义节点扩展，轻松实现**全屏预览、旋转控制、图片介绍**以及更多功能
* 基于 `typescript`，`7KB Gzipped`，支持服务端渲染
* 简单易用的 `API`，上手零成本

## 关于[](#关于)

![stars](https://badgen.net/github/stars/MinJieLiu/react-photo-view)![version](https://img.shields.io/npm/v/react-photo-view.svg?style=flat-square)![downloads](http://img.shields.io/npm/dm/react-photo-view.svg?style=flat-square)![license](https://badgen.net/npm/license/react-photo-view)![min](https://badgen.net/bundlephobia/min/react-photo-view?label=minified)![gzip](https://badgen.net/bundlephobia/minzip/react-photo-view?label=gzip)

`react-photo-view` 由 [MinJieLiu (opens in a new tab)](https://github.com/MinJieLiu) 创建

* [稀土掘金 (opens in a new tab)](https://juejin.cn/user/289926798650509)
* [知乎 (opens in a new tab)](https://www.zhihu.com/people/liumingyi)
* [GitHub (opens in a new tab)](https://github.com/MinJieLiu)
* [Gitee (opens in a new tab)](https://gitee.com/MinJieLiu)

加我好友，拉你进前端交流进阶大群（备注：加群）

![code](https://react-photo-view.vercel.app/_next/static/media/qrcode.44dc8faf.jpg)

## License[](#license)

Apache-2.0 © [MinJieLiu (opens in a new tab)](https://github.com/MinJieLiu)

Last updated on 2023年12月26日


