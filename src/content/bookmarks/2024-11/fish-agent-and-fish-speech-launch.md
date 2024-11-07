---
title: Fish Audio 团队推出 Fish Agent v0.1 和 Fish Speech 1.4 技术报告
slug: fish-agent-and-fish-speech-launch
description: 🎉 Fish Audio 团队宣布双重发布，推出 Fish Agent v0.1 和 Fish Speech 1.4 技术报告！核心新特性包括：真正的端到端架构、无语义分层、零样本声音克隆、紧凑的3B参数规模，支持文本和音频输入，具备超快的200ms首包延迟。在开发过程中较为便利，官方模型地址敬请关注！
tags: 
  - ai
  - tool
  - dev
  - opensource
pubDatetime: 2024-11-05T22:21:11+08:00
ogImage: https://pbs.twimg.com/media/GbmEQo2bsAEmVMb.jpg
---

[原文链接](https://x.com/shao__meng/status/1853658476326916192?s=12&t=D3VZWD30-f7ylSHW3OdYgQ)

---

🎉 Fish Audio 团队推出 Fish Agent v0.1 + Fish Speech 1.4 技术报告 🚀

## Fish Agent ##

核心新特性:
- 真正的端到端架构 - 无语义分层
- 零样本声音克隆
- 紧凑的 3B 参数规模, 便于开发
- 支持文本和音频输入
- 超快的 200ms 首包延迟(TTFA, Time To First Audio)

模型地址:
https://huggingface.co/fishaudio/fish-agent-v0.1-3b  
在线体验:
https://huggingface.co/spaces/fishaudio/fish-agent

## Fish Speech 1.4 技术报告 ##

# 主要创新点:

- 双自回归架构 (Dual-AR):
    - 引入了由"慢变换器"和"快变换器"组成的串行快慢双自回归架构
    - 慢变换器处理全局语言结构和语义内容
    - 快变换器处理详细的声学特征, 优化 codebook 使用

- 不依赖音素转换:
    - 利用 LLM 直接进行语言特征提取
    - 避免了传统的 grapheme-to-phoneme (G2P) 转换
    - 简化了合成管道, 增强了多语言支持

- FireFly-GAN (FF-GAN):
    - 基于分组有限标量向量量化(GFSQ)的新型声码器架构
    - 实现了接近 100% codebook 利用率
    - 在保持高质量输出的同时提高了压缩比

# 性能优势:

- 多语言支持:
    - 在 720,000 小时的多语言数据上训练
    - 包括英语、中文各 300,000 小时, 以及其他语系各 20,000 小时
    - 能够自然处理混合语言内容

- 推理性能:
    - 在 RTX 4060 上可达到 1:5 的实时率
    - 在 RTX 4090 上可达到 1:15 的实时率
    - 延迟仅 150ms, 远低于其他 TTS 系统

- 实验结果:
    - 词错率(WER)为 6.89%, 优于基准模型
    - 说话人相似度接近真实语音
    - 主观平均意见得分(MOS)达到 4.05

论文地址:
https://huggingface.co/papers/2411.01156