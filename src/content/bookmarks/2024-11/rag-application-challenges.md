---
title: 探讨RAG应用中的向量数据库一致性维护挑战
slug: rag-application-challenges
description: 在开发RAG应用过程中，我深刻体会到向量数据库作为辅助组件的重要性。它存储着核心数据生成的text embedding，但当核心数据变化时，向量存储及其metadata也需更新。这会增加一致性维护的负担，使系统变得更加复杂且容易出错。
tags: 
  - rag
  - ai
  - dev
  - opensource
pubDatetime: 2024-11-04T17:29:48+08:00
ogImage: https://abs.twimg.com/responsive-web/client-web/icon-ios.77d25eba.png
---

[原文链接](https://x.com/novoreorx/status/1852915256265441447?s=12&t=D3VZWD30-f7ylSHW3OdYgQ)

---

在开发RAG应用过程中，我深刻体会到向量数据库作为辅助组件的重要性。它存储着核心数据生成的text embedding，但当核心数据变化时，向量存储及其metadata也需更新。这会增加一致性维护的负担，使系统变得更加复杂且容易出错。

