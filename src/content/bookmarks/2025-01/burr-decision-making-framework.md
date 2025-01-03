---
title: "DAGWorks-Inc/burr：构建决策应用程序的强大框架（聊天机器人、代理、模拟等）"
slug: burr-decision-making-framework
description: |
  DAGWorks-Inc发布了Burr，一个用于构建决策型应用程序（如聊天机器人、代理和模拟等）的框架。它支持实时监控、跟踪和持久化，并且可以集成您喜爱的框架，简单易用，帮助您实现复杂工作的状态管理。
tags: 
  - dev
  - python
  - DAG
  - workflow
pubDatetime: 2025-01-03T13:01:23+08:00
ogImage: https://opengraph.githubassets.com/7b423ce086de75e8fef233455f8cefcddb281a5c8fd812422b6e678de50cda14/DAGWorks-Inc/burr
---

[原文链接](https://github.com/DAGWorks-Inc/burr)

---

# [![](https://private-user-images.githubusercontent.com/2328071/349278524-2ab9b499-7ca2-4ae9-af72-ccc775f30b4e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzU4ODA3MjcsIm5iZiI6MTczNTg4MDQyNywicGF0aCI6Ii8yMzI4MDcxLzM0OTI3ODUyNC0yYWI5YjQ5OS03Y2EyLTRhZTktYWY3Mi1jY2M3NzVmMzBiNGUucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDEwMyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAxMDNUMDUwMDI3WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZGIyOWRmNzFiMTkyODllZDAyNzVkNDIwNDUzMTYwMWRiMzZjZjZlODdiYTk5MThmMWM4NmRkZjI3ZmI1OTI4ZiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ._ZyhfW9OWVSQC5r-AFLWOMeqhGo17AwKM68A9bPPj4M)](https://private-user-images.githubusercontent.com/2328071/349278524-2ab9b499-7ca2-4ae9-af72-ccc775f30b4e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzU4ODA3MjcsIm5iZiI6MTczNTg4MDQyNywicGF0aCI6Ii8yMzI4MDcxLzM0OTI3ODUyNC0yYWI5YjQ5OS03Y2EyLTRhZTktYWY3Mi1jY2M3NzVmMzBiNGUucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDEwMyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAxMDNUMDUwMDI3WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZGIyOWRmNzFiMTkyODllZDAyNzVkNDIwNDUzMTYwMWRiMzZjZjZlODdiYTk5MThmMWM4NmRkZjI3ZmI1OTI4ZiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ._ZyhfW9OWVSQC5r-AFLWOMeqhGo17AwKM68A9bPPj4M) Burr

[](#-burr)

[![Discord](https://camo.githubusercontent.com/6d3545926e7f277f984b83fb6aece94529c981eb8dce0e365bb7a10ef64bde30/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a6f696e2d427572725f446973636f72642d3732383944413f6c6f676f3d646973636f7264)](https://discord.gg/6Zy2DwP4f3) [![Downloads](https://camo.githubusercontent.com/465749828c5749cd4f27d7acc3352bff8238c6eec6f63eec93b3a01afd88c6c0/68747470733a2f2f7374617469632e706570792e746563682f62616467652f627572722f6d6f6e7468)](https://pepy.tech/project/burr) [![PyPI Downloads](https://camo.githubusercontent.com/ca125108d4149a008714baac6ea1a76aa708e7a250547b4b9ee35b135ae5fece/68747470733a2f2f7374617469632e706570792e746563682f62616467652f62757272)](https://camo.githubusercontent.com/ca125108d4149a008714baac6ea1a76aa708e7a250547b4b9ee35b135ae5fece/68747470733a2f2f7374617469632e706570792e746563682f62616467652f62757272) [![GitHub Last Commit](https://camo.githubusercontent.com/50256de7aee202fb9447b31741ec0d742de2ab9ac2ff47695294223b26d19545/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6173742d636f6d6d69742f646167776f726b732d696e632f62757272)](https://github.com/dagworks-inc/burr/pulse) [![X](https://camo.githubusercontent.com/db378069d51874c73dd10cd8504f0238828837a786377e5d040d86eeabb44052/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f666f6c6c6f772d253430627572725f6672616d65776f726b2d3144413146323f6c6f676f3d78267374796c653d736f6369616c)](https://twitter.com/burr_framework) [![](https://camo.githubusercontent.com/8f9abab144366d0114bfd20b8deac2486d72c46f1485e6402fb04214b7c27ffa/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f41492d436f64652532304167656e742d454239464441)](https://app.commanddash.io/agent/github_DAGWorks-Inc_burr) [![](https://camo.githubusercontent.com/e6ef6311c84c08d01a4605077c0d86f2a2528b1c05c0837bb87d37d4e1c53136/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f444147576f726b732d466f6c6c6f772d707572706c652e7376673f6c6f676f3d6c696e6b6564696e) ](https://linkedin.com/showcase/dagster)[![](https://camo.githubusercontent.com/5e50db2a7e404b297efcef4dbbff90e6da01cf6be2aa183205f519214afdb0c2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f627572725f6672616d65776f726b2d466f6c6c6f772d707572706c652e7376673f6c6f676f3d58) ](https://twitter.com/burr_framework)[![](https://camo.githubusercontent.com/95e04b9bf30756cc354e2fe0448c59526a50f8963350b6f886f8d951cfec8882/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f444147576f726b732d466f6c6c6f772d707572706c652e7376673f6c6f676f3d58)](https://twitter.com/dagworks)

Burr makes it easy to develop applications that make decisions (chatbots, agents, simulations, etc...) from simple python building blocks.

Burr works well for any application that uses LLMs, and can integrate with any of your favorite frameworks. Burr includes a UI that can track/monitor/trace your system in real time, along with pluggable persisters (e.g. for memory) to save & load application state.

Link to [documentation](https://burr.dagworks.io/). Quick (<3min) video intro [here](https://www.loom.com/share/a10f163428b942fea55db1a84b1140d8?sid=1512863b-f533-4a42-a2f3-95b13deb07c9). Longer [video intro & walkthrough](https://www.youtube.com/watch?v=rEZ4oDN0GdU). Blog post [here](https://blog.dagworks.io/p/burr-develop-stateful-ai-applications). Join discord for help/questions [here](https://discord.gg/6Zy2DwP4f3).

## 🏃Quick start

[](#quick-start)

Install from `pypi`:

```
pip install "burr[start]"
```

(see [the docs](https://burr.dagworks.io/getting_started/install/) if you're using poetry)

Then run the UI server:

```
burr
```

This will open up Burr's telemetry UI. It comes loaded with some default data so you can click around. It also has a demo chat application to help demonstrate what the UI captures enabling you too see things changing in real-time. Hit the "Demos" side bar on the left and select `chatbot`. To chat it requires the `OPENAI_API_KEY` environment variable to be set, but you can still see how it works if you don't have an API key set.

Next, start coding / running examples:

```
git clone https://github.com/dagworks-inc/burr && cd burr/examples/hello-world-counter
python application.py
```

You'll see the counter example running in the terminal, along with the trace being tracked in the UI. See if you can find it.

For more details see the [getting started guide](https://burr.dagworks.io/getting_started/simple-example/).

## 🔩 How does Burr work?

[](#-how-does-burr-work)

With Burr you express your application as a state machine (i.e. a graph/flowchart). You can (and should!) use it for anything in which you have to manage state, track complex decisions, add human feedback, or dictate an idempotent, self-persisting workflow.

The core API is simple -- the Burr hello-world looks like this (plug in your own LLM, or copy from [the docs](https://burr.dagworks.io/getting_started/simple-example/#build-a-simple-chatbot%3E) for *gpt-X*)

```
from burr.core import action, State, ApplicationBuilder

@action(reads=[], writes=["prompt", "chat_history"])
def human_input(state: State, prompt: str) -> State:
    # your code -- write what you want here!
    return state.update(prompt=prompt).append(chat_history=chat_item)

@action(reads=["chat_history"], writes=["response", "chat_history"])
def ai_response(state: State) -> State:
    response = _query_llm(state["chat_history"]) # Burr doesn't care how you use LLMs!
    return state.update(response=content).append(chat_history=chat_item)

app = (
    ApplicationBuilder()
    .with_actions(human_input, ai_response)
    .with_transitions(
        ("human_input", "ai_response"),
        ("ai_response", "human_input")
    ).with_state(chat_history=[])
    .with_entrypoint("human_input")
    .build()
)
*_, state = app.run(halt_after=["ai_response"], inputs={"prompt": "Who was Aaron Burr, sir?"})
print("answer:", app.state["response"])
```

Burr includes:

1. A (dependency-free) low-abstraction python library that enables you to build and manage state machines with simple python functions
2. A UI you can use view execution telemetry for introspection and debugging
3. A set of integrations to make it easier to persist state, connect to telemetry, and integrate with other systems

[![Burr at work](https://github.com/DAGWorks-Inc/burr/raw/main/chatbot.gif)](https://github.com/DAGWorks-Inc/burr/blob/main/chatbot.gif)[![Burr at work](https://github.com/DAGWorks-Inc/burr/raw/main/chatbot.gif) ](https://github.com/DAGWorks-Inc/burr/blob/main/chatbot.gif)     [](https://github.com/DAGWorks-Inc/burr/blob/main/chatbot.gif)

## 💻️ What can you do with Burr?

[](#️-what-can-you-do-with-burr)

Burr can be used to power a variety of applications, including:

1. [A simple gpt-like chatbot](https://github.com/dagworks-inc/burr/tree/main/examples/multi-modal-chatbot)
2. [A stateful RAG-based chatbot](https://github.com/dagworks-inc/burr/tree/main/examples/conversational-rag/simple_example)
3. [An LLM-based adventure game](https://github.com/DAGWorks-Inc/burr/tree/main/examples/llm-adventure-game)
4. [An interactive assistant for writing emails](https://github.com/DAGWorks-Inc/burr/tree/main/examples/email-assistant)

As well as a variety of (non-LLM) use-cases, including a time-series forecasting [simulation](https://github.com/DAGWorks-Inc/burr/tree/main/examples/simulation), and [hyperparameter tuning](https://github.com/DAGWorks-Inc/burr/tree/main/examples/ml-training).

And a lot more!

Using hooks and other integrations you can (a) integrate with any of your favorite vendors (LLM observability, storage, etc...), and (b) build custom actions that delegate to your favorite libraries (like [Hamilton](https://github.com/DAGWorks-Inc/hamilton)).

Burr will *not* tell you how to build your models, how to query APIs, or how to manage your data. It will help you tie all these together in a way that scales with your needs and makes following the logic of your system easy. Burr comes out of the box with a host of integrations including tooling to build a UI in streamlit and watch your state machine execute.

## 🏗 Start building

[](#-start-building)

See the documentation for [getting started](https://burr.dagworks.io/getting_started/simple-example), and follow the example. Then read through some of the concepts and write your own application!

## 📃 Comparison against common frameworks

[](#-comparison-against-common-frameworks)

While Burr is attempting something (somewhat) unique, there are a variety of tools that occupy similar spaces:

| Criteria                                          | Burr | Langgraph | temporal | Langchain | Superagent | Hamilton |
| ------------------------------------------------- | :--: | :-------: | :------: | :-------: | :--------: | :------: |
| Explicitly models a state machine                 |   ✅  |     ✅     |     ❌    |     ❌     |      ❌     |     ❌    |
| Framework-agnostic                                |   ✅  |     ✅     |     ✅    |     ✅     |      ❌     |     ✅    |
| Asynchronous event-based orchestration            |   ❌  |     ❌     |     ✅    |     ❌     |      ❌     |     ❌    |
| Built for core web-service logic                  |   ✅  |     ✅     |     ❌    |     ✅     |      ✅     |     ✅    |
| Open-source user-interface for monitoring/tracing |   ✅  |     ❌     |     ❌    |     ❌     |      ❌     |     ✅    |
| Works with non-LLM use-cases                      |   ✅  |     ❌     |     ❌    |     ❌     |      ❌     |     ✅    |

## 🌯 Why the name Burr?

[](#-why-the-name-burr)

Burr is named after [Aaron Burr](https://en.wikipedia.org/wiki/Aaron_Burr), founding father, third VP of the United States, and murderer/arch-nemesis of [Alexander Hamilton](https://en.wikipedia.org/wiki/Alexander_Hamilton). What's the connection with Hamilton? This is [DAGWorks](https://github.com/DAGWorks-Inc/burr/blob/main/www.dagworks.io)' second open-source library release after the [Hamilton library](https://github.com/dagworks-inc/hamilton) We imagine a world in which Burr and Hamilton lived in harmony and saw through their differences to better the union. We originally built Burr as a *harness* to handle state between executions of Hamilton DAGs (because DAGs don't have cycles), but realized that it has a wide array of applications and decided to release it more broadly.

## Testimonials

[](#testimonials)

"After evaluating several other obfuscating LLM frame-works, their elegant yet comprehensive state management solution proved to be the powerful answer to rolling out robots driven by AI decision making."

#### Ashish Ghosh

[](#ashish-ghosh)

CTO, Peanut Robotics

\
\---

"Of course, you can use it \[LangChain], but whether it's really production-ready and improves the time from 'code-to-prod' \[...], we've been doing LLM apps for two years, and the answer is no \[...] All these 'all-in-one' libs suffer from this \[...]. Honestly, take a look at Burr. Thank me later."

#### Reddit User

[](#reddit-user)

LocalLlama, Subreddit

\
\---

"Using Burr is a no-brainer if you want to build a modular AI application. It is so easy to build with and I especially love their UI which makes debugging, a piece of cake. And the always ready to help team, is the cherry on top."

#### Ishita

[](#ishita)

Founder, Watto.ai

\
\---

"I just came across Burr and I'm like WOW, this seems like you guys predicted this exact need when building this. No weird esoteric concepts just because it's AI."

#### Matthew Rideout

[](#matthew-rideout)

Staff Software Engineer, Paxton AI

\


"Burr's state management part is really helpful for creating state snapshots and build debugging, replaying and even building evaluation cases around that"

#### Rinat Gareev

[](#rinat-gareev)

Senior Solutions Architect, Provectus

"I have been using Burr over the past few months, and compared to many agentic LLM platforms out there (e.g. LangChain, CrewAi, AutoGen, Agency Swarm, etc), Burr provides a more robust framework for designing complex behaviors."

#### Hadi Nayebi

[](#hadi-nayebi)

Co-founder, CognitiveGraphs

\
\---

"Moving from LangChain to Burr was a game-changer!\
Time-Saving: It took me just a few hours to get started with Burr, compared to the days and weeks I spent trying to navigate LangChain.\
Cleaner Implementation: With Burr, I could finally have a cleaner, more sophisticated, and stable implementation. No more wrestling with complex codebases.\
Team Adoption: I pitched Burr to my teammates, and we pivoted our entire codebase to it. It's been a smooth ride ever since."

#### Aditya K.

[](#aditya-k)

DS Architect, TaskHuman

## 🛣 Roadmap

[](#-roadmap)

While Burr is stable and well-tested, we have quite a few tools/features on our roadmap!

1. FastAPI integration + hosted deployment -- make it really easy to get Burr in an app in production without thinking about REST APIs

2. Various efficiency/usability improvements for the core library (see [planned capabilities](https://burr.dagworks.io/concepts/planned-capabilities/) for more details). This includes:

   1. First-class support for retries + exception management
   2. More integration with popular frameworks (LCEL, LLamaIndex, Hamilton, etc...)
   3. Capturing & surfacing extra metadata, e.g. annotations for particular point in time, that you can then pull out for fine-tuning, etc.
   4. Improvements to the pydantic-based typing system

3. Tooling for hosted execution of state machines, integrating with your infrastructure (Ray, modal, FastAPI + EC2, etc...)

4. Additional storage integrations. More integrations with technologies like MySQL, S3, etc. so you can run Burr on top of what you have available.

If you want to avoid self-hosting the above solutions we're building Burr Cloud. To let us know you're interested sign up [here](https://forms.gle/w9u2QKcPrztApRedA) for the waitlist to get access.

## 🤲 Contributing

[](#-contributing)

We welcome contributors! To get started on developing, see the [developer-facing docs](https://burr.dagworks.io/contributing).

## 👪 Contributors

[](#-contributors)

### Code contributions

[](#code-contributions)

Users who have contributed core functionality, integrations, or examples.

* [Elijah ben Izzy](https://github.com/elijahbenizzy)
* [Stefan Krawczyk](https://github.com/skrawcz)
* [Joseph Booth](https://github.com/jombooth)
* [Nandani Thakur](https://github.com/NandaniThakur)
* [Thierry Jean](https://github.com/zilto)
* [Hamza Farhan](https://github.com/HamzaFarhan)
* [Abdul Rafay](https://github.com/proftorch)

### Bug hunters/special mentions

[](#bug-huntersspecial-mentions)

Users who have contributed small docs fixes, design suggestions, and found bugs

* [Luke Chadwick](https://github.com/vertis)
* [Evans](https://github.com/sudoevans)
* [Sasmitha Manathunga](https://github.com/mmz-001)


