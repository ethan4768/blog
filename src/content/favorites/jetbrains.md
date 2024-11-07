---
title: jetbrains 技巧
slug: jetbrains-tips
description: jetbrains 技巧
tags:
  - jetbrains
  - dev
pubDatetime: 2024-10-01T16:33:26+08:00
---

## crack

1. 简单模式，仅限`2021.2.2`及以前版本，原理无限试用
    1. [ide-eval-resetter](https://github.com/zhilepeng/ide-eval-resetter?tab=readme-ov-file)
2. 新模式，最新版本也可
    1. [ja-netfilter](https://gitee.com/ja-netfilter/ja-netfilter)
    2. [Ja-netfilter 常见问题解答](https://chip-tail-e93.notion.site/Ja-netfilter-9886afbfe1ed4d5e90a713e63718f647#0c547d669d9c463d8136b4c30e156a1c)

## code style (JAVA)

1. google style
    1. Settings -> Editor -> Code Style -> Java
    2. Schema 右侧设置中，选择 **Import Schema**
       ，导入 [intellij-java-google-style.xml](https://github.com/google/styleguide/blob/gh-pages/intellij-java-google-style.xml)
2. 保存时自动格式化代码
    1. Settings -> Tools -> Actions on Save
    2. 开启 **Reformat code** 选项
    3. 范围选择 **Whole file**
