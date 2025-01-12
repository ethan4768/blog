---
title: "Sana: 高效高分辨率图像合成的线性扩散变换器"
slug: sana-efficient-image-synthesis
description: |
  Sana 是一种文本到图像的框架，能够高效生成高达4096 × 4096分辨率的图像。它利用深度压缩自编码器和线性扩散变换器，快速合成高质量的图像，适用于笔记本GPU。Sana 的设计旨在实现快速的内容创建，降低成本。英伟达开源的可以直接生成 4K 图片的模型
tags: 
  - AI
  - dev
  - opensource
  - image
pubDatetime: 2025-01-12T22:14:53+08:00
ogImage: 
---

[原文链接](https://nvlabs.github.io/Sana/)

---

英伟达开源了一个可以直接生成 4K 图片的模型 Sana

Sana-0.6B 可以在 16GB 的笔记本电脑 GPU 上部署

生成 1024 × 1024 分辨率的图像只需不到 1 秒钟

官方已经支持了 Comfyui，而且放出了 Lora 训练工具

<!--    <div style="overflow: hidden; background-color: #6699cc;">-->

<!--      <div class="container">-->

<!--        <a href="https://www.nvidia.com/" style="float: left; color: black; text-align: center; padding: 12px 16px; text-decoration: none; font-size: 16px;"><img width="100%" src="https://nv-tlabs.github.io/3DStyleNet/assets/nvidia.svg"></a>-->

<!--        <a href="https://github.com/Efficient-Large-Model/" style="float: left; color: black; text-align: center; padding: 14px 16px; text-decoration: none; font-size: 16px;"><strong>Efficient AI Group</strong></a>-->

<!--      </div>-->

<!--    </div>-->

![Logo](https://nvlabs.github.io/Sana/asset/logo.jpg)

Efficient High-Resolution Image Synthesis\
with Linear Diffusion Transformer
---------------------------------

Exploring the Frontiers of Efficient Generative Foundation Models

<!-- Add author and institution information -->

[Enze Xie](https://xieenze.github.io/)1\*, [Junsong Chen](https://lawrence-cj.github.io/)1\*, [Junyu Chen](https://scholar.google.com.hk/citations?hl=zh-CN\&user=mWdYMZ8AAAAJ)2,3, [Han Cai](https://han-cai.github.io//)1, [Haotian Tang](http://kentang.net/)2,\
[Yujun Lin](https://yujunlin.com//)2, [Zhekai Zhang](https://hanlab.mit.edu/team/zhekai-zhang/)2, [Muyang Li](https://lmxyy.me//)2, [Ligeng Zhu](https://lzhu.me//)1, [Yao Lu](https://scholar.google.com/citations?user=OI7zFmwAAAAJ\&hl=en/)1, [Song Han](https://hanlab.mit.edu/songhan/)1,2

1NVIDIA, 2MIT, 3Tsinghua University\
\*Project co-lead

<!--        <div style="overflow: hidden; background-color: #6699cc;">-->

[Paper](https://arxiv.org/abs/2410.10629) [Code](https://github.com/NVlabs/Sana) [Huggingface](https://huggingface.co/collections/Efficient-Large-Model/sana-673efba2a57ed99843f11f9e) [Demo](https://nv-sana.mit.edu/) [Replicate API](https://replicate.com/chenxwh/sana)

<!-- The Modal -->

![]()

<!-- Text for description -->

![Sana-logo](https://nvlabs.github.io/Sana/asset/SANA.png)

## About Sana

We introduce Sana, a text-to-image framework that can efficiently generate images up to 4096 × 4096 resolution. Sana can synthesize high-resolution, high-quality images with strong text-image alignment at a remarkably fast speed, deployable on laptop GPU. Core designs include: **Deep compression autoencoder:&#x20;**&#x75;nlike traditional AEs, which compress images only 8×, we trained an AE that can compress images 32×, effectively reducing the number of latent tokens. **Linear DiT:&#x20;**&#x77;e replace all vanilla attention in DiT with linear attention, which is more efficient at high resolutions without sacrificing quality. **Decoder-only text encoder:&#x20;**&#x77;e replaced T5 with modern decoder-only small LLM as the text encoder and designed complex human instruction with in-context learning to enhance the image-text alignment. **Efficient training and sampling:&#x20;**&#x77;e propose Flow-DPM-Solver to reduce sampling steps, with efficient caption labeling and selection to accelerate convergence.\
As a result, Sana-0.6B is very competitive with modern giant diffusion model (e.g. Flux-12B), being 20 times smaller and 100+ times faster in measured throughput. Moreover, Sana-0.6B can be deployed on a 16GB laptop GPU, taking less than 1 second to generate a 1024 × 1024 resolution image. Sana enables content creation at low cost.

<!-- Insert your image here -->

![latency comparison with SOTA methods](https://nvlabs.github.io/Sana/asset/content/latency_compare.jpg)

## Several Core Design Details for Efficiency

    •   **Deep Compression Autoencoder:&#x20;**&#x57;e introduce a new [Deep Compression Autoencoder (DC-AE)](https://hanlab.mit.edu/projects/dc-ae) that aggressively increases the scaling factor to 32. Compared with AE-F8, our AE-F32 outputs 16× fewer latent tokens, which is crucial for efficient training and generating ultra-high-resolution images, such as 4K resolution.

![Image 1](https://nvlabs.github.io/Sana/asset/content/ae/4_img_vae_junyu.jpg) ![Image 2](https://nvlabs.github.io/Sana/asset/content/ae/4_img_origin.jpg)

<!--    <section class="image-comparison-container">-->

<!--        <div class="image-comparison-content">-->

<!--            <img src="asset/content/ae/3_img_vae_junyu.png" alt="Image 3" class="image-3"/>-->

<!--            <img src="asset/content/ae/3_img_origin.png" alt="Image 4" class="image-4"/>-->

<!--            <div class="slider-black"></div>-->

<!--        </div>-->

<!--    </section>-->

    •   **Efficient Linear DiT:&#x20;**&#x57;e introduce a new linear DiT, replacing vanilla quadratic attention and reducing complexity from O(N2) to O(N) Mix-FFN, with 3×3 depth-wise convolution in MLP, enhances the local information of tokens. Linear attention achieves comparable results to vanilla, improving 4K generation by 1.7× in latency. Mix-FFN also removes the need for positional encoding (NoPE) without quality loss, marking the first DiT without positional embedding.\
    •   **Decoder-only Small LLM as Text Encoder:&#x20;**&#x57;e use Gemma, a decoder-only LLM, as the text encoder to enhance understanding and reasoning in prompts. Unlike CLIP or T5, Gemma offers superior text comprehension and instruction-following. We address training instability and design complex human instructions (CHI) to leverage Gemma’s in-context learning, improving image-text alignment.

![pipeline for Sana](https://nvlabs.github.io/Sana/asset/content/model-incremental.jpg)

    •   **Efficient Training and Inference Strategy:&#x20;**&#x57;e propose automatic labeling and training strategies to improve text-image consistency. Multiple VLMs generate diverse re-captions, and a CLIPScore-based strategy selects high-CLIPScore captions to enhance convergence and alignment. Additionally, our **Flow-DPM-Solver** reduces inference steps from 28-50 to 14-20 compared to the Flow-Euler-Solver, with better performance.

![flow-dpms vs flow-euler](https://nvlabs.github.io/Sana/asset/content/sampler.jpg)

## Overall Performance

We compare Sana with the most advanced text-to-image diffusion models in Table 1. For 512 × 512 resolution, Sana-0.6 demonstrates a throughput that is 5× faster than PixArt-Σ, which has a similar model size, and significantly outperforms it in FID, Clip Score, GenEval, and DPG-Bench. For 1024 × 1024 resolution, Sana is considerably stronger than most models with <3B parameters and excels in inference latency. Our models achieve competitive performance even when compared to the most advanced large model FLUX-dev. For instance, while the accuracy on DPG-Bench is equivalent and slightly lower on GenEval, Sana-0.6B’s throughput is 39× faster, and Sana-1.6B is 23× faster.

![Sana performance](https://nvlabs.github.io/Sana/asset/content/performance.jpg)

<!-- Video Section -->

## Sana-0.6B is Deployable on Laptop GPU

[Your browser does not support the video tag.](https://nvlabs.github.io/Sana/asset/video/Sana-0.6B-laptop.mp4)

<!-- End Video Section -->

## ComfyUI Usage

We’ve developed a [plugin ](https://github.com/Efficient-Large-Model/ComfyUI_ExtraModels)to integrate Sana with ComfyUI. For guidance and sample workflows, please refer to the [Sana GitHub ](https://github.com/NVlabs/Sana/blob/main/asset/docs/ComfyUI/comfyui.md). Special thanks to [city96/ComfyUI\_ExtraModels ](https://github.com/city96/ComfyUI_ExtraModels)for their open-source contributions.

![Sana-comfyUI workflow](https://nvlabs.github.io/Sana/asset/content/comfyui/sana.jpg)

[Sana workflow in ComfyUI](https://github.com/NVlabs/Sana/blob/main/asset/docs/ComfyUI/comfyui.md)

<!-- Video Section -->

[Your browser does not support the video tag.](https://nvlabs.github.io/Sana/asset/content/comfyui/Sana_CogVideoX_Fun.mp4)

[Sana + CogVideoX workflow in ComfyUI](https://github.com/NVlabs/Sana/blob/main/asset/docs/ComfyUI/comfyui.md)

<!-- End Video Section -->

## Sana-LoRA Dreambooth

Sana-LoRA is support by 🧨diffusers. Check the our [guidance ](https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_lora_dreambooth.md)to train your customized models. Original diffusers doc is [here ](https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_lora_dreambooth.md). We show some samples during Sana-LoRA fine-tuning process below.

![Sana-comfyUI workflow](https://nvlabs.github.io/Sana/asset/content/dreambooth/step0.jpg) ![Sana-comfyUI workflow](https://nvlabs.github.io/Sana/asset/content/dreambooth/step500.jpg)

[Sana-LoRA training samples from 0 to 500 steps](https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_lora_dreambooth.md)

## Our Mission

Our mission is to develop **efficient, lightweight, and accelerated** AI technologies that address practical challenges and deliver fast, open-source solutions.

<!--BibTex citation -->

## BibTeX

```
@misc{xie2024sana,
      title={Sana: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformer},
      author={Enze Xie and Junsong Chen and Junyu Chen and Han Cai and Haotian Tang and Yujun Lin and Zhekai Zhang and Muyang Li and Ligeng Zhu and Yao Lu and Song Han},
      year={2024},
      eprint={2410.10629},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2410.10629},
    }
```

<!--End BibTex citation -->

<!-- Footer Section -->

<!-- End Footer -->


