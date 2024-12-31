---
title: "DiffSensei: 利用多模态LLM和扩散模型进行个性化漫画生成的实现"
slug: diffsensei-manga-generation
description: |
  DiffSensei 是一个桥接多模态LLM与扩散模型的项目，实现了可控的黑白漫画面板生成，具备角色适配灵活、分辨率多样等特性，适用于个性化漫画与真实人类漫画创作。此工具让用户能够轻松生成符合自己需求的漫画内容。
tags: 
  - AI
  - dev
  - LLM
  - tool
  - manga
pubDatetime: 2024-12-31T17:32:14+08:00
ogImage: https://opengraph.githubassets.com/d18d3f98a9e3073da4ec11302175efe22be305f8b5a9c1509506c7d7ebc1d8a9/jianzongwu/DiffSensei
---

[原文链接](https://github.com/jianzongwu/DiffSensei)

---

# DiffSensei: Bridging Multi-Modal LLMs and Diffusion Models for Customized Manga Generation

[](#diffsensei-bridging-multi-modal-llms-and-diffusion-models-for-customized-manga-generation)

[![arXiv](https://camo.githubusercontent.com/1b65570a4b6ab3ddc7707ea6cd7f971a29ccc0b120709456e361f1da0be448d6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f61725869762d323431302e30383236312d6233316231622e737667)](https://arxiv.org/abs/2412.07589) [![Project Page](https://camo.githubusercontent.com/e6bc059b5088888a61fbe89e6f96c7981972e793dbe411dcce519ab2ed4b00b9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50726f6a6563742d506167652d626c75653f6c6f676f3d6769746875622d7061676573)](https://jianzongwu.github.io/projects/diffsensei) [![Video](https://camo.githubusercontent.com/9dd58ede110d69f8d3da3708df472aed012b0082611ce6ba033f55dc0b5069df/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f596f75547562652d566964656f2d4646303030303f6c6f676f3d796f7574756265)](https://www.youtube.com/watch?v=TLJ0MYZmoXc\&source_ve_path=OTY3MTQ) [![Checkpoint](https://camo.githubusercontent.com/7241978504df79ac1520ac791f8845444715b4f909e9e979840200eb2204a8be/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67666163652d4d6f64656c2d79656c6c6f77)](https://huggingface.co/jianzongwu/DiffSensei) [![Dataset](https://camo.githubusercontent.com/bb38e885e46a2340798e4043b2b18b877c8349dd39676e385bd8d19e996b3554/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67666163652d446174617365742d79656c6c6f77)](https://huggingface.co/datasets/jianzongwu/MangaZero)

[![Page results caption1](/jianzongwu/DiffSensei/raw/main/assets/images/results_page/caption1.png)](https://github.com/jianzongwu/DiffSensei/blob/main/assets/images/results_page/caption1.png)

[![Page results1](/jianzongwu/DiffSensei/raw/main/assets/images/results_page/1.png)](https://github.com/jianzongwu/DiffSensei/blob/main/assets/images/results_page/1.png)

[![Page results2](/jianzongwu/DiffSensei/raw/main/assets/images/results_page/2.png)](https://github.com/jianzongwu/DiffSensei/blob/main/assets/images/results_page/2.png)

More demos are in our [project page](https://jianzongwu.github.io/projects/diffsensei).

### A story about LeCun, Hinton, and Benjio winning the Novel Prize...

[](#a-story-about-lecun-hinton-and-benjio-winning-the-novel-prize)

[![Long story](/jianzongwu/DiffSensei/raw/main/assets/images/nobel_prize/image.png)](https://github.com/jianzongwu/DiffSensei/blob/main/assets/images/nobel_prize/image.png)

## 🚀 TL;DR

[](#-tldr)

DiffSensei can generate controllable black-and-white manga panels with flexible character adaptation.

[![](/jianzongwu/DiffSensei/raw/main/assets/images/model_architecture.png)](https://github.com/jianzongwu/DiffSensei/blob/main/assets/images/model_architecture.png)

**Key Features:**

* 🌟 Varied-resolution manga panel generation (64-2048 edge size!)
* 🖼️ One input character image, create various appearances
* ✨ Versatile applications: customized manga generation, real human manga creation

## 🎉 News

[](#-news)

* \[2024-12-13] A new version of gradio demo without MLLM is released (Much fewer memory usage)!
* \[2024-12-10] Checkpoint, dataset, and inference code are released!

## 🛠️ Quick Start

[](#️-quick-start)

### Installation

[](#installation)

```
# Create a new environment with Conda
conda create -n diffsensei python=3.11
conda activate diffsensei
# Install Pytorch and Diffusers related packages
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
conda install -c conda-forge diffusers transformers accelerate
pip3 install -U xformers --index-url https://download.pytorch.org/whl/cu121
# Install other dependencies
pip install -r requirements.txt
# Third-party repo for running the gradio demo
pip install gradio-image-prompter
```

### Model Download

[](#model-download)

Download our DiffSensei model from [huggingface](https://huggingface.co/jianzongwu/DiffSensei) and place it in the `checkpoints` folder like this:

If you plan not to use the MLLM component, you can download the model without the MLLM component and use the `gradio_wo_mllm.py` to produce your results.

```
checkpoints
  |- diffsensei
    |- image_generator
      |- ...
    |- mllm
      |- ...
```

### Inference with Gradio

[](#inference-with-gradio)

We provide gradio demo for inferencing DiffSensei.

```
CUDA_VISIBLE_DEVICES=0 \
python -m scripts.demo.gradio \
  --config_path configs/model/diffsensei.yaml \
  --inference_config_path configs/inference/diffsensei.yaml \
  --ckpt_path checkpoints/diffsensei
```

We also offer a version without MLLM, designed for lower memory usage. If you choose this version, you can skip downloading the MLLM component in the checkpoint, significantly reducing memory consumption. (Can be run on a single 24GB 4090 GPU with batch-size=1 for small or medium panel sizes). While this version may have slightly reduced text compatibility, the overall quality remains largely unaffected.

```
CUDA_VISIBLE_DEVICES=0 \
python -m scripts.demo.gradio_wo_mllm \
  --config_path configs/model/diffsensei.yaml \
  --inference_config_path configs/inference/diffsensei.yaml \
  --ckpt_path checkpoints/diffsensei
```

Please be patient. Try more prompts, characters, and random seeds, and download your favored manga panels! 🤗

### The MangaZero Dataset

[](#the-mangazero-dataset)

For license issues, we cannot directly share the images. Instead, we provide the manga image urls (in MangaDex) and annotations of our MangaZero dataset. Note that the released version of MangaZero is about 3/4 of the full dataset used for training. The missing images is because some urls are not available. For similar usage for manga data, we strongly encourage everyone who is interested to collect their dataset freely from MangaDex, following the instruction of [MangaDex API](https://api.mangadex.org/docs/).

Please download MangaZero from [Huggingface](https://huggingface.co/datasets/jianzongwu/MangaZero).

After downloading the annotation file, please place the annotation file in `data/mangazero/annotations.json` and run `scripts/dataset/download_mangazero.py` to download and organize the images.

```
python -m scripts.dataset.download_mangazero \
  --ann_path data/mangazero/annotations.json \
  --output_image_root data/mangazero/images
```

## Citation

[](#citation)

```
article{wu2024diffsensei,
  title={DiffSensei: Bridging Multi-Modal LLMs and Diffusion Models for Customized Manga Generation},
  author={Jianzong Wu, Chao Tang, Jingbo Wang, Yanhong Zeng, Xiangtai Li, and Yunhai Tong},
  journal={arXiv preprint arXiv:2412.07589},
  year={2024},
}
```

[![Star History Chart](https://camo.githubusercontent.com/1a0d6b16b05f1488bab6c668998b32220978aca10b8009f3d8397f0178455d2e/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d6a69616e7a6f6e6777752f4469666653656e73656926747970653d44617465)](https://star-history.com/#jianzongwu/DiffSensei\&Date)


