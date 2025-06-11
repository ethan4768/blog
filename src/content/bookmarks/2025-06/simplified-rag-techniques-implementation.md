---
title: "简化所有RAG技术实现的实用方法"
slug: simplified-rag-techniques-implementation
description: |
  该仓库以简单易懂的方式实现了各种检索增强生成（RAG）技术，使用熟悉的Python库，例如OpenAI和NumPy。项目旨在提供可读取、可修改的代码，帮助用户深入理解RAG的基本原理，设施学习和使用不同的RAG方法，以满足各类需求。
tags: 
  - AI
  - dev
  - opensource
  - tool
  - course
pubDatetime: 2025-06-11T11:47:36+08:00
ogImage: https://opengraph.githubassets.com/4e6cfda41c4cfb2087951899508f38fc1ba4f30be434159734598f939fdae175/FareedKhan-dev/all-rag-techniques
---

[原文链接](https://github.com/fareedkhan-dev/all-rag-techniques)

---

# All RAG Techniques: A Simpler, Hands-On Approach ✨

[](#all-rag-techniques-a-simpler-hands-on-approach-)

[![Python 3.7+](https://camo.githubusercontent.com/e16651539eac2dfd36c1d089a6905e213fe77b360d624d391938e4faa27dad69/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e372b2d626c75652e737667)](https://www.python.org/downloads/release/python-370/) [![Nebius AI](https://camo.githubusercontent.com/d96ff2b67b4c347266bdae337437b1b7b78afa8b019fdf212ba136f2ccf6ca8b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4e656269757325323041492d4150492d627269676874677265656e)](https://cloud.nebius.ai/services/llm-embedding) [![OpenAI](https://camo.githubusercontent.com/b0b83ecbe6c55876dd01c720303d211839fcbfcfeac2e1b3641f9147ecd3e29e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f70656e41492d4150492d6c6967687467726579)](https://openai.com/) [![Medium](https://camo.githubusercontent.com/ccc38ff36701b4e9606f130fd3b0bd24d736411bb8f3a3d7bf502974beb3702c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d656469756d2d426c6f672d626c61636b3f6c6f676f3d6d656469756d)](https://medium.com/@fareedkhandev/testing-every-rag-technique-to-find-the-best-094d166af27f)

This repository takes a clear, hands-on approach to **Retrieval-Augmented Generation (RAG)**, breaking down advanced techniques into straightforward, understandable implementations. Instead of relying on frameworks like `LangChain` or `FAISS`, everything here is built using familiar Python libraries `openai`, `numpy`, `matplotlib`, and a few others.

The goal is simple: provide code that is readable, modifiable, and educational. By focusing on the fundamentals, this project helps demystify RAG and makes it easier to understand how it really works.

## Update: 📢

[](#update-)

* (12-May-2025) Added a new notebook on how to handle big data using Knowledge Graphs.
* (27-April-2025) Added a new notebook which finds best RAG technique for a given query (Simple RAG + Reranker + Query Rewrite).
* (20-Mar-2025) Added a new notebook on RAG with Reinforcement Learning.
* (07-Mar-2025) Added 20 RAG techniques to the repository.

## 🚀 What's Inside?

[](#-whats-inside)

This repository contains a collection of Jupyter Notebooks, each focusing on a specific RAG technique. Each notebook provides:

* A concise explanation of the technique.
* A step-by-step implementation from scratch.
* Clear code examples with inline comments.
* Evaluations and comparisons to demonstrate the technique's effectiveness.
* Visualization to visualize the results.

Here's a glimpse of the techniques covered:

| Notebook                                                                                                                            | Description                                                                                                                      |
| :---------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| [1. Simple RAG](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/01_simple_rag.ipynb)                                 | A basic RAG implementation. A great starting point!                                                                              |
| [2. Semantic Chunking](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/02_semantic_chunking.ipynb)                   | Splits text based on semantic similarity for more meaningful chunks.                                                             |
| [3. Chunk Size Selector](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/03_chunk_size_selector.ipynb)               | Explores the impact of different chunk sizes on retrieval performance.                                                           |
| [4. Context Enriched RAG](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/04_context_enriched_rag.ipynb)             | Retrieves neighboring chunks to provide more context.                                                                            |
| [5. Contextual Chunk Headers](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/05_contextual_chunk_headers_rag.ipynb) | Prepends descriptive headers to each chunk before embedding.                                                                     |
| [6. Document Augmentation RAG](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/06_doc_augmentation_rag.ipynb)        | Generates questions from text chunks to augment the retrieval process.                                                           |
| [7. Query Transform](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/07_query_transform.ipynb)                       | Rewrites, expands, or decomposes queries to improve retrieval. Includes **Step-back Prompting** and **Sub-query Decomposition**. |
| [8. Reranker](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/08_reranker.ipynb)                                     | Re-ranks initially retrieved results using an LLM for better relevance.                                                          |
| [9. RSE](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/09_rse.ipynb)                                               | Relevant Segment Extraction: Identifies and reconstructs continuous segments of text, preserving context.                        |
| [10. Contextual Compression](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/10_contextual_compression.ipynb)        | Implements contextual compression to filter and compress retrieved chunks, maximizing relevant information.                      |
| [11. Feedback Loop RAG](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/11_feedback_loop_rag.ipynb)                  | Incorporates user feedback to learn and improve RAG system over time.                                                            |
| [12. Adaptive RAG](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/12_adaptive_rag.ipynb)                            | Dynamically selects the best retrieval strategy based on query type.                                                             |
| [13. Self RAG](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/13_self_rag.ipynb)                                    | Implements Self-RAG, dynamically decides when and how to retrieve, evaluates relevance, and assesses support and utility.        |
| [14. Proposition Chunking](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/14_proposition_chunking.ipynb)            | Breaks down documents into atomic, factual statements for precise retrieval.                                                     |
| [15. Multimodel RAG](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/15_multimodel_rag.ipynb)                        | Combines text and images for retrieval, generating captions for images using LLaVA.                                              |
| [16. Fusion RAG](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/16_fusion_rag.ipynb)                                | Combines vector search with keyword-based (BM25) retrieval for improved results.                                                 |
| [17. Graph RAG](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/17_graph_rag.ipynb)                                  | Organizes knowledge as a graph, enabling traversal of related concepts.                                                          |
| [18. Hierarchy RAG](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/18_hierarchy_rag.ipynb)                          | Builds hierarchical indices (summaries + detailed chunks) for efficient retrieval.                                               |
| [19. HyDE RAG](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/19_HyDE_rag.ipynb)                                    | Uses Hypothetical Document Embeddings to improve semantic matching.                                                              |
| [20. CRAG](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/20_crag.ipynb)                                            | Corrective RAG: Dynamically evaluates retrieval quality and uses web search as a fallback.                                       |
| [21. Rag with RL](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/21_rag_with_rl.ipynb)                              | Maximize the reward of the RAG model using Reinforcement Learning.                                                               |
| [Best RAG Finder](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/best_rag_finder.ipynb)                             | Finds the best RAG technique for a given query using Simple RAG + Reranker + Query Rewrite.                                      |
| [22. Big Data with Knowledge Graphs](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/22_Big_data_with_KG.ipynb)      | Handles large datasets using Knowledge Graphs.                                                                                   |

## 🗂️ Repository Structure

[](#️-repository-structure)

```
fareedkhan-dev-all-rag-techniques/
├── README.md                          <- You are here!
├── 01_simple_rag.ipynb
├── 02_semantic_chunking.ipynb
├── 03_chunk_size_selector.ipynb
├── 04_context_enriched_rag.ipynb
├── 05_contextual_chunk_headers_rag.ipynb
├── 06_doc_augmentation_rag.ipynb
├── 07_query_transform.ipynb
├── 08_reranker.ipynb
├── 09_rse.ipynb
├── 10_contextual_compression.ipynb
├── 11_feedback_loop_rag.ipynb
├── 12_adaptive_rag.ipynb
├── 13_self_rag.ipynb
├── 14_proposition_chunking.ipynb
├── 15_multimodel_rag.ipynb
├── 16_fusion_rag.ipynb
├── 17_graph_rag.ipynb
├── 18_hierarchy_rag.ipynb
├── 19_HyDE_rag.ipynb
├── 20_crag.ipynb
├── 21_rag_with_rl.ipynb
├── 22_big_data_with_KG.ipynb
├── best_rag_finder.ipynb
├── requirements.txt                   <- Python dependencies
└── data/
    └── val.json                       <- Sample validation data (queries and answers)
    └── AI_Information.pdf             <- A sample PDF document for testing.
    └── attention_is_all_you_need.pdf  <- A sample PDF document for testing (for Multi-Modal RAG).
```

## 🛠️ Getting Started

[](#️-getting-started)

1. **Clone the repository:**

   ```
   git clone https://github.com/FareedKhan-dev/all-rag-techniques.git
   cd all-rag-techniques
   ```

2. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key:**

   * Obtain an API key from [Nebius AI](https://studio.nebius.com/).

   * Set the API key as an environment variable:

     ```
     export OPENAI_API_KEY='YOUR_NEBIUS_AI_API_KEY'
     ```

     or

     ```
     setx OPENAI_API_KEY "YOUR_NEBIUS_AI_API_KEY"  # On Windows
     ```

     or, within your Python script/notebook:

     ```
     import os
     os.environ["OPENAI_API_KEY"] = "YOUR_NEBIUS_AI_API_KEY"
     ```

4. **Run the notebooks:**

   Open any of the Jupyter Notebooks (`.ipynb` files) using Jupyter Notebook or JupyterLab. Each notebook is self-contained and can be run independently. The notebooks are designed to be executed sequentially within each file.

   **Note:** The `data/AI_Information.pdf` file provides a sample document for testing. You can replace it with your own PDF. The `data/val.json` file contains sample queries and ideal answers for evaluation. The 'attention\_is\_all\_you\_need.pdf' is for testing Multi-Modal RAG Notebook.

## 💡 Core Concepts

[](#-core-concepts)

* **Embeddings:** Numerical representations of text that capture semantic meaning. We use Nebius AI's embedding API and, in many notebooks, also the `BAAI/bge-en-icl` embedding model.

* **Vector Store:** A simple database to store and search embeddings. We create our own `SimpleVectorStore` class using NumPy for efficient similarity calculations.

* **Cosine Similarity:** A measure of similarity between two vectors. Higher values indicate greater similarity.

* **Chunking:** Dividing text into smaller, manageable pieces. We explore various chunking strategies.

* **Retrieval:** The process of finding the most relevant text chunks for a given query.

* **Generation:** Using a Large Language Model (LLM) to create a response based on the retrieved context and the user's query. We use the `meta-llama/Llama-3.2-3B-Instruct` model via Nebius AI's API.

* **Evaluation:** Assessing the quality of the RAG system's responses, often by comparing them to a reference answer or using an LLM to score relevance.

## 🤝 Contributing

[](#-contributing)

Contributions are welcome!


