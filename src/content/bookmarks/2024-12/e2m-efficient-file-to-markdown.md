---
title: E2M：高效的文件到Markdown转换工具，基于AI解析器与转换器
slug: e2m-efficient-file-to-markdown
description: E2M是一款多功能Python库，旨在高效地将多种文件格式（如DOC、PDF、EPUB等）转换为Markdown。它利用专用的解析器和转换器，支持自定义配置，并简化了为检索增强生成（RAG）准备数据的过程，可以进行简单安装和开源使用。
tags: 
  - ai
  - dev
  - tool
  - opensource
  - writing
pubDatetime: 2024-12-11T10:05:25+08:00
ogImage: https://opengraph.githubassets.com/e90fbd95863dd2bfc6aeba09a99e9b18c8e324b6c3a616ece6ff51b4be62c731/wisupai/e2m
---

[原文链接](https://github.com/wisupai/e2m)

---

[![wisup\_e2m Logo](https://github.com/wisupai/e2m/raw/main/docs/images/wisup_e2m_banner.jpg?raw=true)](https://github.com/wisupai/e2m/blob/main/docs/images/wisup_e2m_banner.jpg?raw=true)

[![License](https://camo.githubusercontent.com/70e10b4c650db97135ee7018da809d9720418313d6416bcd20920c56d291c77e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4170616368655f322e302d626c7565) ](https://github.com/user/repo/blob/main/LICENSE)[![E2M Repo](https://camo.githubusercontent.com/27ba9371f22a0f3af2faa3b1261df86893e53cee9b14b836ee8bfb8fbb54a3bd/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f65326d2d7265706f2d626c7565) ](https://github.com/wisupai/e2m)[![E2M Version](https://camo.githubusercontent.com/4953f5bd1fc3641302686ac7611979d101b151770195f4a5fd471c5f70f4e879/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f76657273696f6e2d302e312e36332d626c7565) ](https://github.com/Jing-yilin/E2M/tags/0.1.63)[![Python Version](https://camo.githubusercontent.com/ee38edd42b186f5862136349aafb3046c893e9497a6b94b8b8f6a91a877b4144/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e3130253230253743253230332e31312d626c7565) ](https://www.python.org/downloads/)[![PyPI](https://camo.githubusercontent.com/c2334a672a4ab33093053b2fe30e3d21afbc8fca11d15d707dfed5863d150dda/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707970692d77697375705f5f65326d2d626c7565) ](https://pypi.org/project/wisup_e2m/)[![中文文档](https://camo.githubusercontent.com/ffe4388e00d91bbdd2a2d057557ac44d0c9d1a3aa310d30bb0054bd0e0575a0f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f63732de4b8ade69687e69687e6a1a32d726564)](https://github.com/wisupai/e2m/blob/main/README-zh.md)

# 🚀 E2M: Everything to Markdown

[](#-e2m-everything-to-markdown)

**Everything to Markdown**

E2M is a Python library that can parse and convert various file types into Markdown format. By utilizing a parser-converter architecture, it supports the conversion of multiple file formats, including doc, docx, epub, html, htm, url, pdf, ppt, pptx, mp3, and m4a.

✨The ultimate goal of the E2M project is to provide high-quality data for Retrieval-Augmented Generation (RAG) and model training or fine-tuning.

**Core Architecture of the Project:**

* **Parser**: Responsible for parsing various file types into text or image data.
* **Converter**: Responsible for converting text or image data into Markdown format.

Generally, for any type of file, the parser is run first to extract internal data such as text and images. Then, the converter is used to transform this data into Markdown format.

[![wisup\_e2m Logo](https://github.com/wisupai/e2m/raw/main/docs/images/e2m_pipeline.jpg?raw=true)](https://github.com/wisupai/e2m/blob/main/docs/images/e2m_pipeline.jpg?raw=true)

## 📹 Video Introduction

[](#-video-introduction)

[![Watch the video](/wisupai/e2m/raw/main/docs/images/video_banner.png)](https://www.bilibili.com/video/BV1HvWeenEYQ)

## 📂 All Converters and Parsers

[](#-all-converters-and-parsers)

| Parser      |                                                                 |                     |
| ----------- | --------------------------------------------------------------- | ------------------- |
| Parser Type | Engine                                                          | Supported File Type |
| PdfParser   | surya\_layout, marker, unstructured                             | pdf                 |
| DocParser   | pandoc, xml                                                     | doc                 |
| DocxParser  | pandoc, xml                                                     | docx                |
| PptParser   | unstructured                                                    | ppt                 |
| PptxParser  | unstructured                                                    | pptx                |
| UrlParser   | unstructured, jina, firecrawl                                   | url                 |
| EpubParser  | unstructured                                                    | epub                |
| HtmlParser  | unstructured                                                    | html, htm           |
| VoiceParser | openai\_whisper\_api, openai\_whisper\_local, SpeechRecognition | mp3, m4a            |

| Converter      |                                                                   |          |
| -------------- | ----------------------------------------------------------------- | -------- |
| Converter Type | Engine                                                            | Strategy |
| ImageConverter | litellm, zhipuai (Not Well in Image Recognition, Not Recommended) | default  |
| TextConverter  | litellm, zhipuai                                                  | default  |

### Supported Models

[](#supported-models)

1. Litellm: <https://docs.litellm.ai/docs/providers/>
2. Zhipuai: <https://open.bigmodel.cn/dev/howuse/model>

## 📦 Installation

[](#-installation)

Create Environment:

```
conda create -n e2m python=3.10
conda activate e2m
```

Update pip:

```
pip install --upgrade pip
```

Install E2M using pip:

```
# Option 1: Install via git, most recommended
pip install git+https://github.com/wisupai/e2m.git --index-url https://pypi.org/simple
# Option 2: Install via pip
pip install --upgrade wisup_e2m
# Option 3: Manual installation
git clone https://github.com/wisupai/e2m.git
cd e2m
pip install poetry
poetry build
pip install dist/wisup_e2m-0.1.63-py3-none-any.whl
```

## Start API Service

[](#start-api-service)

```
gunicorn wisup_e2m.api.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

API Documentation:

* <http://127.0.0.1:8000/docs>

## ⚡️ Parser Quick Start

[](#️-parser-quick-start)

Here's simple examples demonstrating how to use E2M Parsers:

### 📄 Pdf Parser

[](#-pdf-parser)

```
from wisup_e2m import PdfParser

pdf_path = "./test.pdf"
parser = PdfParser(engine="marker") # pdf engines: marker, unstructured, surya_layout
pdf_data = parser.parse(pdf_path)
print(pdf_data.text)
```

### 📝 Doc Parser

[](#-doc-parser)

```
from wisup_e2m import DocParser

doc_path = "./test.doc"
parser = DocParser(engine="pandoc") # doc engines: pandoc, xml
doc_data = parser.parse(doc_path)
print(doc_data.text)
```

### 📜 Docx Parser

[](#-docx-parser)

```
from wisup_e2m import DocxParser

docx_path = "./test.docx"
parser = DocxParser(engine="pandoc") # docx engines: pandoc, xml
docx_data = parser.parse(docx_path)
print(docx_data.text)
```

### 📚 Epub Parser

[](#-epub-parser)

```
from wisup_e2m import EpubParser

epub_path = "./test.epub"
parser = EpubParser(engine="unstructured") # epub engines: unstructured
epub_data = parser.parse(epub_path)
print(epub_data.text)
```

### 🌐 Html Parser

[](#-html-parser)

```
from wisup_e2m import HtmlParser

html_path = "./test.html"
parser = HtmlParser(engine="unstructured") # html engines: unstructured
html_data = parser.parse(html_path)
print(html_data.text)
```

### 🔗 Url Parser

[](#-url-parser)

```
from wisup_e2m import UrlParser

url = "https://www.example.com"
parser = UrlParser(engine="jina") # url engines: jina, firecrawl, unstructured
url_data = parser.parse(url)
print(url_data.text)
```

### 🖼️ Ppt Parser

[](#️-ppt-parser)

```
from wisup_e2m import PptParser

ppt_path = "./test.ppt"
parser = PptParser(engine="unstructured") # ppt engines: unstructured
ppt_data = parser.parse(ppt_path)
print(ppt_data.text)
```

### 🖼️ Pptx Parser

[](#️-pptx-parser)

```
from wisup_e2m import PptxParser

pptx_path = "./test.pptx"
parser = PptxParser(engine="unstructured") # pptx engines: unstructured
pptx_data = parser.parse(pptx_path)
print(pptx_data.text)
```

### 🎤 Voice Parser

[](#-voice-parser)

```
from wisup_e2m import VoiceParser

voice_path = "./test.mp3"
parser = VoiceParser(
  engine="openai_whisper_local", # voice engines: openai_whisper_api, openai_whisper_local
  model="large" # available models: https://github.com/openai/whisper#available-models-and-languages
  )

voice_data = parser.parse(voice_path)
print(voice_data.text)
```

## 🔄 Converter Quick Start

[](#-converter-quick-start)

Here's simple examples demonstrating how to use E2M Converters:

### 📝 Text Converter

[](#-text-converter)

```
from wisup_e2m import TextConverter

text = "Parsed text data from any parser"
converter = TextConverter(
  engine="litellm", # text engines: litellm
  model="deepseek/deepseek-chat",
  api_key="your api key",
  base_url="your base url"
  )
text_data = converter.convert(text)
print(text_data)
```

### 🖼️ Image Converter

[](#️-image-converter)

```
from wisup_e2m import ImageConverter

images = ["./test1.png", "./test2.png"]
converter = ImageConverter(
  engine="litellm", # image engines: litellm
  model="gpt-4o",
  api_key="your api key",
  base_url="your base url"
  )
image_data = converter.convert(image_path)
print(image_data)
```

## 🆙 Next Level

[](#-next-level)

### 🛠️ E2MParser

[](#️-e2mparser)

`E2MParser` is an integrated parser that supports multiple file types. It can be used to parse a wide range of file types into Markdown format.

```
from wisup_e2m import E2MParser

# Initialize the parser with your configuration file
ep = E2MParser.from_config("config.yaml")

# Parse the desired file
data = ep.parse(file_name="/path/to/file.pdf")

# Print the parsed data as a dictionary
print(data.to_dict())
```

### 🛠️ E2MConverter

[](#️-e2mconverter)

`E2MConverter` is an integrated converter that supports text and image conversion. It can be used to convert text and images into Markdown format.

```
from wisup_e2m import E2MConverter

ec = E2MConverter.from_config("./config.yaml")

text = "Parsed text data from any parser"

ec.convert(text=text)

images = ["test.jpg", "test.png"]
ec.convert(images=images)
```

You can use a `config.yaml` file to specify the parsers and converters you want to use. Here is an example of a `config.yaml` file:

```
parsers:
    doc_parser:
        engine: "pandoc"
        langs: ["en", "zh"]
    docx_parser:
        engine: "pandoc"
        langs: ["en", "zh"]
    epub_parser:
        engine: "unstructured"
        langs: ["en", "zh"]
    html_parser:
        engine: "unstructured"
        langs: ["en", "zh"]
    url_parser:
        engine: "jina"
        langs: ["en", "zh"]
    pdf_parser:
        engine: "marker"
        langs: ["en", "zh"]
    pptx_parser:
        engine: "unstructured"
        langs: ["en", "zh"]
    voice_parser:
        # option 1: use openai whisper api
        # engine: "openai_whisper_api"
        # api_base: "https://api.openai.com/v1"
        # api_key: "your_api_key"
        # model: "whisper"

        # option 2: use local whisper model
        engine: "openai_whisper_local"
        model: "large" # available models: https://github.com/openai/whisper#available-models-and-languages

converters:
    text_converter:
        engine: "litellm"
        model: "deepseek/deepseek-chat"
        api_key: "your_api_key"
        # base_url: ""
    image_converter:
        engine: "litellm"
        model: "gpt-4o-mini"
        api_key: "your_api_key"
        # base_url: ""
```

## ❓ Q\&A

[](#-qa)

[FAQ Document](https://github.com/wisupai/e2m/blob/main/docs/faq/FAQ-en.md)

## 📜 License

[](#-license)

This project is licensed under the MIT License. See the [LICENSE](https://github.com/wisupai/e2m/blob/main/LICENSE) file for details.

## 📧 Contact

[](#-contact)

You can scan the QR code below to join our WeChat group:

[![wisup\_e2m Logo](/wisupai/e2m/raw/main/docs/images/wechat_QR.png)](https://github.com/wisupai/e2m/blob/main/docs/images/wechat_QR.png)

For any questions or inquiries, please open an issue on [GitHub](https://github.com/wisupai/e2m) or contact us at <team@wisup.ai>.

Contact for business cooperation: <team@wisup.ai>

## 💼 Join Us

[](#-join-us)

[![wisup\_e2m Logo](/wisupai/e2m/raw/main/docs/images/wisup_logo.png)](https://github.com/wisupai/e2m/blob/main/docs/images/wisup_logo.png)

* Wisup is an AI startup with a strong focus on data and algorithms. We specialize in providing high-quality data and algorithm services for enterprises. We embrace a remote working model and welcome talented individuals from around the world to join us.

* Our philosophy: From information to data, from data to knowledge, from knowledge to value.

* Our vision: To make the world a better place through data.

* We are looking for: Like-minded Co-Founders

  * No restrictions on education, age, location, race, or gender
  * Keen interest in AI and familiarity with AI and related vertical industries
  * Passionate about AI and data, with a strong sense of purpose
  * Possess unique strengths, responsibility, and a team-oriented mindset

* To apply, send your resume to: <team@wisup.ai>

* You also need to answer three questions in your email:

  * What makes you irreplaceable?
  * What is the most challenging situation you have faced, and how did you resolve it?
  * How do you view the future development of AI?

## 🌟 Contributing

[](#-contributing)

[![](https://camo.githubusercontent.com/a5f939a125b06a4e1f6f2d6b7ce4ae593044a976a4e8b1530f7bbc5c89a6e54f/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d776973757061692f65326d)](https://github.com/wisupai/e2m/graphs/contributors)


