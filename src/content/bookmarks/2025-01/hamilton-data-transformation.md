---
title: "Hamilton：用于定义可测试、模块化且自文档化数据流程的工具"
slug: hamilton-data-transformation
description: |
  Hamilton 是一个轻量级 Python 库，帮助数据科学家和工程师定义可测试、模块化、自文档化的数据流程。它支持数据追踪和元数据记录，并在 Python 能运行的任何地方运行和扩展，极大提高了数据处理的灵活性和可维护性。
tags: 
  - dev
  - opensource
  - workflow
  - python
  - DAG
pubDatetime: 2025-01-03T13:35:41+08:00
ogImage: https://opengraph.githubassets.com/4031528a2883434f6b56842e16a5742db95cb4d78f6ca91004268acf87b0cf47/DAGWorks-Inc/hamilton
---

[原文链接](https://github.com/dagworks-inc/hamilton)

---

[![](https://private-user-images.githubusercontent.com/2328071/270543538-feb6abaa-b6d5-4271-a320-0ae4a18d8aa7.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzU4ODI4MTUsIm5iZiI6MTczNTg4MjUxNSwicGF0aCI6Ii8yMzI4MDcxLzI3MDU0MzUzOC1mZWI2YWJhYS1iNmQ1LTQyNzEtYTMyMC0wYWU0YTE4ZDhhYTcucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDEwMyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAxMDNUMDUzNTE1WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YTg3MWQ3MDkzOGIxMjBjYzNmM2VlNWQzYWVmZTZhZmIxMDVkZTAxZWM4MjI2NDcyZDY4ZjMxYTM3ZGMyYzBlNSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.jvgT44elW2pMylW1Ipm3LrVMHIOXxnUvIRYJZPBAQ6g)](https://private-user-images.githubusercontent.com/2328071/270543538-feb6abaa-b6d5-4271-a320-0ae4a18d8aa7.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzU4ODI4MTUsIm5iZiI6MTczNTg4MjUxNSwicGF0aCI6Ii8yMzI4MDcxLzI3MDU0MzUzOC1mZWI2YWJhYS1iNmQ1LTQyNzEtYTMyMC0wYWU0YTE4ZDhhYTcucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDEwMyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAxMDNUMDUzNTE1WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YTg3MWQ3MDkzOGIxMjBjYzNmM2VlNWQzYWVmZTZhZmIxMDVkZTAxZWM4MjI2NDcyZDY4ZjMxYTM3ZGMyYzBlNSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.jvgT44elW2pMylW1Ipm3LrVMHIOXxnUvIRYJZPBAQ6g) Hamilton — portable & expressive\
data transformation DAGs
========================

[](#-hamilton--portable--expressive--data-transformation-dags)

[![Documentation Status](https://camo.githubusercontent.com/f29625c2506cfa275470914251aebc8bb2048414979e4a91a7d6a50caafd3d79/68747470733a2f2f72656164746865646f63732e6f72672f70726f6a656374732f68616d696c746f6e2f62616467652f3f76657273696f6e3d6c6174657374) ](https://hamilton.dagworks.io/en/latest/?badge=latest)[![Python supported](https://camo.githubusercontent.com/3375244836b51869e6c50ba36e8efc6d034593afe0e4ecbcd348cca335a65e0e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e387c253230332e397c253230332e31307c253230332e31317c253230332e31322d626c75652e737667)](https://www.python.org/downloads/)[ ![PyPi Version](https://camo.githubusercontent.com/a1f095191284f7917959545bfd64d075b7c2421631c37775f98d63a8b42fbcb3/68747470733a2f2f62616467652e667572792e696f2f70792f73662d68616d696c746f6e2e737667) ](https://pypi.org/project/sf-hamilton/)[![Total Downloads](https://camo.githubusercontent.com/a56a0fa1eecf2cd3489d8ab26a94a845490df133ae6bb43b5c0ee8a16bf6856a/68747470733a2f2f706570792e746563682f62616467652f73662d68616d696c746f6e) ](https://pepy.tech/project/sf-hamilton)[![Total Monthly Downloads](https://camo.githubusercontent.com/e23ca3bd08cc39a4124634f59b90588ee4eee5899659beeb12f564b548b149a5/68747470733a2f2f7374617469632e706570792e746563682f62616467652f73662d68616d696c746f6e2f6d6f6e7468)](https://pepy.tech/project/sf-hamilton)\
[![](https://camo.githubusercontent.com/e6ef6311c84c08d01a4605077c0d86f2a2528b1c05c0837bb87d37d4e1c53136/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f444147576f726b732d466f6c6c6f772d707572706c652e7376673f6c6f676f3d6c696e6b6564696e) ](https://linkedin.com/showcase/dagster)[![Hamilton Slack](https://camo.githubusercontent.com/142a6131e90f9d4e184a94a9018ce814ee7160814df1ffdaeac88d8427f4f6f3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f48616d696c746f6e2d4a6f696e2d707572706c652e7376673f6c6f676f3d736c61636b) ](https://join.slack.com/t/hamilton-opensource/shared_invite/zt-2niepkra8-DGKGf_tTYhXuJWBTXtIs4g)[![](https://camo.githubusercontent.com/3ddb692aada87c3cfab4e0a3a51ba188efa5598c524a082edde96114867f4ccc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f48616d696c746f6e4f532d466f6c6c6f772d707572706c652e7376673f6c6f676f3d58) ](https://twitter.com/hamilton_os)[![](https://camo.githubusercontent.com/95e04b9bf30756cc354e2fe0448c59526a50f8963350b6f886f8d951cfec8882/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f444147576f726b732d466f6c6c6f772d707572706c652e7376673f6c6f676f3d58)](https://twitter.com/dagworks)

\
\


Hamilton is a lightweight Python library for directed acyclic graphs (DAGs) of data transformations. Your DAG is **portable**; it runs anywhere Python runs, whether it's a script, notebook, Airflow pipeline, FastAPI server, etc. Your DAG is **expressive**; Hamilton has extensive features to define and modify the execution of a DAG (e.g., data validation, experiment tracking, remote execution).

To create a DAG, write regular Python functions that specify their dependencies with their parameters. As shown below, it results in readable code that can always be visualized. Hamilton loads that definition and automatically builds the DAG for you!

[![Create a project](/DAGWorks-Inc/hamilton/raw/main/docs/_static/abc_highlight.png)](https://github.com/DAGWorks-Inc/hamilton/blob/main/docs/_static/abc_highlight.png)

Functions `B()` and `C()` refer to function `A` via their parameters

\


Hamilton brings modularity and structure to any Python application moving data: ETL pipelines, ML workflows, LLM applications, RAG systems, BI dashboards, and the [Hamilton UI](https://hamilton.dagworks.io/en/latest/concepts/ui) allows you to automatically visualize, catalog, and monitor execution.

> Hamilton is great for DAGs, but if you need loops or conditional logic to create an LLM agent or a simulation, take a look at our sister library [Burr](https://github.com/dagworks-inc/burr) 🤖 .

# Installation

[](#installation)

Hamilton supports Python 3.8+. We include the optional `visualization` dependency to display our Hamilton DAG. For visualizations, [Graphviz](https://graphviz.org/download/) needs to be installed on your system separately.

```
pip install "sf-hamilton[visualization]"
```

To use the Hamilton UI, install the `ui` and `sdk` dependencies.

```
pip install "sf-hamilton[ui,sdk]"
```

To try Hamilton in the browser, visit [www.tryhamilton.dev](https://www.tryhamilton.dev/?utm_source=README)

# Why use Hamilton?

[](#why-use-hamilton)

Data teams write code to deliver business value, but few have the resources to standardize practices and provide quality assurance. Moving from proof-of-concept to production and cross-function collaboration (e.g., data science, engineering, ops) remain challenging for teams, big or small. Hamilton is designed to help throughout a project's lifecycle:

* **Separation of concerns**. Hamilton separates the DAG "definition" and "execution" which lets data scientists focus on solving problems and engineers manage production pipelines.

* **Effective collaboration**. The [Hamilton UI provides a shared interface](https://hamilton.dagworks.io/en/latest/hamilton-ui/ui/) for teams to inspect results and debug failures throughout the development cycle.

* **Low-friction dev to prod**. Use `@config.when()` to modify your DAG between execution environments instead of error-prone `if/else` feature flags. The notebook extension prevents the pain of migrating code from a notebook to a Python module.

* **Portable transformations**. Your DAG is [independent of infrastructure or orchestration](https://blog.dagworks.io/publish/posts/detail/145543927?referrer=%2Fpublish%2Fposts), meaning you can develop and debug locally and reuse code across contexts (local, Airflow, FastAPI, etc.).

* **Maintainable DAG definition**. Hamilton [automatically builds the DAG from a single line of code whether it has 10 or 1000 nodes](https://hamilton.dagworks.io/en/latest/concepts/driver/). It can also assemble multiple Python modules into a pipeline, encouraging modularity.

* **Expressive DAGs**. [Function modifiers](https://hamilton.dagworks.io/en/latest/concepts/function-modifiers/) are a unique feature to keep your code [DRY](https://en.wikipedia.org/wiki/Don't_repeat_yourself) and reduce the complexity of maintaining large DAGs. Other frameworks inevitably lead to code redundancy or bloated functions.

* **Built-in coding style**. The Hamilton DAG is [defined using Python functions](https://hamilton.dagworks.io/en/latest/concepts/node/), encouraging modular, easy-to-read, self-documenting, and unit testable code.

* **Data and schema validation**. Decorate functions with `@check_output` to validate output properties, and raise warnings or exceptions. Add the `SchemaValidator()` adapter to automatically inspect dataframe-like objects (pandas, polars, Ibis, etc.) to track and validate their schema.

* **Built for plugins**. Hamilton is designed to play nice with all tools and provides the right abstractions to create custom integrations with your stack. Our lively community will help you build what you need!

# Hamilton UI

[](#hamilton-ui)

You can track the execution of your Hamilton DAG in the [Hamilton UI](https://hamilton.dagworks.io/en/latest/hamilton-ui/ui/). It automatically populates a data catalog with lineage / tracing and provides execution observability to inspect results and debug errors. You can run it as a [local server](https://hamilton.dagworks.io/en/latest/hamilton-ui/ui/#local-mode) or a [self-hosted application using Docker](https://hamilton.dagworks.io/en/latest/hamilton-ui/ui/#docker-deployed-mode).

[![Description1](/DAGWorks-Inc/hamilton/raw/main/docs/_static/hamilton_1.jpeg)](https://github.com/DAGWorks-Inc/hamilton/blob/main/docs/_static/hamilton_1.jpeg) [![Description2](/DAGWorks-Inc/hamilton/raw/main/docs/_static/hamilton_2.jpeg)](https://github.com/DAGWorks-Inc/hamilton/blob/main/docs/_static/hamilton_2.jpeg) [![Description3](/DAGWorks-Inc/hamilton/raw/main/docs/_static/hamilton_3.jpeg)](https://github.com/DAGWorks-Inc/hamilton/blob/main/docs/_static/hamilton_3.jpeg)

*DAG catalog, automatic dataset profiling, and execution tracking*

## Get started with the Hamilton UI

[](#get-started-with-the-hamilton-ui)

1. To use the Hamilton UI, install the dependencies (see `Installation` section) and start the server with

   ```
   hamilton ui
   ```

2. On the first connection, create a `username` and a new project (the `project_id` should be `1`).

[![Create a project](/DAGWorks-Inc/hamilton/raw/main/docs/_static/new_project.png)](https://github.com/DAGWorks-Inc/hamilton/blob/main/docs/_static/new_project.png)

\


3. Track your Hamilton DAG by creating a `HamiltonTracker` object with your `username` and `project_id` and adding it to your `Builder`. Now, your DAG will appear in the UI's catalog and all executions will be tracked!

   ```
   from hamilton import driver
   from hamilton_sdk.adapters import HamiltonTracker
   import my_dag

   # use your `username` and `project_id`
   tracker = HamiltonTracker(
      username="my_username",
      project_id=1,
      dag_name="hello_world",
   )

   # adding the tracker to the `Builder` will add the DAG to the catalog
   dr = (
      driver.Builder()
      .with_modules(my_dag)
      .with_adapters(tracker)  # add your tracker here
      .build()
   )

   # executing the `Driver` will track results
   dr.execute(["C"])
   ```

# Documentation & learning resources

[](#documentation--learning-resources)

* 📚 See the [official documentation](https://hamilton.dagworks.io/) to learn about the core concepts of Hamilton.

* 👨‍🏫 Consult the [examples on GitHub](https://github.com/DAGWorks-Inc/hamilton/tree/main/examples) to learn about specific features or integrations with other frameworks.

* 📰 The [DAGWorks blog](https://blog.dagworks.io/) includes guides about how to build a data platform and narrative tutorials.

* 📺 Find video tutorials on the [DAGWorks YouTube channel](https://www.youtube.com/@DAGWorks-Inc)

* 📣 Reach out via the [Hamilton Slack community](https://join.slack.com/t/hamilton-opensource/shared_invite/zt-2niepkra8-DGKGf_tTYhXuJWBTXtIs4g) for help and troubleshooting

# How does Hamilton compare to X?

[](#how-does-hamilton-compare-to-x)

Hamilton is not an orchestrator ([you might not need one](https://blog.dagworks.io/p/lean-data-automation-a-principal)), nor a feature store ([but you can use it to build one!](https://blog.dagworks.io/p/featurization-integrating-hamilton)). Its purpose is to help you structure and manage data transformations. If you know dbt, Hamilton does for Python what dbt does for SQL.

Another way to frame it is to think about the different layers of a data stack. Hamilton is at the **asset layer**. It helps you organize data transformations code (the **expression layer**), manage changes, and validate & test data.

| Layer         | Purpose                                                                     | Example Tools                                                                 |
| ------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Orchestration | Operational system for the creation of assets                               | Airflow, Metaflow, Prefect, Dagster                                           |
| Asset         | Organize expressions into meaningful units (e.g., dataset, ML model, table) | **Hamilton**, dbt, dlt, SQLMesh, [Burr](https://github.com/dagworks-inc/burr) |
| Expression    | Language to write data transformations                                      | pandas, SQL, polars, Ibis, LangChain                                          |
| Execution     | Perform data transformations                                                | Spark, Snowflake, DuckDB, RAPIDS                                              |
| Data          | Physical representation of data, inputs and outputs                         | S3, Postgres, file system, Snowflake                                          |

See our page on [Why use Hamilton?](https://hamilton.dagworks.io/en/latest/get-started/why-hamilton/) and framework [code comparisons](https://hamilton.dagworks.io/en/latest/code-comparisons/) for more information.

# 📑 License

[](#-license)

Hamilton is released under the BSD 3-Clause Clear License. See [LICENSE](https://github.com/DAGWorks-Inc/hamilton/blob/main/LICENSE.md) for details.

# 🌎 Community

[](#-community)

## 👨‍💻 Contributing

[](#-contributing)

We're very supportive of changes by new contributors, big or small! Make sure to discuss potential changes by creating an issue or commenting on an existing one before opening a pull request. Good first contributions include creating an example or an integration with your favorite Python library!

To contribute, checkout our [contributing guidelines](https://github.com/DAGWorks-Inc/hamilton/blob/main/CONTRIBUTING.md), our [developer setup guide](https://github.com/DAGWorks-Inc/hamilton/blob/main/developer_setup.md), and our [Code of Conduct](https://github.com/DAGWorks-Inc/hamilton/blob/main/CODE_OF_CONDUCT.md).

## 😎 Used by

[](#-used-by)

Hamilton was started at Stitch Fix before the original creators founded DAGWorks Inc! The library is battle-tested and has been supporting production use cases since 2019.

> Read more about the [origin story](https://multithreaded.stitchfix.com/blog/2021/10/14/functions-dags-hamilton/).

* [Stitch Fix](https://www.stitchfix.com/) — Time series forecasting
* [UK Government Digital Services](https://github.com/alphagov/govuk-feedback-analysis) — National feedback pipeline (processing & analysis)
* [IBM](https://www.ibm.com/) — Internal search and ML pipelines
* [Opendoor](https://www.opendoor.com/) — Manage PySpark pipelines
* [Lexis Nexis](https://www.lexisnexis.com/en-us/home.page) — Feature processing and lineage
* [Adobe](https://www.adobe.com/) — Prompt engineering research
* [WrenAI](https://github.com/Canner/WrenAI) — async text-to-SQL workflows
* [British Cycling](https://www.britishcycling.org.uk/) — Telemetry analysis
* [Oak Ridge & PNNL](https://pnnl.gov/) — Naturf project
* [ORNL](https://www.ornl.gov/)
* [Federal Reserve Board](https://www.federalreserve.gov/)
* [Joby Aviation](https://www.jobyaviation.com/) — Flight data processing
* [Two](https://www.two.inc/)
* [Transfix](https://transfix.io/) — Online featurization and prediction
* [Railofy](https://www.railofy.com) — Orchestrate pandas code
* [Habitat Energy](https://www.habitat.energy/) — Time-series feature engineering
* [KI-Insurance](https://www.ki-insurance.com/) — Feature engineering
* [Ascena Retail](https://www.ascena.com/) — Feature engineering
* [NaroHQ](https://www.narohq.com/)
* [EquipmentShare](https://www.equipmentshare.com/)
* [Everstream.ai](https://www.everstream.ai/)
* [Flectere](https://flectere.net/)
* [F33.ai](https://f33.ai/)
* [Kora Money](https://www.koramoney.com)
* [Capitec Bank](https://www.capitecbank.co.za/)
* [Best Egg](https://bestegg.com/)
* [RTV Euro AGD](https://www.euro.com.pl/)
* [Wealth.com](https://www.wealth.com/)
* [wren.ai](https://wren.ai/)

## 🤝 Code Contributors

[](#-code-contributors)

[![Contributors](https://camo.githubusercontent.com/b32061a2b1f736797b49664bd6af7e9908ce449c2bbccc0740037dcd614e0d20/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d646167776f726b732d696e632f68616d696c746f6e)](https://github.com/DAGWorks-Inc/hamilton/graphs/contributors)

## 🙌 Special Mentions & 🦟 Bug Hunters

[](#-special-mentions---bug-hunters)

Thanks to our awesome community and their active involvement in the Hamilton library.

[Nils Olsson](https://github.com/nilsso), [Michał Siedlaczek](https://github.com/elshize), [Alaa Abedrabbo](https://github.com/AAbedrabbo), [Shreya Datar](https://github.com/datarshreya), [Baldo Faieta](https://github.com/baldofaieta), [Anwar Brini](https://github.com/AnwarBrini), [Gourav Kumar](https://github.com/gms101), [Amos Aikman](https://github.com/amosaikman), [Ankush Kundaliya](https://github.com/akundaliya), [David Weselowski](https://github.com/j7zAhU), [Peter Robinson](https://github.com/Peter4137), [Seth Stokes](https://github.com/sT0v), [Louis Maddox](https://github.com/lmmx), [Stephen Bias](https://github.com/s-ducks), [Anup Joseph](https://github.com/AnupJoseph), [Jan Hurst](https://github.com/janhurst), [Flavia Santos](https://github.com/flaviassantos), [Nicolas Huray](https://github.com/nhuray), [Manabu Niseki](https://github.com/ninoseki), [Kyle Pounder](https://github.com/kpounder), [Alex Bustos](https://github.com/bustosalex1), [Andy Day](https://github.com/adayNU), [Alexander Cai](https://github.com/adzcai), [Nils Müller-Wendt](https://github.com/ChronoJon), [Paul Larsen](https://github.com/munichpavel), [Kemal Eren](https://github.com/kemaleren), [Jernej Frank](https://github.com/jernejfrank), [Noah Ridge](https://github.com/noahridge)

# 🎓 Citations

[](#-citations)

We'd appreciate citing Hamilton by referencing one of the following:

```
@inproceedings{DBLP:conf/vldb/KrawczykI22,
  title     = {Hamilton: a modular open source declarative paradigm for high level
               modeling of dataflows},
  author    = {Stefan Krawczyk and Elijah ben Izzy},
  editor    = {Satyanarayana R. Valluri and Mohamed Za{\"{\i}}t},
  booktitle = {1st International Workshop on Composable Data Management Systems,
               CDMS@VLDB 2022, Sydney, Australia, September 9, 2022},
  year      = {2022},
  url       = {https://cdmsworkshop.github.io/2022/Proceedings/ShortPapers/Paper6\_StefanKrawczyk.pdf},
  timestamp = {Wed, 19 Oct 2022 16:20:48 +0200},
  biburl    = {https://dblp.org/rec/conf/vldb/KrawczykI22.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

```
@inproceedings{CEURWS:conf/vldb/KrawczykIQ22,
  title     = {Hamilton: enabling software engineering best practices for data transformations via generalized dataflow graphs},
  author    = {Stefan Krawczyk and Elijah ben Izzy and Danielle Quinn},
  editor    = {Cinzia Cappiello and Sandra Geisler and Maria-Esther Vidal},
  booktitle = {1st International Workshop on Data Ecosystems co-located with 48th International Conference on Very Large Databases (VLDB 2022)},
  pages     = {41--50},
  url       = {https://ceur-ws.org/Vol-3306/paper5.pdf},
  year      = {2022}
}
```

# 📚 Libraries built on / for Hamilton

[](#-libraries-built-on--for-hamilton)

* [Hypster](https://github.com/gilad-rubin/hypster) - hyperparameter management
* [DSP Decision Engine](https://github.com/capitec/dsp-decision-engine) - decision trees
* [NaturF](https://github.com/IMMM-SFA/naturf/) - library for data transformation for weather forecasting
* [WrenAI](https://github.com/Canner/WrenAI) - RAG
* [FlowerPower](https://github.com/legout/flowerpower/) - Scheduler for Hamilton


