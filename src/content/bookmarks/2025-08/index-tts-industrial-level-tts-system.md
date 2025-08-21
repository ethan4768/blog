---
title: "IndexTTS：工业级可控高效的零样本文本转语音系统"
slug: index-tts-industrial-level-tts-system
description: |
  IndexTTS是一个基于GPT风格的工业级文本转语音（TTS）系统，具有高效的可控性和零样本能力。它通过拼音纠正汉字发音，优化停顿控制，并实现超越当前主流TTS系统的性能。体验最新的IndexTTS，尽在此处！
tags: 
  - AI
  - tts
pubDatetime: 2025-08-21T10:26:49+08:00
ogImage: https://opengraph.githubassets.com/ad6468cfa74cac689df9b5a785f783f1b9be00bd8e82de7cd09687626177edc9/index-tts/index-tts
---

[原文链接](https://github.com/index-tts/index-tts)

---

[![](/index-tts/index-tts/raw/main/assets/index_icon.png)](https://github.com/index-tts/index-tts/blob/main/assets/index_icon.png)

## IndexTTS: An Industrial-Level Controllable and Efficient Zero-Shot Text-To-Speech SystemIndexTTS：工业级可控高效零样本文本转语音系统

[](#indextts-an-industrial-level-controllable-and-efficient-zero-shot-text-to-speech-system)

[![](https://camo.githubusercontent.com/16dc1905dfa9f885e3df9fe4016765ffcbf48162b83d4a3c2dab351dcbb670db/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f41725869762d323530322e30353531322d726564)](https://arxiv.org/abs/2502.05512)

## 👉🏻 IndexTTS 👈🏻  👉🏻 索引 TTS 👈🏻

[](#-indextts-)

[\[HuggingFace Demo\]](https://huggingface.co/spaces/IndexTeam/IndexTTS) [\[ModelScope Demo\]](https://modelscope.cn/studios/IndexTeam/IndexTTS-Demo)[\[HuggingFace 演示\]](https://huggingface.co/spaces/IndexTeam/IndexTTS)[\[ModelScope 演示\]](https://modelscope.cn/studios/IndexTeam/IndexTTS-Demo)\
[\[Paper\]](https://arxiv.org/abs/2502.05512) [\[Demos\]](https://index-tts.github.io)[\[论文\]](https://arxiv.org/abs/2502.05512)[\[演示\]](https://index-tts.github.io)

**IndexTTS** is a GPT-style text-to-speech (TTS) model mainly based on XTTS and Tortoise. It is capable of correcting the pronunciation of Chinese characters using pinyin and controlling pauses at any position through punctuation marks. We enhanced multiple modules of the system, including the improvement of speaker condition feature representation, and the integration of BigVGAN2 to optimize audio quality. Trained on tens of thousands of hours of data, our system achieves state-of-the-art performance, outperforming current popular TTS systems such as XTTS, CosyVoice2, Fish-Speech, and F5-TTS.**IndexTTS** 是一种主要基于 XTTS 和 Tortoise 的 GPT 风格的文本转语音 （TTS） 模型。它能够使用拼音纠正汉字的发音，并通过标点符号控制任意位置的停顿。我们增强了系统的多个模块，包括改进扬声器条件特征表示，以及集成 BigVGAN2 以优化音频质量。我们的系统经过数万小时的数据训练，实现了最先进的性能，优于当前流行的 TTS 系统，如 XTTS、CosyVoice2、Fish-Speech 和 F5-TTS。Experience **IndexTTS**: Please contact <xuanwu@bilibili.com> for more detailed information.体验**指数 TTS**：请联系 <xuanwu@bilibili.com> 了解更多详细信息。

### Contact  联系

[](#contact)

QQ群（二群）：1048202584\
Discord：<https://discord.gg/uT32E7KDmy>不和谐：<https://discord.gg/uT32E7KDmy>\
简历：<indexspeech@bilibili.com>\
欢迎大家来交流讨论！

## 📣 Updates  📣 更新

[](#-updates)

* `2025/05/14` 🔥🔥 We release the **IndexTTS-1.5**, Significantly improve the model's stability and its performance in the English language.`2025/05/14` 🔥🔥 我们发布了 **IndexTTS-1.5**，显着提高了模型的稳定性和英语性能。
* `2025/03/25` 🔥 We release IndexTTS-1.0 model parameters and inference code.`2025/03/25` 🔥 发布 IndexTTS-1.0 模型参数和推理代码。
* `2025/02/12` 🔥 We submitted our paper on arXiv, and released our demos and test sets.`2025/02/12` 🔥 我们在 arXiv 上提交了论文，并发布了我们的演示和测试集。

## 🖥️ Method  🖥️ 方法

[](#️-method)

The overview of IndexTTS is shown as follows.IndexTTS 概述如下图所示。

![](/index-tts/index-tts/raw/main/assets/IndexTTS.png)

The main improvements and contributions are summarized as follows:主要改进和贡献总结如下：

* In Chinese scenarios, we have introduced a character-pinyin hybrid modeling approach. This allows for quick correction of mispronounced characters.在中文场景中，我们引入了一种字符-拼音混合建模方法。这允许快速纠正发音错误的字符。
* **IndexTTS** incorporate a conformer conditioning encoder and a BigVGAN2-based speechcode decoder. This improves training stability, voice timbre similarity, and sound quality.**IndexTTS** 包含构象构象调节编码器和基于 BigVGAN2 的语音码解码器。这提高了训练稳定性、音色相似性和音质。
* We release all test sets here, including those for polysyllabic words, subjective and objective test sets.我们在这里发布所有测试集，包括多音节单词、主观和客观测试集的测试集。

## Model Download  模型下载

[](#model-download)

| 🤗**HuggingFace**  �&#xDD17;**&#x20;拥抱脸**                                     | **ModelScope  模型作用域**                                                           |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [IndexTTS  索引 TTS](https://huggingface.co/IndexTeam/Index-TTS)                | [IndexTTS  索引 TTS](https://modelscope.cn/models/IndexTeam/Index-TTS)            |
| [😁IndexTTS-1.5  😁索引 TTS-1.5](https://huggingface.co/IndexTeam/IndexTTS-1.5) | [IndexTTS-1.5  索引 TTS-1.5](https://modelscope.cn/models/IndexTeam/IndexTTS-1.5) |

## 📑 Evaluation  📑 评估

[](#-evaluation)

**Word Error Rate (WER) Results for IndexTTS and Baseline Models on the** [**seed-test**](https://github.com/BytedanceSpeech/seed-tts-eval)[**种子测试**](https://github.com/BytedanceSpeech/seed-tts-eval)**中 IndexTTS 和基线模型的单词错误率 （WER） 结果**

|            **WER**           | **test\_zh** | **test\_en** | **test\_hard** |
| :--------------------------: | :----------: | :----------: | :------------: |
|         **Human  人**         |     1.26     |     2.14     |        -       |
|      **SeedTTS  种子 TTS**     |     1.002    |     1.945    |    **6.243**   |
|    **CosyVoice 2  舒适之声 2**   |     1.45     |     2.57     |      6.83      |
|           **F5TTS**          |     1.56     |     1.83     |      8.67      |
|    **FireRedTTS  火红 TTS**    |     1.51     |     3.82     |      17.45     |
|          **MaskGCT**         |     2.27     |     2.62     |      10.27     |
|     **Spark-TTS  火花-TTS**    |      1.2     |     1.98     |        -       |
|    **MegaTTS 3  超级 TTS 3**   |     1.36     |     1.82     |        -       |
|     **IndexTTS  索引 TTS**     |     0.937    |     1.936    |      6.831     |
| **IndexTTS-1.5  索引 TTS-1.5** |   **0.821**  |   **1.606**  |      6.565     |

**Word Error Rate (WER) Results for IndexTTS and Baseline Models on the other opensource test另一个开源测试中 IndexTTS 和基线模型的单词错误率 （WER） 结果**

|           **Model**          | **aishell1\_test** | **commonvoice\_20\_test\_zh** | **commonvoice\_20\_test\_en** | **librispeech\_test\_clean** | **avg** |
| :--------------------------: | :----------------: | :---------------------------: | :---------------------------: | :--------------------------: | :-----: |
|         **Human  人**         |         2.0        |              9.5              |              10.0             |              2.4             |   5.1   |
|    **CosyVoice 2  舒适之声 2**   |         1.8        |              9.1              |              7.3              |              4.9             |   5.9   |
|           **F5TTS**          |         3.9        |              11.7             |              5.4              |              7.8             |   8.2   |
|      **Fishspeech  鱼语**      |         2.4        |              11.4             |              8.8              |              8.0             |   8.3   |
|    **FireRedTTS  火红 TTS**    |         2.2        |              11.0             |              16.3             |              5.7             |   7.7   |
|           **XTTS**           |         3.0        |              11.4             |              7.1              |              3.5             |   6.0   |
|     **IndexTTS  索引 TTS**     |         1.3        |              7.0              |              5.3              |              2.1             |   3.7   |
| **IndexTTS-1.5  索引 TTS-1.5** |       **1.2**      |            **6.8**            |            **3.9**            |            **1.7**           | **3.1** |

**Speaker Similarity (SS) Results for IndexTTS and Baseline ModelsIndexTTS 和基线模型的说话人相似度 （SS） 结果**

|           **Model**          | **aishell1\_test** | **commonvoice\_20\_test\_zh** | **commonvoice\_20\_test\_en** | **librispeech\_test\_clean** |  **avg**  |
| :--------------------------: | :----------------: | :---------------------------: | :---------------------------: | :--------------------------: | :-------: |
|         **Human  人**         |        0.846       |             0.809             |             0.820             |             0.858            |   0.836   |
|    **CosyVoice 2  舒适之声 2**   |      **0.796**     |             0.743             |             0.742             |           **0.837**          | **0.788** |
|           **F5TTS**          |        0.743       |           **0.747**           |             0.746             |             0.828            |   0.779   |
|      **Fishspeech  鱼语**      |        0.488       |             0.552             |             0.622             |             0.701            |   0.612   |
|    **FireRedTTS  火红 TTS**    |        0.579       |             0.593             |             0.587             |             0.698            |   0.631   |
|           **XTTS**           |        0.573       |             0.586             |             0.648             |             0.761            |   0.663   |
|     **IndexTTS  索引 TTS**     |        0.744       |             0.742             |           **0.758**           |             0.823            |   0.776   |
| **IndexTTS-1.5  索引 TTS-1.5** |        0.741       |             0.722             |             0.753             |             0.819            |   0.771   |

**MOS Scores for Zero-Shot Cloned Voice零样本克隆语音的 MOS 分数**

| **Model**               | **Prosody  韵律** | **Timbre  音色** | **Quality  质量** |  **AVG** |
| ----------------------- | :-------------: | :------------: | :-------------: | :------: |
| **CosyVoice 2  舒适之声 2** |       3.67      |      4.05      |       3.73      |   3.81   |
| **F5TTS**               |       3.56      |      3.88      |       3.56      |   3.66   |
| **Fishspeech  鱼语**      |       3.40      |      3.63      |       3.69      |   3.57   |
| **FireRedTTS  火红 TTS**  |       3.79      |      3.72      |       3.60      |   3.70   |
| **XTTS**                |       3.23      |      2.99      |       3.10      |   3.11   |
| **IndexTTS  索引 TTS**    |     **3.79**    |    **4.20**    |     **4.05**    | **4.01** |

## Usage Instructions  使用说明

[](#usage-instructions)

### Environment Setup  环境设置

[](#environment-setup)

1. Download this repository:下载此存储库：

```
git clone https://github.com/index-tts/index-tts.git
```

2. Install dependencies:  安装依赖项：

Create a new conda environment and install dependencies:创建新的 conda 环境并安装依赖项：

```
conda create -n index-tts python=3.10
conda activate index-tts
apt-get install ffmpeg
# or use conda to install ffmpeg
conda install -c conda-forge ffmpeg
```

Install [PyTorch](https://pytorch.org/get-started/locally/), e.g.:安装 [PyTorch](https://pytorch.org/get-started/locally/)，例如：

```
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118
```

Note  注意

If you are using Windows you may encounter [an error](https://github.com/index-tts/index-tts/issues/61) when installing `pynini`: `ERROR: Failed building wheel for pynini` In this case, please install `pynini` via `conda`:如果您使用的是 Windows，则在安装 `pynini` 时可能会遇到[错误 ](https://github.com/index-tts/index-tts/issues/61)： `ERROR: Failed building wheel for pynini` 在这种情况下，请通过 `conda` 安装 `pynini`：

```
# after conda activate index-tts
conda install -c conda-forge pynini==2.1.6
pip install WeTextProcessing --no-deps
```

Install `IndexTTS` as a package:将 `IndexTTS` 作为包安装：

```
cd index-tts
pip install -e .
```

3. Download models:  下载型号：

Download by `huggingface-cli`:通过 `huggingface-cli` 下载：

```
huggingface-cli download IndexTeam/IndexTTS-1.5 \
  config.yaml bigvgan_discriminator.pth bigvgan_generator.pth bpe.model dvae.pth gpt.pth unigram_12000.vocab \
  --local-dir checkpoints
```

Recommended for China users. 如果下载速度慢，可以使用镜像：

```
export HF_ENDPOINT="https://hf-mirror.com"
```

Or by `wget`:  或者通过 `wget`：

```
wget https://huggingface.co/IndexTeam/IndexTTS-1.5/resolve/main/bigvgan_discriminator.pth -P checkpoints
wget https://huggingface.co/IndexTeam/IndexTTS-1.5/resolve/main/bigvgan_generator.pth -P checkpoints
wget https://huggingface.co/IndexTeam/IndexTTS-1.5/resolve/main/bpe.model -P checkpoints
wget https://huggingface.co/IndexTeam/IndexTTS-1.5/resolve/main/dvae.pth -P checkpoints
wget https://huggingface.co/IndexTeam/IndexTTS-1.5/resolve/main/gpt.pth -P checkpoints
wget https://huggingface.co/IndexTeam/IndexTTS-1.5/resolve/main/unigram_12000.vocab -P checkpoints
wget https://huggingface.co/IndexTeam/IndexTTS-1.5/resolve/main/config.yaml -P checkpoints
```

Note  注意

If you prefer to use the `IndexTTS-1.0` model, please replace `IndexTeam/IndexTTS-1.5` with `IndexTeam/IndexTTS` in the above commands.如果您更喜欢使用 `IndexTTS-1.0` 模型，请在上述命令中将 `IndexTeam/IndexTTS-1.5` 替换为 `IndexTeam/IndexTTS`。

4. Run test script:  运行测试脚本：

```
# Please put your prompt audio in 'test_data' and rename it to 'input.wav'
python indextts/infer.py
```

5. Use as command line tool:用作命令行工具：

```
# Make sure pytorch has been installed before running this command
indextts "大家好，我现在正在bilibili 体验 ai 科技，说实话，来之前我绝对想不到！AI技术已经发展到这样匪夷所思的地步了！" \
  --voice reference_voice.wav \
  --model_dir checkpoints \
  --config checkpoints/config.yaml \
  --output output.wav
```

Use `--help` to see more options.使用 `--help` 查看更多选项。

```
indextts --help
```

#### Web Demo  网络演示

[](#web-demo)

```
pip install -e ".[webui]" --no-build-isolation
python webui.py

# use another model version:
python webui.py --model_dir IndexTTS-1.5
```

Open your browser and visit `http://127.0.0.1:7860` to see the demo.打开浏览器并访问 `http://127.0.0.1:7860` 查看演示。

#### Sample Code  示例代码

[](#sample-code)

```
from indextts.infer import IndexTTS
tts = IndexTTS(model_dir="checkpoints",cfg_path="checkpoints/config.yaml")
voice="reference_voice.wav"
text="大家好，我现在正在bilibili 体验 ai 科技，说实话，来之前我绝对想不到！AI技术已经发展到这样匪夷所思的地步了！比如说，现在正在说话的其实是B站为我现场复刻的数字分身，简直就是平行宇宙的另一个我了。如果大家也想体验更多深入的AIGC功能，可以访问 bilibili studio，相信我，你们也会吃惊的。"
tts.infer(voice, text, output_path)
```

## Acknowledge  承认

[](#acknowledge)

1. [tortoise-tts  -TTS](https://github.com/neonbjb/tortoise-tts)
2. [XTTSv2](https://github.com/coqui-ai/TTS)
3. [BigVGAN  大 VGAN](https://github.com/NVIDIA/BigVGAN)
4. [wenet  韦内特](https://github.com/wenet-e2e/wenet/tree/main)
5. [icefall  冰瀑](https://github.com/k2-fsa/icefall)

## 📚 Citation  📚 引文

[](#-citation)

🌟 If you find our work helpful, please leave us a star and cite our paper.🌟 如果您觉得我们的工作有帮助，请给我们留下星号并引用我们的论文。

```
@article{deng2025indextts,
  title={IndexTTS: An Industrial-Level Controllable and Efficient Zero-Shot Text-To-Speech System},
  author={Wei Deng, Siyi Zhou, Jingchen Shu, Jinchao Wang, Lu Wang},
  journal={arXiv preprint arXiv:2502.05512},
  year={2025}
}
```


