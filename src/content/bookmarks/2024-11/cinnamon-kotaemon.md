---
title: kotaemon 一个开源的、高颜值、清爽干净且可定制的 RAG UI 系统
slug: cinnamon-kotaemon
description: Cinnamon开源了一款基于RAG的工具kotaemon，可以与您的文档进行互动对话。这款工具能有效解析文档内容并提供智能反馈，帮助用户获取所需信息。其特点包括支持多种文件格式、快速响应以及易于集成的API。
tags: 
  - opensource
  - ai
  - rag
  - tool
  - dev
pubDatetime: 2024-11-05T17:52:21+08:00
ogImage: https://opengraph.githubassets.com/702a2733fd887db9681c8b085c28f7d0e7429636597a534a263bbd0f9ddcc842/Cinnamon/kotaemon
---

[原文链接](https://github.com/Cinnamon/kotaemon)

---

kotaemon 是一个开源的、高颜值、清爽干净且可定制的 RAG UI 系统, 既能让普通用户轻松实现文档问答, 又能让开发者构建自己的 RAG 管道, 支持多种 LLM、多模态文档处理和复杂推理能力, 最近更新也支持了思维导图模式。

※ 核心特点 ※

文档管理与协作:
- 支持多用户登录
- 可以组织私有/公共文档集合
- 支持协作和聊天分享

模型支持:
- 支持多种 LLM:
    - 云服务: OpenAI、Azure、
      @GroqInc
      等
    - 本地模型: 通过
      @ollama
      和 llama-cpp-python
- 灵活的模型组织管理

RAG 技术特色:
- 混合检索系统: 结合全文检索和向量检索
- 支持重排序以确保最佳检索质量
- 支持多模态问答(包含图表支持)
- 提供详细的引用支持和文档预览
- 支持复杂推理方法(问题分解、ReAct、ReWOO 等)

技术架构:
- 基于
  @Gradio
  构建 UI
- 支持 Python 3.10+
- 提供 Docker 部署支持(lite 和 full)
- 可扩展性强, 支持自定义 UI 和检索策略