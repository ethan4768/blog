---
title: 美团首页推荐的全域用户建模探索与实践
slug: meituan-user-modeling-recommendation
description: 本文详细探讨了美团首页推荐系统中全域用户建模技术的发展与应用。美团的推荐算法团队通过多阶段递进式探索，成功将多源用户交互数据引入召回和排序模块，并应对了多展位、多业务及时空场景相关性导致的跨域信号负迁移挑战。
tags:
  - ai
  - startup
  - dev
  - tool
pubDatetime: 2024-11-01T19:37:42+08:00
ogImage: https://awps-assets.meituan.net/mit/blog/v20190629/asset/icon/apple-icon-180x180.png?v=Whistle&t=20181017-1r

---

[原文链接](https://tech.meituan.com/2024/10/10/exploration-and-practice-of-user-modeling-recommended.html) | [原文内容](../raw/meituan-user-modeling-recommendation) | [AI 总结](../summary/meituan-user-modeling-recommendation)

---

本文详细探讨了美团首页推荐系统中全域用户建模技术的发展与应用。美团的推荐算法团队通过多阶段递进式探索，成功将多源用户交互数据引入召回和排序模块，并应对了多展位、多业务及时空场景相关性导致的跨域信号负迁移挑战。

