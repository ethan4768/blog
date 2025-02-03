---
title: "Sonic：聚焦全球音频感知的肖像动画官方实现"
slug: sonic-global-audio-perception
description: |
  Sonic是一个专注于肖像动画中全球音频感知的工具。其官方实现可以在[GitHub](https://github.com/jixiaozhong/Sonic)找到，提供了多种功能，包括演示和模型下载。了解更多关于Sonic的最新动态和开发更新。
tags: 
  - AI
  - audio
  - tool
  - opensource
  - dev
pubDatetime: 2025-02-03T09:56:55+08:00
ogImage: https://opengraph.githubassets.com/90c0a7630322bb5da05da36fc1608524b7f39b9354713f72bd8b21d7c1d92eef/jixiaozhong/Sonic
---

[原文链接](https://github.com/jixiaozhong/Sonic)

---

# Sonic

[](#sonic)

Sonic: Shifting Focus to Global Audio Perception in Portrait Animation

[![](https://camo.githubusercontent.com/bf3933961c03cc78ffde90f26e4a3376b69d4efd5b7c54936d89419b6085c055/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50726f6a6563742d506167652d477265656e)](https://jixiaozhong.github.io/Sonic/) [![Demo](https://camo.githubusercontent.com/c57f8b331cb8aa9f2bc8270c93c6a492fe1a53cba672a60bea1fc06009a7da61/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f44656d6f2d47726164696f2d676f6c643f7374796c653d666c6174266c6f676f3d47726164696f266c6f676f436f6c6f723d726564) ](http://demo.sonic.jixiaozhong.online/)[![](https://camo.githubusercontent.com/c4067caad6706c9a5130b5a77c4961d46463f51f051aaa1be0fcaf9d5f164183/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617065722d41727869762d726564)](https://arxiv.org/pdf/2411.16331) [![Demo](https://camo.githubusercontent.com/f3e8a15ba4968bb6be2b79dfb212ba843f823b759a8a1985dab98df886e9c09a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53706163652d5a65726f4750552d6f72616e67653f7374796c653d666c6174266c6f676f3d47726164696f266c6f676f436f6c6f723d726564) ](https://huggingface.co/spaces/xiaozhongji/Sonic)[![License](https://camo.githubusercontent.com/43c88798b139cc885e8608218638de0da6abd5f64e96e8ab03dc1336c9c41b11/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d43432042592d2d4e432d2d53412d2d342e302d6c69676874677265656e3f7374796c653d666c6174266c6f676f3d4c6973656e6365)](https://raw.githubusercontent.com/jixiaozhong/Sonic/refs/heads/main/LICENSE)

👋 Join our [QQ Chat Group](https://github.com/jixiaozhong/Sonic/blob/main/examples/image/QQ.png)

## 🔥🔥🔥 NEWS

[](#-news)

**`2025/01/17`**: Our [**Online huggingface Demo**](https://huggingface.co/spaces/xiaozhongji/Sonic/) is released.

**`2025/01/17`**: Thank you to NewGenAI for promoting our Sonic and creating a Windows-based tutorial on [**YouTube**](https://www.youtube.com/watch?v=KiDDtcvQyS0).

**`2024/12/16`**: Our [**Online Demo**](http://demo.sonic.jixiaozhong.online/) is released.

## 🎥 Demo

[](#-demo)

| Input                                                                                                                                  | Output                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Input                                                                                                                                                | Output                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [![](/jixiaozhong/Sonic/raw/main/examples/image/anime1.png)](https://github.com/jixiaozhong/Sonic/blob/main/examples/image/anime1.png) | anime1.mp4[](https://private-user-images.githubusercontent.com/8861423/405063517-636c3ff5-210e-44b8-b901-acf828071133.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzg1NDgwOTUsIm5iZiI6MTczODU0Nzc5NSwicGF0aCI6Ii84ODYxNDIzLzQwNTA2MzUxNy02MzZjM2ZmNS0yMTBlLTQ0YjgtYjkwMS1hY2Y4MjgwNzExMzMubXA0P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDIwMyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAyMDNUMDE1NjM1WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9N2UxZGYxYzlmMDRjYmQ1Njk5MzhhYzdhMThmOWNhMjg5MzZlNTViNjhjNDhiYmM1NGRhYTBjMzBmNTE4MmFiMyZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.NEzrUivUyavw3qPkQf3S_fqpdtM2R0fi5cK2kAYfgmY) | [![](/jixiaozhong/Sonic/raw/main/examples/image/female_diaosu.png)](https://github.com/jixiaozhong/Sonic/blob/main/examples/image/female_diaosu.png) | female\_diaosu.mp4[](https://private-user-images.githubusercontent.com/8861423/405063654-e8207300-2569-47d1-9ad4-4b4c9b0f0bd4.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzg1NDgwOTUsIm5iZiI6MTczODU0Nzc5NSwicGF0aCI6Ii84ODYxNDIzLzQwNTA2MzY1NC1lODIwNzMwMC0yNTY5LTQ3ZDEtOWFkNC00YjRjOWIwZjBiZDQubXA0P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDIwMyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAyMDNUMDE1NjM1WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZjQ2MGZhMTNlN2NjNDRkNjBjOTY2ZDhiM2MyYjQ3NmU0ODQ3NzNlMThmZDYxZmZmNDRhYzQ2M2RjMTczNGUwNSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.hIrkYfLqteccUiarwAryf70fUXWnC8hj9ZH-ONiuJH4) |
| [![](/jixiaozhong/Sonic/raw/main/examples/image/hair.png)](https://github.com/jixiaozhong/Sonic/blob/main/examples/image/hair.png)     | hair.mp4[](https://private-user-images.githubusercontent.com/8861423/405063734-dcb755c1-de01-4afe-8b4f-0e0b2c2439c1.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzg1NDgwOTUsIm5iZiI6MTczODU0Nzc5NSwicGF0aCI6Ii84ODYxNDIzLzQwNTA2MzczNC1kY2I3NTVjMS1kZTAxLTRhZmUtOGI0Zi0wZTBiMmMyNDM5YzEubXA0P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDIwMyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAyMDNUMDE1NjM1WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MDYxODcxODYxMjBiOTFjNzc1MGQ5NTIwZDk0ZTZjM2RhOTAxYTk3NzNjYTRlODkyOTU1ZWM1MzZmYWIxMmZjMyZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.I7ajxzjYQ83VdW9R_7VhS3XpCoVkquhk7ECyA8bRjVk)   | [![](/jixiaozhong/Sonic/raw/main/examples/image/leonnado.jpg)](https://github.com/jixiaozhong/Sonic/blob/main/examples/image/leonnado.jpg)           | leonnado.mp4[](https://private-user-images.githubusercontent.com/8861423/405063780-b50e61bb-62d4-469d-b402-b37cda3fbd27.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzg1NDgwOTUsIm5iZiI6MTczODU0Nzc5NSwicGF0aCI6Ii84ODYxNDIzLzQwNTA2Mzc4MC1iNTBlNjFiYi02MmQ0LTQ2OWQtYjQwMi1iMzdjZGEzZmJkMjcubXA0P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDIwMyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAyMDNUMDE1NjM1WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9OGViNWNlZmRhMmQ2YjNjZGZlMDk2ZTVlNzQxZDhmOGI4ODYwNGI3Y2ExNWI1YTI1NDAwYTdmMTY2NmE5NjM5NiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.m-qkdBFggw1a7hvgDCXiUsRFTSg6zXf19k58BMv3Vho)       |

For more visual demos, please visit our [**Page**](https://jixiaozhong.github.io/Sonic/).

## 🧩 Community Contributions

[](#-community-contributions)

If you develop/use Sonic in your projects, welcome to let us know.

## 📑 Updates

[](#-updates)

**`2025/01/14`**: Our inference code and weights are released. Stay tuned, we will continue to polish the model.

## 📜 Requirements

[](#-requirements)

* An NVIDIA GPU with CUDA support is required.
  * The model is tested on a single 32G GPU.
* Tested operating system: Linux

## 🔑 Inference

[](#-inference)

### Installtion

[](#installtion)

* install pytorch

```
  pip3 install -r requirements.txt
```

* All models are stored in `checkpoints` by default, and the file structure is as follows

```
Sonic
  ├──checkpoints
  │  ├──Sonic
  │  │  ├──audio2bucket.pth
  │  │  ├──audio2token.pth
  │  │  ├──unet.pth
  │  ├──stable-video-diffusion-img2vid-xt
  │  │  ├──...
  │  ├──whisper-tiny
  │  │  ├──...
  │  ├──RIFE
  │  │  ├──flownet.pkl
  │  ├──yoloface_v5m.pt
  ├──...
```

Download by `huggingface-cli` follow

```
  python3 -m pip install "huggingface_hub[cli]"
  huggingface-cli download LeonJoe13/Sonic --local-dir  checkpoints
  huggingface-cli download stabilityai/stable-video-diffusion-img2vid-xt --local-dir  checkpoints/stable-video-diffusion-img2vid-xt
  huggingface-cli download openai/whisper-tiny --local-dir checkpoints/whisper-tiny
```

or manully download [pretrain model](https://drive.google.com/drive/folders/1oe8VTPUy0-MHHW2a_NJ1F8xL-0VN5G7W?usp=drive_link), [svd-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) and [whisper-tiny](https://huggingface.co/openai/whisper-tiny) to checkpoints/

### Run demo

[](#run-demo)

```
  python3 demo.py \
  '/path/to/input_image' \
  '/path/to/input_audio' \
  '/path/to/output_video'
```

## 🔗 Citation

[](#-citation)

```
@misc{ji2024sonicshiftingfocusglobal,
      title={Sonic: Shifting Focus to Global Audio Perception in Portrait Animation}, 
      author={Xiaozhong Ji and Xiaobin Hu and Zhihong Xu and Junwei Zhu and Chuming Lin and Qingdong He and Jiangning Zhang and Donghao Luo and Yi Chen and Qin Lin and Qinglin Lu and Chengjie Wang},
      year={2024},
      eprint={2411.16331},
      archivePrefix={arXiv},
      primaryClass={cs.MM},
      url={https://arxiv.org/abs/2411.16331}, 
}
```

## 📈 Star History

[](#-star-history)

[![Star History Chart](https://camo.githubusercontent.com/4b942676285897c300f4e83dacfacfc2f0e57d390236d4f8ece1b8450105fbe3/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d6a697869616f7a686f6e672f536f6e696326747970653d44617465)](https://star-history.com/#jixiaozhong/Sonic\&Date)


