---
title: "Tencent WeKnora：基于 LLM 的深度文档理解和语义检索框架"
slug: weknora-llm-document-understanding
description: |
  Tencent WeKnora 是一个基于 LLM 的框架，旨在实现深度文档理解和语义检索。它结合了多模态预处理、智能检索与 RAG（检索增强生成）范式，实现高质量、上下文感知的答案。可广泛应用于知识管理、学术研究、医疗辅助等多个场景。
tags: 
  - AI
  - RAG
pubDatetime: 2025-09-12T17:01:46+08:00
ogImage: https://opengraph.githubassets.com/1ae245e25e75b5d0bd5bd06b87568cefda46e4c38764086fd605051ab2f187ff/Tencent/WeKnora
---

[原文链接](https://github.com/Tencent/WeKnora)

---

![WeKnora Logo](/Tencent/WeKnora/raw/main/docs/images/logo.png)

[![官方网站](https://camo.githubusercontent.com/75b7685deff3f43b78ae75970ca48416efb745beafbf35ae5655d74c727793bf/68747470733a2f2f696d672e736869656c64732e696f2f62616467652fe5ae98e696b9e7bd91e7ab992d57654b6e6f72612d346536623939) ](https://weknora.weixin.qq.com)[![微信对话开放平台](https://camo.githubusercontent.com/7eac94e93bd468bf81c08068c9acc6f2090efca633386fff93ab999f063764b8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652fe5beaee4bfa1e5afb9e8af9de5bc80e694bee5b9b3e58fb02d356163373235) ](https://chatbot.weixin.qq.com)[![License](https://camo.githubusercontent.com/ed96d6424f84d5b0243aa4f9a638efe236de3c346b18bcda36def9b8867200c8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d6666666666663f6c6162656c436f6c6f723d64346561663726636f6c6f723d326536636334) ](https://github.com/Tencent/WeKnora/blob/main/LICENSE)[![Version](https://camo.githubusercontent.com/9b357c932113af589b21ed212f4706f29f7b0f461d3572783ca3658330b7cef4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f76657273696f6e2d302e312e302d3265366363343f6c6162656c436f6c6f723d643465616637)](https://github.com/Tencent/WeKnora/blob/main/CHANGELOG.md)

\| **English** | [**简体中文**](https://github.com/Tencent/WeKnora/blob/main/README_CN.md) | [**日本語**](https://github.com/Tencent/WeKnora/blob/main/README_JA.md) |

#### [Overview](#-overview) • [Architecture](#-architecture) • [Key Features](#-key-features) • [Getting Started](#-getting-started) • [API Reference](#-api-reference) • [Developer Guide](#-developer-guide)

[](#overview--architecture--key-features--getting-started--api-reference--developer-guide--)

# 💡 WeKnora - LLM-Powered Document Understanding & Retrieval Framework

[](#-weknora---llm-powered-document-understanding--retrieval-framework)

## 📌 Overview

[](#-overview)

[**WeKnora**](https://weknora.weixin.qq.com) is an LLM-powered framework designed for deep document understanding and semantic retrieval, especially for handling complex, heterogeneous documents.

It adopts a modular architecture that combines multimodal preprocessing, semantic vector indexing, intelligent retrieval, and large language model inference. At its core, WeKnora follows the **RAG (Retrieval-Augmented Generation)** paradigm, enabling high-quality, context-aware answers by combining relevant document chunks with model reasoning.

**Website:** <https://weknora.weixin.qq.com>

## 🏗️ Architecture

[](#️-architecture)

[![weknora-pipeline.png](/Tencent/WeKnora/raw/main/docs/images/pipeline.jpg)](https://github.com/Tencent/WeKnora/blob/main/docs/images/pipeline.jpg)

WeKnora employs a modern modular design to build a complete document understanding and retrieval pipeline. The system primarily includes document parsing, vector processing, retrieval engine, and large model inference as core modules, with each component being flexibly configurable and extendable.

## 🎯 Key Features

[](#-key-features)

* **🔍 Precise Understanding**: Structured content extraction from PDFs, Word documents, images and more into unified semantic views
* **🧠 Intelligent Reasoning**: Leverages LLMs to understand document context and user intent for accurate Q\&A and multi-turn conversations
* **🔧 Flexible Extension**: All components from parsing and embedding to retrieval and generation are decoupled for easy customization
* **⚡ Efficient Retrieval**: Hybrid retrieval strategies combining keywords, vectors, and knowledge graphs
* **🎯 User-Friendly**: Intuitive web interface and standardized APIs for zero technical barriers
* **🔒 Secure & Controlled**: Support for local deployment and private cloud, ensuring complete data sovereignty

## 📊 Application Scenarios

[](#-application-scenarios)

| Scenario                            | Applications                                                               | Core Value                                                    |
| ----------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Enterprise Knowledge Management** | Internal document retrieval, policy Q\&A, operation manual search          | Improve knowledge discovery efficiency, reduce training costs |
| **Academic Research Analysis**      | Paper retrieval, research report analysis, scholarly material organization | Accelerate literature review, assist research decisions       |
| **Product Technical Support**       | Product manual Q\&A, technical documentation search, troubleshooting       | Enhance customer service quality, reduce support burden       |
| **Legal & Compliance Review**       | Contract clause retrieval, regulatory policy search, case analysis         | Improve compliance efficiency, reduce legal risks             |
| **Medical Knowledge Assistance**    | Medical literature retrieval, treatment guideline search, case analysis    | Support clinical decisions, improve diagnosis quality         |

## 🧩 Feature Matrix

[](#-feature-matrix)

| Module                | Support                                                                       | Description                                                                                                                        |
| --------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Document Formats      | ✅ PDF / Word / Txt / Markdown / Images (with OCR / Caption)                   | Support for structured and unstructured documents with text extraction from images                                                 |
| Embedding Models      | ✅ Local models, BGE / GTE APIs, etc.                                          | Customizable embedding models, compatible with local deployment and cloud vector generation APIs                                   |
| Vector DB Integration | ✅ PostgreSQL (pgvector), Elasticsearch                                        | Support for mainstream vector index backends, flexible switching for different retrieval scenarios                                 |
| Retrieval Strategies  | ✅ BM25 / Dense Retrieval / GraphRAG                                           | Support for sparse/dense recall and knowledge graph-enhanced retrieval with customizable retrieve-rerank-generate pipelines        |
| LLM Integration       | ✅ Support for Qwen, DeepSeek, etc., with thinking/non-thinking mode switching | Compatible with local models (e.g., via Ollama) or external API services with flexible inference configuration                     |
| QA Capabilities       | ✅ Context-aware, multi-turn dialogue, prompt templates                        | Support for complex semantic modeling, instruction control and chain-of-thought Q\&A with configurable prompts and context windows |
| E2E Testing           | ✅ Retrieval+generation process visualization and metric evaluation            | End-to-end testing tools for evaluating recall hit rates, answer coverage, BLEU/ROUGE and other metrics                            |
| Deployment Modes      | ✅ Support for local deployment / Docker images                                | Meets private, offline deployment and flexible operation requirements                                                              |
| User Interfaces       | ✅ Web UI + RESTful API                                                        | Interactive interface and standard API endpoints, suitable for both developers and business users                                  |

## 🚀 Getting Started

[](#-getting-started)

### 🛠 Prerequisites

[](#-prerequisites)

Make sure the following tools are installed on your system:

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* [Git](https://git-scm.com/)

### 📦 Installation

[](#-installation)

#### ① Clone the repository

[](#-clone-the-repository)

```
# Clone the main repository
git clone https://github.com/Tencent/WeKnora.git
cd WeKnora
```

#### ② Configure environment variables

[](#-configure-environment-variables)

```
# Copy example env file
cp .env.example .env

# Edit .env and set required values
# All variables are documented in the .env.example comments
```

#### ③ Start the services

[](#-start-the-services)

```
# Start all services (Ollama + backend containers)
./scripts/start_all.sh
# Or
make start-all
```

#### ③ Start the services (backup)

[](#-start-the-services-backup)

```
# Start ollama services (Optional)
ollama serve > /dev/null 2>&1 &

# Start the service
docker compose up -d
```

#### ④ Stop the services

[](#-stop-the-services)

```
./scripts/start_all.sh --stop
# Or
make stop-all
```

### 🌐 Access Services

[](#-access-services)

Once started, services will be available at:

* Web UI: `http://localhost`
* Backend API: `http://localhost:8080`
* Jaeger Tracing: `http://localhost:16686`

### 🔌 Using WeChat Dialog Open Platform

[](#-using-wechat-dialog-open-platform)

WeKnora serves as the core technology framework for the [WeChat Dialog Open Platform](https://chatbot.weixin.qq.com), providing a more convenient usage approach:

* **Zero-code Deployment**: Simply upload knowledge to quickly deploy intelligent Q\&A services within the WeChat ecosystem, achieving an "ask and answer" experience
* **Efficient Question Management**: Support for categorized management of high-frequency questions, with rich data tools to ensure accurate, reliable, and easily maintainable answers
* **WeChat Ecosystem Integration**: Through the WeChat Dialog Open Platform, WeKnora's intelligent Q\&A capabilities can be seamlessly integrated into WeChat Official Accounts, Mini Programs, and other WeChat scenarios, enhancing user interaction experiences

### 🔗 Access WeKnora via MCP Server

[](#-access-weknora-via-mcp-server)

#### 1️⃣ Clone the repository

[](#1️⃣-clone-the-repository)

```
git clone https://github.com/Tencent/WeKnora
```

#### 2️⃣ Configure MCP Server

[](#2️⃣-configure-mcp-server)

Configure the MCP client to connect to the server:

```
{
  "mcpServers": {
    "weknora": {
      "args": [
        "path/to/WeKnora/mcp-server/run_server.py"
      ],
      "command": "python",
      "env":{
        "WEKNORA_API_KEY":"Enter your WeKnora instance, open developer tools, check the request header x-api-key starting with sk",
        "WEKNORA_BASE_URL":"http(s)://your-weknora-address/api/v1"
      }
    }
  }
}
```

Run directly using stdio command:

```
pip install weknora-mcp-server
python -m weknora-mcp-server
```

## 🔧 Initialization Configuration Guide

[](#-initialization-configuration-guide)

To help users quickly configure various models and reduce trial-and-error costs, we've improved the original configuration file initialization method by adding a Web UI interface for model configuration. Before using, please ensure the code is updated to the latest version. The specific steps are as follows: If this is your first time using this project, you can skip steps ①② and go directly to steps ③④.

### ① Stop the services

[](#-stop-the-services-1)

```
./scripts/start_all.sh --stop
```

### ② Clear existing data tables (recommended when no important data exists)

[](#-clear-existing-data-tables-recommended-when-no-important-data-exists)

```
make clean-db
```

### ③ Compile and start services

[](#-compile-and-start-services)

```
./scripts/start_all.sh
```

### ④ Access Web UI

[](#-access-web-ui)

<http://localhost>

On first access, it will automatically redirect to the initialization configuration page. After configuration is complete, it will automatically redirect to the knowledge base page. Please follow the page instructions to complete model configuration.

[![Configuration Page](/Tencent/WeKnora/raw/main/docs/images/config.png)](https://github.com/Tencent/WeKnora/blob/main/docs/images/config.png)

## 📱 Interface Showcase

[](#-interface-showcase)

### Web UI Interface

[](#web-ui-interface)

|                                                                                                                                                                                     |                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Knowledge Upload** [![Knowledge Upload Interface](/Tencent/WeKnora/raw/main/docs/images/knowledges.png)](https://github.com/Tencent/WeKnora/blob/main/docs/images/knowledges.png) | **Q\&A Entry** [![Q\&A Entry Interface](/Tencent/WeKnora/raw/main/docs/images/qa.png)](https://github.com/Tencent/WeKnora/blob/main/docs/images/qa.png) |
| **Rich Text & Image Responses** [![Rich Answer Interface](/Tencent/WeKnora/raw/main/docs/images/answer.png)](https://github.com/Tencent/WeKnora/blob/main/docs/images/answer.png)   |                                                                                                                                                         |

**Knowledge Base Management:** Support for dragging and dropping various documents, automatically identifying document structures and extracting core knowledge to establish indexes. The system clearly displays processing progress and document status, achieving efficient knowledge base management.

### Document Knowledge Graph

[](#document-knowledge-graph)

|                                                                                                                                                    |                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [![Knowledge Graph View 1](/Tencent/WeKnora/raw/main/docs/images/graph2.png)](https://github.com/Tencent/WeKnora/blob/main/docs/images/graph2.png) | [![Knowledge Graph View 2](/Tencent/WeKnora/raw/main/docs/images/graph1.png)](https://github.com/Tencent/WeKnora/blob/main/docs/images/graph1.png) |

WeKnora supports transforming documents into knowledge graphs, displaying the relationships between different sections of the documents. Once the knowledge graph feature is enabled, the system analyzes and constructs an internal semantic association network that not only helps users understand document content but also provides structured support for indexing and retrieval, enhancing the relevance and breadth of search results.

### MCP Server Integration Effects

[](#mcp-server-integration-effects)

[![MCP Server Integration Demo](https://private-user-images.githubusercontent.com/111996670/486508870-09111ec8-0489-415c-969d-aa3835778e14.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTc2Njc5NzksIm5iZiI6MTc1NzY2NzY3OSwicGF0aCI6Ii8xMTE5OTY2NzAvNDg2NTA4ODcwLTA5MTExZWM4LTA0ODktNDE1Yy05NjlkLWFhMzgzNTc3OGUxNC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwOTEyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDkxMlQwOTAxMTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03M2NmNzEwOGQyZWVkZDliZGMwMTM5ZmFmMGY2MzJiMDhiMmEzMzI5Y2UyZDUyMWQ3MWI4OGYxZDg1Y2NmYjIyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Yh_55C7H0uzQFSaMKzOVUnZ5pLzfl25fvIxuJUkxqiE)](https://private-user-images.githubusercontent.com/111996670/486508870-09111ec8-0489-415c-969d-aa3835778e14.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTc2Njc5NzksIm5iZiI6MTc1NzY2NzY3OSwicGF0aCI6Ii8xMTE5OTY2NzAvNDg2NTA4ODcwLTA5MTExZWM4LTA0ODktNDE1Yy05NjlkLWFhMzgzNTc3OGUxNC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwOTEyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDkxMlQwOTAxMTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03M2NmNzEwOGQyZWVkZDliZGMwMTM5ZmFmMGY2MzJiMDhiMmEzMzI5Y2UyZDUyMWQ3MWI4OGYxZDg1Y2NmYjIyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Yh_55C7H0uzQFSaMKzOVUnZ5pLzfl25fvIxuJUkxqiE)

## 📘 API Reference

[](#-api-reference)

Troubleshooting FAQ: [Troubleshooting FAQ](https://github.com/Tencent/WeKnora/blob/main/docs/QA.md)

Detailed API documentation is available at: [API Docs](https://github.com/Tencent/WeKnora/blob/main/docs/API.md)

## 🧭 Developer Guide

[](#-developer-guide)

### 📁 Directory Structure

[](#-directory-structure)

```
WeKnora/
├── cmd/         # Main entry point
├── internal/    # Core business logic
├── config/      # Configuration files
├── migrations/  # DB migration scripts
├── scripts/     # Shell scripts
├── services/    # Microservice logic
├── frontend/    # Frontend app
└── docs/        # Project documentation
```

### 🔧 Common Commands

[](#-common-commands)

```
# Wipe all data from DB (use with caution)
make clean-db
```

## 🤝 Contributing

[](#-contributing)

We welcome community contributions! For suggestions, bugs, or feature requests, please submit an [Issue](https://github.com/Tencent/WeKnora/issues) or directly create a Pull Request.

### 🎯 How to Contribute

[](#-how-to-contribute)

* 🐛 **Bug Fixes**: Discover and fix system defects
* ✨ **New Features**: Propose and implement new capabilities
* 📚 **Documentation**: Improve project documentation
* 🧪 **Test Cases**: Write unit and integration tests
* 🎨 **UI/UX Enhancements**: Improve user interface and experience

### 📋 Contribution Process

[](#-contribution-process)

1. **Fork the project** to your GitHub account
2. **Create a feature branch** `git checkout -b feature/amazing-feature`
3. **Commit changes** `git commit -m 'Add amazing feature'`
4. **Push branch** `git push origin feature/amazing-feature`
5. **Create a Pull Request** with detailed description of changes

### 🎨 Code Standards

[](#-code-standards)

* Follow [Go Code Review Comments](https://github.com/golang/go/wiki/CodeReviewComments)
* Format code using `gofmt`
* Add necessary unit tests
* Update relevant documentation

### 📝 Commit Guidelines

[](#-commit-guidelines)

Use [Conventional Commits](https://www.conventionalcommits.org/) standard:

```
feat: Add document batch upload functionality
fix: Resolve vector retrieval precision issue
docs: Update API documentation
test: Add retrieval engine test cases
refactor: Restructure document parsing module
```

## 📄 License

[](#-license)

This project is licensed under the [MIT License](https://github.com/Tencent/WeKnora/blob/main/LICENSE). You are free to use, modify, and distribute the code with proper attribution.


