---
title: "基于fabric.js和Vue的插件化开源图片编辑器"
slug: vue-fabric-editor
description: |
  快图设计是一个基于fabric.js和Vue构建的开源图片编辑器，支持自定义字体、素材和设计模板，拥有优秀的拖拽式设计和插件化架构，适合用户轻松上手创建多样化的设计作品。
tags: 
  - AI
  - dev
  - opensource
  - image
  - Vue
pubDatetime: 2025-05-13T10:12:57+08:00
ogImage: https://repository-images.githubusercontent.com/532317770/8536ac6c-fb52-48cc-a0aa-35ad85ae403d
---

[原文链接](https://github.com/ikuaitu/vue-fabric-editor)

---

[English](https://github.com/ikuaitu/vue-fabric-editor/blob/main/README-en.md)| 中文

[![开源图片编辑器](https://private-user-images.githubusercontent.com/13534626/356800570-4e519179-8d19-41cc-ad2b-a1d7ebc63836.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDcwNTg2MDgsIm5iZiI6MTc0NzA1ODMwOCwicGF0aCI6Ii8xMzUzNDYyNi8zNTY4MDA1NzAtNGU1MTkxNzktOGQxOS00MWNjLWFkMmItYTFkN2ViYzYzODM2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MTIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTEyVDEzNTgyOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTFhOGE4OTZhNTRlYWYwMjZiNmM0ODRjMWVkYjUzMTg5NTFmYWJhM2M2M2FiM2ZhY2I4NTBkOWM1NjZlMjU5NmQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.zkxD-jNHQv6_Shz62wtPemOE3E9jyBsnYVPe-130-xE)](https://pro.kuaitu.cc)

### 开源图片编辑器 · 插件化架构 · 拖拽式设计 · 功能完善

[](#开源图片编辑器--插件化架构--拖拽式设计--功能完善-)

基于 fabric.js 和 Vue 开发的插件化图片编辑器，可自定义字体、素材、设计模板、右键菜单、快捷键

[演示](https://ikuaitu.github.io/vue-fabric-editor/) · [文档](https://ikuaitu.github.io/doc/#/) · [商业版演示](https://www.kuaitu.cc/) · [商业版介绍](https://pro.kuaitu.cc/)

\


[![stars](https://camo.githubusercontent.com/6cc722bd2cb68391f325f02831a5b2006a43c38b0298eddb1f0c91db84c177ac/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f696b75616974752f7675652d6661627269632d656469746f723f7374796c653d666c6174) ](https://github.com/ikuaitu/vue-fabric-editor/blob/main)[![stars](https://camo.githubusercontent.com/c5b2e1abdbb0a487bcf0f198dac16c034c4ed8e0ec6b34df7cfcd3597d536a52/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f696b75616974752f7675652d6661627269632d656469746f723f7374796c653d666c6174) ](https://github.com/ikuaitu/vue-fabric-editor/blob/main)[![contributors](https://camo.githubusercontent.com/9bcc935d4235c0821e24b2b3643cb4ff6b37b21b9f16568c3d61011bffd8d92e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6e7472696275746f72732f696b75616974752f7675652d6661627269632d656469746f72) ](https://github.com/ikuaitu/vue-fabric-editor/graphs/contributors)[![license](https://camo.githubusercontent.com/939d469b253186979a362f84a62032030dc9c8e8be54fdcdb500b6343cc3773b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f696b75616974752f7675652d6661627269632d656469746f723f7374796c653d666c6174) ](https://github.com/ikuaitu/vue-fabric-editor?tab=MIT-1-ov-file)[![快图设计网站](https://camo.githubusercontent.com/b05721e93bc7529033cb928cf2e19bd8ef688fe9dd42c78e360ccaa5357af28e/68747470733a2f2f696d672e736869656c64732e696f2f776562736974653f75726c3d6874747025334125324625324670726f2e6b75616974752e6363253246)](https://www.kuaitu.cc/)

\


[![演示](https://private-user-images.githubusercontent.com/13534626/356800766-2a41f5ac-2211-45b8-b683-ffbdf72e6d8b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDcwNTg2MDgsIm5iZiI6MTc0NzA1ODMwOCwicGF0aCI6Ii8xMzUzNDYyNi8zNTY4MDA3NjYtMmE0MWY1YWMtMjIxMS00NWI4LWI2ODMtZmZiZGY3MmU2ZDhiLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MTIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTEyVDEzNTgyOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTFjYWJhNmVlODMyM2RjOGIzZGNlOWMyOWQwMTdlOWVkZTUxOGE0YmM1N2EyMWJhMWI2NzQ4YmNlZTA5YzA4NjQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.kc-usLwkXG1KcVw8CGPBR7vcHuVUdOPlQeds5-XpLAM)](https://github.com/ikuaitu/vue-fabric-editor/blob/main)

## 简介

[](#简介)

快图设计，vue-fabric-editor 是一款基于 fabric.js 和 Vue 开发的图片编辑器，可自定义字体、素材、设计模板、右键菜单、快捷键。

[动图介绍](https://juejin.cn/post/7222141882515128375) · [介绍视频](https://www.bilibili.com/video/BV1US421A7TU/?spm_id_from=333.999.0.0)

### 特点

[](#特点)

1. **插件化架构**：可通过插件的进行扩展开发，支持右键菜单和快捷键。
2. **拖拽式设计**：以轻量、简洁为主的图形编辑器，而非大而全的在线 PS 类的重行设计工具。
3. **功能完善**：PSD 解析、辅助线、历史记录、渐变、自定义字体、裁剪等功能。

### 已有功能

[](#已有功能)

* 导入 JSON、PSD 文件
* 导出 PNG、SVG、JSON 文件
* 组合/拆分组合
* 图层功能
* 渐变属性
* 外观属性/字体属性/描边/阴影
* 撤销/重做
* 快捷键
* 右键菜单
* 辅助线
* 标尺
* 自定义字体
* 自定义模板素材
* 插入 SVG、图片素材
* 多元素水平、垂直对齐方式
* 背景属性设置
* 箭头/线条
* 画笔/多边形绘制
* 二维码/条形码
* 图片替换/裁剪/滤镜
* 水印
* 国际化

## 使用

[](#使用)

请先安装 node.js v18-v20，及 pnpm 8.4.0， 然后执行以下命令：

```
// 安装pnpm
npm install -g pnpm@8.4.0

// 中国使用淘宝代理
// npm install -g pnpm@8.4.0 --registry=https://registry.npmmirror.com
pnpm i
pnpm dev
```

重要：必须使用pnpm 8.x，高版本pnpm会导致依赖不一致出现页面运行报错。

## 开发者服务

[](#开发者服务)

* **微信交流群**：我们组建了多个微信项目交流群，作者和项目维护者活跃在群内，定期解答问题。
* **fabric.js 中文教程**：[https://blog.kuaitu.cc](https://blog.kuaitu.cc/)。
* **知识星球**：长期更新开源编辑器与 fabric.js 的相关资料，沉淀最佳实践、开发经验分享、代码示例等。 [![二维码](https://private-user-images.githubusercontent.com/13534626/320255466-25e9075e-f751-4110-aadd-30fe453e02d9.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDcwNTg2MDgsIm5iZiI6MTc0NzA1ODMwOCwicGF0aCI6Ii8xMzUzNDYyNi8zMjAyNTU0NjYtMjVlOTA3NWUtZjc1MS00MTEwLWFhZGQtMzBmZTQ1M2UwMmQ5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MTIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTEyVDEzNTgyOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWM4YzliYzRjMWI4OTJkNWZmNDVjZjUxMmI3NzlhOWZhOGU5NWRiNzQyZTRlYjgyYWY5ZGM4OTM1MGVmZTM0N2QmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.jeH14sZ7oRrhjYOAVjIbXMeJ1d3o7leqGvZKi_KiMwg)](https://private-user-images.githubusercontent.com/13534626/320255466-25e9075e-f751-4110-aadd-30fe453e02d9.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDcwNTg2MDgsIm5iZiI6MTc0NzA1ODMwOCwicGF0aCI6Ii8xMzUzNDYyNi8zMjAyNTU0NjYtMjVlOTA3NWUtZjc1MS00MTEwLWFhZGQtMzBmZTQ1M2UwMmQ5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MTIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTEyVDEzNTgyOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWM4YzliYzRjMWI4OTJkNWZmNDVjZjUxMmI3NzlhOWZhOGU5NWRiNzQyZTRlYjgyYWY5ZGM4OTM1MGVmZTM0N2QmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.jeH14sZ7oRrhjYOAVjIbXMeJ1d3o7leqGvZKi_KiMwg)

## 付费版本

[](#付费版本)

帮助企业快速搭建在线设计工具，**减少企业研发投入，避免重复造轮子。**

[功能介绍](https://ws0gdejldw.feishu.cn/docx/GKmnddCgFokr4sxFeYNcoql1nAb) · [产品介绍](http://pro.kuaitu.cc/) · [演示](https://www.kuaitu.cc/)

开源版本仅前端代码，付费版本**提供完整的前后端、管理后台，功能完整开箱即用，提供源码授权、支持二次开发**。

* **开箱即用，功能完整**：设计能力丰富，提供完整前台、后台功能，部署即可使用。
* **插件架构，扩展方便**：基于插件化 API，快速对编辑器进行二次开发。
* **批量生成，快速出图**：支持通过 HTTP 接口、表格文件批量生成图片。
* **拖拽式设计，简单易用**：适合普通用户操作，无需培训轻松上手。
* **全平台适配**：PC 版本、H5 版本支持各种应用场景。
* **技术对接，文档培训**：提供更多的支持，高效完成技术对接。
* **定制开发，减少投入**：支持快速完成功能定制开发，减少研发投入。 [![开源图片编辑器](https://private-user-images.githubusercontent.com/13534626/358521113-5303395b-247d-45be-a411-ef27a389156c.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDcwNTg2MDgsIm5iZiI6MTc0NzA1ODMwOCwicGF0aCI6Ii8xMzUzNDYyNi8zNTg1MjExMTMtNTMwMzM5NWItMjQ3ZC00NWJlLWE0MTEtZWYyN2EzODkxNTZjLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MTIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTEyVDEzNTgyOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTQxMTZkNTQyYmUyYmJlODgzOGE2ZWFhNWM0MDViN2NiZWFmYTNmMzFhZTU1OTc0ZTMwNjI4N2Q0ZDYxYmQ4YTgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.A9Q5H-lbwRULI2Tquj_tVxhXUVnmwn_MWO66e-u8s8E)](https://pro.kuaitu.cc)

## 贡献指南

[](#贡献指南)

项目致力于打造一个开箱即用的 web 图片编辑器应用，同时沉淀一个介于 web 图片编辑器应用与 fabric.js 之间的封装层，期望封装层面向开发者设计，提供更简单的接口，让开发者可以轻松的实现图片应用开发。

如果你对这件事情感兴趣，真诚的邀请你加入，我们一起成长，你只要会简单的 Git 和 Javascript 语法就可以。

[【提交代码送赢雷蛇游戏鼠标】](https://github.com/ikuaitu/vue-fabric-editor/issues/526)

### 相关资料

[](#相关资料)

这是我发表在掘金社区关于编辑器的技术笔记，会有更多的细节：

1. [使用 fabric.js 快速开发一个图片编辑器](https://juejin.cn/post/7155040639497797645)，
2. [fabric.js 开发图片编辑器的细节实现](https://juejin.cn/post/7199849226745430076)
3. [fabric.js 开发图片编辑器可以实现哪些功能？多图](https://juejin.cn/post/7222141882515128375)
4. [我的开源项目与开源经历分享](https://juejin.cn/post/7224765991896121401)
5. [Canvas 库 fabric.js 可以实现哪些功能？ 动图介绍](https://juejin.cn/post/7336743827827015731)
6. [Vue 开源图片编辑器](https://juejin.cn/post/7384258569590636595)
7. [个人开源项目商业化经验分享](https://juejin.cn/post/7400687574967271478)
8. [开源 fabric.js 图片编辑器的插件化架构](https://juejin.cn/post/7401071861847949339)

注：如果遇到技术问题，期望使用 issue 讨论，它更加开放与透明，足够多的信息会让解决问题变得更高效，参考[提问的智慧](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/main/README-zh_CN.md#%E6%8F%90%E9%97%AE%E7%9A%84%E6%99%BA%E6%85%A7)。

## 致谢

[](#致谢)

* [刘明野](https://github.com/liumingye)标尺功能作者。
* [palxiao](https://github.com/palxiao/poster-design/tree/main/packages/color-picker)设计编辑器的渐变组件。

## 友情赞助

[](#友情赞助)

[![开源图片编辑器](https://camo.githubusercontent.com/c2e1897d4b065be872bf3f346e66366b54a6a874abfdaa7e577c9c360a473898/68747470733a2f2f7777772e73756e6d616f2d64657369676e2e746f702f73756e6d616f2f61646d696e2f6173736574732f6c6f676f2e38393661613137362e706e67) ](https://github.com/wangyuan389/mall-cook)[![开源图片编辑器](https://raw.githubusercontent.com/rubickCenter/rubick/refs/heads/master/public/logo.png) ](https://github.com/rubickCenter/rubick)[![开源图片编辑器](https://private-user-images.githubusercontent.com/13534626/405137406-0c6ed3c4-bc2b-49fb-854d-f9ed75a96121.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDcwNTg2MDgsIm5iZiI6MTc0NzA1ODMwOCwicGF0aCI6Ii8xMzUzNDYyNi80MDUxMzc0MDYtMGM2ZWQzYzQtYmMyYi00OWZiLTg1NGQtZjllZDc1YTk2MTIxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MTIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTEyVDEzNTgyOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTM3ZmE0ZDVhNWQyNDIyZDZhNGUxZDI3MzY1M2M1MDkyNDNjNjc5MTdhZjk2ZGExYzQ5YjYyMWE0ZTRhMDI0NGImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.BYGJvWFiGHOR7yCPxxVPTvuH1Nv9GNXzDkcxCM5nG-M)](https://github.com/leaferjs/leafer-ui)

## 管理员

[](#管理员)

## 贡献者

[](#贡献者)

|                                                                                                                     |                                                                                                                        |                                                                                                                                    |                                                                                                                              |                                                                                                                              |                                                                                                                         |
| :-----------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------: |
|    [![nihaojob](https://avatars.githubusercontent.com/u/13534626?v=4) **nihaojob**](https://github.com/nihaojob)    |       [![Qiu-Jun](https://avatars.githubusercontent.com/u/24954362?v=4) **Qiu-Jun**](https://github.com/Qiu-Jun)       | [![wuchenguang1998](https://avatars.githubusercontent.com/u/63847336?v=4) **wuchenguang1998**](https://github.com/wuchenguang1998) | [![AliceLanniste](https://avatars.githubusercontent.com/u/17617116?v=4) **AliceLanniste**](https://github.com/AliceLanniste) |            [![ylx252](https://avatars.githubusercontent.com/u/6425957?v=4) **ylx252**](https://github.com/ylx252)            |     [![liumingye](https://avatars.githubusercontent.com/u/8676207?v=4) **liumingye**](https://github.com/liumingye)     |
|    [![momo2019](https://avatars.githubusercontent.com/u/26078793?v=4) **momo2019**](https://github.com/momo2019)    |       [![ByeWord](https://avatars.githubusercontent.com/u/37115721?v=4) **ByeWord**](https://github.com/ByeWord)       |       [![bigFace2019](https://avatars.githubusercontent.com/u/55651401?v=4) **bigFace2019**](https://github.com/bigFace2019)       |    [![wohuweixiya](https://avatars.githubusercontent.com/u/86701050?v=4) **wohuweixiya**](https://github.com/wohuweixiya)    |          [![zjc2233](https://avatars.githubusercontent.com/u/43945226?v=4) **zjc2233**](https://github.com/zjc2233)          |             [![ijry](https://avatars.githubusercontent.com/u/3102798?v=4) **ijry**](https://github.com/ijry)            |
|       [![makeng](https://avatars.githubusercontent.com/u/23654388?v=4) **makeng**](https://github.com/makeng)       |    [![z09176141](https://avatars.githubusercontent.com/u/49260613?v=4) **z09176141**](https://github.com/z09176141)    |         [![a847244052](https://avatars.githubusercontent.com/u/28621500?v=4) **a847244052**](https://github.com/a847244052)        |      [![briver0825](https://avatars.githubusercontent.com/u/87807886?v=4) **briver0825**](https://github.com/briver0825)     | [![skyscraperno1](https://avatars.githubusercontent.com/u/63391543?v=4) **skyscraperno1**](https://github.com/skyscraperno1) | [![pengzhijian](https://avatars.githubusercontent.com/u/133614612?v=4) **pengzhijian**](https://github.com/pengzhijian) |
|   [![JiangShuQ](https://avatars.githubusercontent.com/u/95730895?v=4) **JiangShuQ**](https://github.com/JiangShuQ)  |    [![hudenghui](https://avatars.githubusercontent.com/u/17875293?v=4) **hudenghui**](https://github.com/hudenghui)    |             [![ddshiyu](https://avatars.githubusercontent.com/u/37503208?v=4) **ddshiyu**](https://github.com/ddshiyu)             |          [![yehan68](https://avatars.githubusercontent.com/u/40497166?v=4) **yehan68**](https://github.com/yehan68)          |          [![luke358](https://avatars.githubusercontent.com/u/48149577?v=4) **luke358**](https://github.com/luke358)          |        [![xiaozeo](https://avatars.githubusercontent.com/u/13568242?v=4) **xiaozeo**](https://github.com/xiaozeo)       |
|      [![x007xyz](https://avatars.githubusercontent.com/u/13807549?v=4) **x007xyz**](https://github.com/x007xyz)     |      [![wozhi-cl](https://avatars.githubusercontent.com/u/25359239?v=4) **wozhi-cl**](https://github.com/wozhi-cl)     |               [![vvbear](https://avatars.githubusercontent.com/u/32010827?v=4) **vvbear**](https://github.com/vvbear)              |      [![slarkerino](https://avatars.githubusercontent.com/u/7014849?v=4) **slarkerino**](https://github.com/slarkerino)      |         [![rolitter](https://avatars.githubusercontent.com/u/27326998?v=4) **rolitter**](https://github.com/rolitter)        |     [![moJiXiang](https://avatars.githubusercontent.com/u/5847011?v=4) **moJiXiang**](https://github.com/moJiXiang)     |
| [![macheteHot](https://avatars.githubusercontent.com/u/26652329?v=4) **macheteHot**](https://github.com/macheteHot) |    [![liuyaojun](https://avatars.githubusercontent.com/u/25071631?v=4) **liuyaojun**](https://github.com/liuyaojun)    |               [![jooyyy](https://avatars.githubusercontent.com/u/30552622?v=4) **jooyyy**](https://github.com/jooyyy)              |         [![guda-art](https://avatars.githubusercontent.com/u/66010134?v=4) **guda-art**](https://github.com/guda-art)        |             [![nanfb](https://avatars.githubusercontent.com/u/56207464?v=4) **nanfb**](https://github.com/nanfb)             |   [![dulltackle](https://avatars.githubusercontent.com/u/45963660?v=4) **dulltackle**](https://github.com/dulltackle)   |
|         [![Bamzc](https://avatars.githubusercontent.com/u/10151046?v=4) **Bamzc**](https://github.com/Bamzc)        | [![Yangzongtai](https://avatars.githubusercontent.com/u/93592008?v=4) **Yangzongtai**](https://github.com/Yangzongtai) |         [![Alicehhhmm](https://avatars.githubusercontent.com/u/86783773?v=4) **Alicehhhmm**](https://github.com/Alicehhhmm)        |         [![fuqianxi](https://avatars.githubusercontent.com/u/20251751?v=4) **fuqianxi**](https://github.com/fuqianxi)        |  [![icleitoncosta](https://avatars.githubusercontent.com/u/3260480?v=4) **icleitoncosta**](https://github.com/icleitoncosta) |        [![liucity](https://avatars.githubusercontent.com/u/12006542?v=4) **liucity**](https://github.com/liucity)       |

## License

[](#license)

Licensed under the [MIT](https://github.com/ikuaitu/vue-fabric-editor/blob/main/LICENSE) License.


