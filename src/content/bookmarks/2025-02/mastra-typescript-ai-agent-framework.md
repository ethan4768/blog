---
title: "Mastra：一个快速构建AI应用的TypeScript框架"
slug: mastra-typescript-ai-agent-framework
description: |
  Mastra是一个高效的TypeScript框架，旨在帮助开发者快速构建AI应用。它支持多种功能，包括工作流、智能代理、检索增强生成（RAG）以及与多种LLM供应商的集成。通过Mastra，您可以轻松搭建和测试您的AI项目。
tags: 
  - AI
  - dev
  - tool
  - typescript
pubDatetime: 2025-02-24T10:23:04+08:00
ogImage: https://opengraph.githubassets.com/54be9b3cb53639840836e80534ec1f8a5babf53bb6cc9cd546b2d97b7b42dbf2/mastra-ai/mastra
---

[原文链接](https://github.com/mastra-ai/mastra)

---

# Mastra [![Project Status: Beta](https://camo.githubusercontent.com/fc20203462aac126108c45996135a27581fc3819a1134b59d1943e695500b232/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f626574612d7374617475732d626c7565)](https://camo.githubusercontent.com/fc20203462aac126108c45996135a27581fc3819a1134b59d1943e695500b232/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f626574612d7374617475732d626c7565) [![Project Status: Alpha](https://camo.githubusercontent.com/eba86d8b38cba382489c0de325f7b9d4dac9848aa2793dc187d05a8cc9ba609b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f59253230436f6d62696e61746f722d5732352d6f72616e67653f7374796c653d666c61742d737175617265)](https://camo.githubusercontent.com/eba86d8b38cba382489c0de325f7b9d4dac9848aa2793dc187d05a8cc9ba609b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f59253230436f6d62696e61746f722d5732352d6f72616e67653f7374796c653d666c61742d737175617265)

[](#mastra--)

Mastra is an opinionated Typescript framework that helps you build AI applications and features quickly. It gives you the set of primitives you need: workflows, agents, RAG, integrations and evals. You can run Mastra on your local machine, or deploy to a serverless cloud.

The main Mastra features are:

| Features                                                      | Description                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| LLM Models                                                    | Mastra uses the [Vercel AI SDK](https://sdk.vercel.ai/docs/introduction) for model routing, providing a unified interface to interact with any LLM provider including OpenAI, Anthropic, and Google Gemini. You can choose the specific model and provider, and decide whether to stream the response. |
| [Agents](https://mastra.ai/docs/agents/00-overview)           | Agents are systems where the language model chooses a sequence of actions. In Mastra, agents provide LLM models with tools, workflows, and synced data. Agents can call your own functions or APIs of third-party integrations and access knowledge bases you build.                                   |
| [Tools](https://mastra.ai/docs/agents/02-adding-tools)        | Tools are typed functions that can be executed by agents or workflows, with built-in integration access and parameter validation. Each tool has a schema that defines its inputs, an executor function that implements its logic, and access to configured integrations.                               |
| [Workflows](https://mastra.ai/docs/workflows/00-overview)     | Workflows are durable graph-based state machines. They have loops, branching, wait for human input, embed other workflows, do error handling, retries, parsing and so on. They can be built in code or with a visual editor. Each step in a workflow has built-in OpenTelemetry tracing.               |
| [RAG](https://mastra.ai/docs/rag/overview)                    | Retrieval-augemented generation (RAG) lets you construct a knowledge base for agents. RAG is an ETL pipeline with specific querying techniques, including chunking, embedding, and vector search.                                                                                                      |
| [Integrations](https://mastra.ai/docs/local-dev/integrations) | In Mastra, integrations are auto-generated, type-safe API clients for third-party services that can be used as tools for agents or steps in workflows.                                                                                                                                                 |
| [Evals](https://mastra.ai/docs/08-running-evals)              | Evals are automated tests that evaluate LLM outputs using model-graded, rule-based, and statistical methods. Each eval returns a normalized score between 0-1 that can be logged and compared. Evals can be customized with your own prompts and scoring functions.                                    |

## Quick Start

[](#quick-start)

### Prerequisites

[](#prerequisites)

* Node.js (v20.0+)

## Get an LLM provider API key

[](#get-an-llm-provider-api-key)

If you don't have an API key for an LLM provider, you can get one from the following services:

* [OpenAI](https://platform.openai.com/)
* [Anthropic](https://console.anthropic.com/settings/keys)
* [Google Gemini](https://ai.google.dev/gemini-api/docs)

If you don't have an account with these providers, you can sign up and get an API key. Anthropic require a credit card to get an API key. Some OpenAI models and Gemini do not and have a generous free tier for its API.

## Create a new project

[](#create-a-new-project)

The easiest way to get started with Mastra is by using `create-mastra`. This CLI tool enables you to quickly start building a new Mastra application, with everything set up for you.

```
npx create-mastra@latest
```

### Run the script

[](#run-the-script)

Finally, run `mastra dev` to open the Mastra playground.

```
npm run dev
```

If you're using Anthropic, set the `ANTHROPIC_API_KEY`. If you're using Gemini, set the `GOOGLE_GENERATIVE_AI_API_KEY`.

## Contributing

[](#contributing)

Looking to contribute? All types of help are appreciated, from coding to testing and feature specification.

If you are a developer and would like to contribute with code, please open an issue to discuss before opening a Pull Request.

Information about the project setup can be found in the [development documentation](https://github.com/mastra-ai/mastra/blob/main/DEVELOPMENT.md)

## Support

[](#support)

We have an [open community Discord](https://discord.gg/BTYqqHKUrf). Come and say hello and let us know if you have any questions or need any help getting things running.

It's also super helpful if you leave the project a star here at the [top of the page](https://github.com/mastra-ai/mastra)


