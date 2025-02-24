---
title: "RAGFlow：基于深度文档理解的开源检索增强生成引擎"
slug: ragflow-open-source-engine
description: |
  RAGFlow是一个开源的检索增强生成（RAG）引擎，旨在实现深度文档理解。它结合大型语言模型（LLM），为各规模企业提供真实的问题解答能力，并实现对复杂格式数据的有效归纳。适用于多种数据源，RAGFlow是推动智能应用的重要工具。
tags: 
  - AI
  - opensource
  - RAG
  - dev
  - python
pubDatetime: 2025-02-24T10:21:17+08:00
ogImage: 
---

[原文链接](https://github.com/infiniflow/ragflow)

---

[![ragflow logo](/infiniflow/ragflow/raw/main/web/src/assets/logo-with-text.png)](https://demo.ragflow.io/)

[English](https://github.com/infiniflow/ragflow/blob/main/README.md) | [简体中文](https://github.com/infiniflow/ragflow/blob/main/README_zh.md) | [繁体中文](https://github.com/infiniflow/ragflow/blob/main/README_tzh.md) | [日本語](https://github.com/infiniflow/ragflow/blob/main/README_ja.md) | [한국어](https://github.com/infiniflow/ragflow/blob/main/README_ko.md) | [Bahasa Indonesia](https://github.com/infiniflow/ragflow/blob/main/README_id.md) | [Português (Brasil)](https://github.com/infiniflow/ragflow/blob/main/README_pt_br.md)

[![follow on X(Twitter)](https://camo.githubusercontent.com/79209f7492b56c8c14bf825f9509cb9ef2596ee42158e5874863d06855101ba8/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f696e66696e69666c6f773f6c6f676f3d5826636f6c6f723d253230253233663566356635) ](https://x.com/intent/follow?screen_name=infiniflowai)[![Static Badge](https://camo.githubusercontent.com/fa96e87b3d7abf8a86ab2e3ea015163bdd2df51d162f7eb263fa83e085273888/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f6e6c696e652d44656d6f2d346536623939) ](https://demo.ragflow.io)[![docker pull infiniflow/ragflow:v0.16.0](https://camo.githubusercontent.com/f867f184aa51e745ebab911e055e0926863129b24ab199c3bfeaf97d245ecc07/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f636b65725f70756c6c2d726167666c6f773a76302e31362e302d627269676874677265656e) ](https://hub.docker.com/r/infiniflow/ragflow)[![Latest Release](https://camo.githubusercontent.com/27a37bccb671f574f4e3fac27bedffb460d8b35fe58fd1fcc771c95cacb5263b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f696e66696e69666c6f772f726167666c6f773f636f6c6f723d626c7565266c6162656c3d4c617465737425323052656c65617365) ](https://github.com/infiniflow/ragflow/releases/latest)[![license](https://camo.githubusercontent.com/a04a140c9d7ce4a4cd9359413e1b35a05dab44f346726faba73cc7066fac2d89/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4170616368652d2d322e302d6666666666663f6c6162656c436f6c6f723d64346561663726636f6c6f723d326536636334)](https://github.com/infiniflow/ragflow/blob/main/LICENSE)

#### [Document](https://ragflow.io/docs/dev/) | [Roadmap](https://github.com/infiniflow/ragflow/issues/4214) | [Twitter](https://twitter.com/infiniflowai) | [Discord](https://discord.gg/4XxujFgUN7) | [Demo](https://demo.ragflow.io)

[](#--document---roadmap---twitter---discord---demo)

**📕 Table of Contents**

* 💡 [What is RAGFlow?](#-what-is-ragflow)
* 🎮 [Demo](#-demo)
* 📌 [Latest Updates](#-latest-updates)
* 🌟 [Key Features](#-key-features)
* 🔎 [System Architecture](#-system-architecture)
* 🎬 [Get Started](#-get-started)
* 🔧 [Configurations](#-configurations)
* 🔧 [Build a docker image without embedding models](#-build-a-docker-image-without-embedding-models)
* 🔧 [Build a docker image including embedding models](#-build-a-docker-image-including-embedding-models)
* 🔨 [Launch service from source for development](#-launch-service-from-source-for-development)
* 📚 [Documentation](#-documentation)
* 📜 [Roadmap](#-roadmap)
* 🏄 [Community](#-community)
* 🙌 [Contributing](#-contributing)

## 💡 What is RAGFlow?

[](#-what-is-ragflow)

[RAGFlow](https://ragflow.io/) is an open-source RAG (Retrieval-Augmented Generation) engine based on deep document understanding. It offers a streamlined RAG workflow for businesses of any scale, combining LLM (Large Language Models) to provide truthful question-answering capabilities, backed by well-founded citations from various complex formatted data.

## 🎮 Demo

[](#-demo)

Try our demo at <https://demo.ragflow.io>.

[![](https://private-user-images.githubusercontent.com/7248/337628841-2f6baa3e-1092-4f11-866d-36f6a9d075e5.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii83MjQ4LzMzNzYyODg0MS0yZjZiYWEzZS0xMDkyLTRmMTEtODY2ZC0zNmY2YTlkMDc1ZTUuZ2lmP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDIyNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAyMjRUMDIyMDUzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MjU0ZDQ3MjAwYzM4ZDYzNWVjZTJmOTAyNDliNDM2ZGU0NzkzNDk4MjAyNWQ1NjRiZmI3Y2VkZTNiMTQzNWIxYiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.SzWdmdWMsDWcgGTxt3TabVfpp7lutCI8M6LhBCMS3zs)](https://private-user-images.githubusercontent.com/7248/337628841-2f6baa3e-1092-4f11-866d-36f6a9d075e5.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii83MjQ4LzMzNzYyODg0MS0yZjZiYWEzZS0xMDkyLTRmMTEtODY2ZC0zNmY2YTlkMDc1ZTUuZ2lmP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDIyNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAyMjRUMDIyMDUzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MjU0ZDQ3MjAwYzM4ZDYzNWVjZTJmOTAyNDliNDM2ZGU0NzkzNDk4MjAyNWQ1NjRiZmI3Y2VkZTNiMTQzNWIxYiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.SzWdmdWMsDWcgGTxt3TabVfpp7lutCI8M6LhBCMS3zs) [![337628841-2f6baa3e-1092-4f11-866d-36f6a9d075e5.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii83MjQ4LzMzNzYyODg0MS0yZjZiYWEzZS0xMDkyLTRmMTEtODY2ZC0zNmY2YTlkMDc1ZTUuZ2lmP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDIyNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAyMjRUMDIyMDUzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MjU0ZDQ3MjAwYzM4ZDYzNWVjZTJmOTAyNDliNDM2ZGU0NzkzNDk4MjAyNWQ1NjRiZmI3Y2VkZTNiMTQzNWIxYiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.SzWdmdWMsDWcgGTxt3TabVfpp7lutCI8M6LhBCMS3zs](https://private-user-images.githubusercontent.com/7248/337628841-2f6baa3e-1092-4f11-866d-36f6a9d075e5.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii83MjQ4LzMzNzYyODg0MS0yZjZiYWEzZS0xMDkyLTRmMTEtODY2ZC0zNmY2YTlkMDc1ZTUuZ2lmP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDIyNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAyMjRUMDIyMDUzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MjU0ZDQ3MjAwYzM4ZDYzNWVjZTJmOTAyNDliNDM2ZGU0NzkzNDk4MjAyNWQ1NjRiZmI3Y2VkZTNiMTQzNWIxYiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.SzWdmdWMsDWcgGTxt3TabVfpp7lutCI8M6LhBCMS3zs) ](https://private-user-images.githubusercontent.com/7248/337628841-2f6baa3e-1092-4f11-866d-36f6a9d075e5.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii83MjQ4LzMzNzYyODg0MS0yZjZiYWEzZS0xMDkyLTRmMTEtODY2ZC0zNmY2YTlkMDc1ZTUuZ2lmP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDIyNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAyMjRUMDIyMDUzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MjU0ZDQ3MjAwYzM4ZDYzNWVjZTJmOTAyNDliNDM2ZGU0NzkzNDk4MjAyNWQ1NjRiZmI3Y2VkZTNiMTQzNWIxYiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.SzWdmdWMsDWcgGTxt3TabVfpp7lutCI8M6LhBCMS3zs)     [ ](https://private-user-images.githubusercontent.com/7248/337628841-2f6baa3e-1092-4f11-866d-36f6a9d075e5.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii83MjQ4LzMzNzYyODg0MS0yZjZiYWEzZS0xMDkyLTRmMTEtODY2ZC0zNmY2YTlkMDc1ZTUuZ2lmP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDIyNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAyMjRUMDIyMDUzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MjU0ZDQ3MjAwYzM4ZDYzNWVjZTJmOTAyNDliNDM2ZGU0NzkzNDk4MjAyNWQ1NjRiZmI3Y2VkZTNiMTQzNWIxYiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.SzWdmdWMsDWcgGTxt3TabVfpp7lutCI8M6LhBCMS3zs)[![](https://private-user-images.githubusercontent.com/12318111/382190237-504bbbf1-c9f7-4d83-8cc5-e9cb63c26db6.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii8xMjMxODExMS8zODIxOTAyMzctNTA0YmJiZjEtYzlmNy00ZDgzLThjYzUtZTljYjYzYzI2ZGI2LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjI0VDAyMjA1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTVkNTJkMGM0ZmVlZWQ2ZjVlY2FlOTM3ZmE2MzBlNTYyYzdlODM2NzAwNzlhZTZiMmRiMjU2ODRhOGFjNjY2Y2QmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.OyeXkuiQs_-Pg4WMHLCGVqtiHE4OYWH_ORvDGmc2PzI)](https://private-user-images.githubusercontent.com/12318111/382190237-504bbbf1-c9f7-4d83-8cc5-e9cb63c26db6.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii8xMjMxODExMS8zODIxOTAyMzctNTA0YmJiZjEtYzlmNy00ZDgzLThjYzUtZTljYjYzYzI2ZGI2LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjI0VDAyMjA1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTVkNTJkMGM0ZmVlZWQ2ZjVlY2FlOTM3ZmE2MzBlNTYyYzdlODM2NzAwNzlhZTZiMmRiMjU2ODRhOGFjNjY2Y2QmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.OyeXkuiQs_-Pg4WMHLCGVqtiHE4OYWH_ORvDGmc2PzI)[![382190237-504bbbf1-c9f7-4d83-8cc5-e9cb63c26db6.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii8xMjMxODExMS8zODIxOTAyMzctNTA0YmJiZjEtYzlmNy00ZDgzLThjYzUtZTljYjYzYzI2ZGI2LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjI0VDAyMjA1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTVkNTJkMGM0ZmVlZWQ2ZjVlY2FlOTM3ZmE2MzBlNTYyYzdlODM2NzAwNzlhZTZiMmRiMjU2ODRhOGFjNjY2Y2QmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.OyeXkuiQs\_-Pg4WMHLCGVqtiHE4OYWH\_ORvDGmc2PzI](https://private-user-images.githubusercontent.com/12318111/382190237-504bbbf1-c9f7-4d83-8cc5-e9cb63c26db6.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii8xMjMxODExMS8zODIxOTAyMzctNTA0YmJiZjEtYzlmNy00ZDgzLThjYzUtZTljYjYzYzI2ZGI2LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjI0VDAyMjA1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTVkNTJkMGM0ZmVlZWQ2ZjVlY2FlOTM3ZmE2MzBlNTYyYzdlODM2NzAwNzlhZTZiMmRiMjU2ODRhOGFjNjY2Y2QmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.OyeXkuiQs_-Pg4WMHLCGVqtiHE4OYWH_ORvDGmc2PzI) ](https://private-user-images.githubusercontent.com/12318111/382190237-504bbbf1-c9f7-4d83-8cc5-e9cb63c26db6.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii8xMjMxODExMS8zODIxOTAyMzctNTA0YmJiZjEtYzlmNy00ZDgzLThjYzUtZTljYjYzYzI2ZGI2LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjI0VDAyMjA1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTVkNTJkMGM0ZmVlZWQ2ZjVlY2FlOTM3ZmE2MzBlNTYyYzdlODM2NzAwNzlhZTZiMmRiMjU2ODRhOGFjNjY2Y2QmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.OyeXkuiQs_-Pg4WMHLCGVqtiHE4OYWH_ORvDGmc2PzI)     [](https://private-user-images.githubusercontent.com/12318111/382190237-504bbbf1-c9f7-4d83-8cc5-e9cb63c26db6.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii8xMjMxODExMS8zODIxOTAyMzctNTA0YmJiZjEtYzlmNy00ZDgzLThjYzUtZTljYjYzYzI2ZGI2LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjI0VDAyMjA1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTVkNTJkMGM0ZmVlZWQ2ZjVlY2FlOTM3ZmE2MzBlNTYyYzdlODM2NzAwNzlhZTZiMmRiMjU2ODRhOGFjNjY2Y2QmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.OyeXkuiQs_-Pg4WMHLCGVqtiHE4OYWH_ORvDGmc2PzI)

## 🔥 Latest Updates

[](#-latest-updates)

* 2025-02-05 Updates the model list of 'SILICONFLOW' and adds support for Deepseek-R1/DeepSeek-V3.
* 2025-01-26 Optimizes knowledge graph extraction and application, offering various configuration options.
* 2024-12-18 Upgrades Document Layout Analysis model in Deepdoc.
* 2024-12-04 Adds support for pagerank score in knowledge base.
* 2024-11-22 Adds more variables to Agent.
* 2024-11-01 Adds keyword extraction and related question generation to the parsed chunks to improve the accuracy of retrieval.
* 2024-08-22 Support text to SQL statements through RAG.

## 🎉 Stay Tuned

[](#-stay-tuned)

⭐️ Star our repository to stay up-to-date with exciting new features and improvements! Get instant notifications for new releases! 🌟

[![](https://private-user-images.githubusercontent.com/12318111/371996934-18c9707e-b8aa-4caf-a154-037089c105ba.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii8xMjMxODExMS8zNzE5OTY5MzQtMThjOTcwN2UtYjhhYS00Y2FmLWExNTQtMDM3MDg5YzEwNWJhLmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjI0VDAyMjA1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTM0MGJiNjYxNmQxZTc3ODAyYzBhMjg0N2FiNDljMjA1MmM2YTgyOTViODRmOTFhZWVlMDA5ZmVhYjNiNWU2NjUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.sLmsybpT0uFFSeieHV0E8wuq-PKcBBUmI5LIESqwgYw)](https://private-user-images.githubusercontent.com/12318111/371996934-18c9707e-b8aa-4caf-a154-037089c105ba.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii8xMjMxODExMS8zNzE5OTY5MzQtMThjOTcwN2UtYjhhYS00Y2FmLWExNTQtMDM3MDg5YzEwNWJhLmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjI0VDAyMjA1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTM0MGJiNjYxNmQxZTc3ODAyYzBhMjg0N2FiNDljMjA1MmM2YTgyOTViODRmOTFhZWVlMDA5ZmVhYjNiNWU2NjUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.sLmsybpT0uFFSeieHV0E8wuq-PKcBBUmI5LIESqwgYw)[![371996934-18c9707e-b8aa-4caf-a154-037089c105ba.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii8xMjMxODExMS8zNzE5OTY5MzQtMThjOTcwN2UtYjhhYS00Y2FmLWExNTQtMDM3MDg5YzEwNWJhLmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjI0VDAyMjA1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTM0MGJiNjYxNmQxZTc3ODAyYzBhMjg0N2FiNDljMjA1MmM2YTgyOTViODRmOTFhZWVlMDA5ZmVhYjNiNWU2NjUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.sLmsybpT0uFFSeieHV0E8wuq-PKcBBUmI5LIESqwgYw](https://private-user-images.githubusercontent.com/12318111/371996934-18c9707e-b8aa-4caf-a154-037089c105ba.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii8xMjMxODExMS8zNzE5OTY5MzQtMThjOTcwN2UtYjhhYS00Y2FmLWExNTQtMDM3MDg5YzEwNWJhLmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjI0VDAyMjA1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTM0MGJiNjYxNmQxZTc3ODAyYzBhMjg0N2FiNDljMjA1MmM2YTgyOTViODRmOTFhZWVlMDA5ZmVhYjNiNWU2NjUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.sLmsybpT0uFFSeieHV0E8wuq-PKcBBUmI5LIESqwgYw) ](https://private-user-images.githubusercontent.com/12318111/371996934-18c9707e-b8aa-4caf-a154-037089c105ba.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii8xMjMxODExMS8zNzE5OTY5MzQtMThjOTcwN2UtYjhhYS00Y2FmLWExNTQtMDM3MDg5YzEwNWJhLmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjI0VDAyMjA1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTM0MGJiNjYxNmQxZTc3ODAyYzBhMjg0N2FiNDljMjA1MmM2YTgyOTViODRmOTFhZWVlMDA5ZmVhYjNiNWU2NjUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.sLmsybpT0uFFSeieHV0E8wuq-PKcBBUmI5LIESqwgYw)     [](https://private-user-images.githubusercontent.com/12318111/371996934-18c9707e-b8aa-4caf-a154-037089c105ba.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii8xMjMxODExMS8zNzE5OTY5MzQtMThjOTcwN2UtYjhhYS00Y2FmLWExNTQtMDM3MDg5YzEwNWJhLmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjI0VDAyMjA1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTM0MGJiNjYxNmQxZTc3ODAyYzBhMjg0N2FiNDljMjA1MmM2YTgyOTViODRmOTFhZWVlMDA5ZmVhYjNiNWU2NjUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.sLmsybpT0uFFSeieHV0E8wuq-PKcBBUmI5LIESqwgYw)

## 🌟 Key Features

[](#-key-features)

### 🍭 **"Quality in, quality out"**

[](#-quality-in-quality-out)

* [Deep document understanding](https://github.com/infiniflow/ragflow/blob/main/deepdoc/README.md)-based knowledge extraction from unstructured data with complicated formats.
* Finds "needle in a data haystack" of literally unlimited tokens.

### 🍱 **Template-based chunking**

[](#-template-based-chunking)

* Intelligent and explainable.
* Plenty of template options to choose from.

### 🌱 **Grounded citations with reduced hallucinations**

[](#-grounded-citations-with-reduced-hallucinations)

* Visualization of text chunking to allow human intervention.
* Quick view of the key references and traceable citations to support grounded answers.

### 🍔 **Compatibility with heterogeneous data sources**

[](#-compatibility-with-heterogeneous-data-sources)

* Supports Word, slides, excel, txt, images, scanned copies, structured data, web pages, and more.

### 🛀 **Automated and effortless RAG workflow**

[](#-automated-and-effortless-rag-workflow)

* Streamlined RAG orchestration catered to both personal and large businesses.
* Configurable LLMs as well as embedding models.
* Multiple recall paired with fused re-ranking.
* Intuitive APIs for seamless integration with business.

## 🔎 System Architecture

[](#-system-architecture)

[![](https://private-user-images.githubusercontent.com/12318111/317212466-d6ac5664-c237-4200-a7c2-a4a00691b485.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii8xMjMxODExMS8zMTcyMTI0NjYtZDZhYzU2NjQtYzIzNy00MjAwLWE3YzItYTRhMDA2OTFiNDg1LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjI0VDAyMjA1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWM3YTdmM2NjNTYwZDQ5Y2NiYmY5ZWY4YTM1ZjZiNWRiNmIwZDYxMWViYTE1Njk5ZTMzMGQzNWYxMjY0NmRmNDImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.cdf1biGTpBNp7u-eqJEPtE-D7GW-0N5FRnRtX94hmyQ)](https://private-user-images.githubusercontent.com/12318111/317212466-d6ac5664-c237-4200-a7c2-a4a00691b485.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii8xMjMxODExMS8zMTcyMTI0NjYtZDZhYzU2NjQtYzIzNy00MjAwLWE3YzItYTRhMDA2OTFiNDg1LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjI0VDAyMjA1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWM3YTdmM2NjNTYwZDQ5Y2NiYmY5ZWY4YTM1ZjZiNWRiNmIwZDYxMWViYTE1Njk5ZTMzMGQzNWYxMjY0NmRmNDImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.cdf1biGTpBNp7u-eqJEPtE-D7GW-0N5FRnRtX94hmyQ)

## 🎬 Get Started

[](#-get-started)

### 📝 Prerequisites

[](#-prerequisites)

* CPU >= 4 cores

* RAM >= 16 GB

* Disk >= 50 GB

* Docker >= 24.0.0 & Docker Compose >= v2.26.1

  > If you have not installed Docker on your local machine (Windows, Mac, or Linux), see [Install Docker Engine](https://docs.docker.com/engine/install/).

### 🚀 Start up the server

[](#-start-up-the-server)

1. Ensure `vm.max_map_count` >= 262144:

   > To check the value of `vm.max_map_count`:
   >
   > ```
   > $ sysctl vm.max_map_count
   > ```
   >
   > Reset `vm.max_map_count` to a value at least 262144 if it is not.
   >
   > ```
   > # In this case, we set it to 262144:
   > $ sudo sysctl -w vm.max_map_count=262144
   > ```
   >
   > This change will be reset after a system reboot. To ensure your change remains permanent, add or update the `vm.max_map_count` value in **/etc/sysctl.conf** accordingly:
   >
   > ```
   > vm.max_map_count=262144
   > ```

2. Clone the repo:

   ```
   $ git clone https://github.com/infiniflow/ragflow.git
   ```

3. Start up the server using the pre-built Docker images:

   > The command below downloads the `v0.16.0-slim` edition of the RAGFlow Docker image. Refer to the following table for descriptions of different RAGFlow editions. To download a RAGFlow edition different from `v0.16.0-slim`, update the `RAGFLOW_IMAGE` variable accordingly in **docker/.env** before using `docker compose` to start the server. For example: set `RAGFLOW_IMAGE=infiniflow/ragflow:v0.16.0` for the full edition `v0.16.0`.

   ```
   $ cd ragflow/docker
   $ docker compose -f docker-compose.yml up -d
   ```

   | RAGFlow image tag | Image size (GB) | Has embedding models? | Stable?                  |
   | ----------------- | --------------- | --------------------- | ------------------------ |
   | v0.16.0           | ≈9              | ✔️                    | Stable release           |
   | v0.16.0-slim      | ≈2              | ❌                     | Stable release           |
   | nightly           | ≈9              | ✔️                    | *Unstable* nightly build |
   | nightly-slim      | ≈2              | ❌                     | *Unstable* nightly build |

4. Check the server status after having the server up and running:

   ```
   $ docker logs -f ragflow-server
   ```

   *The following output confirms a successful launch of the system:*

   ```
         ____   ___    ______ ______ __
        / __ \ /   |  / ____// ____// /____  _      __
       / /_/ // /| | / / __ / /_   / // __ \| | /| / /
      / _, _// ___ |/ /_/ // __/  / // /_/ /| |/ |/ /
     /_/ |_|/_/  |_|\____//_/    /_/ \____/ |__/|__/

    * Running on all addresses (0.0.0.0)
    * Running on http://127.0.0.1:9380
    * Running on http://x.x.x.x:9380
    INFO:werkzeug:Press CTRL+C to quit
   ```

   > If you skip this confirmation step and directly log in to RAGFlow, your browser may prompt a `network anormal` error because, at that moment, your RAGFlow may not be fully initialized.

5. In your web browser, enter the IP address of your server and log in to RAGFlow.

   > With the default settings, you only need to enter `http://IP_OF_YOUR_MACHINE` (**sans** port number) as the default HTTP serving port `80` can be omitted when using the default configurations.

6. In [service\_conf.yaml.template](https://github.com/infiniflow/ragflow/blob/main/docker/service_conf.yaml.template), select the desired LLM factory in `user_default_llm` and update the `API_KEY` field with the corresponding API key.

   > See [llm\_api\_key\_setup](https://ragflow.io/docs/dev/llm_api_key_setup) for more information.

   *The show is on!*

## 🔧 Configurations

[](#-configurations)

When it comes to system configurations, you will need to manage the following files:

* [.env](https://github.com/infiniflow/ragflow/blob/main/docker/.env): Keeps the fundamental setups for the system, such as `SVR_HTTP_PORT`, `MYSQL_PASSWORD`, and `MINIO_PASSWORD`.
* [service\_conf.yaml.template](https://github.com/infiniflow/ragflow/blob/main/docker/service_conf.yaml.template): Configures the back-end services. The environment variables in this file will be automatically populated when the Docker container starts. Any environment variables set within the Docker container will be available for use, allowing you to customize service behavior based on the deployment environment.
* [docker-compose.yml](https://github.com/infiniflow/ragflow/blob/main/docker/docker-compose.yml): The system relies on [docker-compose.yml](https://github.com/infiniflow/ragflow/blob/main/docker/docker-compose.yml) to start up.

> The [./docker/README](https://github.com/infiniflow/ragflow/blob/main/docker/README.md) file provides a detailed description of the environment settings and service configurations which can be used as `${ENV_VARS}` in the [service\_conf.yaml.template](https://github.com/infiniflow/ragflow/blob/main/docker/service_conf.yaml.template) file.

To update the default HTTP serving port (80), go to [docker-compose.yml](https://github.com/infiniflow/ragflow/blob/main/docker/docker-compose.yml) and change `80:80` to `<YOUR_SERVING_PORT>:80`.

Updates to the above configurations require a reboot of all containers to take effect:

> ```
> $ docker compose -f docker-compose.yml up -d
> ```

### Switch doc engine from Elasticsearch to Infinity

[](#switch-doc-engine-from-elasticsearch-to-infinity)

RAGFlow uses Elasticsearch by default for storing full text and vectors. To switch to [Infinity](https://github.com/infiniflow/infinity/), follow these steps:

1. Stop all running containers:

   ```
   $ docker compose -f docker/docker-compose.yml down -v
   ```

   Note: `-v` will delete the docker container volumes, and the existing data will be cleared.

2. Set `DOC_ENGINE` in **docker/.env** to `infinity`.

3. Start the containers:

   ```
   $ docker compose -f docker-compose.yml up -d
   ```

Warning

Switching to Infinity on a Linux/arm64 machine is not yet officially supported.

## 🔧 Build a Docker image without embedding models

[](#-build-a-docker-image-without-embedding-models)

This image is approximately 2 GB in size and relies on external LLM and embedding services.

```
git clone https://github.com/infiniflow/ragflow.git
cd ragflow/
docker build --build-arg LIGHTEN=1 -f Dockerfile -t infiniflow/ragflow:nightly-slim .
```

## 🔧 Build a Docker image including embedding models

[](#-build-a-docker-image-including-embedding-models)

This image is approximately 9 GB in size. As it includes embedding models, it relies on external LLM services only.

```
git clone https://github.com/infiniflow/ragflow.git
cd ragflow/
docker build -f Dockerfile -t infiniflow/ragflow:nightly .
```

## 🔨 Launch service from source for development

[](#-launch-service-from-source-for-development)

1. Install uv, or skip this step if it is already installed:

   ```
   pipx install uv
   ```

2. Clone the source code and install Python dependencies:

   ```
   git clone https://github.com/infiniflow/ragflow.git
   cd ragflow/
   uv sync --python 3.10 --all-extras # install RAGFlow dependent python modules
   ```

3. Launch the dependent services (MinIO, Elasticsearch, Redis, and MySQL) using Docker Compose:

   ```
   docker compose -f docker/docker-compose-base.yml up -d
   ```

   Add the following line to `/etc/hosts` to resolve all hosts specified in **docker/.env** to `127.0.0.1`:

   ```
   127.0.0.1       es01 infinity mysql minio redis
   ```

4. If you cannot access HuggingFace, set the `HF_ENDPOINT` environment variable to use a mirror site:

   ```
   export HF_ENDPOINT=https://hf-mirror.com
   ```

5. Launch backend service:

   ```
   source .venv/bin/activate
   export PYTHONPATH=$(pwd)
   bash docker/launch_backend_service.sh
   ```

6. Install frontend dependencies:

   ```
   cd web
   npm install
   ```

7. Launch frontend service:

   ```
   npm run dev
   ```

   *The following output confirms a successful launch of the system:*

   [![](https://private-user-images.githubusercontent.com/93570324/371018995-0daf462c-a24d-4496-a66f-92533534e187.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii85MzU3MDMyNC8zNzEwMTg5OTUtMGRhZjQ2MmMtYTI0ZC00NDk2LWE2NmYtOTI1MzM1MzRlMTg3LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjI0VDAyMjA1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTA3N2Y3YmMyYTNhZWFhNzgyZTg5OTMxYWY0Mzc2YTA4ZTIwN2JkZjFiMjc4MTRiODIzYzQxZjAwZTdjODJlYWImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.YaKltK2Z_a9NfjbtEH1hGMERY87boIzESv_0Cf4NJ0E)](https://private-user-images.githubusercontent.com/93570324/371018995-0daf462c-a24d-4496-a66f-92533534e187.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDAzNjM5NTMsIm5iZiI6MTc0MDM2MzY1MywicGF0aCI6Ii85MzU3MDMyNC8zNzEwMTg5OTUtMGRhZjQ2MmMtYTI0ZC00NDk2LWE2NmYtOTI1MzM1MzRlMTg3LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjI0VDAyMjA1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTA3N2Y3YmMyYTNhZWFhNzgyZTg5OTMxYWY0Mzc2YTA4ZTIwN2JkZjFiMjc4MTRiODIzYzQxZjAwZTdjODJlYWImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.YaKltK2Z_a9NfjbtEH1hGMERY87boIzESv_0Cf4NJ0E)

## 📚 Documentation

[](#-documentation)

* [Quickstart](https://ragflow.io/docs/dev/)
* [User guide](https://ragflow.io/docs/dev/category/guides)
* [References](https://ragflow.io/docs/dev/category/references)
* [FAQ](https://ragflow.io/docs/dev/faq)

## 📜 Roadmap

[](#-roadmap)

See the [RAGFlow Roadmap 2025](https://github.com/infiniflow/ragflow/issues/4214)

## 🏄 Community

[](#-community)

* [Discord](https://discord.gg/4XxujFgUN7)
* [Twitter](https://twitter.com/infiniflowai)
* [GitHub Discussions](https://github.com/orgs/infiniflow/discussions)

## 🙌 Contributing

[](#-contributing)

RAGFlow flourishes via open-source collaboration. In this spirit, we embrace diverse contributions from the community. If you would like to be a part, review our [Contribution Guidelines](https://github.com/infiniflow/ragflow/blob/main/CONTRIBUTING.md) first.


