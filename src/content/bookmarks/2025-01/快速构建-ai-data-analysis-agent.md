---
title: "使用 GPT-4o 快速构建 AI 数据分析 Agent：自然语言转 SQL 查询"
slug: 快速构建-ai-data-analysis-agent
description: |
  探索如何使用 GPT-4o 构建一款 AI 数据分析 Agent，能够将自然语言转换为 SQL 查询。该工具通过 Streamlit 提供界面，支持 CSV/Excel 文件输入，使用 DuckDB 进行快速数据处理。实现自动数据处理与友好的用户交互界面。
tags: 
  - AI
  - dev
  - tool
  - LLM
  - opensource
pubDatetime: 2025-01-08T20:09:22+08:00
ogImage: https://abs.twimg.com/responsive-web/client-web/icon-ios.77d25eba.png
---

[原文链接](https://x.com/shao__meng/status/1876475609603563587?s=12&t=D3VZWD30-f7ylSHW3OdYgQ)

---

快速构建 AI 数据分析 AgentTL;DR用 GPT-4o 将自然语言转换为 SQL 查询的数据分析工具，通过 Streamlit 提供界面，Phidata 构建和管理 Agents，支持 CSV/Excel 文件输入，使用 DuckDB 执行查询主要特点：· 使用自然语言查询：用户可以用普通语言提问，系统会自动转换为 SQL 查询\
· 支持多种文件格式：可以处理 CSV 和 Excel 文件\
· 自动数据处理：包括数据类型检测和模式推断\
· 交互式界面：使用 Streamlit 构建友好的用户界面技术栈：· OpenAI GPT-4o 作为 LLM\
·

[@phidatahq](https://x.com/phidatahq)

框架用于 AI Agents 构建管理\
· DuckDB 用于数据处理\
·

[@streamlit](https://x.com/streamlit)

用于前端界面构建对 CSV 和 Excel 文件的处理步骤：· 输入处理：\
\- CSV → [http://pd.read](https://t.co/HGLX3VlEvB)\_csv()\
\- Excel → [http://pd.read](https://t.co/HGLX3VlEvB)\_excel()\
· 数据标准化：\
\- 文本列 → 字符串转换\
\- 日期列 → datetime 转换\
\- 特殊字符处理 → 引号转义\
· 输出标准化：\
\- 统一转为 CSV 格式\
\- 使用临时文件存储\
\- 返回(文件路径, 列名列表, 数据框)\
· 查询处理流程：\
\- 自然语言解析\
\- SQL 转换\
\- 查询执行\
\- 结果格式化

We built an AI Data Analysis Agent.\
Just upload CSV/Excel files and analyze data through natural language. It uses DuckDB for lightning-fast processing.\
100% Opensource Code with step-by-step tutorial.

教程地址：[https://theunwindai.com/p/build-an-ai-data-analysis-agent…](https://t.co/p4WvNd8P6D)LLMs App 开源项目合集：

[@readwise](https://x.com/readwise)

save thread

[@readwise](https://x.com/readwise)

save

![Image](https://pbs.twimg.com/media/GgqUfuvbcAA9QTR?format=jpg\&name=900x900)

[![](https://pbs.twimg.com/ext_tw_video_thumb/1876468361808289792/pu/img/LDFGg0thls9wwxaQ.jpg)](blob:https://x.com/65475cdd-c1c4-48f6-9925-25811e9d0741)

![](https://pbs.twimg.com/ext_tw_video_thumb/1876468361808289792/pu/img/LDFGg0thls9wwxaQ.jpg)


