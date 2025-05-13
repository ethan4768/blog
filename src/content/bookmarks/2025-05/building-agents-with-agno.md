---
title: "Agno: 轻量级智能代理构建库，具备记忆、知识和推理能力"
slug: building-agents-with-agno
description: |
  Agno 是一款轻量级的库，旨在帮助开发者构建具备记忆、知识和推理的智能代理。它支持多模态输入，提供丰富的 API 和可视化功能，让创建复杂项目更为便捷和高效。
tags: 
  - AI
  - dev
  - tool
  - reasoning
  - multimodal
pubDatetime: 2025-05-13T10:00:00+08:00
ogImage: https://opengraph.githubassets.com/049b6fd2dd759f7f95f9387b279f3fb5f4a9fe154e1a2ef8c81f4da8f33b5835/agno-agi/agno
---

[原文链接](https://github.com/agno-agi/agno)

---

[![Agno](https://camo.githubusercontent.com/3fd5a9a03ec16da77b97a372a8cea9193dd6f1c30aba8f3f7222c1cf30c7e012/68747470733a2f2f61676e6f2d7075626c69632e73332e75732d656173742d312e616d617a6f6e6177732e636f6d2f6173736574732f6c6f676f2d6c696768742e737667)](https://docs.agno.com)

[📚 Documentation](https://docs.agno.com)  |  [💡 Examples](https://docs.agno.com/examples/introduction)  |  [🌟 Star Us](https://github.com/agno-agi/agno/stargazers)

## Introduction

[](#introduction)

[Agno](https://docs.agno.com) is a lightweight library for building Agents with memory, knowledge, tools and reasoning.

Developers use Agno to build Reasoning Agents, Multimodal Agents, Teams of Agents and Agentic Workflows. Agno also provides a beautiful UI to chat with your Agents, pre-built FastAPI routes to serve your Agents and tools to monitor and evaluate their performance.

Here's an Agent that writes a report on a stock, reasoning through each step:

```
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=Claude(id="claude-3-7-sonnet-latest"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True),
    ],
    instructions=[
        "Use tables to display data",
        "Only output the report, no other text",
    ],
    markdown=True,
)
agent.print_response("Write a report on NVDA", stream=True, show_full_reasoning=True, stream_intermediate_steps=True)
```

reasoning\_finance\_agent.mp4

[](https://private-user-images.githubusercontent.com/22579644/431624338-bbb99955-9848-49a9-9732-3e19d77b2ff8.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDcxMDE4NzEsIm5iZiI6MTc0NzEwMTU3MSwicGF0aCI6Ii8yMjU3OTY0NC80MzE2MjQzMzgtYmJiOTk5NTUtOTg0OC00OWE5LTk3MzItM2UxOWQ3N2IyZmY4Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MTMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTEzVDAxNTkzMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWIxZmE4NDgyM2QxODNkMzM4MjQxNWM2ZGEzM2NlZDg2MDg3ZTVjYjljYmRlMWFlNjAyMTdmNTk3NmVmYWY2MDMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.kWZq9FGWF62l1eoDdqFfi4GVSJIzvY20n8Yc3iRUF2c)

## Key features

[](#key-features)

Agno is simple, fast and model-agnostic. Here are some key features:

* **Model Agnostic**: Agno Agents can connect to 23+ model providers, no lock-in.
* **Lightning Fast**: - **Lightning Fast**: Agents instantiate in **\~3μs** and use **\~5Kib** memory on average (see [performance](#performance) for more details).
* **Reasoning is a first class citizen**: Make your Agents "think" and "analyze" using Reasoning Models, `ReasoningTools` or our custom `chain-of-thought` approach.
* **Natively Multi Modal**: Agno Agents are natively multi modal, they can take in text, image, audio and video and generate text, image, audio and video as output.
* **Advanced Multi Agent Architecture**: Agno provides an industry leading multi-agent architecture (**Agent Teams**) with 3 different modes: `route`, `collaborate` and `coordinate`.
* **Agentic Search built-in**: Give your Agents the ability to search for information at runtime using one of 20+ vector databases. Get access to state-of-the-art Agentic RAG that uses hybrid search with re-ranking. **Fully async and highly performant.**
* **Long-term Memory & Session Storage**: Agno provides plug-n-play `Storage` & `Memory` drivers that give your Agents long-term memory and session storage.
* **Pre-built FastAPI Routes**: Agno provides pre-built FastAPI routes to serve your Agents, Teams and Workflows.
* **Structured Outputs**: Agno Agents can return fully-typed responses using model provided structured outputs or `json_mode`.
* **Monitoring**: Monitor agent sessions and performance in real-time on [agno.com](https://app.agno.com).

## Building Agents with Agno

[](#building-agents-with-agno)

If you're new to Agno, start by building your [first Agent](https://docs.agno.com/introduction/agents), chat with it on the [playground](https://docs.agno.com/introduction/playground) and finally, monitor it on [agno.com](https://docs.agno.com/introduction/monitoring).

After that, checkout the [Examples Gallery](https://docs.agno.com/examples) and build real-world applications with Agno.

## Installation

[](#installation)

```
pip install -U agno
```

## What are Agents?

[](#what-are-agents)

**Agents** are AI programs that operate autonomously.

* The core of an Agent is a model, tools and instructions.
* Agents also have **memory**, **knowledge**, **storage** and the ability to **reason**.

Read more about each of these in the [docs](https://docs.agno.com/introduction/agents#what-are-agents%3F).

> Let's build a few Agents to see how they work.

## Example - Reasoning Agent

[](#example---reasoning-agent)

Let's start with a Reasoning Agent so we get a sense of Agno's capabilities.

Save this code to a file: `reasoning_agent.py`.

```
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=Claude(id="claude-3-7-sonnet-latest"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        ),
    ],
    instructions=[
        "Use tables to display data",
        "Only output the report, no other text",
    ],
    markdown=True,
)
agent.print_response(
    "Write a report on NVDA",
    stream=True,
    show_full_reasoning=True,
    stream_intermediate_steps=True,
)
```

Then create a virtual environment, install dependencies, export your `ANTHROPIC_API_KEY` and run the agent.

```
uv venv --python 3.12
source .venv/bin/activate

uv pip install agno anthropic yfinance

export ANTHROPIC_API_KEY=sk-ant-api03-xxxx

python reasoning_agent.py
```

We can see the Agent is reasoning through the task, using the `ReasoningTools` and `YFinanceTools` to gather information. This is how the output looks like:

reasoning\_finance\_agent.mp4

[](https://private-user-images.githubusercontent.com/22579644/431624338-bbb99955-9848-49a9-9732-3e19d77b2ff8.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDcxMDE4NzEsIm5iZiI6MTc0NzEwMTU3MSwicGF0aCI6Ii8yMjU3OTY0NC80MzE2MjQzMzgtYmJiOTk5NTUtOTg0OC00OWE5LTk3MzItM2UxOWQ3N2IyZmY4Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MTMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTEzVDAxNTkzMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWIxZmE4NDgyM2QxODNkMzM4MjQxNWM2ZGEzM2NlZDg2MDg3ZTVjYjljYmRlMWFlNjAyMTdmNTk3NmVmYWY2MDMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.kWZq9FGWF62l1eoDdqFfi4GVSJIzvY20n8Yc3iRUF2c)

> Now let's walk through the simple -> tools -> knowledge -> teams of agents flow.

## Example - Basic Agent

[](#example---basic-agent)

The simplest Agent is just an inference task, no tools, no memory, no knowledge.

```
from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    markdown=True
)
agent.print_response("Tell me about a breaking news story from New York.", stream=True)
```

To run the agent, install dependencies and export your `OPENAI_API_KEY`.

```
pip install agno openai

export OPENAI_API_KEY=sk-xxxx

python basic_agent.py
```

[View this example in the cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/getting_started/01_basic_agent.py)

## Example - Agent with tools

[](#example---agent-with-tools)

This basic agent will obviously make up a story, lets give it a tool to search the web.

```
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)
agent.print_response("Tell me about a breaking news story from New York.", stream=True)
```

Install dependencies and run the Agent:

```
pip install duckduckgo-search

python agent_with_tools.py
```

Now you should see a much more relevant result.

[View this example in the cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/getting_started/02_agent_with_tools.py)

## Example - Agent with knowledge

[](#example---agent-with-knowledge)

Agents can store knowledge in a vector database and use it for RAG or dynamic few-shot learning.

**Agno agents use Agentic RAG** by default, which means they will search their knowledge base for the specific information they need to achieve their task.

```
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a Thai cuisine expert!",
    instructions=[
        "Search your knowledge base for Thai recipes.",
        "If the question is better suited for the web, search the web to fill in gaps.",
        "Prefer the information in your knowledge base over the web results."
    ],
    knowledge=PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="recipes",
            search_type=SearchType.hybrid,
            embedder=OpenAIEmbedder(id="text-embedding-3-small"),
        ),
    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

# Comment out after the knowledge base is loaded
if agent.knowledge is not None:
    agent.knowledge.load()

agent.print_response("How do I make chicken and galangal in coconut milk soup", stream=True)
agent.print_response("What is the history of Thai curry?", stream=True)
```

Install dependencies and run the Agent:

```
pip install lancedb tantivy pypdf duckduckgo-search

python agent_with_knowledge.py
```

[View this example in the cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/getting_started/03_agent_with_knowledge.py)

## Example - Multi Agent Teams

[](#example---multi-agent-teams)

Agents work best when they have a singular purpose, a narrow scope and a small number of tools. When the number of tools grows beyond what the language model can handle or the tools belong to different categories, use a team of agents to spread the load.

```
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.team import Team

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions="Use tables to display data",
    show_tool_calls=True,
    markdown=True,
)

agent_team = Team(
    mode="coordinate",
    members=[web_agent, finance_agent],
    model=OpenAIChat(id="gpt-4o"),
    success_criteria="A comprehensive financial news report with clear sections and data-driven insights.",
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("What's the market outlook and financial performance of AI semiconductor companies?", stream=True)
```

Install dependencies and run the Agent team:

```
pip install duckduckgo-search yfinance

python agent_team.py
```

[View this example in the cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/getting_started/05_agent_team.py)

## 🚨 Global Agent Hackathon! 🚨

[](#-global-agent-hackathon-)

We're thrilled to announce a month long, open source AI Agent Hackathon — open to all builders and dreamers working on agents, RAG, tool use, and multi-agent systems.

### 💰 Build something extordinary, win up to $20,000 in cash

[](#-build-something-extordinary-win-up-to-20000-in-cash)

We're giving away $20,000 in prizes for the most ambitious Agent projects

* 🏅 10 winners: $300 each
* 🥉 10 winners: $500 each
* 🥈 5 winners: $1,000 each
* 🥇 1 winner: $2,000
* 🏆 GRAND PRIZE: $5,000 🏆

> Follow this [post](https://www.agno.com/blog/agent-hackathon-april-2025) for more details and updates

### 🤝 Want to partner or judge?

[](#-want-to-partner-or-judge)

If you're building in the AI Agent space, or want to help shape the next generation of Agent builders - we'd love to work with you.

Reach out to <support@agno.com> to get involved.

## Performance

[](#performance)

At Agno, we're obsessed with performance. Why? because even simple AI workflows can spawn thousands of Agents to achieve their goals. Scale that to a modest number of users and performance becomes a bottleneck. Agno is designed to power high performance agentic systems:

* Agent instantiation: \~3μs on average
* Memory footprint: \~6.5Kib on average

> Tested on an Apple M4 Mackbook Pro.

While an Agent's run-time is bottlenecked by inference, we must do everything possible to minimize execution time, reduce memory usage, and parallelize tool calls. These numbers may seem trivial at first, but our experience shows that they add up even at a reasonably small scale.

### Instantiation time

[](#instantiation-time)

Let's measure the time it takes for an Agent with 1 tool to start up. We'll run the evaluation 1000 times to get a baseline measurement.

You should run the evaluation yourself on your own machine, please, do not take these results at face value.

```
# Setup virtual environment
./scripts/perf_setup.sh
source .venvs/perfenv/bin/activate
# OR Install dependencies manually
# pip install openai agno langgraph langchain_openai

# Agno
python evals/performance/instantiation_with_tool.py

# LangGraph
python evals/performance/other/langgraph_instantiation.py
```

> The following evaluation is run on an Apple M4 Mackbook Pro. It also runs as a Github action on this repo.

LangGraph is on the right, **let's start it first and give it a head start**.

Agno is on the left, notice how it finishes before LangGraph gets 1/2 way through the runtime measurement, and hasn't even started the memory measurement. That's how fast Agno is.

agno\_vs\_langgraph\_perf.mp4

[](https://private-user-images.githubusercontent.com/22579644/407806244-ba466d45-75dd-45ac-917b-0a56c5742e23.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDcxMDE4NzEsIm5iZiI6MTc0NzEwMTU3MSwicGF0aCI6Ii8yMjU3OTY0NC80MDc4MDYyNDQtYmE0NjZkNDUtNzVkZC00NWFjLTkxN2ItMGE1NmM1NzQyZTIzLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MTMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTEzVDAxNTkzMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTU4OTg5YjUwYmUzM2U4OGY3M2YxM2NlNWE4NzUyNmM1NzViYmU1ODdkZWNhNDI2YjgyYjY4ZDk5YWU3YWJjOTImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.IwUnRjIpHg312k9-j9ZBXnvKE91AFnKHh9ynXOxc0JE)

### Memory usage

[](#memory-usage)

To measure memory usage, we use the `tracemalloc` library. We first calculate a baseline memory usage by running an empty function, then run the Agent 1000x times and calculate the difference. This gives a (reasonably) isolated measurement of the memory usage of the Agent.

We recommend running the evaluation yourself on your own machine, and digging into the code to see how it works. If we've made a mistake, please let us know.

### Conclusion

[](#conclusion)

Agno agents are designed for performance and while we do share some benchmarks against other frameworks, we should be mindful that accuracy and reliability are more important than speed.

We'll be publishing accuracy and reliability benchmarks running on Github actions in the future. Given that each framework is different and we won't be able to tune their performance like we do with Agno, for future benchmarks we'll only be comparing against ourselves.

## Cursor Setup

[](#cursor-setup)

When building Agno agents, using Agno documentation as a source in Cursor is a great way to speed up your development.

1. In Cursor, go to the settings or preferences section.
2. Find the section to manage documentation sources.
3. Add `https://docs.agno.com` to the list of documentation URLs.
4. Save the changes.

Now, Cursor will have access to the Agno documentation.

## Documentation, Community & More examples

[](#documentation-community--more-examples)

* Docs: [docs.agno.com](https://docs.agno.com)
* Getting Started Examples: [Getting Started Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook/getting_started)
* All Examples: [Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook)
* Community forum: [community.agno.com](https://community.agno.com/)
* Chat: [discord](https://discord.gg/4MtYHHrgA8)

## Contributions

[](#contributions)

We welcome contributions, read our [contributing guide](https://github.com/agno-agi/agno/blob/main/CONTRIBUTING.md) to get started.

## Telemetry

[](#telemetry)

Agno logs which model an agent used so we can prioritize updates to the most popular providers. You can disable this by setting `AGNO_TELEMETRY=false` in your environment.

[⬆️ Back to Top](#top)


