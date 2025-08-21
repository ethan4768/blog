---
title: "F5-TTS：一个伪造流利与忠实语音的童话故事生成工具"
slug: f5-tts-fairytale-speech-synthesis
description: |
  F5-TTS 是一款通过流量匹配生成流利忠实语音的童话故事工具，基于扩散变压器和 ConvNeXt V2。该工具支持多种语言，提供了快速的推理与训练方法。立即体验，提升您的语音合成效果！
tags: 
  - AI
  - opensource
  - tts
pubDatetime: 2025-08-21T10:26:20+08:00
ogImage: https://opengraph.githubassets.com/4b8514916fe4172a95dc0cc5f0e0f3fb6078a719aef1a410a18dbd16ccbc9c28/SWivid/F5-TTS
---

[原文链接](https://github.com/SWivid/F5-TTS)

---

# F5-TTS: A Fairytaler that Fakes Fluent and Faithful Speech with Flow MatchingF5-TTS：通过流量匹配伪造流利忠实语音的童话故事

[](#f5-tts-a-fairytaler-that-fakes-fluent-and-faithful-speech-with-flow-matching)

[![python](https://camo.githubusercontent.com/729dd5f03bac108f24899b73fa15736c1e2a953c81cf0ca13c3c4913f11f4c26/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31302d627269676874677265656e)](https://github.com/SWivid/F5-TTS) [![arXiv](https://camo.githubusercontent.com/8c97b85cae0e49a09ad6842ab2c9c80caba9639b3826192eef8e451258c5732a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f61725869762d323431302e30363838352d6233316231622e7376673f6c6f676f3d6172586976)](https://arxiv.org/abs/2410.06885) [![demo](https://camo.githubusercontent.com/4f79bac2c13fd77aa7d019ba3747a3c884c4cdaeed7102289323365c72409ddf/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d44656d6f253230706167652d6f72616e67652e737667)](https://swivid.github.io/F5-TTS/) [![hfspace](https://camo.githubusercontent.com/35ac16d7b4178e35196575e1069538b7a92958d0f8dbd2edf6e712b8e709fbe5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2546302539462541342539372d537061636525323064656d6f2d79656c6c6f77)](https://huggingface.co/spaces/mrfakename/E2-F5-TTS) [![msspace](https://camo.githubusercontent.com/7f0eb0fb9b09c265fcfc997bc46384507fe7782b929c66a7c51f01dd2a47bfc7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2546302539462541342539362d537061636525323064656d6f2d626c7565)](https://modelscope.cn/studios/modelscope/E2-F5-TTS) [![lab](https://camo.githubusercontent.com/40d03f48fc249b11708e45792f18d52312b72de09d4d1f5439f7f111774cd2ad/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f582d2d4c414e43452d4c61622d677265793f6c6162656c436f6c6f723d6c6967687467726579)](https://x-lance.sjtu.edu.cn/) [![lab](https://camo.githubusercontent.com/91a1ad32b58ceff07f77c59d7b5b0b4fec3d65eb143c3027fde576af7f0c0610/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50656e672532304368656e672d4c61622d677265793f6c6162656c436f6c6f723d6c6967687467726579)](https://www.pcl.ac.cn)

**F5-TTS**: Diffusion Transformer with ConvNeXt V2, faster trained and inference.**F5-TTS**：采用 ConvNeXt V2 的扩散变压器，训练和推理速度更快。

**E2 TTS**: Flat-UNet Transformer, closest reproduction from [paper](https://arxiv.org/abs/2406.18009).**E2 TTS**：Flat-UNet Transformer，最接近[纸张](https://arxiv.org/abs/2406.18009)复制品。

**Sway Sampling**: Inference-time flow step sampling strategy, greatly improves performance**摇摆采样&#x20;**：推理时间流步长采样策略，大幅提升性能

### Thanks to all the contributors !感谢所有贡献者！

[](#thanks-to-all-the-contributors-)

## News  新闻

[](#news)

* **2025/03/12**: 🔥 F5-TTS v1 base model with better training and inference performance. [Few demo](https://swivid.github.io/F5-TTS_updates).**2025/03/12**： 🔥 F5-TTS v1 基础模型，具有更好的训练和推理性能。[ 很少有演示 ](https://swivid.github.io/F5-TTS_updates)。
* **2024/10/08**: F5-TTS & E2 TTS base models on [🤗 Hugging Face](https://huggingface.co/SWivid/F5-TTS), [🤖 Model Scope](https://www.modelscope.cn/models/SWivid/F5-TTS_Emilia-ZH-EN), [🟣 Wisemodel](https://wisemodel.cn/models/SJTU_X-LANCE/F5-TTS_Emilia-ZH-EN).**2024/10/08**： [Hugging Face、Model Scope、Wisemodel 上的 🤗](https://huggingface.co/SWivid/F5-TTS) F5-TTS 和 E2 TTS 基础模型。 [🟣](https://wisemodel.cn/models/SJTU_X-LANCE/F5-TTS_Emilia-ZH-EN) [🤖](https://www.modelscope.cn/models/SWivid/F5-TTS_Emilia-ZH-EN)

## Installation  安装

[](#installation)

### Create a separate environment if needed如果需要，请创建单独的环境

[](#create-a-separate-environment-if-needed)

```
# Create a python 3.10 conda env (you could also use virtualenv)
conda create -n f5-tts python=3.10
conda activate f5-tts
```

### Install PyTorch with matched device使用匹配的设备安装 PyTorch

[](#install-pytorch-with-matched-device)

NVIDIA GPU  英伟达 GPU

> ```
> # Install pytorch with your CUDA version, e.g.
> pip install torch==2.4.0+cu124 torchaudio==2.4.0+cu124 --extra-index-url https://download.pytorch.org/whl/cu124
> ```

AMD GPU  AMD 显卡

> ```
> # Install pytorch with your ROCm version (Linux only), e.g.
> pip install torch==2.5.1+rocm6.2 torchaudio==2.5.1+rocm6.2 --extra-index-url https://download.pytorch.org/whl/rocm6.2
> ```

Intel GPU  英特尔 GPU

> ```
> # Install pytorch with your XPU version, e.g.
> # Intel® Deep Learning Essentials or Intel® oneAPI Base Toolkit must be installed
> pip install torch torchaudio --index-url https://download.pytorch.org/whl/test/xpu
>
> # Intel GPU support is also available through IPEX (Intel® Extension for PyTorch)
> # IPEX does not require the Intel® Deep Learning Essentials or Intel® oneAPI Base Toolkit
> # See: https://pytorch-extension.intel.com/installation?request=platform
> ```

Apple Silicon  苹果硅

> ```
> # Install the stable pytorch, e.g.
> pip install torch torchaudio
> ```

### Then you can choose one from below:然后您可以从以下中选择一个：

[](#then-you-can-choose-one-from-below)

> ### 1. As a pip package (if just for inference)1. 作为 pip 包（如果只是为了推理）
>
> [](#1-as-a-pip-package-if-just-for-inference)
>
> ```
> pip install f5-tts
> ```
>
> ### 2. Local editable (if also do training, finetuning)2. 本地可编辑（如果也做训练、微调）
>
> [](#2-local-editable-if-also-do-training-finetuning)
>
> ```
> git clone https://github.com/SWivid/F5-TTS.git
> cd F5-TTS
> # git submodule update --init --recursive  # (optional, if use bigvgan as vocoder)
> pip install -e .
> ```

### Docker usage also available也提供 Docker 使用

[](#docker-usage-also-available)

```
# Build from Dockerfile
docker build -t f5tts:v1 .

# Run from GitHub Container Registry
docker container run --rm -it --gpus=all --mount 'type=volume,source=f5-tts,target=/root/.cache/huggingface/hub/' -p 7860:7860 ghcr.io/swivid/f5-tts:main

# Quickstart if you want to just run the web interface (not CLI)
docker container run --rm -it --gpus=all --mount 'type=volume,source=f5-tts,target=/root/.cache/huggingface/hub/' -p 7860:7860 ghcr.io/swivid/f5-tts:main f5-tts_infer-gradio --host 0.0.0.0
```

### Runtime  运行

[](#runtime)

Deployment solution with Triton and TensorRT-LLM.使用 Triton 和 TensorRT-LLM 的部署解决方案。

#### Benchmark Results  基准测试结果

[](#benchmark-results)

Decoding on a single L20 GPU, using 26 different prompt\_audio & target\_text pairs, 16 NFE.在单个 L20 GPU 上解码，使用 26 个不同的 prompt\_audio 和 target\_text 对，16 个 NFE。

| Model                                  | Concurrency  并发                  | Avg Latency  平均延迟 | RTF    | Mode  模式                    |
| -------------------------------------- | -------------------------------- | ----------------- | ------ | --------------------------- |
| F5-TTS Base (Vocos)  F5-TTS 底座 （Vocos） | 2                                | 253 ms  253 毫秒    | 0.0394 | Client-Server  客户端-服务器      |
| F5-TTS Base (Vocos)  F5-TTS 底座 （Vocos） | 1 (Batch\_size)  1 （Batch\_size） | -                 | 0.0402 | Offline TRT-LLM  离线 TRT-LLM |
| F5-TTS Base (Vocos)  F5-TTS 底座 （Vocos） | 1 (Batch\_size)  1 （Batch\_size） | -                 | 0.1467 | Offline Pytorch  离线 Pytorch |

See [detailed instructions](https://github.com/SWivid/F5-TTS/blob/main/src/f5_tts/runtime/triton_trtllm/README.md) for more information.有关更多信息，请参阅[详细说明 ](https://github.com/SWivid/F5-TTS/blob/main/src/f5_tts/runtime/triton_trtllm/README.md)。

## Inference  推理

[](#inference)

* In order to achieve desired performance, take a moment to read [detailed guidance](https://github.com/SWivid/F5-TTS/blob/main/src/f5_tts/infer).为了达到预期的性能，请花点时间阅读[详细指南 ](https://github.com/SWivid/F5-TTS/blob/main/src/f5_tts/infer)。
* By properly searching the keywords of problem encountered, [issues](https://github.com/SWivid/F5-TTS/issues?q=is%3Aissue) are very helpful.通过正确搜索遇到问题的关键词，[ 问题](https://github.com/SWivid/F5-TTS/issues?q=is%3Aissue)非常有帮助。

### 1. Gradio App  1. Gradio 应用程序

[](#1-gradio-app)

Currently supported features:当前支持的功能：

* Basic TTS with Chunk Inference具有块推理的基本 TTS
* Multi-Style / Multi-Speaker Generation多风格/多扬声器生成
* Voice Chat powered by Qwen2.5-3B-Instruct语音聊天 powered by Qwen2.5-3B-Instruct
* [Custom inference with more language support具有更多语言支持的自定义推理](https://github.com/SWivid/F5-TTS/blob/main/src/f5_tts/infer/SHARED.md)

```
# Launch a Gradio app (web interface)
f5-tts_infer-gradio

# Specify the port/host
f5-tts_infer-gradio --port 7860 --host 0.0.0.0

# Launch a share link
f5-tts_infer-gradio --share
```

NVIDIA device docker compose file exampleNVIDIA 设备 docker compose 文件示例

```
services:
  f5-tts:
    image: ghcr.io/swivid/f5-tts:main
    ports:
      - "7860:7860"
    environment:
      GRADIO_SERVER_PORT: 7860
    entrypoint: ["f5-tts_infer-gradio", "--port", "7860", "--host", "0.0.0.0"]
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]

volumes:
  f5-tts:
    driver: local
```

### 2. CLI Inference  2. CLI 推理

[](#2-cli-inference)

```
# Run with flags
# Leave --ref_text "" will have ASR model transcribe (extra GPU memory usage)
f5-tts_infer-cli --model F5TTS_v1_Base \
--ref_audio "provide_prompt_wav_path_here.wav" \
--ref_text "The content, subtitle or transcription of reference audio." \
--gen_text "Some text you want TTS model generate for you."

# Run with default setting. src/f5_tts/infer/examples/basic/basic.toml
f5-tts_infer-cli
# Or with your own .toml file
f5-tts_infer-cli -c custom.toml

# Multi voice. See src/f5_tts/infer/README.md
f5-tts_infer-cli -c src/f5_tts/infer/examples/multi/story.toml
```

## Training  训练

[](#training)

### 1. With Hugging Face Accelerate1. 与 Hugging Face Accelerate

[](#1-with-hugging-face-accelerate)

Refer to [training & finetuning guidance](https://github.com/SWivid/F5-TTS/blob/main/src/f5_tts/train) for best practice.有关最佳实践，请参阅[培训和微调指南 ](https://github.com/SWivid/F5-TTS/blob/main/src/f5_tts/train)。

### 2. With Gradio App  2. 使用 Gradio 应用程序

[](#2-with-gradio-app)

```
# Quick start with Gradio web interface
f5-tts_finetune-gradio
```

Read [training & finetuning guidance](https://github.com/SWivid/F5-TTS/blob/main/src/f5_tts/train) for more instructions.阅读[培训和微调指南以](https://github.com/SWivid/F5-TTS/blob/main/src/f5_tts/train)获取更多说明。

## [Evaluation  评估](https://github.com/SWivid/F5-TTS/blob/main/src/f5_tts/eval)

[](#evaluation)

## Development  发展

[](#development)

Use pre-commit to ensure code quality (will run linters and formatters automatically):使用预提交来确保代码质量（将自动运行 linter 和格式化程序）：

```
pip install pre-commit
pre-commit install
```

When making a pull request, before each commit, run:在发出拉取请求时，在每次提交之前，运行：

```
pre-commit run --all-files
```

Note: Some model components have linting exceptions for E722 to accommodate tensor notation.注意：某些模型组件对 E722 具有 linting 例外，以适应张量表示法。

## Acknowledgements  确认

[](#acknowledgements)

* [E2-TTS](https://arxiv.org/abs/2406.18009) brilliant work, simple and effective[E2-TTS](https://arxiv.org/abs/2406.18009) 精彩工作，简单有效
* [Emilia](https://arxiv.org/abs/2407.05361), [WenetSpeech4TTS](https://arxiv.org/abs/2406.05763), [LibriTTS](https://arxiv.org/abs/1904.02882), [LJSpeech](https://keithito.com/LJ-Speech-Dataset/) valuable datasets[Emilia](https://arxiv.org/abs/2407.05361)、[WenetSpeech4TTS](https://arxiv.org/abs/2406.05763)、[LibriTTS](https://arxiv.org/abs/1904.02882)、[LJSpeech](https://keithito.com/LJ-Speech-Dataset/) 有价值的数据集
* [lucidrains](https://github.com/lucidrains) initial CFM structure with also [bfs18](https://github.com/bfs18) for discussion[lucidrains](https://github.com/lucidrains) 初始 CFM 结构与 [bfs18](https://github.com/bfs18) 进行讨论
* [SD3](https://arxiv.org/abs/2403.03206) & [Hugging Face diffusers](https://github.com/huggingface/diffusers) DiT and MMDiT code structure[SD3](https://arxiv.org/abs/2403.03206) & [Hugging Face 扩散器 ](https://github.com/huggingface/diffusers)DiT 和 MMDiT 代码结构
* [torchdiffeq](https://github.com/rtqichen/torchdiffeq) as ODE solver, [Vocos](https://huggingface.co/charactr/vocos-mel-24khz) and [BigVGAN](https://github.com/NVIDIA/BigVGAN) as vocoder[torchdiffeq](https://github.com/rtqichen/torchdiffeq) 作为 ODE 求解器，[Vocos](https://huggingface.co/charactr/vocos-mel-24khz) 和 [BigVGAN](https://github.com/NVIDIA/BigVGAN) 作为声码器
* [FunASR](https://github.com/modelscope/FunASR), [faster-whisper](https://github.com/SYSTRAN/faster-whisper), [UniSpeech](https://github.com/microsoft/UniSpeech), [SpeechMOS](https://github.com/tarepan/SpeechMOS) for evaluation tools[FunASR](https://github.com/modelscope/FunASR)、[faster-whisper](https://github.com/SYSTRAN/faster-whisper)、[UniSpeech](https://github.com/microsoft/UniSpeech)、[SpeechMOS](https://github.com/tarepan/SpeechMOS) 评估工具
* [ctc-forced-aligner](https://github.com/MahmoudAshraf97/ctc-forced-aligner) for speech edit test用于语音编辑测试的 [ctc-forced-aligner](https://github.com/MahmoudAshraf97/ctc-forced-aligner)
* [mrfakename](https://x.com/realmrfakename) huggingface space demo \~[MrFakeName](https://x.com/realmrfakename) HuggingFace 空间演示 \~
* [f5-tts-mlx](https://github.com/lucasnewman/f5-tts-mlx/tree/main) Implementation with MLX framework by [Lucas Newman](https://github.com/lucasnewman)[F5-TTS-MLX](https://github.com/lucasnewman/f5-tts-mlx/tree/main)[Lucas Newman](https://github.com/lucasnewman) 使用 MLX 框架实现
* [F5-TTS-ONNX](https://github.com/DakeQQ/F5-TTS-ONNX) ONNX Runtime version by [DakeQQ](https://github.com/DakeQQ)[F5-TTS-ONNX](https://github.com/DakeQQ/F5-TTS-ONNX)[DakeQQ](https://github.com/DakeQQ) 的 ONNX 运行时版本
* [Yuekai Zhang](https://github.com/yuekaizhang) Triton and TensorRT-LLM support \~[张跃凯 ](https://github.com/yuekaizhang)Triton 和 TensorRT-LLM 支持 \~

## Citation  引文

[](#citation)

If our work and codebase is useful for you, please cite as:如果我们的工作和代码库对您有用，请引用：

```
@article{chen-etal-2024-f5tts,
      title={F5-TTS: A Fairytaler that Fakes Fluent and Faithful Speech with Flow Matching}, 
      author={Yushen Chen and Zhikang Niu and Ziyang Ma and Keqi Deng and Chunhui Wang and Jian Zhao and Kai Yu and Xie Chen},
      journal={arXiv preprint arXiv:2410.06885},
      year={2024},
}
```

## License  许可证

[](#license)

Our code is released under MIT License. The pre-trained models are licensed under the CC-BY-NC license due to the training data Emilia, which is an in-the-wild dataset. Sorry for any inconvenience this may cause.我们的代码是在 MIT 许可下发布的。由于训练数据 Emilia，预训练模型在 CC-BY-NC 许可下获得许可，这是一个野外数据集。对于由此造成的任何不便，我们深表歉意。


