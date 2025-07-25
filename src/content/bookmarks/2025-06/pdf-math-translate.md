---
title: "PDFMathTranslate: 用于学术论文的AI翻译工具，保留格式"
slug: pdf-math-translate
description: |
  PDFMathTranslate 是一个用于学术论文的翻译工具，支持多种语言，并保留公式、图表和目录等格式。该工具可以通过命令行、图形界面或Docker进行使用，提供多种翻译服务，适用于需要双语比较的学术研究者。
tags: 
  - AI
  - dev
  - tool
pubDatetime: 2025-06-30T16:07:07+08:00
ogImage: 
---

[原文链接](https://github.com/Byaidu/PDFMathTranslate/tree/main)

---

English | [简体中文](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/README_zh-CN.md) | [繁體中文](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/README_zh-TW.md) | [日本語](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/README_ja-JP.md) | [한국어](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/README_ko-KR.md)

[![PDF2ZH](/Byaidu/PDFMathTranslate/raw/main/docs/images/banner.png)](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/images/banner.png)

## PDFMathTranslate

[](#pdfmathtranslate)

[![](https://camo.githubusercontent.com/1979980005d1807ecd4ec85a5adea164a0de4c50a13507a102473a2e5d6376e7/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f706466327a68)](https://pypi.org/project/pdf2zh/) [![](https://camo.githubusercontent.com/9f40687efb34ebfcd5c15dff60336204d77f07021ab22ecfedde1ec53156f992/68747470733a2f2f7374617469632e706570792e746563682f62616467652f706466327a68)](https://pepy.tech/projects/pdf2zh) [![](https://camo.githubusercontent.com/5b6eea57c182bf40324d7ebe66520c740350554798a56e0f8dbf272bc75deec2/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f70756c6c732f6279616964752f706466327a68)](https://hub.docker.com/repository/docker/byaidu/pdf2zh) [![Featured｜HelloGitHub](https://camo.githubusercontent.com/f49261526bcaecf749c998500aa6f2f7a483657393607d310c396ef560d44867/68747470733a2f2f6170692e68656c6c6f6769746875622e636f6d2f76312f776964676574732f7265636f6d6d656e642e7376673f7269643d386563326366643365663734343736326266353331323332666133326263343726636c61696d5f7569643d4a5130796665424e6a615475714455267468656d653d736d616c6c)](https://hellogithub.com/repository/8ec2cfd3ef744762bf531232fa32bc47) [![](https://camo.githubusercontent.com/c387211c724a4da730bc9bf6173e27d5fb2731f5f8024a6beef9972eb4f43fbf/68747470733a2f2f676974636f64652e636f6d2f4279616964752f5044464d6174685472616e736c6174652f737461722f62616467652e737667)](https://gitcode.com/Byaidu/PDFMathTranslate/overview) [![](https://camo.githubusercontent.com/038dcc8fe05ee0971fb741fd324c16631872f2a6f97a118452181322e4d5e06f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2546302539462541342539372d4f6e6c696e6525323044656d6f2d464639453044)](https://huggingface.co/spaces/reycn/PDFMathTranslate-Docker) [![](https://camo.githubusercontent.com/05849f284a6809aa898f7c07529869059be7c6629b2bbb0473efc2dd86f2d7b5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d6f64656c53636f70652d44656d6f2d626c7565)](https://www.modelscope.cn/studios/AI-ModelScope/PDFMathTranslate) [![](https://camo.githubusercontent.com/c7fd64c88cfffb9947bf5b0eff7119cb3e3115110b83d73c957970f981a8d7ad/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f6e747269627574696f6e732d77656c636f6d652d677265656e)](https://github.com/Byaidu/PDFMathTranslate/pulls) [![](https://camo.githubusercontent.com/319447b7de63636e4cfd81c002fe3b02c25ae1cefc09686f824deaccd3c5ca68/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f54656c656772616d2d3243413545303f7374796c653d666c61742d73717565617265266c6f676f3d74656c656772616d266c6f676f436f6c6f723d7768697465)](https://t.me/+Z9_SgnxmsmA5NzBl) [![](https://camo.githubusercontent.com/8f57d6cdf002babece25e78a86d501103ca389ede211c3d2a360138d892d5fad/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f4279616964752f5044464d6174685472616e736c617465)](https://github.com/Byaidu/PDFMathTranslate/blob/main/LICENSE)

[![Byaidu%2FPDFMathTranslate | Trendshift](https://camo.githubusercontent.com/22718c85e0b7a6a71cdc9c8d6982de7f4dfa2d835067ce89d12deb058b09daaa/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7265706f7369746f726965732f3132343234)](https://trendshift.io/repositories/12424)

PDF scientific paper translation and bilingual comparison.

* 📊 Preserve formulas, charts, table of contents, and annotations *([preview](#preview))*.
* 🌐 Support [multiple languages](#language), and diverse [translation services](#services).
* 🤖 Provides [commandline tool](#usage), [interactive user interface](#gui), and [Docker](#docker)

Feel free to provide feedback in [GitHub Issues](https://github.com/Byaidu/PDFMathTranslate/issues) or [Telegram Group](https://t.me/+Z9_SgnxmsmA5NzBl).

For details on how to contribute, please consult the [Contribution Guide](https://github.com/Byaidu/PDFMathTranslate/wiki/Contribution-Guide---%E8%B4%A1%E7%8C%AE%E6%8C%87%E5%8D%97).

## Updates

[](#updates)

* \[May 9, 2025] pdf2zh 2.0 Preview Version [#586](https://github.com/Byaidu/PDFMathTranslate/issues/586): The Windows ZIP file and Docker image are now available.

Note

2.0 Moved to a new repository under the organization: [PDFMathTranslate/PDFMathTranslate-next](https://github.com/PDFMathTranslate/PDFMathTranslate-next)

Version 2.0 official release has been published.

* \[Mar. 3, 2025] Experimental support for the new backend [BabelDOC](https://github.com/funstory-ai/BabelDOC) WebUI added as an experimental option (by [@awwaawwa](https://github.com/awwaawwa))
* \[Feb. 22 2025] Better release CI and well-packaged windows-amd64 exe (by [@awwaawwa](https://github.com/awwaawwa))
* \[Dec. 24 2024] The translator now supports local models on [Xinference](https://github.com/xorbitsai/inference) *(by [@imClumsyPanda](https://github.com/imClumsyPanda))*
* \[Dec. 19 2024] Non-PDF/A documents are now supported using `-cp` *(by [@reycn](https://github.com/reycn))*
* \[Dec. 13 2024] Additional support for backend by *(by [@YadominJinta](https://github.com/YadominJinta))*
* \[Dec. 10 2024] The translator now supports OpenAI models on Azure *(by [@yidasanqian](https://github.com/yidasanqian))*

## Preview

[](#preview)

[![](/Byaidu/PDFMathTranslate/raw/main/docs/images/preview.gif)](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/images/preview.gif)[![preview.gif](https://github.com/Byaidu/PDFMathTranslate/raw/main/docs/images/preview.gif) ](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/images/preview.gif)     [](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/images/preview.gif)

## Online Service 🌟

[](#online-service-)

You can try our application out using either of the following demos:

* [Public free service](https://pdf2zh.com/) online without installation *(recommended)*.
* [Immersive Translate - BabelDOC](https://app.immersivetranslate.com/babel-doc/) 1000 free pages per month. *(recommended)*
* [Demo hosted on HuggingFace](https://huggingface.co/spaces/reycn/PDFMathTranslate-Docker)
* [Demo hosted on ModelScope](https://www.modelscope.cn/studios/AI-ModelScope/PDFMathTranslate) without installation.

Note that the computing resources of the demo are limited, so please avoid abusing them.

## Installation and Usage

[](#installation-and-usage)

### Methods

[](#methods)

For different use cases, we provide distinct methods to use our program:

1\. UV install

1. Python installed (3.10 <= version <= 3.12)

2. Install our package:

   ```
   pip install uv
   uv tool install --python 3.12 pdf2zh
   ```

3. Execute translation, files generated in [current working directory](https://chatgpt.com/share/6745ed36-9acc-800e-8a90-59204bd13444):

   ```
   pdf2zh document.pdf
   ```

2\. Windows exe

1. Download pdf2zh-version-win64.zip from [release page](https://github.com/Byaidu/PDFMathTranslate/releases)

2. Unzip and double-click `pdf2zh.exe` to run.

3\. Graphic user interface

1. Python installed (3.10 <= version <= 3.12)

2. Install our package:

```
pip install pdf2zh
```

3. Start using in browser:

   ```
   pdf2zh -i
   ```

4. If your browser has not been started automatically, goto

   ```
   http://localhost:7860/
   ```

   [![](/Byaidu/PDFMathTranslate/raw/main/docs/images/gui.gif)](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/images/gui.gif)[![gui.gif](https://github.com/Byaidu/PDFMathTranslate/raw/main/docs/images/gui.gif)  ](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/images/gui.gif)    [](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/images/gui.gif)

See [documentation for GUI](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/README_GUI.md) for more details.

4\. Docker

1. Pull and run:

   ```
   docker pull byaidu/pdf2zh
   docker run -d -p 7860:7860 byaidu/pdf2zh
   ```

2. Open in browser:

   ```
   http://localhost:7860/
   ```

For docker deployment on cloud service:

[![Deploy](https://camo.githubusercontent.com/dc2056acd0e6ff421bfc2b129417f4f832d626c61d1c083221211d8503a429f7/68747470733a2f2f7777772e6865726f6b7563646e2e636f6d2f6465706c6f792f627574746f6e2e737667)](https://www.heroku.com/deploy?template=https://github.com/Byaidu/PDFMathTranslate) [![Deploy to Koyeb](https://camo.githubusercontent.com/a103822afe1d58c7da6beafbc0c65bb7b8d622dd193dded1b45b3c0ad6466d82/68747470733a2f2f72656e6465722e636f6d2f696d616765732f6465706c6f792d746f2d72656e6465722d627574746f6e2e737667)](https://render.com/deploy) [![Deploy on Zeabur](https://camo.githubusercontent.com/34df6b95f619465d16570ca8dd4d5a2aae99f4211d5de6d77bda8cfe5eba10f5/68747470733a2f2f7a65616275722e636f6d2f627574746f6e2e737667)](https://zeabur.com/templates/5FQIGX?referralCode=reycn) [![Deploy on Sealos](https://camo.githubusercontent.com/b677ccbcdf2979dd5f53bcd2fc29535cf89c95afc0920dee3654e5f1d99c554d/68747470733a2f2f7365616c6f732e696f2f4465706c6f792d6f6e2d5365616c6f732e737667)](https://template.sealos.io/deploy?templateName=pdf2zh) [![Deploy to Koyeb](https://camo.githubusercontent.com/51dd7a80bb71edc298ed843b159567bf2e169fab91d4a554b5428ab49b2ee613/68747470733a2f2f7777772e6b6f7965622e636f6d2f7374617469632f696d616765732f6465706c6f792f627574746f6e2e737667)](https://app.koyeb.com/deploy?type=git\&builder=buildpack\&repository=github.com/Byaidu/PDFMathTranslate\&branch=main\&name=pdf-math-translate)

5\. Zotero Plugin

See [Zotero PDF2zh](https://github.com/guaguastandup/zotero-pdf2zh) for more details.

6\. Commandline

1. Python installed (3.10 <= version <= 3.12)

2. Install our package:

   ```
   pip install pdf2zh
   ```

3. Execute translation, files generated in [current working directory](https://chatgpt.com/share/6745ed36-9acc-800e-8a90-59204bd13444):

   ```
   pdf2zh document.pdf
   ```

Tip

* If you're using Windows and cannot open the file after downloading, please install [vc\_redist.x64.exe](https://aka.ms/vs/17/release/vc_redist.x64.exe) and try again.

* If you cannot access Docker Hub, please try the image on [GitHub Container Registry](https://github.com/Byaidu/PDFMathTranslate/pkgs/container/pdfmathtranslate).

```
docker pull ghcr.io/byaidu/pdfmathtranslate
docker run -d -p 7860:7860 ghcr.io/byaidu/pdfmathtranslate
```

### Unable to install?

[](#unable-to-install)

The present program needs an AI model(`wybxc/DocLayout-YOLO-DocStructBench-onnx`) before working and some users are not able to download due to network issues. If you have a problem with downloading this model, we provide a workaround using the following environment variable:

```
set HF_ENDPOINT=https://hf-mirror.com
```

For PowerShell user:

```
$env:HF_ENDPOINT = https://hf-mirror.com
```

If the solution does not work to you / you encountered other issues, please refer to [frequently asked questions](https://github.com/Byaidu/PDFMathTranslate/wiki#-faq--%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98).

## Advanced Options

[](#advanced-options)

Execute the translation command in the command line to generate the translated document `example-mono.pdf` and the bilingual document `example-dual.pdf` in the current working directory. Use Google as the default translation service. More support translation services can find [HERE](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#services).

[![cmd](/Byaidu/PDFMathTranslate/raw/main/docs/images/cmd.explained.png)](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/images/cmd.explained.png)

In the following table, we list all advanced options for reference:

| Option                | Function                                                                                                      | Example                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| files                 | Local files                                                                                                   | `pdf2zh ~/local.pdf`                           |
| links                 | Online files                                                                                                  | `pdf2zh http://arxiv.org/paper.pdf`            |
| `-i`                  | [Enter GUI](#gui)                                                                                             | `pdf2zh -i`                                    |
| `-p`                  | [Partial document translation](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#partial) | `pdf2zh example.pdf -p 1`                      |
| `-li`                 | [Source language](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#languages)            | `pdf2zh example.pdf -li en`                    |
| `-lo`                 | [Target language](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#languages)            | `pdf2zh example.pdf -lo zh`                    |
| `-s`                  | [Translation service](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#services)         | `pdf2zh example.pdf -s deepl`                  |
| `-t`                  | [Multi-threads](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#threads)                | `pdf2zh example.pdf -t 1`                      |
| `-o`                  | Output dir                                                                                                    | `pdf2zh example.pdf -o output`                 |
| `-f`, `-c`            | [Exceptions](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#exceptions)                | `pdf2zh example.pdf -f "(MS.*)"`               |
| `-cp`                 | Compatibility Mode                                                                                            | `pdf2zh example.pdf --compatible`              |
| `--skip-subset-fonts` | [Skip font subset](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#font-subset)         | `pdf2zh example.pdf --skip-subset-fonts`       |
| `--ignore-cache`      | [Ignore translate cache](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#cache)         | `pdf2zh example.pdf --ignore-cache`            |
| `--share`             | Public link                                                                                                   | `pdf2zh -i --share`                            |
| `--authorized`        | [Authorization](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#auth)                   | `pdf2zh -i --authorized users.txt [auth.html]` |
| `--prompt`            | [Custom Prompt](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#prompt)                 | `pdf2zh --prompt [prompt.txt]`                 |
| `--onnx`              | \[Use Custom DocLayout-YOLO ONNX model]                                                                       | `pdf2zh --onnx [onnx/model/path]`              |
| `--serverport`        | \[Use Custom WebUI port]                                                                                      | `pdf2zh --serverport 7860`                     |
| `--dir`               | \[batch translate]                                                                                            | `pdf2zh --dir /path/to/translate/`             |
| `--config`            | [configuration file](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md#cofig)             | `pdf2zh --config /path/to/config/config.json`  |
| `--serverport`        | \[custom gradio server port]                                                                                  | `pdf2zh --serverport 7860`                     |
| `--babeldoc`          | Use Experimental backend [BabelDOC](https://funstory-ai.github.io/BabelDOC/) to translate                     | `pdf2zh --babeldoc` -s openai example.pdf      |
| `--mcp`               | Enable MCP STDIO mode                                                                                         | `pdf2zh --mcp`                                 |
| `--sse`               | Enable MCP SSE mode                                                                                           | `pdf2zh --mcp --sse`                           |

For detailed explanations, please refer to our document about [Advanced Usage](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/ADVANCED.md) for a full list of each option.

## Secondary Development (APIs)

[](#secondary-development-apis)

For downstream applications, please refer to our document about [API Details](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/APIS.md) for further information about:

* [Python API](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/APIS.md#api-python), how to use the program in other Python programs
* [HTTP API](https://github.com/Byaidu/PDFMathTranslate/blob/main/docs/APIS.md#api-http), how to communicate with a server with the program installed

## TODOs

[](#todos)

* [ ] Parse layout with DocLayNet based models, [PaddleX](https://github.com/PaddlePaddle/PaddleX/blob/17cc27ac3842e7880ca4aad92358d3ef8555429a/paddlex/repo_apis/PaddleDetection_api/object_det/official_categories.py#L81), [PaperMage](https://github.com/allenai/papermage/blob/9cd4bb48cbedab45d0f7a455711438f1632abebe/README.md?plain=1#L102), [SAM2](https://github.com/facebookresearch/sam2)

* [ ] Fix page rotation, table of contents, format of lists

* [ ] Fix pixel formula in old papers

* [ ] Async retry except KeyboardInterrupt

* [ ] Knuth–Plass algorithm for western languages

* [ ] Support non-PDF/A files

* [ ] Plugins of [Zotero](https://github.com/zotero/zotero) and [Obsidian](https://github.com/obsidianmd/obsidian-releases)

## Acknowledgements

[](#acknowledgements)

* [Immersive Translation](https://immersivetranslate.com) sponsors monthly Pro membership redemption codes for active contributors to this project, see details at: [CONTRIBUTOR\_REWARD.md](https://github.com/funstory-ai/BabelDOC/blob/main/docs/CONTRIBUTOR_REWARD.md)

* New backend: [BabelDOC](https://github.com/funstory-ai/BabelDOC)

* Document merging: [PyMuPDF](https://github.com/pymupdf/PyMuPDF)

* Document parsing: [Pdfminer.six](https://github.com/pdfminer/pdfminer.six)

* Document extraction: [MinerU](https://github.com/opendatalab/MinerU)

* Document Preview: [Gradio PDF](https://github.com/freddyaboulton/gradio-pdf)

* Multi-threaded translation: [MathTranslate](https://github.com/SUSYUSTC/MathTranslate)

* Layout parsing: [DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO)

* Document standard: [PDF Explained](https://zxyle.github.io/PDF-Explained/), [PDF Cheat Sheets](https://pdfa.org/resource/pdf-cheat-sheets/)

* Multilingual Font: [Go Noto Universal](https://github.com/satbyy/go-noto-universal)

## Contributors

[](#contributors)

[![](https://camo.githubusercontent.com/7e6f63d1f37afcaef3378c7a0686ce83d09f5d865ae826660f3351cb74d02572/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f5044464d6174685472616e736c6174652f636f6e7472696275746f72732e7376673f77696474683d38393026627574746f6e3d66616c7365)](https://github.com/Byaidu/PDFMathTranslate/graphs/contributors)

[![Alt](https://camo.githubusercontent.com/2a13e53a3f59280392c0587f717cb20f87d69b0b84b94b357a1775b8c8167f57/68747470733a2f2f7265706f62656174732e6178696f6d2e636f2f6170692f656d6265642f646661373538336461353333326131313436386436383666626432396239323332306136613836392e737667 "Repobeats analytics image")](https://camo.githubusercontent.com/2a13e53a3f59280392c0587f717cb20f87d69b0b84b94b357a1775b8c8167f57/68747470733a2f2f7265706f62656174732e6178696f6d2e636f2f6170692f656d6265642f646661373538336461353333326131313436386436383666626432396239323332306136613836392e737667)

## Star History

[](#star-history)

[![Star History Chart](https://camo.githubusercontent.com/e36b882836a58c1774ee53f32b25804e087fbcffd76df986b7aa72e2291f735f/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d4279616964752f5044464d6174685472616e736c61746526747970653d44617465)](https://star-history.com/#Byaidu/PDFMathTranslate\&Date)


