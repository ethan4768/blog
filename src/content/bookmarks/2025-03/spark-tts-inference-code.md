---
title: "Spark-TTS：一个高效的基于LLM的文本转语音模型推理代码"
slug: spark-tts-inference-code
description: |
  Spark-TTS是一个高级文本转语音系统，利用大型语言模型（LLM）实现高质量和自然的语音合成。该项目提供推理代码，旨在高效、灵活，适合研究和生产使用。支持中英文零样本语音克隆，具有可控的语音生成能力，适用于多种应用场景。
tags: 
  - AI
  - audio
  - LLM
  - tool
  - opensource
pubDatetime: 2025-03-26T13:18:48+08:00
ogImage: https://opengraph.githubassets.com/373d87accbdcb43f1adbe4e2d7936a9cb97a214e2be49cdd72f84a2a89a609e9/SparkAudio/Spark-TTS
---

[原文链接](https://github.com/SparkAudio/Spark-TTS?tab=readme-ov-file)

---

# Spark-TTS   Spark 语音合成

[](#----spark-tts----)

Official PyTorch code for inference of官方 PyTorch 代码用于推理\
***Spark-TTS: An Efficient LLM-Based Text-to-Speech Model with Single-Stream Decoupled Speech TokensSpark-TTS：基于 LLM 的高效文本转语音模型，具有单流解耦语音标记***

[![Spark-TTS Logo](/SparkAudio/Spark-TTS/raw/main/src/logo/SparkTTS.jpg)](https://github.com/SparkAudio/Spark-TTS/blob/main/src/logo/SparkTTS.jpg)

[![Institution 1](/SparkAudio/Spark-TTS/raw/main/src/logo/HKUST.jpg)](https://github.com/SparkAudio/Spark-TTS/blob/main/src/logo/HKUST.jpg) [![Institution 2](/SparkAudio/Spark-TTS/raw/main/src/logo/mobvoi.jpg)](https://github.com/SparkAudio/Spark-TTS/blob/main/src/logo/mobvoi.jpg) [![Institution 3](/SparkAudio/Spark-TTS/raw/main/src/logo/SJU.jpg)](https://github.com/SparkAudio/Spark-TTS/blob/main/src/logo/SJU.jpg)

[![Institution 4](/SparkAudio/Spark-TTS/raw/main/src/logo/NTU.jpg)](https://github.com/SparkAudio/Spark-TTS/blob/main/src/logo/NTU.jpg) [![Institution 5](/SparkAudio/Spark-TTS/raw/main/src/logo/NPU.jpg)](https://github.com/SparkAudio/Spark-TTS/blob/main/src/logo/NPU.jpg) [![Institution 6](/SparkAudio/Spark-TTS/raw/main/src/logo/SparkAudio2.jpg)](https://github.com/SparkAudio/Spark-TTS/blob/main/src/logo/SparkAudio2.jpg)

[![paper](https://camo.githubusercontent.com/4d10ac1ff2fccd3ae1974d16ac70c95678e45025c94851249dffb88b6cfbd039/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617065722d41725869762d726564)](https://arxiv.org/pdf/2503.01710)[![version](https://camo.githubusercontent.com/1f285962aba99055f825cdefa8fbd822eb30ee4423050236de0008320c5d5d55/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f44656d6f2d506167652d6c6967687467726579)](https://sparkaudio.github.io/spark-tts/)[![Hugging Face](https://camo.githubusercontent.com/ac7531af0f31e6212a4e27330fb492073994ad2707a7a9c647faa0e39c4237f9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f48756767696e67253230466163652d4d6f64656c253230506167652d79656c6c6f77)](https://huggingface.co/SparkAudio/Spark-TTS-0.5B)[![version](https://camo.githubusercontent.com/d1abd4ca80a147660b380e49ccdf33861ff7135484fbc97c570ffec7bce5364e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506c6174666f726d2d6c696e75782d6c6967687467726579)](https://github.com/SparkAudio/Spark-TTS)[![version](https://camo.githubusercontent.com/b511c4733f3aeed7d4f4dc8d6d3d1fae6a4f67ebd2ffb0df9aa06516b2f6d3df/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31322b2d6f72616e6765)](https://github.com/SparkAudio/Spark-TTS)[![python](https://camo.githubusercontent.com/2e9267db3b82a2eb7a4bd1e1ab67466564b775775740994cf7917896f365832a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5079546f7263682d322e352b2d627269676874677265656e)](https://github.com/SparkAudio/Spark-TTS)[![mit](https://camo.githubusercontent.com/859a1a0bc85ce8bbd7a730a274fec5c9e77c4726ffdf6aa762a78685e26033a4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d417061636865253230322e302d626c75652e737667)](https://github.com/SparkAudio/Spark-TTS)

## Spark-TTS 🔥

[](#spark-tts-)

### Overview  概述

[](#overview)

Spark-TTS is an advanced text-to-speech system that uses the power of large language models (LLM) for highly accurate and natural-sounding voice synthesis. It is designed to be efficient, flexible, and powerful for both research and production use.Spark-TTS 是一种先进的文本转语音系统，它利用大型语言模型 (LLM) 的强大功能实现高度准确且听起来自然的语音合成。它旨在高效、灵活且功能强大，适合研究和生产用途。

### Key Features  主要特点

[](#key-features)

* **Simplicity and Efficiency**: Built entirely on Qwen2.5, Spark-TTS eliminates the need for additional generation models like flow matching. Instead of relying on separate models to generate acoustic features, it directly reconstructs audio from the code predicted by the LLM. This approach streamlines the process, improving efficiency and reducing complexity.**简单高效&#x20;**：Spark-TTS 完全基于 Qwen2.5 构建，无需使用流匹配等额外生成模型。它无需依赖单独的模型来生成声学特征，而是直接从预测的代码中重建音频。这种方法简化了流程，提高了效率并降低了复杂性。
* **High-Quality Voice Cloning**: Supports zero-shot voice cloning, which means it can replicate a speaker's voice even without specific training data for that voice. This is ideal for cross-lingual and code-switching scenarios, allowing for seamless transitions between languages and voices without requiring separate training for each one.**高质量语音克隆&#x20;**：支持零样本语音克隆，这意味着即使没有针对该语音的特定训练数据，它也可以复制说话者的声音。这非常适合跨语言和代码切换场景，允许在语言和语音之间无缝转换，而无需对每种语言和语音进行单独训练。
* **Bilingual Support**: Supports both Chinese and English, and is capable of zero-shot voice cloning for cross-lingual and code-switching scenarios, enabling the model to synthesize speech in multiple languages with high naturalness and accuracy.**双语支持&#x20;**：支持中英文，并具备跨语言、代码切换场景的零样本语音克隆能力，使模型能够高自然度、高准确度地合成多种语言的语音。
* **Controllable Speech Generation**: Supports creating virtual speakers by adjusting parameters such as gender, pitch, and speaking rate.**可控的语音生成&#x20;**：支持通过调整性别、音调、语速等参数创建虚拟说话人。

***

|                                                                                                                                                                                                                  |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| **Inference Overview of Voice Cloning语音克隆推理概述** [![](/SparkAudio/Spark-TTS/raw/main/src/figures/infer_voice_cloning.png)](https://github.com/SparkAudio/Spark-TTS/blob/main/src/figures/infer_voice_cloning.png) |
|   **Inference Overview of Controlled Generation受控发电的推理概述** [![](/SparkAudio/Spark-TTS/raw/main/src/figures/infer_control.png)](https://github.com/SparkAudio/Spark-TTS/blob/main/src/figures/infer_control.png)  |

## 🚀 News  🚀 新闻

[](#-news)

* **\[2025-03-04]** Our paper on this project has been published! You can read it here: [Spark-TTS](https://arxiv.org/pdf/2503.01710).**\[2025-03-04]** 我们关于这个项目的论文已经发表！你可以在这里阅读： [Spark-TTS](https://arxiv.org/pdf/2503.01710) 。

* **\[2025-03-12]** Nvidia Triton Inference Serving is now supported. See the Runtime section below for more details.**\[2025-03-12]** 现已支持 Nvidia Triton Inference Serving。有关更多详细信息，请参阅下面的运行时部分。

## Install  安装

[](#install)

**Clone and Install  克隆并安装**

Here are instructions for installing on Linux. If you're on Windows, please refer to the [Windows Installation Guide](https://github.com/SparkAudio/Spark-TTS/issues/5).以下是在 Linux 上安装的说明。如果您使用的是 Windows，请参阅 [Windows 安装指南 ](https://github.com/SparkAudio/Spark-TTS/issues/5)。\
*(Thanks to [@AcTePuKc](https://github.com/AcTePuKc) for the detailed Windows instructions!)（感谢 [@AcTePuKc](https://github.com/AcTePuKc) 提供详细的 Windows 说明！）*

* Clone the repo  克隆仓库

```
git clone https://github.com/SparkAudio/Spark-TTS.git
cd Spark-TTS
```

* Install Conda: please see <https://docs.conda.io/en/latest/miniconda.html>安装 Conda：请参阅 <https://docs.conda.io/en/latest/miniconda.html>

* Create Conda env:  创建 Conda 环境：

```
conda create -n sparktts -y python=3.12
conda activate sparktts
pip install -r requirements.txt
# If you are in mainland China, you can set the mirror as follows:
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com
```

**Model Download  模型下载**

Download via python:  通过 python 下载：

```
from huggingface_hub import snapshot_download

snapshot_download("SparkAudio/Spark-TTS-0.5B", local_dir="pretrained_models/Spark-TTS-0.5B")
```

Download via git clone:  通过 git clone 下载：

```
mkdir -p pretrained_models

# Make sure you have git-lfs installed (https://git-lfs.com)
git lfs install

git clone https://huggingface.co/SparkAudio/Spark-TTS-0.5B pretrained_models/Spark-TTS-0.5B
```

**Basic Usage  基本用法**

You can simply run the demo with the following commands:你可以简单地使用以下命令运行该演示：

```
cd example
bash infer.sh
```

Alternatively, you can directly execute the following command in the command line to perform inference：或者也可以直接在命令行中执行以下命令进行推理：

```
python -m cli.inference \
    --text "text to synthesis." \
    --device 0 \
    --save_dir "path/to/save/audio" \
    --model_dir pretrained_models/Spark-TTS-0.5B \
    --prompt_text "transcript of the prompt audio" \
    --prompt_speech_path "path/to/prompt_audio"
```

**Web UI Usage  Web UI 使用**

You can start the UI interface by running `python webui.py --device 0`, which allows you to perform Voice Cloning and Voice Creation. Voice Cloning supports uploading reference audio or directly recording the audio.您可以通过运行 `python webui.py --device 0` 启动 UI 界面，从而执行语音克隆和语音创建。语音克隆支持上传参考音频或直接录制音频。

|                                                                **Voice Cloning  语音克隆**                                                                |                                                                    **Voice Creation  语音创作**                                                                   |
| :---------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [![Image 1](/SparkAudio/Spark-TTS/raw/main/src/figures/gradio_TTS.png)](https://github.com/SparkAudio/Spark-TTS/blob/main/src/figures/gradio_TTS.png) | [![Image 2](/SparkAudio/Spark-TTS/raw/main/src/figures/gradio_control.png)](https://github.com/SparkAudio/Spark-TTS/blob/main/src/figures/gradio_control.png) |

**Optional Methods  可选方法**

For additional CLI and Web UI methods, including alternative implementations and extended functionalities, you can refer to:有关其他 CLI 和 Web UI 方法，包括替代实现和扩展功能，您可以参考：

* [CLI and UI by AcTePuKcAcTePuKc 提供的 CLI 和 UI](https://github.com/SparkAudio/Spark-TTS/issues/10)

## Runtime  运行

[](#runtime)

**Nvidia Triton Inference ServingNvidia Triton 推理服务**

We now provide a reference for deploying Spark-TTS with Nvidia Triton and TensorRT-LLM. The table below presents benchmark results on a single L20 GPU, using 26 different prompt\_audio/target\_text pairs (totalling 169 seconds of audio):我们现在提供使用 Nvidia Triton 和 TensorRT- 部署 Spark-TTS 的参考。下表显示了单个 L20 GPU 上的基准测试结果，使用了 26 个不同的 prompt\_audio/target\_text 对（总共 169 秒的音频）：

| Model          | Note  笔记                                                                                                                         | Concurrency  并发性 | Avg Latency  平均延迟      | RTF    |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------------------- | ------ |
| Spark-TTS-0.5B | [Code Commit  代码提交](https://github.com/SparkAudio/Spark-TTS/tree/4d769ff782a868524f29e0be851ca64f8b22ebf1/runtime/triton_trtllm) | 1                | 876.24 ms  876.24 毫秒   | 0.1362 |
| Spark-TTS-0.5B | [Code Commit  代码提交](https://github.com/SparkAudio/Spark-TTS/tree/4d769ff782a868524f29e0be851ca64f8b22ebf1/runtime/triton_trtllm) | 2                | 920.97 ms  920.97 毫秒   | 0.0737 |
| Spark-TTS-0.5B | [Code Commit  代码提交](https://github.com/SparkAudio/Spark-TTS/tree/4d769ff782a868524f29e0be851ca64f8b22ebf1/runtime/triton_trtllm) | 4                | 1611.51 ms  1611.51 毫秒 | 0.0704 |

Please see the detailed instructions in [runtime/triton\_trtllm/README.md](https://github.com/SparkAudio/Spark-TTS/blob/main/runtime/triton_trtllm/README.md) for more information.有关更多信息，请参阅 [runtime/triton\_trtllm/README.md](https://github.com/SparkAudio/Spark-TTS/blob/main/runtime/triton_trtllm/README.md) 中的详细说明。

## **Demos  演示**

[](#demos)

Here are some demos generated by Spark-TTS using zero-shot voice cloning. For more demos, visit our [demo page](https://sparkaudio.github.io/spark-tts/).以下是 Spark-TTS 使用零样本语音克隆生成的一些演示。如需更多演示，请访问我们的[演示页面 ](https://sparkaudio.github.io/spark-tts/)。

***

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                                                                                                                                                                                                                                                                                                                                                             **Donald Trump  唐纳德·特朗普**                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                   **Zhongli (Genshin Impact)  钟离（原神）**                                                                                                                                                                                                                                                                                                                                                                                                  |
| Donald\_Trump.webm  唐纳德·特朗普.webm[](https://private-user-images.githubusercontent.com/52398987/417031663-fb225780-d9fe-44b2-9b2e-54390cb3d8fd.webm?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDI5NjYxODUsIm5iZiI6MTc0Mjk2NTg4NSwicGF0aCI6Ii81MjM5ODk4Ny80MTcwMzE2NjMtZmIyMjU3ODAtZDlmZS00NGIyLTliMmUtNTQzOTBjYjNkOGZkLndlYm0_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMyNlQwNTExMjVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03NTdkZDEzMTAyYjFkMjI3MzcyYjJkYmI3MjQ4NDg3M2Y3NzkyNThiYmRkYjBlZTExNjFiOGU1ZTYyYTljMzM2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.YCcQsS4IjBgqxOtg-cduJzKwYFJGaiCmab-aP2HAIdo) | Zhong\_Li.webm  钟丽.webm[](https://private-user-images.githubusercontent.com/52398987/417031589-80eeb9c7-0443-4758-a1ce-55ac59e64bd6.webm?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDI5NjYxODUsIm5iZiI6MTc0Mjk2NTg4NSwicGF0aCI6Ii81MjM5ODk4Ny80MTcwMzE1ODktODBlZWI5YzctMDQ0My00NzU4LWExY2UtNTVhYzU5ZTY0YmQ2LndlYm0_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMyNlQwNTExMjVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xMzIxMTE5ZGU3OGVkMWI0ZTE2ZmEyZTMyNzIxZGZmYjhkODBiN2VhNjRmYWJkNmQ5OGM4ZTQ0OTEzMGYxMzgwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.GpfaSVyR4PxFqPN8iOedhMwaG_H64sukTeCLh_FnZqY) |

***

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                                                                                                                                                                                                                                                                                                                                                             **陈鲁豫 Chen Luyu**                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                             **杨澜 Yang Lan**                                                                                                                                                                                                                                                                                                                                                                                                             |
| Chen\_Luyu.webm  陈鲁豫.webm[](https://private-user-images.githubusercontent.com/52398987/417033449-5c6585ae-830d-47b1-992d-ee3691f48cf4.webm?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDI5NjYxODUsIm5iZiI6MTc0Mjk2NTg4NSwicGF0aCI6Ii81MjM5ODk4Ny80MTcwMzM0NDktNWM2NTg1YWUtODMwZC00N2IxLTk5MmQtZWUzNjkxZjQ4Y2Y0LndlYm0_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMyNlQwNTExMjVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kY2I0NDJkMDBlYzY2Njg5OTJlY2RkMGI4NjViNmIzYWEyYmUyOWM5NWRkZGI0MmU4ZjU1YmJlOWM2Zjg5MzY5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.MVAoOG1JDyD1fCbv6PMrbeHV_ywW8ckiW-OEARLhgL0) | Yang\_Lan.webm  杨澜.webm[](https://private-user-images.githubusercontent.com/52398987/417035253-2fb3d00c-abc3-410e-932f-46ba204fb1d7.webm?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDI5NjYxODUsIm5iZiI6MTc0Mjk2NTg4NSwicGF0aCI6Ii81MjM5ODk4Ny80MTcwMzUyNTMtMmZiM2QwMGMtYWJjMy00MTBlLTkzMmYtNDZiYTIwNGZiMWQ3LndlYm0_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMyNlQwNTExMjVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jYjkxZDUwM2U4YWRiYWI5ZTllMjI0ZTBmN2RjMjE4ZTRlNzkxNzlmMTFkYmU1YjMyNzhhM2IxMDQ4YzI1NjlkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.mXsuljTS-fETTceySm4x5LPMLyDVEFfF-1pIZ6rhjH0) |

***

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                                                                                                                                                                                                                                                                                                                                                              **余承东 Richard Yu**                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                          **马云 Jack Ma**                                                                                                                                                                                                                                                                                                                                                                                                          |
| Yu\_Chengdong.webm  余成栋.webm[](https://private-user-images.githubusercontent.com/52398987/417036927-78feca02-84bb-4d3a-a770-0cfd02f1a8da.webm?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDI5NjYxODUsIm5iZiI6MTc0Mjk2NTg4NSwicGF0aCI6Ii81MjM5ODk4Ny80MTcwMzY5MjctNzhmZWNhMDItODRiYi00ZDNhLWE3NzAtMGNmZDAyZjFhOGRhLndlYm0_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMyNlQwNTExMjVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mMjUzODUyZmQ4YTZiMWE5OGRhOTFlYjkxMjg4ZDA1YmJjNDJiMDA0M2RlYmVkNjM3NDQyZTYyNzJhYjNjOTg0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.2GSFy7Rm046134LO-7-Pn9R01kzjQocaoVCnd2ngjeA) | Ma\_Yun.webm  马云[](https://private-user-images.githubusercontent.com/52398987/417037024-2d54e2eb-cec4-4c2f-8c84-8fe587da321b.webm?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDI5NjYxODUsIm5iZiI6MTc0Mjk2NTg4NSwicGF0aCI6Ii81MjM5ODk4Ny80MTcwMzcwMjQtMmQ1NGUyZWItY2VjNC00YzJmLThjODQtOGZlNTg3ZGEzMjFiLndlYm0_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMyNlQwNTExMjVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iNjBkZjNkMWIxZDAyYTQ2NTQ5ODFjZWM2NGY2MTljZjlhODE2NzQ0ZDIwZjY1ZGRiYWEwNzY4MDc1ZjBhOWYwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.mt_KPBp9AVA6kJXbKVl8SsMu2Aw7xKi7vagMgK0f5cQ) |

***

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                                                                                                                                                                                                                                                                                                                                                              **刘德华 Andy Lau**                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                             **徐志胜 Xu Zhisheng**                                                                                                                                                                                                                                                                                                                                                                                                             |
| Liu\_Dehua.webm  刘德华.webm[](https://private-user-images.githubusercontent.com/52398987/417037108-195b5e97-1fee-4955-b954-6d10fa04f1d7.webm?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDI5NjYxODUsIm5iZiI6MTc0Mjk2NTg4NSwicGF0aCI6Ii81MjM5ODk4Ny80MTcwMzcxMDgtMTk1YjVlOTctMWZlZS00OTU1LWI5NTQtNmQxMGZhMDRmMWQ3LndlYm0_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMyNlQwNTExMjVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xYjlhMTQ2NjdjMTczYWM4NDY2Yjg3MDIyOTc2NjM4MTZjNTQwYjI3OTY2OTMwODJhOTNmMGRmOTZkNzQ3NmQ1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.hNpQGAYC0QLrHZh6Np00FhtWTinDVNng2uxtqb34iE0) | Xu\_Zhisheng.webm  徐志胜.webm[](https://private-user-images.githubusercontent.com/52398987/417037286-dd812af9-76bd-4e26-9988-9cdb9ccbb87b.webm?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDI5NjYxODUsIm5iZiI6MTc0Mjk2NTg4NSwicGF0aCI6Ii81MjM5ODk4Ny80MTcwMzcyODYtZGQ4MTJhZjktNzZiZC00ZTI2LTk5ODgtOWNkYjljY2JiODdiLndlYm0_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMyNlQwNTExMjVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zODk0MGM2Y2MyNTVhYTAxYWQxNWJkYTM4Nzc5OWM0NGMzNDBiNzAwMmY1ZGY2OWM2MGQxZDhmY2EwNzRhN2E0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.j9PE2EspuA6kUAZ3NkUAiy7U5IjmUwowxDYpJKjd1KA) |

***

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                                                                                                                                                                                                                                                                                                                                                              **哪吒 Nezha**                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                             **李靖 Li Jing**                                                                                                                                                                                                                                                                                                                                                                                                             |
| Ne\_Zha.webm  哪吒.webm[](https://private-user-images.githubusercontent.com/52398987/417037436-8c608037-a17a-46d4-8588-4db34b49ed1d.webm?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDI5NjYxODUsIm5iZiI6MTc0Mjk2NTg4NSwicGF0aCI6Ii81MjM5ODk4Ny80MTcwMzc0MzYtOGM2MDgwMzctYTE3YS00NmQ0LTg1ODgtNGRiMzRiNDllZDFkLndlYm0_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMyNlQwNTExMjVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mMDhjYTg4ZDBhMTg2OTNjNjZmNTJkNDg1MDU4OWZkYmU3MWRlN2M3ZDQxM2UyNGQwM2I5ZGY1YTI3MDQyNjkwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.8uhzQzDM4mQBLM9-xXd8eLsPoE3uRkQBIvubHOCrr_U) | Li\_Jing.webm  李静.webm[](https://private-user-images.githubusercontent.com/52398987/417037687-aa8ba091-097c-4156-b4e3-6445da5ea101.webm?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDI5NjYxODUsIm5iZiI6MTc0Mjk2NTg4NSwicGF0aCI6Ii81MjM5ODk4Ny80MTcwMzc2ODctYWE4YmEwOTEtMDk3Yy00MTU2LWI0ZTMtNjQ0NWRhNWVhMTAxLndlYm0_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMyNlQwNTExMjVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yZDI3ZDIxNDIxM2MwMzMxMzI5ODFmOWFiZmIwMjhkNjViYzAxYWZlZmRlYTAzMTkyNjlkMjgzZDU3MmYwYzRkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.usJY_puSXrgMTkumtrlm0S5KC-Zv7N18PL8rQU2vGu0) |

## To-Do List  待办事项清单

[](#to-do-list)

* [x] Release the Spark-TTS paper.发布 Spark-TTS 论文。
* [ ] Release the training code.发布训练代码。
* [ ] Release the training dataset, VoxBox.发布训练数据集 VoxBox。

## Citation  引用

[](#citation)

```
@misc{wang2025sparktts,
      title={Spark-TTS: An Efficient LLM-Based Text-to-Speech Model with Single-Stream Decoupled Speech Tokens}, 
      author={Xinsheng Wang and Mingqi Jiang and Ziyang Ma and Ziyu Zhang and Songxiang Liu and Linqin Li and Zheng Liang and Qixi Zheng and Rui Wang and Xiaoqin Feng and Weizhen Bian and Zhen Ye and Sitong Cheng and Ruibin Yuan and Zhixian Zhao and Xinfa Zhu and Jiahao Pan and Liumeng Xue and Pengcheng Zhu and Yunlin Chen and Zhifei Li and Xie Chen and Lei Xie and Yike Guo and Wei Xue},
      year={2025},
      eprint={2503.01710},
      archivePrefix={arXiv},
      primaryClass={cs.SD},
      url={https://arxiv.org/abs/2503.01710}, 
}
```

## ⚠️ Usage Disclaimer   ⚠️ 使用免责声明

[](#️-usage-disclaimer)

This project provides a zero-shot voice cloning TTS model intended for academic research, educational purposes, and legitimate applications, such as personalized speech synthesis, assistive technologies, and linguistic research.该项目提供了零样本语音克隆 TTS 模型，旨在用于学术研究、教育目的和合法应用，例如个性化语音合成、辅助技术和语言研究。

Please note:  请注意：

* Do not use this model for unauthorized voice cloning, impersonation, fraud, scams, deepfakes, or any illegal activities.请勿将此模型用于未经授权的语音克隆、冒充、欺诈、诈骗、深度伪造或任何非法活动。

* Ensure compliance with local laws and regulations when using this model and uphold ethical standards.确保使用该模型时遵守当地法律法规并遵守道德标准。

* The developers assume no liability for any misuse of this model.开发人员对于此模型的任何误用不承担任何责任。

We advocate for the responsible development and use of AI and encourage the community to uphold safety and ethical principles in AI research and applications. If you have any concerns regarding ethics or misuse, please contact us.我们提倡负责任地开发和使用人工智能，并鼓励社区在人工智能研究和应用中坚持安全和道德原则。如果您对道德或滥用有任何疑虑，请联系我们。


