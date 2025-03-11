---
title: "xiaozhi-esp32 后端服务: 快速搭建 ESP32 设备控制服务器"
slug: xiaozhi-esp32-server
description: |
  本项目为开源智能硬件项目xiaozhi-esp32提供后端服务，帮助用户快速搭建ESP32设备控制服务器。该服务通过Python实现，支持多种LLM和TTS接口，适合有ESP32硬件设备的用户。
tags: 
  - AI
  - dev
  - opensource
  - tool
  - management
pubDatetime: 2025-03-11T15:30:03+08:00
ogImage: 
---

[原文链接](https://github.com/xinnan-tech/xiaozhi-esp32-server)

---

[![SVG Banners](https://camo.githubusercontent.com/3bcda9aec5a26b8f79a08500662474f1767a2c37dea4b910d89b50abd7a3dc25/68747470733a2f2f7376672d62616e6e6572732e76657263656c2e6170702f6170693f747970653d6f726967696e2674657874313d2545342542442541302545352541352542442546302539462539382538332545462542432538432545352542302538462545362539392542412546302539462539332539462674657874323d2545352542432538302545362542412539302545352542302538462545362539392542414553502d33322545352539302538452545372541422541462545362539432538442545352538412541312677696474683d383330266865696768743d323130)](https://github.com/xinnan-tech/xiaozhi-esp32-server)

[![GitHub Contributors](https://camo.githubusercontent.com/d99edbbaca6465bf7bddaf83e57313b2244f64080cb4ce7d307c894a97be6187/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6e7472696275746f72732f78696e6e616e2d746563682f7869616f7a68692d65737033322d736572766572) ](https://github.com/xinnan-tech/xiaozhi-esp32-server/graphs/contributors)[![Issues](https://camo.githubusercontent.com/39bcb0377d37a6db6e7714b9dd475f96f881153a01183d5cf9113f6cb0d193ec/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f78696e6e616e2d746563682f7869616f7a68692d65737033322d7365727665723f636f6c6f723d303038386666) ](https://github.com/xinnan-tech/xiaozhi-esp32-server/issues)[![GitHub pull requests](https://camo.githubusercontent.com/020685151c0045703307e68fb552b0099e8f1765b6b8558a6bee62b258ee9121/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732d70722f78696e6e616e2d746563682f7869616f7a68692d65737033322d7365727665723f636f6c6f723d303038386666)](https://github.com/xinnan-tech/xiaozhi-esp32-server/pulls)

# 小智 ESP-32 后端服务(xiaozhi-esp32-server)

[](#小智-esp-32-后端服务xiaozhi-esp32-server)

（中文 | [English](https://github.com/xinnan-tech/xiaozhi-esp32-server/blob/main/README_en.md)）

本项目为开源智能硬件项目 [xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) 提供后端服务。根据 [小智通信协议](https://ccnphfhqs21z.feishu.cn/wiki/M0XiwldO9iJwHikpXD5cEx71nKh) 使用 `Python` 实现。

***

## 适用人群 👥

[](#适用人群-)

本项目需要配合 ESP32 硬件设备使用。如果您已经购买了 ESP32 相关硬件，且成功对接过虾哥部署的后端服务，并希望独立搭建自己的 `xiaozhi-esp32` 后端服务，那么本项目非常适合您。

想看使用效果？请猛戳视频 🎥

|                                                                                                                                      |                                                                                                                           |                                                                                                                            |                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [![小智esp32连接自己的后台模型](/xinnan-tech/xiaozhi-esp32-server/raw/main/docs/images/demo1.png)](https://www.bilibili.com/video/BV1FMFyejExX) | [![自定义音色](/xinnan-tech/xiaozhi-esp32-server/raw/main/docs/images/demo2.png)](https://www.bilibili.com/video/BV1CDKWemEU6) | [![使用粤语交流](/xinnan-tech/xiaozhi-esp32-server/raw/main/docs/images/demo3.png)](https://www.bilibili.com/video/BV12yA2egEaC) | [![控制家电开关](/xinnan-tech/xiaozhi-esp32-server/raw/main/docs/images/demo5.png)](https://www.bilibili.com/video/av114036381327149) |
| [![自定义音色](/xinnan-tech/xiaozhi-esp32-server/raw/main/docs/images/demo6.png)](https://www.bilibili.com/video/BV1Vy96YCE3R)            | [![播放音乐](/xinnan-tech/xiaozhi-esp32-server/raw/main/docs/images/demo7.png)](https://www.bilibili.com/video/BV1VC96Y5EMH)  | [![成本最低配置](/xinnan-tech/xiaozhi-esp32-server/raw/main/docs/images/demo4.png)](https://www.bilibili.com/video/BV1kgA2eYEQ9) |                                                                                                                                 |

***

## 系统要求与部署前提 🖥️

[](#系统要求与部署前提-️)

* **硬件**：一套兼容 `xiaozhi-esp32` 的硬件设备（具体型号请参考 [此处](https://rcnv1t9vps13.feishu.cn/wiki/DdgIw4BUgivWDPkhMj1cGIYCnRf)）。

* **电脑或服务器**：至少 4 核 CPU、8G 内存的电脑。

* **固件编译**：请将本后端服务的接口地址更新至 `xiaozhi-esp32` 项目中，再重新编译`xiaozhi-esp32`固件并烧录到设备上。

如果你没有esp32相关的硬件设备，但是非常想体验该项目，可以使用以下的项目让你的电脑、手机模拟成esp32设备。

* [小智安卓端](https://github.com/TOM88812/xiaozhi-android-client)
* [小智电脑端](https://github.com/Huang-junsen/py-xiaozhi)

***

## 警告 ⚠️

[](#警告-️)

1、本项目为开源软件，本软件与对接的任何第三方API服务商（包括但不限于语音识别、大模型、语音合成等平台）均不存在商业合作关系，不为其服务质量及资金安全提供任何形式的担保。 建议使用者优先选择持有相关业务牌照的服务商，并仔细阅读其服务协议及隐私政策。本软件不托管任何账户密钥、不参与资金流转、不承担充值资金损失风险。

2、本项目成立时间较短，还未通过网络安全测评，请勿在生产环境中使用。 如果您在公网环境中部署学习本项目，请务必在配置文件 `config.yaml` 中开启防护：

```
server:
  auth:
    # 开启防护
    enabled: true  
```

开启防护后，您需要根据实际情况校验机器的 token 或 mac 地址，详细请参见配置说明。

***

## 功能清单 ✨

[](#功能清单-)

### 已实现 ✅

[](#已实现-)

* **通信协议**\
  基于 `xiaozhi-esp32` 协议，通过 WebSocket 实现数据交互。
* **对话交互**\
  支持唤醒对话、手动对话及实时打断。长时间无对话时自动休眠
* **意图识别**\
  支持使用LLM意图识别、function call函数调用，减少硬编码意图判断
* **多语言识别**\
  支持国语、粤语、英语、日语、韩语（默认使用 FunASR）。
* **LLM 模块**\
  支持灵活切换 LLM 模块，默认使用 ChatGLMLLM，也可选用阿里百炼、DeepSeek、Ollama 等接口。
* **TTS 模块**\
  支持 EdgeTTS（默认）、火山引擎豆包 TTS 等多种 TTS 接口，满足语音合成需求。
* **记忆功能**\
  支持超长记忆、本地总结记忆、无记忆三种模式，满足不同场景需求。

### 正在开发 🚧

[](#正在开发-)

* 多种心情模式
* 智控台webui
* iot功能

## [![图片](/xinnan-tech/xiaozhi-esp32-server/raw/main/docs/images/webui.png)](https://github.com/xinnan-tech/xiaozhi-esp32-server/blob/main/docs/images/webui.png)

[](#)

## 本项目支持的平台/组件列表 📋

[](#本项目支持的平台组件列表-)

### LLM 语言模型

[](#llm-语言模型)

|  类型 |        平台名称        |          使用方式         |     收费模式    |                                                            备注                                                            |
| :-: | :----------------: | :-------------------: | :---------: | :----------------------------------------------------------------------------------------------------------------------: |
| LLM |    阿里百炼 (AliLLM)   |      openai 接口调用      |   消耗 token  |                              [点击申请密钥](https://bailian.console.aliyun.com/?apiKey=1#/api-key)                             |
| LLM |      DoubaoLLM     |      openai 接口调用      |   消耗 token  | [点击申请密钥](https://console.volcengine.com/ark/region:ark+cn-beijing/model/detail?Id=doubao-pro-32k\&projectName=undefined) |
| LLM | 深度求索 (DeepSeekLLM) |      openai 接口调用      |   消耗 token  |                                         [点击申请密钥](https://platform.deepseek.com/)                                         |
| LLM |   智谱（ChatGLMLLM）   |      openai 接口调用      |      免费     |                             虽然免费，仍需[点击申请密钥](https://bigmodel.cn/usercenter/proj-mgmt/apikeys)                            |
| LLM |      OllamaLLM     |      ollama 接口调用      | 免费/消耗 token |                                   需预先下载模型（`ollama pull`），服务地址：`http://localhost:11434`                                   |
| LLM |       DifyLLM      |       dify 接口调用       | 免费/消耗 token |                                                本地化部署，注意配置提示词需在 Dify 控制台设置                                                |
| LLM |     FastgptLLM     |      fastgpt 接口调用     | 免费/消耗 token |                                               本地化部署，注意配置提示词需在 Fastgpt 控制台设置                                              |
| LLM |      GeminiLLM     |      gemini 接口调用      |      免费     |                                       [点击申请密钥](https://aistudio.google.com/apikey)                                       |
| LLM |       CozeLLM      |       coze 接口调用       |   消耗 token  |                                                需提供 bot\_id、user\_id 及个人令牌                                                |
| LLM |   Home Assistant   | homeassistant语音助手接口调用 |      免费     |                                                    需提供home assistant令牌                                                   |

实际上，任何支持 openai 接口调用的 LLM 均可接入使用。

***

### TTS 语音合成

[](#tts-语音合成)

|  类型 |          平台名称          | 使用方式 |   收费模式   |                                             备注                                            |
| :-: | :--------------------: | :--: | :------: | :---------------------------------------------------------------------------------------: |
| TTS |         EdgeTTS        | 接口调用 |    免费    |                                     默认 TTS，基于微软语音合成技术                                     |
| TTS | 火山引擎豆包 TTS (DoubaoTTS) | 接口调用 | 消耗 token |         [点击创建密钥](https://console.volcengine.com/speech/service/8)；建议使用付费版本以获得更高并发         |
| TTS |        AliyunTTS       | 接口调用 | 消耗 token |                  [点击创建密钥](https://nls-portal.console.aliyun.com/applist)                  |
| TTS |  CosyVoiceSiliconflow  | 接口调用 | 消耗 token |                                  需申请硅基流动 API 密钥；输出格式为 wav                                 |
| TTS |        TTS302AI        | 接口调用 | 消耗 token |                          [点击创建密钥](https://dash.302.ai/apis/list)                          |
| TTS |        CozeCnTTS       | 接口调用 | 消耗 token |                                 需提供 Coze API key；输出格式为 wav                                |
| TTS |         ACGNTTS        | 接口调用 | 消耗 token | [联系网站管理员购买密钥](https://github.com/xinnan-tech/xiaozhi-esp32-server/blob/main/www.ttson.cn) |
| TTS |        OpenAITTS       | 接口调用 | 消耗 token |                                         境外使用，境外购买                                         |
| TTS |       FishSpeech       | 接口调用 |  免费/自定义  |                                  本地启动 TTS 服务；启动方法见配置文件内说明                                 |
| TTS |     GPT\_SOVITS\_V2    | 接口调用 |  免费/自定义  |                                  本地启动 TTS 服务，适用于个性化语音合成场景                                 |
| TTS |     GPT\_SOVITS\_V3    | 接口调用 |  免费/自定义  |                                  本地启动 TTS 服务，适用于个性化语音合成场景                                 |
| TTS |       MinimaxTTS       | 接口调用 |  免费/自定义  |                                  本地启动 TTS 服务，适用于个性化语音合成场景                                 |

***

### VAD 语音活动检测

[](#vad-语音活动检测)

|  类型 |    平台名称   | 使用方式 | 收费模式 |  备注 |
| :-: | :-------: | :--: | :--: | :-: |
| VAD | SileroVAD | 本地使用 |  免费  |     |

***

### ASR 语音识别

[](#asr-语音识别)

|  类型 |    平台名称   | 使用方式 | 收费模式 |  备注 |
| :-: | :-------: | :--: | :--: | :-: |
| ASR |   FunASR  | 本地使用 |  免费  |     |
| ASR | DoubaoASR | 接口调用 |  收费  |     |

***

### Memory 记忆存储

[](#memory-记忆存储)

|   类型   |        平台名称       | 使用方式 |   收费模式   |  备注 |
| :----: | :---------------: | :--: | :------: | :-: |
| Memory |       mem0ai      | 接口调用 | 100次/月额度 |     |
| Memory | mem\_local\_short | 本地总结 |    免费    |     |

***

### Intent 意图识别

[](#intent-意图识别)

|   类型   |      平台名称      | 使用方式 |   收费模式  |           备注          |
| :----: | :------------: | :--: | :-----: | :-------------------: |
| Intent |   intent\_llm  | 接口调用 | 根据LLM收费 |     通过大模型识别意图，通用性强    |
| Intent | function\_call | 接口调用 | 根据LLM收费 | 通过大模型函数调用完成意图，速度快，效果好 |

***

## 使用方式 🚀

[](#使用方式-)

### 一、[部署文档](https://github.com/xinnan-tech/xiaozhi-esp32-server/blob/main/docs/Deployment.md)

[](#一部署文档)

本项目支持以下三种部署方式，您可根据实际需求选择。

本项目的文档主要是`文字版本`的教程，如果你想要`视频版本` 的教程，您可以学习一下[这个大佬的手把手教程](https://www.bilibili.com/video/BV1gePuejEvT)。

如果你能把`文字版本的教程`和`视频版本的教程`结合起来一起看，可以让你更快上手。

1. [Docker 快速部署](https://github.com/xinnan-tech/xiaozhi-esp32-server/blob/main/docs/Deployment.md)

适合快速体验的普通用户，不需过多环境配置。缺点是，拉取镜像有点慢。

2. [借助 Docker 环境运行部署](https://github.com/xinnan-tech/xiaozhi-esp32-server/blob/main/docs/Deployment.md#%E6%96%B9%E5%BC%8F%E4%BA%8C%E5%80%9F%E5%8A%A9docker%E7%8E%AF%E5%A2%83%E8%BF%90%E8%A1%8C%E9%83%A8%E7%BD%B2)

适用于已安装 Docker 且希望对代码进行自定义修改的软件工程师。

3. [本地源码运行](https://github.com/xinnan-tech/xiaozhi-esp32-server/blob/main/docs/Deployment.md#%E6%96%B9%E5%BC%8F%E4%B8%89%E6%9C%AC%E5%9C%B0%E6%BA%90%E7%A0%81%E8%BF%90%E8%A1%8C)

适合熟悉`Conda` 环境或希望从零搭建运行环境的用户。

对于对响应速度要求较高的场景，推荐使用本地源码运行方式以降低额外开销。

### 二、[固件编译](https://github.com/xinnan-tech/xiaozhi-esp32-server/blob/main/docs/firmware-build.md)

[](#二固件编译)

点这里查看[固件编译](https://github.com/xinnan-tech/xiaozhi-esp32-server/blob/main/docs/firmware-build.md)的详细过程。

烧录成功且联网成功后，通过唤醒词唤醒小智，留意server端输出的控制台信息。

***

## 常见问题 ❓

[](#常见问题-)

### 1、为什么我说的话，小智识别出来很多韩文、日文、英文？🇰🇷

[](#1为什么我说的话小智识别出来很多韩文日文英文)

建议：检查一下`models/SenseVoiceSmall`是否已经有`model.pt` 文件，如果没有就要下载，查看这里[下载语音识别模型文件](https://github.com/xinnan-tech/xiaozhi-esp32-server/blob/main/docs/Deployment.md#%E6%A8%A1%E5%9E%8B%E6%96%87%E4%BB%B6)

### 2、为什么会出现“TTS 任务出错 文件不存在”？📁

[](#2为什么会出现tts-任务出错-文件不存在)

建议：检查一下是否正确使用`conda` 安装了`libopus`和`ffmpeg`库。

如果没有安装，就安装

```
conda install conda-forge::libopus
conda install conda-forge::ffmpeg
```

### 3、TTS 经常失败，经常超时 ⏰

[](#3tts-经常失败经常超时-)

建议：如果 `EdgeTTS` 经常失败，请先检查是否使用了代理（梯子）。如果使用了，请尝试关闭代理后再试；\
如果用的是火山引擎的豆包 TTS，经常失败时建议使用付费版本，因为测试版本仅支持 2 个并发。

### 4、如何提高小智对话响应速度？ ⚡

[](#4如何提高小智对话响应速度-)

本项目默认配置为低成本方案，建议初学者先使用默认免费模型，解决“跑得动”的问题，再优化“跑得快”。\
如需提升响应速度，可尝试更换各组件。以下为各组件的响应速度测试数据（仅供参考，不构成承诺）：

|  影响因素 |        因素值       |
| :---: | :--------------: |
|  测试地点 |     广东省广州市海珠区    |
|  测试时间 | 2025年2月19日 12:52 |
| 宽带运营商 |       中国联通       |

测试方法：

1、把各组件的密钥配置上去，只有配置了密钥的组件才参与测试。

2、配置完密钥后，执行以下方法

```
# 进入项目根目录，执行以下命令：
conda activate xiaozhi-esp32-server
python performance_tester.py 
```

生成报告如下

LLM 性能排行:

| 模块名称       | 平均首Token时间 | 平均总响应时间 |
| :--------- | :--------- | :------ |
| AliLLM     | 0.547s     | 1.485s  |
| ChatGLMLLM | 0.677s     | 3.057s  |

TTS 性能排行:

| 模块名称                 | 平均合成时间 |
| -------------------- | ------ |
| EdgeTTS              | 1.019s |
| DoubaoTTS            | 0.503s |
| CosyVoiceSiliconflow | 3.732s |

推荐配置组合 (综合响应速度):

| 组合方案                          | 综合得分  | LLM首Token | TTS合成  |
| ----------------------------- | ----- | --------- | ------ |
| AliLLM + DoubaoTTS            | 0.539 | 0.547s    | 0.503s |
| AliLLM + EdgeTTS              | 0.642 | 0.547s    | 1.019s |
| ChatGLMLLM + DoubaoTTS        | 0.642 | 0.677s    | 0.503s |
| ChatGLMLLM + EdgeTTS          | 0.745 | 0.677s    | 1.019s |
| AliLLM + CosyVoiceSiliconflow | 1.184 | 0.547s    | 3.732s |

### 结论 🔍

[](#结论-)

`2025年2月19日`，如果我的电脑在`广东省广州市海珠区`，且使用的是`中国联通`网络，我会优先使用：

* LLM：`AliLLM`
* TTS：`DoubaoTTS`

### 5、我说话很慢，停顿时小智老是抢话 🗣️

[](#5我说话很慢停顿时小智老是抢话-️)

建议：在配置文件中找到如下部分，将 `min_silence_duration_ms` 的值调大（例如改为 `1000`）：

```
VAD:
  SileroVAD:
    threshold: 0.5
    model_dir: models/snakers4_silero-vad
    min_silence_duration_ms: 700  # 如果说话停顿较长，可将此值调大
```

### 6、我想通过小智控制电灯、空调、远程开关机等操作 💡

[](#6我想通过小智控制电灯空调远程开关机等操作-)

建议：在配置文件中将 `LLM` 设置为 `HomeAssistant`，通过 调用`HomeAssistant`接口实现相关控制。

### 7、更多问题，可联系我们反馈 💬

[](#7更多问题可联系我们反馈-)

我们的联系方式放在[百度网盘中,点击前往](https://pan.baidu.com/s/1x6USjvP1nTRsZ45XlJu65Q)，提取码是`223y`。

网盘里有“硬件烧录QQ群”、“开源服务端交流群”、“产品建议联系人” 三张图片，请根据需要选择加入。

* 硬件烧录QQ群：适用于硬件烧录问题
* 开源服务端交流群：适用于服务端问题
* 产品建议联系人：适用于产品功能、产品设计等建议

***

## 鸣谢 🙏

[](#鸣谢-)

* 本项目受 [百聆语音对话机器人](https://github.com/wwbin2017/bailing) 启发，并在其基础上实现。
* 感谢 [十方融海](https://www.tenclass.com/) 对小智通讯协议提供的详尽文档支持。

[![Star History Chart](https://camo.githubusercontent.com/d191b350249fdb74a8de6dd0a6efc353db1049be1bd1ca720123c68b81a056a8/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d78696e6e616e2d746563682f7869616f7a68692d65737033322d73657276657226747970653d44617465)](https://star-history.com/#xinnan-tech/xiaozhi-esp32-server\&Date)


